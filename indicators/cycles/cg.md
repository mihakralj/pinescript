# CG - Cg


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. CG addresses this by implementing `Calculates Ehlers' Center of Gravity indicator` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Ehlers' Center of Gravity indicator`

### Parameters

| Parameter | Purpose |
|---|---|
| `src` | Series to calculate Center of Gravity from |
| `length` | Period for the Center of Gravity calculation |

### Returns

- Center of Gravity value identifying cycle turning points

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_length` | `input.int` | default: `10`, label: "Length" |
| `i_source` | `input.source` | default: `close`, label: "Source" |

## Runtime profile

- Declared optimization: for performance and dirty data
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

- Source code: `indicators/cycles/cg.pine`
- Documentation file: `indicators/cycles/cg.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/cycles/cg.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/cycles/cg.md
