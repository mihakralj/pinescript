# YZVAMA - Yzvama


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. YZVAMA addresses this by implementing `Calculates YZVAMA by adjusting MA length based on percentile rank of short-term YZV` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates YZVAMA by adjusting MA length based on percentile rank of short-term YZV`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | Series to calculate YZVAMA from |
| `yzv_short_period` | Short-term YZV period for current volatility |
| `yzv_long_period` | Long-term YZV period for baseline volatility |
| `percentile_lookback` | Lookback for percentile calculation |
| `min_length` | Minimum allowed adjusted length |
| `max_length` | Maximum allowed adjusted length |

### Returns

- YZVAMA value

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_source` | `input.source` | default: `close`, label: "Source" |
| `i_yzv_short` | `input.int` | default: `3`, label: "Short YZV Period" |
| `i_yzv_long` | `input.int` | default: `50`, label: "Long YZV Period" |
| `i_percentile_lookback` | `input.int` | default: `100`, label: "Percentile Lookback" |
| `i_min_length` | `input.int` | default: `5`, label: "Minimum Length" |
| `i_max_length` | `input.int` | default: `100`, label: "Maximum Length" |

## Runtime profile

- Declared optimization: Uses RMA compensators for YZV and circular buffers for O(1) sum updates
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

- Source code: `indicators/trends_IIR/yzvama.pine`
- Documentation file: `indicators/trends_IIR/yzvama.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/trends_IIR/yzvama.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/trends_IIR/yzvama.md
