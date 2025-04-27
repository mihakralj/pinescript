# HAMMA: Hamming Moving Average

[Pine Script Implementation of HAMMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_FIR/hamma.pine)

## Overview and Purpose

The Hamming Moving Average (HAMMA) is a technical indicator that applies the Hamming window function from digital signal processing to price data. Developed by Richard Hamming at Bell Labs in 1959 for telecommunications signal processing, the Hamming window was later adapted for financial market analysis in the 1990s as digital signal processing techniques gained traction in technical analysis. HAMMA uses a modified cosine weighting scheme to create an effective filter that reduces market noise while preserving important price movements.

## Core Concepts

* **Modified cosine weighting:** HAMMA uses a precisely offset cosine function (0.54 - 0.46cos) that creates an optimized weight distribution with excellent frequency domain characteristics
* **Side-lobe suppression:** The Hamming window provides better side-lobe attenuation than Hanning and other windows, effectively filtering out market noise
* **Timeframe flexibility:** Works across multiple timeframes with appropriate period adjustments

The core innovation of HAMMA is its ability to balance main-lobe width and side-lobe suppression. Unlike simpler moving averages, the Hamming window's precise offset creates a near-optimal trade-off between frequency selectivity and noise reduction, making it particularly effective at identifying meaningful market trends in noisy conditions.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 14 | Controls the lookback period | Increase for smoother signals in volatile markets, decrease for responsiveness |
| Source | close | Price data used for calculation | Consider using hlc3 for a more balanced price representation |

**Pro Tip:** For trend following, use a length of 20-30 to maximize the Hamming window's noise reduction capabilities without introducing excessive lag.

## Calculation and Mathematical Foundation

**Simplified explanation:**
HAMMA calculates a weighted average of prices where the weights follow a bell-shaped pattern. The weights are highest in the middle and gradually decrease toward both ends, with a specific offset that creates an optimal balance between smoothing and accuracy.

**Technical formula:**
The Hamming window weights are calculated as:
w(n) = 0.54 - 0.46 × cos(2π × n / (N - 1))

Where:
- n is the position in the window (0 to N-1)
- N is the window size (period)

The final HAMMA calculation: HAMMA = Σ(Price[i] × Window_Weight[i]) / Σ(Window_Weight[i])

> 🔍 **Technical Note:** The precise 0.54-0.46 ratio in the Hamming window was specifically designed to cancel the first sidelobe, providing approximately -42dB of side-lobe attenuation compared to about -32dB in the Hanning window.

## Interpretation Details

HAMMA can be used in various trading strategies:

* **Trend identification:** The direction of HAMMA indicates the prevailing trend
* **Signal generation:** Crossovers between price and HAMMA generate trade signals
* **Support/resistance levels:** HAMMA can act as dynamic support during uptrends and resistance during downtrends
* **Trend strength assessment:** Distance between price and HAMMA can indicate trend strength
* **Noise filtering:** Using HAMMA to filter noisy price data before applying other indicators

## Limitations and Considerations

* **Market conditions:** Like all moving averages, less effective in choppy, sideways markets
* **Lag factor:** More lag than linear-weighted averages due to center-weighted emphasis
* **Limited adaptability:** Fixed weighting scheme cannot adapt to changing market volatility
* **Main-lobe width:** Wider main lobe than some window functions, trading frequency selectivity for side-lobe suppression
* **Complementary tools:** Best used with momentum oscillators or volume indicators for confirmation

## References

* Hamming, R.W. "Digital Filters," Prentice-Hall, 1977
* Harris, F.J. "On the Use of Windows for Harmonic Analysis with the Discrete Fourier Transform", Proceedings of the IEEE, 1978
