# BOP - Bop


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. BOP addresses this by implementing `Calculates Balance of Power with optional smoothing` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Balance of Power with optional smoothing`

### Parameters

| Parameter | Purpose |
|---|---|
| `length` | Smoothing period (0 for no smoothing) |

### Returns

- BOP value measuring buying/selling pressure

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_smooth` | `input.int` | default: `14`, label: "Smoothing Length" |

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

- Source code: `indicators/momentum/bop.pine`
- Documentation file: `indicators/momentum/bop.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/momentum/bop.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/momentum/bop.md
