# ZTEST - Ztest


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. T-TEST addresses this by implementing `Calculates the t-statistic for a one-sample hypothesis test` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates the t-statistic for a one-sample hypothesis test`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | Source series to test (use returns for meaningful results) |
| `period` | Lookback period for calculating sample mean and standard deviation |
| `mu0` | Hypothesized population mean to test against |

### Returns

- t-statistic (positive values indicate sample mean > mu0, negative indicate sample mean < mu0)

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_source` | `input.source` | default: `close`, label: "Source" |
| `i_period` | `input.int` | default: `30`, label: "Period" |
| `i_mu0` | `input.float` | default: `0.0`, label: "Hypothesized Mean (μ₀)" |

## Runtime profile

- Declared optimization: Uses circular buffer with running sums for O(1) complexity, Bessel correction for sample variance
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

- Source code: `indicators/statistics/ztest.pine`
- Documentation file: `indicators/statistics/ztest.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/statistics/ztest.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/statistics/ztest.md
