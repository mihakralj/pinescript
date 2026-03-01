# LMS - Lms


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. LMS addresses this by implementing `Applies Widrow-Hoff LMS adaptive FIR filter to input series` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Applies Widrow-Hoff LMS adaptive FIR filter to input series`

### Parameters

| Parameter | Purpose |
|---|---|
| `src` | Input series to filter |
| `order` | Number of FIR filter taps (adaptive weights) |
| `mu` | Step size (learning rate) controlling adaptation speed |

### Returns

- Adaptively filtered series

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_order` | `input.int` | default: `16`, label: "Filter Order (taps)" |
| `i_mu` | `input.float` | default: `0.5`, label: "Learning Rate (mu)" |
| `i_source` | `input.source` | default: `close`, label: "Source" |

## Runtime profile

- Declared optimization: Uses normalized LMS weight update with O(order) complexity per bar
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

- Source code: `indicators/filters/lms.pine`
- Documentation file: `indicators/filters/lms.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/filters/lms.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/filters/lms.md
