# BETADIST - Betadist


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. BETADIST addresses this by implementing `Log-gamma via Lanczos approximation (g=7, 9 coefficients)` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Log-gamma via Lanczos approximation (g=7, 9 coefficients)`
- `Regularized incomplete beta function I_x(a,b) via continued fraction (Lentz)`
- `Computes Beta Distribution CDF for a normalized price series`

### Parameters

| Parameter | Purpose |
|---|---|
| `z` | Input value (z > 0) |
| `x` | Evaluation point (0 <= x <= 1) |
| `a` | Shape parameter alpha (a > 0) |
| `b` | Shape parameter beta (b > 0) |
| `source` | Series to transform |
| `period` | Lookback period for min-max normalization to [0,1] |
| `alpha` | Shape parameter alpha (controls left skew) |
| `beta_param` | Shape parameter beta (controls right skew) |

### Returns

- ln(Gamma(z))

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_source` | `input.source` | default: `close`, label: "Source" |
| `i_period` | `input.int` | default: `50`, label: "Lookback Period" |
| `i_alpha` | `input.float` | default: `2.0`, label: "Alpha (α)" |
| `i_beta` | `input.float` | default: `2.0`, label: "Beta (β)" |

## Runtime profile

- Declared optimization: Lentz continued fraction converges in ~10-20 iterations for typical parameters
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

- Source code: `indicators/numerics/betadist.pine`
- Documentation file: `indicators/numerics/betadist.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/numerics/betadist.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/numerics/betadist.md
