# SGF - Sgf


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. SGF addresses this by implementing `Applies Savitzky-Golay filter to input series` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Applies Savitzky-Golay filter to input series`

### Parameters

| Parameter | Purpose |
|---|---|
| `src` | Input series to filter |
| `window_size` | Window size (rounded down to nearest odd number) |
| `poly_order` | Polynomial order (2 or 4 recommended) |

### Returns

- Filtered series

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_window` | `input.int` | default: `21`, label: "Window Size" |
| `i_order` | `input.int` | default: `2`, label: "Polynomial Order" |
| `i_source` | `input.source` | default: `close`, label: "Source" |

## Runtime profile

- Declared optimization: Uses polynomial convolution with O(n) complexity per bar
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

- Source code: `indicators/filters/sgf.pine`
- Documentation file: `indicators/filters/sgf.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/filters/sgf.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/filters/sgf.md
