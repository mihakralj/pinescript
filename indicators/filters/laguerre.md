# LAGUERRE - Laguerre


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. LAGUERRE addresses this by implementing `Calculates Laguerre Filter using 4 cascaded all-pass IIR elements` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Laguerre Filter using 4 cascaded all-pass IIR elements`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | Series to calculate Laguerre filter from |
| `gamma` | Damping factor controlling smoothing (0 = FIR, higher = more smoothing) |

### Returns

- Laguerre filter value with frequency-dependent smoothing

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_gamma` | `input.float` | default: `0.8`, label: "Gamma" |
| `i_source` | `input.source` | default: `close`, label: "Source" |

## Runtime profile

- Declared optimization: Uses 4-element all-pass cascade with O(1) complexity per bar
- Streaming model: single-pass update on each new bar.
- Warm-up behavior: outputs can be unstable until enough samples satisfy `lookback parameter`.
- Memory model: state is kept in Pine series context rather than external buffers.

## Trade-offs

Streaming logic keeps incremental cost stable, but initialization and edge-case handling become first-class concerns. That is a deliberate choice: predictable execution beats opaque recalculation spikes in live charts.

## Verification checklist

1. Open the script in TradingView and confirm it compiles under Pine Script v6.
2. Validate warm-up behavior on sparse data and short histories.
3. Compare output against a trusted reference implementation for the same parameters.
4. Confirm parameter bounds reject invalid values without silent fallback.

## References

- Source code: `indicators/filters/laguerre.pine`
- Documentation file: `indicators/filters/laguerre.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/filters/laguerre.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/filters/laguerre.md
