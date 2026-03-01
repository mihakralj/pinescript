# KAISER - Kaiser


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. KAISER addresses this by implementing `I0 approximation (modified Bessel, first kind, order 0) via 25-term power series.` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `I0 approximation (modified Bessel, first kind, order 0) via 25-term power series.`
- `Computes Kaiser Window Moving Average — a symmetric FIR filter using the`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | Series to smooth |
| `period` | Lookback window (>= 2) |
| `beta` | Kaiser shape parameter controlling sidelobe attenuation (default 3.0). |

### Returns

- Kaiser-weighted moving average

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `src` | `input.source` | default: `close`, label: "Source" |
| `per` | `input.int` | default: `14`, label: "Period" |

## Runtime profile

- Declared optimization: O(period) per bar for convolution; weights precomputed once via I0 series
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

- Source code: `indicators/trends_FIR/kaiser.pine`
- Documentation file: `indicators/trends_FIR/kaiser.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/trends_FIR/kaiser.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/trends_FIR/kaiser.md
