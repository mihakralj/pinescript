# QSTICK - Qstick


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. QSTICK addresses this by implementing `Calculates Qstick (moving average of close-open difference)` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Qstick (moving average of close-open difference)`

### Parameters

| Parameter | Purpose |
|---|---|
| `source_close` | Closing price series |
| `source_open` | Opening price series |
| `length` | Lookback period for moving average |
| `use_ema` | Use EMA (true) or SMA (false) |

### Returns

- Qstick value

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_length` | `input.int` | default: `14`, label: "Length" |
| `i_ma_type` | `input.string` | default: `"SMA"`, label: "SMA" |
| `i_source_close` | `input.source` | default: `close`, label: "Close Source" |
| `i_source_open` | `input.source` | default: `open`, label: "Open Source" |

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

- Source code: `indicators/dynamics/qstick.pine`
- Documentation file: `indicators/dynamics/qstick.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/dynamics/qstick.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/dynamics/qstick.md
