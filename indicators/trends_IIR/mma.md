# MMA - Mma


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. MMA addresses this by implementing `Calculates MMA using combined simple and weighted moving average components` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates MMA using combined simple and weighted moving average components`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | Series to calculate MMA from |
| `period` | Lookback period - must be at least 2 |

### Returns

- MMA value, combines SMA with weighted component for balanced smoothing

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_period` | `input.int` | default: `10`, label: "Period" |
| `i_source` | `input.source` | default: `close`, label: "Source" |

## Runtime profile

- Declared optimization: Uses circular buffer for O(1) sum updates, O(n) for weighted component
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

- Source code: `indicators/trends_IIR/mma.pine`
- Documentation file: `indicators/trends_IIR/mma.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/trends_IIR/mma.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/trends_IIR/mma.md
