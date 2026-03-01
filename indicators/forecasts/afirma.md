# AFIRMA - Afirma


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. AFIRMA addresses this by implementing `Calculates AFIRMA using various windowing functions with optional least squares cubic spline fitting` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates AFIRMA using various windowing functions with optional least squares cubic spline fitting`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | Series to calculate AFIRMA from |
| `period` | Lookback period - window size |
| `windowType` | Window function type (1:Hanning, 2:Hamming, 3:Blackman, 4:Blackman-Harris) |
| `leastSquares` | Apply least squares cubic polynomial fitting for autoregressive prediction |

### Returns

- AFIRMA value, calculates from first bar using available data

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_period` | `input.int` | default: `20`, label: "Period" |
| `i_source` | `input.source` | default: `close`, label: "Source" |
| `i_windowType` | `input.int` | default: `4`, label: "Window Function" |
| `i_leastSquares` | `input.bool` | default: `false`, label: "Least Squares Method" |

## Runtime profile

- Declared optimization: Uses windowing functions with O(n) complexity; least squares adds O(n) for polynomial fitting
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

- Source code: `indicators/forecasts/afirma.pine`
- Documentation file: `indicators/forecasts/afirma.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/forecasts/afirma.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/forecasts/afirma.md
