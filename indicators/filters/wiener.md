# WIENER: Wiener Filter

[Pine Script Implementation of WIENER](https://github.com/mihakralj/pinescript/blob/main/indicators/filters/wiener.pine)

## Overview and Purpose

The Wiener Filter is an adaptive filter that optimizes signal-to-noise ratio based on statistical characteristics of the input data. Developed by Norbert Wiener, it minimizes the mean square error between the filtered output and the desired signal. This implementation provides a practical adaptation for financial time series, automatically adjusting its filtering strength based on local signal and noise estimates. The filter is particularly effective when dealing with varying noise levels in price data, as it adapts its response based on the statistical properties of recent price movements.

## Core Concepts

* **Adaptive filtering:** Automatically adjusts filter response based on local signal-to-noise ratio
* **Statistical optimization:** Minimizes mean square error between filtered output and desired signal
* **Noise estimation:** Uses first differences to estimate local noise variance
* **Signal separation:** Distinguishes between signal and noise components using variance analysis
* **Market application:** Particularly effective in markets with varying volatility levels

The core innovation of the Wiener filter is its ability to adapt to changing market conditions by estimating and using local statistical properties of both signal and noise components.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 20 | Window size for noise estimation | Increase for more stable noise estimates, decrease for faster adaptation |
| Smoothing | 10 | Length for signal power estimation | Adjust based on typical trend duration in your timeframe |
| Source | close | Price data used for calculation | Consider using hlc3 for more stable estimates |

**Pro Tip:** The ratio between Length and Smoothing parameters affects the filter's ability to distinguish between trend and noise. A Length/Smoothing ratio of about 2:1 often provides good results.

## Calculation and Mathematical Foundation

**Simplified explanation:**
The filter estimates local signal and noise power, then uses these estimates to compute optimal weights for filtering. When signal power is high relative to noise, the filter allows more of the original signal through. When noise dominates, it applies stronger smoothing.

**Technical formula:**
The Wiener filter coefficient k is calculated as:

k = σ²_signal / (σ²_signal + σ²_noise)

Where:
- σ²_noise is estimated from first differences
- σ²_signal is estimated from smoothed squared deviations
- Output = mean + k(input - mean)

> 🔍 **Technical Note:** The filter uses first differences for noise estimation based on the assumption that high-frequency components in price data are dominated by noise.

## Interpretation Details

The Wiener filter can be used in various trading strategies:

* **Trend following:** Adapts smoothing strength to trend strength automatically
* **Volatility analysis:** Filter coefficient k provides a measure of signal quality
* **Regime detection:** Changes in noise variance indicate market regime shifts
* **Entry/exit timing:** Cleaner signals during high signal-to-noise periods
* **Risk management:** Use noise estimates to adjust position sizing

## Limitations and Considerations

* **Computational complexity:** Requires maintaining arrays for variance calculations
* **Initialization period:** Needs sufficient data for stable variance estimates
* **Assumption validity:** Assumes noise is primarily in high frequencies
* **Parameter sensitivity:** Performance depends on appropriate Length/Smoothing ratio
* **Complementary tools:** Best used with trend strength indicators

## References

* Wiener, N. "Extrapolation, Interpolation, and Smoothing of Stationary Time Series," MIT Press
* Press, W.H. et al. "Numerical Recipes: The Art of Scientific Computing," Chapter 13
* Vaseghi, S.V. "Advanced Digital Signal Processing and Noise Reduction," Chapter 6
