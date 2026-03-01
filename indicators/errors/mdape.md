# MDAPE - Mdape


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. MDAPE addresses this by implementing `Calculates Median Absolute Percentage Error` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Median Absolute Percentage Error`

### Parameters

| Parameter | Purpose |
|---|---|
| `actual` | Series of actual values |
| `predicted` | Series of predicted/forecast values |
| `length` | Rolling window for median calculation |

### Returns

- MdAPE value as percentage

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_length` | `input.int` | default: `14`, label: "Length" |
| `i_actual` | `input.source` | default: `close`, label: "Actual" |
| `i_predicted` | `input.source` | default: `open`, label: "Predicted" |

## Runtime profile

- Declared optimization: not explicitly annotated in source comments.
- Streaming model: single-pass update on each new bar.
- Warm-up behavior: outputs can be unstable until enough samples satisfy `length`.
- Memory model: state is kept in Pine series context rather than external buffers.

## Trade-offs

Streaming logic keeps incremental cost stable, but initialization and edge-case handling become first-class concerns. That is a deliberate choice: predictable execution beats opaque recalculation spikes in live charts.

## Verification checklist

1. Open the script in TradingView and confirm it compiles under Pine Script v6.
2. Validate warm-up behavior on sparse data and short histories.
3. Compare output against a trusted reference implementation for the same parameters.
4. Confirm parameter bounds reject invalid values without silent fallback.

## References

- Source code: `indicators/errors/mdape.pine`
- Documentation file: `indicators/errors/mdape.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/errors/mdape.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/errors/mdape.md
