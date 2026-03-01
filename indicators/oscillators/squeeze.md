# SQUEEZE - Squeeze


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. SQUEEZE addresses this by implementing `Calculates Squeeze Momentum — BB vs KC squeeze detection with LinReg momentum` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Squeeze Momentum — BB vs KC squeeze detection with LinReg momentum`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | Series to evaluate (typically close) |
| `period` | Lookback period for BB, KC, Donchian midline, and LinReg |
| `bbMult` | Bollinger Band standard deviation multiplier |
| `kcMult` | Keltner Channel ATR multiplier |

### Returns

- [momentum, squeezeOn] momentum histogram and squeeze state (1=on, 0=off)

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_source` | `input.source` | default: `close`, label: "Source" |
| `i_period` | `input.int` | default: `20`, label: "Period" |
| `i_bbMult` | `input.float` | default: `2.0`, label: "BB Multiplier" |
| `i_kcMult` | `input.float` | default: `1.5`, label: "KC Multiplier" |

## Runtime profile

- Declared optimization: not explicitly annotated in source comments.
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

- Source code: `indicators/oscillators/squeeze.pine`
- Documentation file: `indicators/oscillators/squeeze.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/oscillators/squeeze.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/oscillators/squeeze.md
