# QUANTILE - Quantile


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. QUANTILE addresses this by implementing `Calculates the quantile of a series over a lookback period using linear interpolation.` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates the quantile of a series over a lookback period using linear interpolation.`

### Parameters

| Parameter | Purpose |
|---|---|
| `src` | {series float} The source series to calculate the quantile from. |
| `len` | {simple int} The lookback period. Must be greater than 0. |
| `q_level` | {simple float} The quantile level to calculate (between 0.0 and 1.0). |

### Returns

- {series float} The calculated quantile value, or na if insufficient data.

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_source` | `input.source` | default: `close`, label: "Source" |
| `i_length` | `input.int` | default: `14`, label: "Period" |
| `i_quantile_level` | `input.float` | default: `0.25`, label: "Quantile Level (0.0-1.0)" |

## Runtime profile

- Declared optimization: not explicitly annotated in source comments.
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

- Source code: `indicators/statistics/quantile.pine`
- Documentation file: `indicators/statistics/quantile.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/statistics/quantile.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/statistics/quantile.md
