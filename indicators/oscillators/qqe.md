# QQE - Qqe


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. QQE addresses this by implementing `Calculates QQE — smoothed RSI with dynamic volatility bands` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates QQE — smoothed RSI with dynamic volatility bands`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | Series to evaluate (typically close) |
| `rsiPeriod` | RSI lookback period |
| `smoothFactor` | EMA smoothing factor for RSI (SF) |
| `qqeFactor` | Multiplier for the ATR-like trailing band (Wilders factor) |

### Returns

- [qqeLine, trailingLevel] QQE smoothed RSI and its trailing signal

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_source` | `input.source` | default: `close`, label: "Source" |
| `i_rsiPeriod` | `input.int` | default: `14`, label: "RSI Period" |
| `i_smoothFactor` | `input.int` | default: `5`, label: "Smooth Factor" |
| `i_qqeFactor` | `input.float` | default: `4.236`, label: "QQE Factor" |

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

- Source code: `indicators/oscillators/qqe.pine`
- Documentation file: `indicators/oscillators/qqe.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/oscillators/qqe.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/oscillators/qqe.md
