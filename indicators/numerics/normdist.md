# NORMDIST - Normdist


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. NORMDIST addresses this by implementing `Computes Normal Distribution CDF for a normalized price series` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Computes Normal Distribution CDF for a normalized price series`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | Series to transform |
| `period` | Lookback period for z-score normalization |
| `mu` | Mean parameter (0.0 for standard normal after z-score) |
| `sigma` | Standard deviation parameter (1.0 for standard normal after z-score) |

### Returns

- CDF value in [0,1]: Φ(z) = 0.5 × (1 + erf(z / √2))

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_source` | `input.source` | default: `close`, label: "Source" |
| `i_period` | `input.int` | default: `50`, label: "Lookback Period" |
| `i_mu` | `input.float` | default: `0.0`, label: "Mu (μ)" |
| `i_sigma` | `input.float` | default: `1.0`, label: "Sigma (σ)" |

## Runtime profile

- Declared optimization: O(period) per bar for mean/variance scan; CDF itself is O(1)
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

- Source code: `indicators/numerics/normdist.pine`
- Documentation file: `indicators/numerics/normdist.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/numerics/normdist.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/numerics/normdist.md
