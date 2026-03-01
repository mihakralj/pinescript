# REMA - Rema


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. REMA addresses this by implementing `Calculates REMA using exponential smoothing with regularization term` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates REMA using exponential smoothing with regularization term`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | Series to calculate REMA from |
| `period` | Lookback period used to determine alpha value |
| `lambda` | Regularization parameter (0-1) controlling smoothness |

### Returns

- REMA value, calculates from first bar using available data

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_period` | `input.int` | default: `10`, label: "Period" |
| `i_lambda` | `input.float` | default: `0.5`, label: "Lambda" |
| `i_source` | `input.source` | default: `close`, label: "Source" |

## Runtime profile

- Declared optimization: Uses regularization term to reduce noise for O(1) complexity
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

- Source code: `indicators/trends_IIR/rema.pine`
- Documentation file: `indicators/trends_IIR/rema.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/trends_IIR/rema.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/trends_IIR/rema.md
