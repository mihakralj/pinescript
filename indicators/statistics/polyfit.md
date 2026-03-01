# POLYFIT - Polyfit


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. POLYFIT addresses this by implementing `Rolling polynomial regression fit of degree d over a lookback window` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Rolling polynomial regression fit of degree d over a lookback window`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | Series to fit |
| `period` | Lookback period (number of data points) |
| `degree` | Polynomial degree (1=linear, 2=quadratic, 3=cubic, etc.) |

### Returns

- Fitted value at the current bar (polynomial endpoint)

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_period` | `input.int` | default: `20`, label: "Period" |
| `i_degree` | `input.int` | default: `2`, label: "Degree" |
| `i_source` | `input.source` | default: `close`, label: "Source" |

## Runtime profile

- Declared optimization: not explicitly annotated in source comments.
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

- Source code: `indicators/statistics/polyfit.pine`
- Documentation file: `indicators/statistics/polyfit.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/statistics/polyfit.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/statistics/polyfit.md
