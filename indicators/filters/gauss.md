# GAUSS: Gaussian Filter

[Pine Script Implementation of GAUSS](https://github.com/mihakralj/pinescript/blob/main/indicators/filters/gauss.pine)

## Overview and Purpose

The Gaussian Filter implements smoothing based on the normal (Gaussian) distribution, providing a natural and mathematically sound approach to noise reduction in financial time series. Named after Carl Friedrich Gauss, this filter applies weights that follow the bell-shaped normal distribution curve, creating a smooth and continuous filtering effect. This implementation provides a true O(n) convolution that captures the full ±3σ range of the Gaussian distribution, ensuring accurate and comprehensive smoothing of price data.

## Core Concepts

* **Normal distribution weights:** Uses the bell curve shape to naturally weight price contributions, providing smooth and continuous filtering
* **Automatic kernel sizing:** Adapts kernel size based on sigma to capture 99.7% (±3σ) of the distribution's weight
* **True convolution:** Implements exact Gaussian filtering through direct convolution rather than approximations
* **Market application:** Particularly effective for trend identification and noise reduction while preserving important market structures

The core innovation of this implementation is its combination of true Gaussian convolution with efficient computation, providing traders with mathematically rigorous smoothing while maintaining practical applicability to real-time market analysis.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Sigma | 2.0 | Controls the width of the Gaussian distribution | Increase for stronger smoothing, decrease for more responsiveness |
| Source | close | Price data used for calculation | Consider using hlc3 for a more balanced price representation |

**Pro Tip:** A sigma value of 2.0 provides a good balance between smoothing and responsiveness. Values above 3.0 may introduce excessive lag, while values below 1.0 may not provide sufficient noise reduction.

## Calculation and Mathematical Foundation

**Simplified explanation:**
The filter creates a bell-shaped window of weights centered on each price point. The width of this window is determined by sigma, with larger values creating wider windows and thus stronger smoothing. Each filtered value is a weighted average of nearby prices, with weights following the normal distribution curve.

**Technical formula:**
The Gaussian kernel weights are calculated as:

w(x) = e^(-x²/2σ²)

Where:
- x is the distance from the center point
- σ (sigma) is the standard deviation parameter
- Kernel size K = 2⌈3σ⌉ + 1

The filtered output is computed through convolution:

y[n] = Σ(w_k × x[n-k]) / Σw_k

> 🔍 **Technical Note:** The kernel size is automatically set to ±3σ to capture 99.7% of the Gaussian distribution's weight, providing optimal balance between accuracy and computational efficiency.

## Interpretation Details

The Gaussian filter can be used in various trading strategies:

* **Trend identification:** Reveals underlying price direction with natural, smooth transitions
* **Support/resistance levels:** Creates smooth, naturally weighted dynamic levels
* **Multiple timeframe analysis:** Different sigma values can identify trends of varying durations
* **Pattern recognition:** Smooth output helps identify chart patterns with reduced noise
* **Divergence analysis:** Clean price data improves reliability of divergence signals

## Limitations and Considerations

* **Computational complexity:** O(n) complexity with kernel size proportional to sigma
* **Edge effects:** First few bars may show initialization effects
* **Lag characteristics:** Higher sigma values introduce more lag
* **Memory usage:** Requires storing kernel weights and price history
* **Complementary tools:** Best paired with momentum indicators for confirmation

## References

* Gaussian Filter - Wikipedia: https://en.wikipedia.org/wiki/Gaussian_filter
* Digital Image Processing - Gaussian Smoothing: https://homepages.inf.ed.ac.uk/rbf/HIPR2/gsmooth.htm
* Smith, S.W. "The Scientist and Engineer's Guide to Digital Signal Processing," Chapter 24
