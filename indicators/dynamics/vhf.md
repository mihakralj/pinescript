# VHF - Vhf


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. VHF addresses this by implementing `Calculates Vertical Horizontal Filter using max-min range vs sum of absolute changes` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Vertical Horizontal Filter using max-min range vs sum of absolute changes`

### Parameters

| Parameter | Purpose |
|---|---|
| `period` | Lookback period for range and path measurement (default: 28) |

### Returns

- VHF value (positive, typically 0 to 1; higher = trending, lower = ranging)

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_period` | `input.int` | default: `28`, label: "Period" |
| `i_trendThreshold` | `input.float` | default: `0.40`, label: "Trend Threshold" |
| `i_rangeThreshold` | `input.float` | default: `0.25`, label: "Range Threshold" |

## Runtime profile

- Declared optimization: O(1) per bar via circular buffer with running sum + deque-based min/max tracking
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

- Source code: `indicators/dynamics/vhf.pine`
- Documentation file: `indicators/dynamics/vhf.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/dynamics/vhf.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/dynamics/vhf.md
