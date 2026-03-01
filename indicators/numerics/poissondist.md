# POISSONDIST - Poissondist


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. POISSONDIST addresses this by implementing `Log-gamma via Lanczos approximation (g=7, 9 coefficients)` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Log-gamma via Lanczos approximation (g=7, 9 coefficients)`
- `Regularized lower incomplete gamma P(a,x) via series expansion`
- `Regularized upper incomplete gamma Q(a,x) via continued fraction (Lentz)`
- `Regularized lower incomplete gamma function P(a,x)`
- `Computes Poisson Distribution CDF for a normalized price series`

### Parameters

| Parameter | Purpose |
|---|---|
| `z` | Input value (z > 0) |
| `a` | Shape parameter (a > 0) |
| `x` | Evaluation point (x >= 0) |
| `a` | Shape parameter (a > 0) |
| `x` | Evaluation point (x >= 0) |
| `a` | Shape parameter (a > 0) |
| `x` | Evaluation point (x >= 0) |
| `source` | Series to transform |
| `period` | Lookback period for min-max normalization |
| `k` | Threshold count (non-negative integer); P(X <= k) |
| `lambda_scale` | Scale factor applied to normalized price to produce lambda |

### Returns

- ln(Gamma(z))

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_source` | `input.source` | default: `close`, label: "Source" |
| `i_period` | `input.int` | default: `50`, label: "Lookback Period" |
| `i_k` | `input.int` | default: `5`, label: "Threshold (k)" |
| `i_lambda_scale` | `input.float` | default: `10.0`, label: "Lambda Scale" |

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

- Source code: `indicators/numerics/poissondist.pine`
- Documentation file: `indicators/numerics/poissondist.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/numerics/poissondist.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/numerics/poissondist.md
