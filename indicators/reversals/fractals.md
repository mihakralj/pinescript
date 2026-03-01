# FRACTALS - Fractals


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. FRACTALS addresses this by implementing `Detects Williams Fractal patterns (5-bar pattern)` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Detects Williams Fractal patterns (5-bar pattern)`

### Returns

- Tuple [up_fractal, down_fractal] with fractal values (na if no fractal)

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_show_up` | `input.bool` | default: `true`, label: "Show Up Fractals" |
| `i_show_down` | `input.bool` | default: `true`, label: "Show Down Fractals" |
| `i_color_up` | `input.color` | default: `color.red`, label: "Up Fractal Color" |
| `i_color_down` | `input.color` | default: `color.green`, label: "Down Fractal Color" |

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

- Source code: `indicators/reversals/fractals.pine`
- Documentation file: `indicators/reversals/fractals.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/reversals/fractals.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/reversals/fractals.md
