# BESSEL: Bessel Filter

[Pine Script Implementation of BESSEL](https://github.com/mihakralj/pinescript/blob/main/indicators/filters/bessel.pine)

## Overview and Purpose

The Bessel Filter is a linear filter specifically designed to preserve the wave shape of signals in the passband. Its defining characteristic is a maximally flat group delay (linear phase response), which ensures minimal distortion of signals as they pass through the filter. This makes it particularly valuable for financial time series where preserving the shape of price movements is critical for accurate analysis. Derived from work by German mathematician Friedrich Bessel, this implementation provides a 2nd-order low-pass version based on John Ehlers' digital filter adaptations for financial markets.

## Core Concepts

* **Linear phase response:** Maintains consistent time delay across all frequencies in the passband, ensuring waveform shapes remain intact
* **Minimal overshoot:** Provides superior transient response with virtually no ringing or overshoot when responding to rapid changes
* **Market application:** Particularly effective for smoothing price data when preserving the timing and shape of market movements is more important than achieving maximum noise reduction

The core innovation of the Bessel filter is its optimization for constant group delay rather than sharp cutoff, making it ideal for applications where detecting true market turning points with minimal distortion takes priority over achieving the steepest possible filtering slope.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 14 | Controls the cutoff period (frequency) | Increase for smoother signals, decrease for more responsiveness |
| Source | close | Price data used for calculation | Typically left at default; can be changed based on analysis focus |

**Pro Tip:** For price pattern recognition strategies, Bessel filters often outperform sharper filters as they preserve the true shape and timing of market structures while still providing effective noise reduction.

## Calculation and Mathematical Foundation

**Simplified explanation:**
The Bessel filter carefully weights the current price and previous filtered values to create a smooth output that maintains the shape characteristics of the original price movements. Unlike sharper filters that may distort timing relationships, Bessel maintains consistent timing across all frequencies.

**Technical formula:**
The filter is implemented as a 2nd-order IIR filter:

Filt[n] = c1 × Src[n] + c2 × Filt[n-1] + c3 × Filt[n-2]

Where coefficients are calculated as:
- a = exp(-π / length)
- b = 2 × a × cos(1.738 × π / length) (where 1.738 ≈ √3)
- c2 = b
- c3 = -a × a
- c1 = 1 - c2 - c3

> 🔍 **Technical Note:** The 1.738 factor (approximately √3) in the coefficient calculations is key to achieving the maximally flat group delay characteristic that defines the Bessel response.

## Interpretation Details

The Bessel filter can be used in various trading strategies:

* **Trend identification:** Reveals underlying price direction while maintaining timing relationships
* **Pattern recognition:** Preserves the true shape of chart patterns for more accurate identification
* **Support/resistance identification:** Provides clean levels without distorting the timing of price reactions
* **Entry/exit timing:** Maintains accurate timing of market turning points
* **Sequence analysis:** Preserves the relative timing between multiple filtered data streams

## Limitations and Considerations

* **Gradual roll-off:** Less sharp frequency cutoff than Butterworth or Chebyshev filters of the same order
* **Moderate noise reduction:** Trades some noise attenuation for better preservation of signal shape
* **Parameter sensitivity:** Performance highly dependent on appropriate length selection
* **Computational complexity:** More involved calculations than simple moving averages
* **Complementary tools:** Best paired with momentum oscillators that can benefit from its shape-preserving properties

## References

* Ehlers, J.F. "Cycle Analytics for Traders," Wiley, 2013
* Smith, S.W. "The Scientist and Engineer's Guide to Digital Signal Processing," Chapter 20
