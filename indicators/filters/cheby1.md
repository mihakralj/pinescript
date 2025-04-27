# CHEBY1: Chebyshev Type I Filter

[Pine Script Implementation of CHEBY1](https://github.com/mihakralj/pinescript/blob/main/indicators/filters/cheby1.pine)

## Overview and Purpose

The Chebyshev Type I Filter is an advanced signal processing tool that offers steeper roll-off characteristics than Butterworth filters of the same order. Developed by Russian mathematician Pafnuty Chebyshev in the 19th century, this filter design achieves sharper frequency separation by allowing controlled ripples in the passband while maintaining a maximally flat stopband. This implementation provides a 2nd-order low-pass filter that efficiently removes high-frequency market noise while preserving lower-frequency trend components, making it particularly valuable for isolating significant market movements in noisy trading environments.

## Core Concepts

* **Steeper roll-off:** Provides faster attenuation of unwanted frequencies compared to Butterworth filters of the same order
* **Passband ripple control:** Allows user to control the trade-off between roll-off steepness and passband flatness
* **Market application:** Particularly effective for isolating trend signals in highly volatile or noisy market conditions where aggressive filtering is needed

The core innovation of the Chebyshev Type I filter is its ability to achieve more efficient filtering by allowing controlled ripples in the passband. By accepting these small amplitude variations in the frequencies that are passed through, the filter achieves a much sharper transition from passband to stopband, providing better separation between trend signals and market noise.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 14 | Controls the cutoff period | Increase for smoother signals, decrease for more responsiveness |
| Ripple | 1.0 | Controls passband ripple (dB) | Lower values reduce ripple but decrease roll-off steepness, higher values increase both |
| Source | close | Price data used for calculation | Consider using hlc3 for a more balanced price representation |

**Pro Tip:** When using Chebyshev Type I filters for trend identification, start with a ripple setting of 0.5-1.0 dB - this provides excellent noise reduction while keeping ripple effects manageable in most market conditions.

## Calculation and Mathematical Foundation

**Simplified explanation:**
The Chebyshev Type I filter calculates a smoothed output by applying carefully designed coefficients to both current and past price data as well as past filter outputs. This design allows for much sharper filtering of market noise than simpler filters, at the cost of introducing small ripples in the frequency response.

**Technical formula:**
Implemented as a 2nd-order IIR filter:

y[n] = B0 × x[n] + B1 × x[n-1] + B2 × x[n-2] - A1 × y[n-1] - A2 × y[n-2]

Where coefficients are derived from:
- ε = sqrt(10^(Ripple/10) - 1)
- mu = asinh(1/ε) / n
- sigma = -sinh(mu) × Wc
- omega_d = cosh(mu) × Wc

> 🔍 **Technical Note:** The Chebyshev polynomial characteristics used in this filter design create an equiripple response in the passband, meaning the ripples are of equal height throughout the passband frequencies - this is a mathematically optimal solution for minimizing the maximum error.

## Interpretation Details

The Chebyshev Type I filter can be used in various trading strategies:

* **Trend identification:** Reveals underlying price direction with sharper separation between trend and noise
* **Signal generation:** Crossovers between price and filtered output generate trade signals with potentially fewer false positives
* **Support/resistance levels:** Creates cleaner dynamic support and resistance levels
* **Volatility filtering:** Particularly effective at filtering out high-volatility price fluctuations while maintaining core trend movements
* **Pre-processing:** Can be used to clean price data before applying other technical indicators to reduce false signals

## Limitations and Considerations

* **Passband ripple:** Introduces small amplitude variations in passed frequencies that may affect signal interpretation
* **Phase distortion:** More significant non-linear phase response than Butterworth filters, affecting timing of signals
* **Transient response:** Can exhibit more pronounced ringing or overshoot when responding to sharp price changes
* **Parameter complexity:** Requires understanding the ripple parameter in addition to cutoff length
* **Complementary tools:** Best used alongside volume analysis and confirmation indicators

## References

* Parks, T.W. and Burrus, C.S. "Digital Filter Design," Wiley, 1987
* Smith, S.W. "The Scientist and Engineer's Guide to Digital Signal Processing," Chapter 20
