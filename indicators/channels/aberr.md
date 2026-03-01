# ABERR - Aberr


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. ABBER addresses this by implementing `Calculates Aberration bands measuring deviation from a central moving average` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Aberration bands measuring deviation from a central moving average`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | Series to calculate aberration from |
| `ma_line` | Pre-calculated moving average line |
| `period` | Lookback period for deviation calculation |
| `multiplier` | Multiplier for deviation bands |

### Returns

- [upper_band, lower_band, deviation] Aberration band values and deviation

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_source` | `input.source` | default: `close`, label: "Source" |
| `i_period` | `input.int` | default: `20`, label: "Period" |
| `i_ma_type` | `input.string` | default: `"SMA"`, label: "SMA" |
| `i_multiplier` | `input.float` | default: `2.0`, label: "Deviation Multiplier" |
| `i_show_ma` | `input.bool` | default: `true`, label: "Show Moving Average Line" |

## Runtime profile

- Declared optimization: Uses simple deviation averaging with O(n) complexity
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

- Source code: `indicators/channels/aberr.pine`
- Documentation file: `indicators/channels/aberr.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/channels/aberr.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/channels/aberr.md
