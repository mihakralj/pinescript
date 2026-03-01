# EWMA - Ewma


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. EWMA VOLTY addresses this by implementing `Calculates Exponential Weighted Moving Average (EWMA) Volatility.` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Exponential Weighted Moving Average (EWMA) Volatility.`

### Parameters

| Parameter | Purpose |
|---|---|
| `src` | The source series for price data. Default is close. |
| `length` | The period length for the EWMA calculation. |
| `annualize` | Boolean to indicate if the volatility should be annualized. Default is true. |
| `annualPeriods` | Number of periods in a year for annualization. Default is 252 for daily data. |

### Returns

- float The EWMA Volatility value.

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_source` | `input.source` | default: `close`, label: "Source" |
| `i_length` | `input.int` | default: `20`, label: "Length" |
| `i_annualize` | `input.bool` | default: `true`, label: "Annualize Volatility" |
| `i_annualPeriods` | `input.int` | default: `252`, label: "Annual Periods" |

## Runtime profile

- Declared optimization: for performance and dirty data
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

- Source code: `indicators/volatility/ewma.pine`
- Documentation file: `indicators/volatility/ewma.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/volatility/ewma.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/volatility/ewma.md
