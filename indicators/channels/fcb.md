# FCB - Fcb


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. FCB addresses this by implementing `Calculates Fractal Chaos Bands based on fractal highs and lows` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Fractal Chaos Bands based on fractal highs and lows`

### Parameters

| Parameter | Purpose |
|---|---|
| `period` | Lookback period for highest/lowest calculation |

### Returns

- [upper_band, lower_band] Fractal Chaos Band values

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_period` | `input.int` | default: `20`, label: "Period" |
| `plot_fractal_points` | `input.bool` | default: `false`, label: "Show Fractal Points" |

## Runtime profile

- Declared optimization: Uses monotonic deque for O(1) amortized complexity
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

- Source code: `indicators/channels/fcb.pine`
- Documentation file: `indicators/channels/fcb.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/channels/fcb.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/channels/fcb.md
