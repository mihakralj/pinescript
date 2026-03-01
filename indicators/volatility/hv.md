# HV - Hv


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. HV addresses this by implementing `Calculates Historical Volatility (Close-to-Close).` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Historical Volatility (Close-to-Close).`

### Parameters

| Parameter | Purpose |
|---|---|
| `src_price` | The source series to calculate returns from. Default is close. |
| `length_hv` | The period length for calculating the standard deviation of returns. |
| `annualize` | Boolean to indicate if the volatility should be annualized. Default is true. |
| `annualPeriods` | Number of periods in a year for annualization. Default is 252 for daily data. |

### Returns

- float The Historical Volatility value.

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

- Source code: `indicators/volatility/hv.pine`
- Documentation file: `indicators/volatility/hv.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/volatility/hv.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/volatility/hv.md
