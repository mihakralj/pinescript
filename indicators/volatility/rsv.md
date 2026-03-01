# RSV - Rsv


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. RSV addresses this by implementing `Calculates Rogers-Satchell Volatility.` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Rogers-Satchell Volatility.`

### Parameters

| Parameter | Purpose |
|---|---|
| `length` | The lookback period for the SMA smoothing of the Rogers-Satchell variance. Default is 20. |
| `annualize` | Boolean to indicate if the volatility should be annualized. Default is true. |
| `annualPeriods` | Number of periods in a year for annualization. Default is 252 for daily data. |

### Returns

- float The Rogers-Satchell Volatility value.

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_length_rsv` | `input.int` | default: `20`, label: "Length" |
| `i_annualize_rsv` | `input.bool` | default: `true`, label: "Annualize Volatility" |
| `i_annualPeriods_rsv` | `input.int` | default: `252`, label: "Annual Periods" |

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

- Source code: `indicators/volatility/rsv.pine`
- Documentation file: `indicators/volatility/rsv.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/volatility/rsv.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/volatility/rsv.md
