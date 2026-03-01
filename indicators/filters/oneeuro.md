# ONEEURO - Oneeuro


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. ONEEURO addresses this by implementing `One Euro adaptive low-pass filter — trades jitter suppression` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `One Euro adaptive low-pass filter — trades jitter suppression`

### Parameters

| Parameter | Purpose |
|---|---|
| `src` | Input series |
| `minCutoff` | Minimum cutoff frequency. Lower = smoother at low speed. |
| `beta` | Speed coefficient. Higher = faster response to rapid moves. |
| `dCutoff` | Cutoff frequency for the derivative estimator. |

### Returns

- Filtered series (overlay, tracks price)

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_source` | `input.source` | default: `close`, label: "Source" |

## Runtime profile

- Declared optimization: O(1) per bar, O(1) memory — 4 state variables (x̂, d̂x, x_prev, init flag)
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

- Source code: `indicators/filters/oneeuro.pine`
- Documentation file: `indicators/filters/oneeuro.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/filters/oneeuro.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/filters/oneeuro.md
