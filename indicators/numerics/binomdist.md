# BINOMDIST - Binomdist


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. BINOMDIST addresses this by implementing `Log-gamma via Lanczos approximation (g=7, 9 coefficients)` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Log-gamma via Lanczos approximation (g=7, 9 coefficients)`
- `Log of binomial coefficient C(n, i) = ln(n!) - ln(i!) - ln((n-i)!)`
- `Binomial Distribution CDF: P(X <= k) = sum_{i=0}^{k} C(n,i) * p^i * (1-p)^(n-i)`
- `Computes Binomial Distribution CDF for a normalized price series`

### Parameters

| Parameter | Purpose |
|---|---|
| `z` | Input value (z > 0) |
| `n` | Number of trials |
| `i` | Number of successes |
| `p` | Probability of success per trial (0 <= p <= 1) |
| `n` | Number of trials |
| `k` | Threshold (compute P(X <= k)) |
| `source` | Series to transform |
| `period` | Lookback period for min-max normalization to [0,1] as probability p |
| `trials` | Number of Bernoulli trials (n) |
| `threshold` | Success threshold (k) — compute P(X <= k) |

### Returns

- ln(Gamma(z))

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_source` | `input.source` | default: `close`, label: "Source" |
| `i_period` | `input.int` | default: `50`, label: "Lookback Period" |
| `i_trials` | `input.int` | default: `20`, label: "Trials (n)" |
| `i_threshold` | `input.int` | default: `10`, label: "Threshold (k)" |

## Runtime profile

- Declared optimization: Log-space summation avoids factorial overflow for large n
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

- Source code: `indicators/numerics/binomdist.pine`
- Documentation file: `indicators/numerics/binomdist.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/numerics/binomdist.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/numerics/binomdist.md
