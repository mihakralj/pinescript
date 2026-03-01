# STOCHRSI - Stochrsi


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. STOCHRSI addresses this by implementing `Calculates Stochastic RSI oscillator` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Stochastic RSI oscillator`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | Source series to calculate STOCHRSI for |
| `rsi_length` | Period for RSI calculation |
| `stoch_length` | Lookback period for Stochastic calculation on RSI |
| `k_smooth` | Smoothing period for %K line |
| `d_smooth` | Smoothing period for %D line |

### Returns

- [%K, %D] values of Stochastic RSI

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_rsi_length` | `input.int` | default: `14`, label: "RSI Length" |
| `i_stoch_length` | `input.int` | default: `14`, label: "Stochastic Length" |
| `i_k_smooth` | `input.int` | default: `3`, label: "%K Smooth" |
| `i_d_smooth` | `input.int` | default: `3`, label: "%D Smooth" |
| `i_source` | `input.source` | default: `close`, label: "Source" |

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

- Source code: `indicators/oscillators/stochrsi.pine`
- Documentation file: `indicators/oscillators/stochrsi.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/oscillators/stochrsi.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/oscillators/stochrsi.md
