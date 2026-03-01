# RAVI - Ravi


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. RAVI addresses this by implementing `Calculates Range Action Verification Index using short/long SMA divergence` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Range Action Verification Index using short/long SMA divergence`

### Parameters

| Parameter | Purpose |
|---|---|
| `shortPeriod` | Lookback period for fast SMA (default: 7, ~10% of longPeriod) |
| `longPeriod` | Lookback period for slow SMA (default: 65, ~13 weeks daily) |

### Returns

- RAVI value as absolute percentage divergence between short and long SMAs

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_short` | `input.int` | default: `7`, label: "Short Period" |
| `i_long` | `input.int` | default: `65`, label: "Long Period" |
| `i_threshold` | `input.float` | default: `3.0`, label: "Threshold" |

## Runtime profile

- Declared optimization: O(1) per bar via circular buffer running sums for both SMAs
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

- Source code: `indicators/dynamics/ravi.pine`
- Documentation file: `indicators/dynamics/ravi.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/dynamics/ravi.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/dynamics/ravi.md
