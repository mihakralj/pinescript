# ELLIPTIC: Elliptic (Cauer) Filter

[Pine Script Implementation of ELLIPTIC](https://github.com/mihakralj/pinescript/blob/main/indicators/filters/elliptic.pine)

## Overview and Purpose

The Elliptic Filter, also known as the Cauer filter, represents the optimal solution for achieving the steepest possible transition between passed and rejected frequencies. Developed by Wilhelm Cauer in the 1930s, this filter type offers the sharpest roll-off characteristics among all linear filters of the same order. This implementation provides a 2nd-order low-pass filter with fixed characteristics (1dB passband ripple, 40dB stopband attenuation) and adjustable cutoff frequency. The Elliptic filter is particularly valuable when maximum separation between trend and noise components is required, making it effective for identifying clean trend signals in highly volatile market conditions.

## Core Concepts

* **Optimal roll-off:** Provides the steepest possible transition between passed and rejected frequencies for any filter of the same order
* **Dual ripple design:** Achieves its superior performance by allowing controlled ripples in both passband and stopband
* **Market application:** Particularly effective for clear trend identification with maximum noise rejection when signal distortion is acceptable

The core innovation of the Elliptic filter is its mathematically optimal design that achieves the sharpest possible frequency separation with a given filter order. By allowing controlled ripples in both passed and rejected frequency bands, it provides dramatically better filtering efficiency than other designs. This creates exceptionally clean trend signals by maximizing the rejection of market noise components, though at the cost of some waveform distortion.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 20 | Controls the cutoff period | Increase for smoother signals, decrease for more responsiveness |
| Source | close | Price data used for calculation | Consider using hlc3 for a more balanced price representation |

**Pro Tip:** Due to its fixed 1dB passband ripple design, the Elliptic filter works best with length settings 20% longer than you would use for a Butterworth filter to ensure adequate smoothing of important trend components.

## Calculation and Mathematical Foundation

**Simplified explanation:**
The Elliptic filter creates a smoothed output by combining the current price with previous prices and previous filter outputs using carefully designed mathematical relationships. This creates an extremely efficient filter that maximizes the separation between trend and noise components, though with some ripple in both passed and rejected frequencies.

**Technical formula:**
Implemented as a 2nd-order IIR filter using the difference equation:

y[n] = b0 × x[n] + b1 × x[n-1] + b2 × x[n-2] - a1 × y[n-1] - a2 × y[n-2]

Where coefficients are derived from pre-calculated prototype values (for 1dB passband ripple, 40dB stopband attenuation):
- Uses bilinear transform to map analog prototype to digital domain
- Scales prototype based on desired cutoff frequency
- Normalizes for unity DC gain

> 🔍 **Technical Note:** Due to the complexity of calculating elliptic functions, this implementation uses pre-calculated coefficients for the specified ripple characteristics. The elliptic design achieves its optimal performance through precisely placed zeros and poles in the complex plane.

## Interpretation Details

The Elliptic filter can be used in various trading strategies:

* **Trend identification:** Reveals underlying price direction with maximum noise rejection
* **Signal generation:** Crossovers between price and filtered output generate trade signals with minimal false positives
* **Support/resistance levels:** Creates clean dynamic support and resistance levels
* **Trend strength assessment:** The slope and behavior of the filtered line can indicate trend strength
* **Multiple timeframe analysis:** Apply filters with different cutoff periods to identify trends across various time horizons

## Limitations and Considerations

* **Signal distortion:** Significant non-linear phase response causes waveform distortion
* **Ringing/overshoot:** Exhibits substantial ringing in response to sharp price changes
* **Initialization period:** Requires several bars to stabilize after the start of data
* **Fixed ripple characteristics:** This implementation uses fixed 1dB passband ripple and 40dB stopband attenuation
* **Complementary tools:** Best used alongside phase-corrected filters or zero-lag indicators for precise timing

## References

* Cauer, W. "Synthesis of Linear Communication Networks," McGraw-Hill, 1958
* Daniels, R.W. "Approximation Methods for Electronic Filter Design," McGraw-Hill, 1974
