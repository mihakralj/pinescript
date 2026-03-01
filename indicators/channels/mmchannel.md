# MMCHANNEL - Mmchannel


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. MMCHANNEL addresses this by implementing `Calculates the Min-Max Channel efficiently using monotonic deques` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates the Min-Max Channel efficiently using monotonic deques`

### Parameters

| Parameter | Purpose |
|---|---|
| `hi` | Source series for the highest high calculation (usually high) |
| `lo` | Source series for the lowest low calculation (usually low) |
| `period` | Lookback period (period > 0) |

### Returns

- Tuple containing [highest_high, lowest_low]

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_period` | `input.int` | default: `20`, label: "Period" |
| `i_high` | `input.source` | default: `high`, label: "High Source" |
| `i_low` | `input.source` | default: `low`, label: "Low Source" |

## Runtime profile

- Declared optimization: Uses monotonic deque for O(1) amortized complexity per bar
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

- Source code: `indicators/channels/mmchannel.pine`
- Documentation file: `indicators/channels/mmchannel.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/channels/mmchannel.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/channels/mmchannel.md
