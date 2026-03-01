# CHANGE - Change


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. CHANGE addresses this by implementing `Calculates the percentage change of a source series over a specified length using the history referencing operator for efficiency.` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates the percentage change of a source series over a specified length using the history referencing operator for efficiency.`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | The source series (e.g. close price). |
| `length` | The lookback period (number of bars). Must be > 0. |

### Returns

- float The percentage change over the specified length. Returns `na` if the historical value is `na` or zero.

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_source` | `input.source` | default: `close`, label: "Source" |
| `i_length` | `input.int` | default: `1`, label: "Length" |

## Runtime profile

- Declared optimization: Uses direct history access `source[length]` instead of array manipulation.
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

- Source code: `indicators/numerics/change.pine`
- Documentation file: `indicators/numerics/change.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/numerics/change.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/numerics/change.md
