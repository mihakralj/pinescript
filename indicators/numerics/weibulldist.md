# WEIBULLDIST - Weibulldist


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. WEIBULLDIST addresses this by implementing `Calculates the Weibull Distribution CDF` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates the Weibull Distribution CDF`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | Series to evaluate (typically close) |
| `period` | Lookback period for min-max normalization |
| `shape` | Shape parameter k (> 0) — controls distribution form |
| `scale` | Scale parameter λ (> 0) — scales the normalized price |

### Returns

- CDF value F(x) in [0, 1]

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_source` | `input.source` | default: `close`, label: "Source" |
| `i_period` | `input.int` | default: `50`, label: "Period" |
| `i_shape` | `input.float` | default: `2.0`, label: "Shape (k)" |
| `i_scale` | `input.float` | default: `0.5`, label: "Scale (λ)" |

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

- Source code: `indicators/numerics/weibulldist.pine`
- Documentation file: `indicators/numerics/weibulldist.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/numerics/weibulldist.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/numerics/weibulldist.md
