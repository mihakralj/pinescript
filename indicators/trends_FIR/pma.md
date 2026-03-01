# PMA - Pma


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. PMA addresses this by implementing `Calculates Ehlers Predictive Moving Average using WMA-based linear extrapolation` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Ehlers Predictive Moving Average using WMA-based linear extrapolation`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | Series to calculate PMA from |
| `period` | Lookback period for WMA smoothing (>= 1, default 7 per Ehlers) |

### Returns

- [pma, trigger] where PMA = 2×WMA − WMA(WMA) and Trigger = (4×WMA − WMA(WMA)) / 3

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_period` | `input.int` | default: `7`, label: "Period" |
| `i_source` | `input.source` | default: `close`, label: "Source" |

## Runtime profile

- Declared optimization: Uses dual running sums with cached denominator for O(1) WMA complexity per bar
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

- Source code: `indicators/trends_FIR/pma.pine`
- Documentation file: `indicators/trends_FIR/pma.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/trends_FIR/pma.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/trends_FIR/pma.md
