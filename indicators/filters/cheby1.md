# Chebyshev Type I Filter (2nd Order)

The Chebyshev Type I Filter is a type of signal processing filter characterized by a steeper roll-off than Butterworth filters of the same order, achieved at the cost of allowing ripples (equiripple behavior) in the passband. The stopband is maximally flat. This implementation provides a 2nd-order low-pass Chebyshev Type I filter using coefficients derived via the Bilinear Transform method.

[Pine Script Implementation of Chebyshev Type I Filter](https://github.com/mihakralj/pinescript/blob/main/indicators/filters/cheby1.pine)

## Mathematical Foundation

The filter is implemented as a 2nd-order Infinite Impulse Response (IIR) filter using the difference equation:

`y[n] = B0 × x[n] + B1 × x[n-1] + B2 × x[n-2] - A1 × y[n-1] - A2 × y[n-2]`

Where `x[n]` is the input (`src`), `y[n]` is the output (`filt`), and the normalized coefficients `B0, B1, B2, A1, A2` are derived from the continuous-time Chebyshev Type I prototype via the Bilinear Transform. The derivation involves:

1. **Pre-warping** the desired cutoff frequency (`wc = 2 × π / length`) to the analog domain: `Wc = tan(wc / 2)`.
2. Calculating **epsilon** (`ε`) based on the desired passband ripple (`Rp` in dB): `ε = sqrt(10^(Rp / 10) - 1)`.
3. Finding the **pole locations** in the continuous-time s-plane based on `ε` and the filter order (n=2). This involves inverse hyperbolic sine (`asinh`).
    - `mu = asinh(1/ε) / n`
    - `sigma = -sinh(mu) × Wc` (Real part)
    - `omega_d = cosh(mu) × Wc` (Imaginary part)
4. Forming the continuous-time denominator factor `K = sigma² + omega_d²`.
5. Applying the **Bilinear Transform** to map the continuous-time poles to discrete-time coefficients (`a0_z, a1_z, a2_z, b0_z, b1_z, b2_z`).
6. **Normalizing** the coefficients by `a0_z` to get `B0, B1, B2, A1, A2`.

The `length` parameter determines the cutoff frequency, and the `ripple` parameter controls the amount of fluctuation allowed in the passband gain.

## Implementation Details

1. **Coefficient Calculation**:
    - Coefficients are calculated based on `length` and `ripple` using the steps outlined above.
    - Helper functions `_sinh` and `_cosh` are used as Pine Script lacks built-in hyperbolic functions.
    - Input validation ensures `length >= 2` and `ripple > 0`.

2. **Filtering Process**:
    - Implemented as a recursive IIR filter using the normalized difference equation coefficients.
    - The current output `filt` depends on the current input `src`, the two previous inputs (`src[1]`, `src[2]`), and the two previous filter outputs (`filt[1]`, `filt[2]`).
    - Initialization handles the first few bars.

## Advantages and Disadvantages

### Advantages

- **Steep Roll-off**: Provides faster attenuation beyond the cutoff frequency compared to Butterworth or Bessel filters of the same order.
- **Efficient**: Achieves steep roll-off with a relatively low filter order.

### Disadvantages

- **Passband Ripple**: Gain fluctuates within the passband, which may be undesirable for some applications.
- **Non-linear Phase Response**: Significant phase distortion, especially near the cutoff frequency. Worse phase response than Butterworth.
- **Poor Transient Response**: Exhibits more ringing and overshoot in the step response compared to ripple and phase non-linearity.
- **Parameter Complexity**: Requires specifying the allowable passband ripple (`ripple`) in addition to the cutoff (`length`).
