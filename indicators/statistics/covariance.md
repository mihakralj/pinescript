# COVARIANCE - Covariance


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. COVARIANCE addresses this by implementing `Calculates covariance using single pass with circular buffer` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates covariance using single pass with circular buffer`

### Parameters

| Parameter | Purpose |
|---|---|
| `src1` | series float First series to analyze |
| `src2` | series float Second series to analyze |
| `len` | simple int Lookback period for calculation |

### Returns

- float Covariance between src1 and src2

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_source1` | `input.source` | default: `close`, label: "Source 1" |
| `i_source2_ticker` | `input.symbol` | default: `"SPY"`, label: "SPY" |
| `i_period` | `input.int` | default: `20`, label: "Period" |

## Runtime profile

- Declared optimization: for performance using circular buffer
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

- Source code: `indicators/statistics/covariance.pine`
- Documentation file: `indicators/statistics/covariance.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/statistics/covariance.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/statistics/covariance.md
