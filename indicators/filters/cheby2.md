# CHEBY2 - Cheby2


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. CHEBY2 addresses this by implementing `Calculates 2nd Order Chebyshev Type II Lowpass Filter` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates 2nd Order Chebyshev Type II Lowpass Filter`

### Parameters

| Parameter | Purpose |
|---|---|
| `src` | Series to calculate Chebyshev filter from |
| `length` | Cutoff period (related to cutoff frequency) |
| `attenuation` | Stopband attenuation in decibels (dB) > 0 |

### Returns

- Chebyshev Type II filter value

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_length` | `input.int` | default: `10`, label: "Length" |
| `i_attenuation` | `input.float` | default: `5.0`, label: "Stopband Attenuation (dB)" |
| `i_source` | `input.source` | default: `close`, label: "Source" |

## Runtime profile

- Declared optimization: Uses IIR 2nd order Chebyshev Type II filter with O(1) complexity per bar
- Streaming model: single-pass update on each new bar.
- Warm-up behavior: outputs can be unstable until enough samples satisfy `length`.
- Memory model: state is kept in Pine series context rather than external buffers.

## Trade-offs

Streaming logic keeps incremental cost stable, but initialization and edge-case handling become first-class concerns. That is a deliberate choice: predictable execution beats opaque recalculation spikes in live charts.

## Verification checklist

1. Open the script in TradingView and confirm it compiles under Pine Script v6.
2. Validate warm-up behavior on sparse data and short histories.
3. Compare output against a trusted reference implementation for the same parameters.
4. Confirm parameter bounds reject invalid values without silent fallback.

## References

- Source code: `indicators/filters/cheby2.pine`
- Documentation file: `indicators/filters/cheby2.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/filters/cheby2.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/filters/cheby2.md
