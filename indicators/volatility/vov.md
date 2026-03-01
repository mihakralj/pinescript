# VOV - Vov


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. VOV addresses this by implementing `Calculates the Volatility of Volatility (VOV) with embedded rolling standard deviation algorithms.` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates the Volatility of Volatility (VOV) with embedded rolling standard deviation algorithms.`

### Parameters

| Parameter | Purpose |
|---|---|
| `src` | The source series. Default is `close`. |
| `volatilityPeriod` | The lookback period for the initial volatility calculation. Default is 20. |
| `vovPeriod` | The lookback period for calculating the standard deviation of the volatility series. Default is 10. |

### Returns

- float The VOV value.

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_src` | `input.source` | default: `close`, label: "Source" |
| `i_volatilityPeriod` | `input.int` | default: `20`, label: "Volatility Period" |
| `i_vovPeriod` | `input.int` | default: `10`, label: "VOV Period" |

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

- Source code: `indicators/volatility/vov.pine`
- Documentation file: `indicators/volatility/vov.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/volatility/vov.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/volatility/vov.md
