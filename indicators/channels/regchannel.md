# REGCHANNEL - Regchannel


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. REGCHANNEL addresses this by implementing `Calculates Regression Channels with parallel lines equidistant from a central linear regression line` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Regression Channels with parallel lines equidistant from a central linear regression line`

### Parameters

| Parameter | Purpose |
|---|---|
| `period` | Lookback period for regression calculation (period > 1) |
| `source` | Source series for regression calculation (usually close) |
| `multiplier` | Distance multiplier for channel bands (multiplier > 0) |

### Returns

- Tuple containing [upper_band, regression_line, lower_band]

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_period` | `input.int` | default: `20`, label: "Period" |
| `i_source` | `input.source` | default: `close`, label: "Source" |
| `i_multiplier` | `input.float` | default: `2.0`, label: "Standard Deviation Multiplier" |

## Runtime profile

- Declared optimization: Uses linear regression with O(n) complexity per bar
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

- Source code: `indicators/channels/regchannel.pine`
- Documentation file: `indicators/channels/regchannel.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/channels/regchannel.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/channels/regchannel.md
