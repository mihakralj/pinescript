# BRAR - Brar


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. BRAR addresses this by implementing `Calculates BRAR (BR and AR) sentiment oscillator` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates BRAR (BR and AR) sentiment oscillator`

### Parameters

| Parameter | Purpose |
|---|---|
| `period` | Rolling window length for summation (default 26) |

### Returns

- tuple [br, ar] where BR measures buying pressure vs previous close,

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_period` | `input.int` | default: `26`, label: "Period" |

## Runtime profile

- Declared optimization: Uses 4 circular buffers for O(1) per-bar complexity
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

- Source code: `indicators/oscillators/brar.pine`
- Documentation file: `indicators/oscillators/brar.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/oscillators/brar.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/oscillators/brar.md
