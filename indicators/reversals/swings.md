# SWINGS - Swings


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. SWINGS addresses this by implementing `Detects swing highs and swing lows using lookback period` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Detects swing highs and swing lows using lookback period`

### Parameters

| Parameter | Purpose |
|---|---|
| `lookback` | Number of bars on each side to confirm swing point |
| `source_high` | Price series for swing high detection (typically high) |
| `source_low` | Price series for swing low detection (typically low) |

### Returns

- Tuple [swing_high, swing_low] with swing point values (na if no swing)

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_lookback` | `input.int` | default: `5`, label: "Lookback Period" |
| `i_source_high` | `input.source` | default: `high`, label: "Source High" |
| `i_source_low` | `input.source` | default: `low`, label: "Source Low" |
| `i_show_high` | `input.bool` | default: `true`, label: "Show Swing High Lines" |
| `i_show_low` | `input.bool` | default: `true`, label: "Show Swing Low Lines" |
| `i_color_high` | `input.color` | default: `color.red`, label: "Swing High Color" |
| `i_color_low` | `input.color` | default: `color.green`, label: "Swing Low Color" |

## Runtime profile

- Declared optimization: not explicitly annotated in source comments.
- Streaming model: single-pass update on each new bar.
- Warm-up behavior: outputs can be unstable until enough samples satisfy `lookback`.
- Memory model: state is kept in Pine series context rather than external buffers.

## Trade-offs

Streaming logic keeps incremental cost stable, but initialization and edge-case handling become first-class concerns. That is a deliberate choice: predictable execution beats opaque recalculation spikes in live charts.

## Verification checklist

1. Open the script in TradingView and confirm it compiles under Pine Script v6.
2. Validate warm-up behavior on sparse data and short histories.
3. Compare output against a trusted reference implementation for the same parameters.
4. Confirm parameter bounds reject invalid values without silent fallback.

## References

- Source code: `indicators/reversals/swings.pine`
- Documentation file: `indicators/reversals/swings.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/reversals/swings.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/reversals/swings.md
