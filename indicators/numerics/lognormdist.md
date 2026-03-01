# LOGNORMDIST - Lognormdist


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. LOGNORMDIST addresses this by implementing `Standard normal CDF Φ(z) via Abramowitz & Stegun rational approximation (7.1.26)` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Standard normal CDF Φ(z) via Abramowitz & Stegun rational approximation (7.1.26)`
- `Log-Normal Distribution CDF for a normalized price series`

### Parameters

| Parameter | Purpose |
|---|---|
| `z` | Input value |
| `source` | Series to transform |
| `period` | Lookback period for min-max normalization |
| `mu` | Location parameter (mean of ln(X)) |
| `sigma` | Scale parameter (std dev of ln(X)), sigma > 0 |

### Returns

- Φ(z) = P(Z <= z) for Z ~ N(0,1), accurate to ~1.5e-7

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_source` | `input.source` | default: `close`, label: "Source" |
| `i_period` | `input.int` | default: `50`, label: "Lookback Period" |
| `i_mu` | `input.float` | default: `0.0`, label: "Mu (μ)" |
| `i_sigma` | `input.float` | default: `1.0`, label: "Sigma (σ)" |

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

- Source code: `indicators/numerics/lognormdist.pine`
- Documentation file: `indicators/numerics/lognormdist.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/numerics/lognormdist.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/numerics/lognormdist.md
