# PERCENTILE - Percentile


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. PERCENTILE addresses this by implementing `Calculates the value at a given percentile for a series over a lookback period.` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates the value at a given percentile for a series over a lookback period.`

### Parameters

| Parameter | Purpose |
|---|---|
| `src` | series float Input data series. |
| `len` | simple int Lookback period (must be > 0). |
| `p` | simple float Percentile to calculate (0-100). For example, 50 for median. |

### Returns

- series float The value at the specified percentile, or na if insufficient data.

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_source` | `input.source` | default: `close`, label: "Source" |
| `i_length` | `input.int` | default: `14`, label: "Period" |
| `i_percentile` | `input.float` | default: `25`, label: "Percentile (0-100)" |

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

- Source code: `indicators/statistics/percentile.pine`
- Documentation file: `indicators/statistics/percentile.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/statistics/percentile.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/statistics/percentile.md
