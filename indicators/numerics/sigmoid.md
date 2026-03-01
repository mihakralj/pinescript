# SIGMOID - Sigmoid


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. SIGMOID addresses this by implementing `Applies the logistic (sigmoid) function to a source series.` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Applies the logistic (sigmoid) function to a source series.`

### Parameters

| Parameter | Purpose |
|---|---|
| `src` | The source series. |
| `k` | The steepness factor of the sigmoid curve. Higher k means a steeper curve. |
| `x0` | The x-value of the sigmoid's midpoint (where the output is 0.5). |

### Returns

- The sigmoid transformed series, values between 0 and 1.

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_source` | `input.source` | default: `close`, label: "Source" |
| `i_steepness_k` | `input.float` | default: `0.5`, label: "Steepness (k)" |

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

- Source code: `indicators/numerics/sigmoid.pine`
- Documentation file: `indicators/numerics/sigmoid.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/numerics/sigmoid.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/numerics/sigmoid.md
