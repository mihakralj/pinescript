# Bessel Filter (2nd Order)

The Bessel Filter is a type of linear filter known for its maximally flat group delay (linear phase response) in the passband. This characteristic preserves the wave shape of filtered signals in the passband, making it ideal for applications where transient response is critical. This implementation uses coefficients derived from John Ehlers' work for a 2nd-order low-pass Bessel filter.

[Pine Script Implementation of Bessel Filter](https://github.com/mihakralj/pinescript/blob/main/indicators/filters/bessel.pine)

## Mathematical Foundation

The filter is implemented as a 2nd-order Infinite Impulse Response (IIR) filter. The general form is:

Filt[n] = c1 × Src[n] + c2 × Filt[n-1] + c3 × Filt[n-2]

Where the coefficients `c1`, `c2`, and `c3` are derived to approximate the Bessel filter characteristics based on the desired cutoff period (`length`):

- `a = exp(-π / length)`
- `b = 2 × a × cos(1.738 × π / length)` (where 1.738 ≈ √3)
- `c2 = b`
- `c3 = -a × a`
- `c1 = 1 - c2 - c3`

The `length` parameter relates to the filter's cutoff frequency, influencing how much smoothing is applied.

## Implementation Details

1. **Coefficient Calculation**:
    - Coefficients `c1`, `c2`, `c3` are calculated based on the input `length`.
    - The calculation uses exponential and trigonometric functions derived from the continuous-time Bessel filter transfer function transformed to the discrete-time domain.
    - `safe_length` ensures the period is at least 2 to prevent division by zero or instability in calculations.

2. **Filtering Process**:
    - Implemented as a recursive IIR filter.
    - The current output `filt` depends on the current input `src` and the two previous filter outputs (`filt[1]`, `filt[2]`).
    - Initialization handles the first few bars where previous filter values are not yet available.

## Advantages and Disadvantages

### Advantages

- **Linear Phase Response**: Maximally flat group delay in the passband preserves signal shape and minimizes overshoot/ringing in response to steps.
- **Good Transient Response**: Handles abrupt changes in the input signal well.
- **Smooth Roll-off**: Provides a gradual transition from passband to stopband.

### Disadvantages

- **Slower Roll-off**: Attenuates frequencies beyond the cutoff less sharply compared to filters like Butterworth or Chebyshev of the same order.
- **Moderate Lag**: Introduces some lag, although the linear phase characteristic makes the lag consistent across frequencies in the passband.
- **Parameter Sensitivity**: The `length` parameter significantly impacts the smoothing and lag.
