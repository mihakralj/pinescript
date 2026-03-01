# TDIST - Tdist


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. TDIST addresses this by implementing `Natural log of the Gamma function via Lanczos approximation (g=7, 9 coefficients)` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Natural log of the Gamma function via Lanczos approximation (g=7, 9 coefficients)`
- `Regularized incomplete beta function I_x(a, b) via Lentz continued fraction`
- `Calculates Student's t-Distribution CDF`

### Parameters

| Parameter | Purpose |
|---|---|
| `z` | Argument (must be > 0) |
| `x` | Upper integration limit in [0, 1] |
| `a` | First shape parameter (> 0) |
| `b` | Second shape parameter (> 0) |
| `source` | Series to evaluate (typically close) |
| `period` | Lookback period for min-max normalization |
| `df` | Degrees of freedom (ν > 0) |

### Returns

- ln(Γ(z))

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_source` | `input.source` | default: `close`, label: "Source" |
| `i_period` | `input.int` | default: `50`, label: "Period" |
| `i_df` | `input.float` | default: `5.0`, label: "Degrees of Freedom" |

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

- Source code: `indicators/numerics/tdist.pine`
- Documentation file: `indicators/numerics/tdist.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/numerics/tdist.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/numerics/tdist.md
