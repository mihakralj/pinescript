# HOLT - Holt


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. HOLT addresses this by implementing `Calculates Holt EMA using double exponential smoothing (level + trend)` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Holt EMA using double exponential smoothing (level + trend)`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | Series to smooth |
| `period` | Lookback period (determines alpha = 2/(period+1)) |
| `gamma` | Trend smoothing factor (0..1). Default: same as alpha |

### Returns

- Holt EMA value (level + trend) from first bar

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_period` | `input.int` | default: `10`, label: "Period" |
| `i_gamma` | `input.float` | default: `0`, label: "Gamma (0 = auto)" |
| `i_source` | `input.source` | default: `close`, label: "Source" |

## Runtime profile

- Declared optimization: not explicitly annotated in source comments.
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

- Source code: `indicators/trends_IIR/holt.pine`
- Documentation file: `indicators/trends_IIR/holt.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/trends_IIR/holt.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/trends_IIR/holt.md
