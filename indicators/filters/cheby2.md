# Chebyshev Type II Filter (2nd Order)

The Chebyshev Type II Filter, also known as the Inverse Chebyshev filter, is characterized by a maximally flat response in the passband (like Butterworth) and ripples (equiripple behavior) in the stopband. This allows for a steeper roll-off than Butterworth filters without introducing ripple in the frequency range of interest (passband). This implementation provides a 2nd-order low-pass Chebyshev Type II filter using coefficients derived via the Bilinear Transform method.

[Pine Script Implementation of Chebyshev Type II Filter](https://github.com/mihakralj/pinescript/blob/main/indicators/filters/cheby2.pine)

## Mathematical Foundation

The filter is implemented as a 2nd-order Infinite Impulse Response (IIR) filter using the difference equation:

`y[n] = B0 × x[n] + B1 × x[n-1] + B2 × x[n-2] - A1 × y[n-1] - A2 × y[n-2]`

Where `x[n]` is the input (`src`), `y[n]` is the output (`filt`), and the normalized coefficients `B0, B1, B2, A1, A2` are derived from the continuous-time Chebyshev Type II prototype via the Bilinear Transform. The derivation involves:

1. **Pre-warping** the desired cutoff frequency (`wc = 2 × π / length`) to the analog domain: `Wc = tan(wc / 2)`.
2. Calculating **epsilon** (`ε`) based on the desired stopband attenuation (`Rs` in dB): `ε = 1 / sqrt(10^(Rs / 10) - 1)`. Note this is the inverse relationship compared to Type I.
3. Finding the **pole locations** (`sigma_p`, `omega_p`) in the continuous-time s-plane based on `ε` and the filter order (n=2), similar to Type I using `asinh`.
4. Finding the **zero locations** (`omega_z`) on the imaginary axis, which create the stopband ripples: `omega_z = Wc / cos(π / (2n))` for order n=2.
5. Forming the continuous-time denominator factor `K_p = sigma_p² + omega_p²` and numerator factor `K_z = omega_z²`.
6. Calculating the **DC gain** `DC_gain = K_p / K_z` to ensure unity gain at frequency zero.
7. Applying the **Bilinear Transform** to map the continuous-time poles and zeros to discrete-time coefficients (`a0_z, a1_z, a2_z, b0_z, b1_z, b2_z`), incorporating the `DC_gain`.
8. **Normalizing** the coefficients by `a0_z` to get `B0, B1, B2, A1, A2`.

The `length` parameter determines the cutoff frequency, and the `attenuation` parameter controls the minimum attenuation achieved in the stopband.

## Implementation Details

1. **Coefficient Calculation**:
    - Coefficients are calculated based on `length` and `attenuation` using the steps outlined above.
    - Helper functions `_sinh` and `_cosh` are used.
    - Input validation ensures `length >= 2` and `attenuation > 0`.

2. **Filtering Process**:
    - Implemented as a recursive IIR filter using the normalized difference equation coefficients.
    - The current output `filt` depends on the current input `src`, the two previous inputs (`src[1]`, `src[2]`), and the two previous filter outputs (`filt[1]`, `filt[2]`).
    - Initialization handles the first few bars.

## Advantages and Disadvantages

### Advantages

- **Maximally Flat Passband**: No ripple in the passband, similar to Butterworth.
- **Steep Roll-off**: Steeper attenuation slope compared to Butterworth filters of the same order.
- **Good Stopband Attenuation**: Provides guaranteed minimum attenuation in the stopband.

### Disadvantages

- **Stopband Ripple**: Gain fluctuates in the stopband.
- **Non-linear Phase Response**: Phase distortion is present, generally worse than Butterworth but potentially better than Chebyshev Type I near the cutoff.
- **Moderate Transient Response**: Ringing/overshoot is typically less severe than Type I but more pronounced than Butterworth or Bessel.
- **Parameter Complexity**: Requires specifying the desired stopband attenuation (`attenuation`) in addition to the cutoff (`length`).
