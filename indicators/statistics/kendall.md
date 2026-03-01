# KENDALL - Kendall


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. KENDALL addresses this by implementing `Calculates Kendall's Tau-a rank correlation coefficient.` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Kendall's Tau-a rank correlation coefficient.`

### Parameters

| Parameter | Purpose |
|---|---|
| `source1` | series float The first input series. |
| `source2` | series float The second input series. |
| `length` | int The lookback period. Min 2, Max 60. |

### Returns

- series float Kendall's Tau-a coefficient, ranging from -1 to +1.

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_source1` | `input.source` | default: `close`, label: "Source 1" |
| `i_source2_ticker` | `input.symbol` | default: `"SPY"`, label: "SPY" |
| `i_period` | `input.int` | default: `20`, label: "Period" |

## Runtime profile

- Declared optimization: not explicitly annotated in source comments.
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

- Source code: `indicators/statistics/kendall.pine`
- Documentation file: `indicators/statistics/kendall.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/statistics/kendall.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/statistics/kendall.md
