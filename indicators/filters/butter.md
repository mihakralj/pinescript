# Butterworth Filter (2nd Order)

The Butterworth Filter is a type of signal processing filter designed to have a frequency response that is as flat as possible in the passband (maximally flat magnitude response). It offers a good balance between attenuation steepness and phase linearity, although its phase response is not as linear as a Bessel filter. This implementation provides a 2nd-order low-pass Butterworth filter using coefficients derived via the Bilinear Transform method.

[Pine Script Implementation of Butterworth Filter](https://github.com/mihakralj/pinescript/blob/main/indicators/filters/butter.pine)

## Mathematical Foundation

The filter is implemented as a 2nd-order Infinite Impulse Response (IIR) filter using the difference equation derived from the Bilinear Transform of the continuous-time Butterworth prototype:

`a0 × y[n] = b0 × x[n] + b1 × x[n-1] + b2 × x[n-2] - a1 × y[n-1] - a2 × y[n-2]`

Rearranging for `y[n]`:

`y[n] = (b0 × x[n] + b1 × x[n-1] + b2 × x[n-2] - a1 × y[n-1] - a2 × y[n-2]) / a0`

Where `x[n]` is the input (`src`), `y[n]` is the output (`filt`), and the coefficients are calculated based on the cutoff period (`length`):

- `omega = 2 × π / length`
- `alpha = sin(omega) / sqrt(2)` (Defines Q factor for Butterworth)
- `a0 = 1 + alpha`
- `a1 = -2 × cos(omega)`
- `a2 = 1 - alpha`
- `b0 = (1 - cos(omega)) / 2`
- `b1 = 1 - cos(omega)`
- `b2 = (1 - cos(omega)) / 2`

The `length` parameter determines the cutoff frequency (-3dB point) of the filter.

## Implementation Details

1.  **Coefficient Calculation**:
    - Coefficients `a0`, `a1`, `a2`, `b0`, `b1`, `b2` are calculated based on the input `length` using standard digital filter design formulas derived from the Bilinear Transform.
    - `safe_length` ensures the period is at least 2.

2.  **Filtering Process**:
    - Implemented as a recursive IIR filter using the calculated coefficients.
    - The current output `filt` depends on the current input `src`, the two previous inputs (`src[1]`, `src[2]`), and the two previous filter outputs (`filt[1]`, `filt[2]`).
    - Initialization handles the first few bars.

## Advantages and Disadvantages

### Advantages

- **Maximally Flat Passband**: No ripples in the passband frequency response.
- **Good Roll-off**: Steeper attenuation slope compared to Bessel filters of the same order.
- **Predictable Performance**: Well-understood characteristics.

### Disadvantages

- **Non-linear Phase Response**: Introduces phase distortion, especially near the cutoff frequency, which can distort the shape of complex waveforms.
- **Moderate Ringing/Overshoot**: Can exhibit some ringing in the step response compared to Bessel filters.
- **Parameter Sensitivity**: The `length` parameter significantly impacts the smoothing and lag.
