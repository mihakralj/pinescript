# BBWP - Bbwp


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. BBWP addresses this by implementing `Calculates Bollinger Band Width Percentile relative to historical range` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Bollinger Band Width Percentile relative to historical range`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | Series to calculate Bollinger Bands from |
| `period` | Lookback period for BB calculations |
| `multiplier` | Standard deviation multiplier for band width |
| `lookback` | Historical lookback period for percentile calculation |

### Returns

- BBWP value representing current BBW percentile in historical range

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_period` | `input.int` | default: `20`, label: "Period" |
| `i_source` | `input.source` | default: `close`, label: "Source" |
| `i_multiplier` | `input.float` | default: `2.0`, label: "StdDev Multiplier" |
| `i_lookback` | `input.int` | default: `252`, label: "Lookback Period" |

## Runtime profile

- Declared optimization: for performance and dirty data
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

- Source code: `indicators/volatility/bbwp.pine`
- Documentation file: `indicators/volatility/bbwp.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/volatility/bbwp.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/volatility/bbwp.md
