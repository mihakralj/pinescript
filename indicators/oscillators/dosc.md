# DOSC - Dosc


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. DOSC addresses this by implementing `Calculates the Derivative Oscillator: double-smoothed RSI minus its SMA signal line` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates the Derivative Oscillator: double-smoothed RSI minus its SMA signal line`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | Series to calculate from |
| `rsiPeriod` | RSI lookback period |
| `ema1Period` | First EMA smoothing period applied to RSI |
| `ema2Period` | Second EMA smoothing period (double smoothing) |
| `sigPeriod` | SMA signal line period applied to double-smoothed RSI |

### Returns

- DOSC value (histogram: double-smoothed RSI minus signal)

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_source` | `input.source` | default: `close`, label: "Source" |
| `i_rsiPeriod` | `input.int` | default: `14`, label: "RSI Period" |
| `i_ema1` | `input.int` | default: `5`, label: "EMA1 Period" |
| `i_ema2` | `input.int` | default: `3`, label: "EMA2 Period" |
| `i_sigPeriod` | `input.int` | default: `9`, label: "Signal Period" |

## Runtime profile

- Declared optimization: O(1) per bar after warmup for all EMA/SMA stages
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

- Source code: `indicators/oscillators/dosc.pine`
- Documentation file: `indicators/oscillators/dosc.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/oscillators/dosc.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/oscillators/dosc.md
