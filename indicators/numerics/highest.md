# HIGHEST - Highest


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. HIGHEST addresses this by implementing `Highest value over a specified period using a monotonic deque.` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Highest value over a specified period using a monotonic deque.`

### Parameters

| Parameter | Purpose |
|---|---|
| `src` | {series float} Source series. |
| `len` | {int} Lookback length. `len` > 0. |

### Returns

- {series float} Highest value of `src` for `len` bars back. Returns the highest value seen so far during initial bars.

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
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

- Source code: `indicators/numerics/highest.pine`
- Documentation file: `indicators/numerics/highest.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/numerics/highest.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/numerics/highest.md
