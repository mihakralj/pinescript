# RMED - Rmed


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. RMED addresses this by implementing `Ehlers Recursive Median Filter — a nonlinear IIR filter that applies` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Ehlers Recursive Median Filter — a nonlinear IIR filter that applies`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | Series to filter |
| `period` | Cycle period for EMA constant derivation (>= 1) |

### Returns

- Recursive median filtered value

## Runtime profile

- Declared optimization: O(1) per bar — 5-element sort network + EMA update
- Streaming model: single-pass update on each new bar.
- Warm-up behavior: outputs can be unstable until enough samples satisfy `period`.
- Memory model: state is kept in Pine series context rather than external buffers.

## Trade-offs

Streaming logic keeps incremental cost stable, but initialization and edge-case handling become first-class concerns. That is a deliberate choice: predictable execution beats opaque recalculation spikes in live charts.

## Verification checklist

1. Open the script in TradingView and confirm it compiles under Pine Script v6.
2. Validate warm-up behavior on sparse data and short histories.
3. Compare output against a trusted reference implementation for the same parameters.
4. Confirm parameter bounds reject invalid values without silent fallback.

## References

- Source code: `indicators/filters/rmed.pine`
- Documentation file: `indicators/filters/rmed.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/filters/rmed.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/filters/rmed.md
