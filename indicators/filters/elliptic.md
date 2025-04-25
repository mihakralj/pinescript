# Elliptic (Cauer) Filter (2nd Order, Rp=1dB, Rs=40dB)

The Elliptic Filter, also known as the Cauer filter, provides the steepest roll-off characteristic for a given filter order compared to Butterworth, Chebyshev, and Bessel filters. This steep transition comes at the cost of ripples in both the passband and the stopband (equiripple behavior in both bands).

Due to the complexity of calculating Elliptic filter coefficients (requiring elliptic functions), this implementation uses **pre-calculated coefficients** for a specific 2nd-order low-pass filter design:

* Passband Ripple (Rp): **1 dB**
* Stopband Attenuation (Rs): **40 dB**

The cutoff frequency is adjustable via the `length` parameter.

[Pine Script Implementation of Elliptic Filter](https://github.com/mihakralj/pinescript/blob/main/indicators/filters/elliptic.pine)

## Mathematical Foundation

The filter is implemented as a 2nd-order Infinite Impulse Response (IIR) filter using the difference equation:

`y[n] = b0 × x[n] + b1 × x[n-1] + b2 × x[n-2] - a1 × y[n-1] - a2 × y[n-2]`

Where `x[n]` is the input (`src`), `y[n]` is the output (`filt`), and the coefficients `b0, b1, b2, a1, a2` are derived from a pre-calculated continuous-time Elliptic prototype (Rp=1dB, Rs=40dB) via the Bilinear Transform.

The derivation involves:

1. **Defining the Analog Prototype**: Using pre-calculated pole locations (`C_sigma`, `C_omega_d`), zero locations (`C_wz`), and gain (`C_k`) for the normalized (Wc=1) analog filter with Rp=1dB, Rs=40dB.
2. **Pre-warping** the desired digital cutoff frequency (`wc = π / length`) to the analog domain: `Wc = tan(wc)`. (Note: `wc` here is half the typical `2π/length` because `tan` pre-warping uses `ω/2`).
3. **Scaling** the prototype poles (`sigma_scaled`), zeros (`omega_z_scaled`), and pole magnitude squared (`Kp_scaled`) by the pre-warped frequency `Wc`.
4. Applying the **Bilinear Transform** formulas to map the scaled analog poles and zeros to the discrete-time coefficients (`a0_denom`, `a1`, `a2`, `b0_raw`, `b1_raw`, `b2_raw`).
5. **Normalizing for Unity DC Gain**: Calculating a `norm_factor` based on the DC gain of the analog prototype and applying it to the `b` coefficients to ensure the final digital filter has a gain of 1 at frequency zero.
6. **Final Coefficients**: Calculating the final `b0, b1, b2, a1, a2` used in the difference equation, where `a` coefficients are normalized by `a0_denom` and `b` coefficients are normalized by `a0_denom` and the `norm_factor`.

The `length` parameter adjusts the cutoff frequency of this fixed-characteristic (Rp=1dB, Rs=40dB) filter.

## Implementation Details

1. **Coefficient Calculation**:
    - Uses hardcoded constants (`C_wz`, `C_sigma`, `C_omega_d`, `C_Kp_norm`, `C_k`) for the specific analog prototype.
    - Calculates the digital filter coefficients based on the input `length` by scaling the prototype and applying the Bilinear Transform and DC gain normalization.
    - Input validation ensures `length >= 2`. Includes checks to prevent division by very small numbers.

2. **Filtering Process**:
    - Implemented as a recursive IIR filter using the calculated difference equation coefficients.
    - The current output `filt` depends on the current input `src`, the two previous inputs (`src[1]`, `src[2]`), and the two previous filter outputs (`filt[1]`, `filt[2]`).
    - Initialization handles the first few bars.

## Advantages and Disadvantages

### Advantages

- **Steepest Roll-off**: Provides the sharpest transition between the passband and stopband for a given filter order, offering the best frequency selectivity.
- **Efficiency**: Achieves a given filtering requirement (passband ripple, stopband attenuation, cutoff frequency) with the lowest possible filter order compared to other types.

### Disadvantages

- **Passband and Stopband Ripple**: Exhibits ripples in both the passband and stopband, which may be undesirable.
- **Highly Non-linear Phase Response**: The phase response is significantly non-linear, causing substantial waveform distortion (poor transient response, significant ringing/overshoot). This is generally the worst among common filter types.
- **Implementation Complexity**: Calculating coefficients for arbitrary Rp and Rs is very complex. This implementation uses fixed Rp/Rs.
- **Sensitivity**: Coefficients can be sensitive to quantization, although less critical in Pine Script's floating-point environment.
