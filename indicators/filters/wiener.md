# WIENER - Wiener


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. WIENER addresses this by implementing `Calculates Wiener Filter that minimizes mean square error` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Wiener Filter that minimizes mean square error`

### Parameters

| Parameter | Purpose |
|---|---|
| `src` | Series to filter |
| `length` | Window size for noise estimation |
| `smooth_len` | Length for signal power estimation |

### Returns

- Wiener filtered value

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_length` | `input.int` | default: `20`, label: "Length" |
| `i_smooth` | `input.int` | default: `10`, label: "Smoothing" |
| `i_source` | `input.source` | default: `close`, label: "Source" |

## Runtime profile

- Declared optimization: Uses adaptive noise estimation with O(n) complexity per bar
- Streaming model: single-pass update on each new bar.
- Warm-up behavior: outputs can be unstable until enough samples satisfy `length`.
- Memory model: state is kept in Pine series context rather than external buffers.

## Trade-offs

Streaming logic keeps incremental cost stable, but initialization and edge-case handling become first-class concerns. That is a deliberate choice: predictable execution beats opaque recalculation spikes in live charts.

## Verification checklist

1. Open the script in TradingView and confirm it compiles under Pine Script v6.
2. Validate warm-up behavior on sparse data and short histories.
3. Compare output against a trusted reference implementation for the same parameters.
4. Confirm parameter bounds reject invalid values without silent fallback.

## References

- Source code: `indicators/filters/wiener.pine`
- Documentation file: `indicators/filters/wiener.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/filters/wiener.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/filters/wiener.md
