# LOESS - Loess


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. LOESS addresses this by implementing `Applies LOESS (LOcally Estimated Scatterplot Smoothing) filter` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Applies LOESS (LOcally Estimated Scatterplot Smoothing) filter`

### Parameters

| Parameter | Purpose |
|---|---|
| `src` | Input series to filter |
| `length` | Window size (rounded down to nearest odd number) |

### Returns

- LOESS smoothed series

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_length` | `input.int` | default: `7`, label: "Length" |
| `i_source` | `input.source` | default: `close`, label: "Source" |

## Runtime profile

- Declared optimization: Uses locally weighted regression with O(n) complexity per bar
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

- Source code: `indicators/filters/loess.pine`
- Documentation file: `indicators/filters/loess.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/filters/loess.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/filters/loess.md
