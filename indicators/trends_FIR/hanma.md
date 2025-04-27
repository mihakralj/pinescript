# HANMA: Hanning Moving Average

[Pine Script Implementation of HANMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_FIR/hanma.pine)

## Overview and Purpose

The Hanning Moving Average (HANMA) is a technical indicator that applies the Hanning window function from digital signal processing to price data. Developed in the 1960s by Julius von Hann for spectral analysis in signal processing, the Hanning window was later adapted for financial market analysis in the 1990s as digital signal processing techniques gained traction in technical analysis. HANMA uses a cosine-based weighting scheme to create an effective filter that reduces market noise while preserving important price movements.

## Core Concepts

* **Cosine-based weighting:** HANMA uses a raised cosine function that creates a bell-shaped weight distribution with excellent frequency domain characteristics
* **Side-lobe suppression:** The Hanning window provides effective attenuation of side lobes, reducing false signals from market noise
* **Timeframe flexibility:** Works across multiple timeframes with appropriate period adjustments

The core innovation of HANMA is its ability to separate meaningful price movements from market noise. Unlike simpler moving averages, the Hanning window's cosine-based weighting creates a bell-shaped curve that gradually tapers to zero at both ends, minimizing distortion while effectively filtering out random price fluctuations. This makes it particularly valuable in choppy or consolidating markets.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 14 | Controls the lookback period | Increase for smoother signals in volatile markets, decrease for responsiveness |
| Source | close | Price data used for calculation | Consider using hlc3 for a more balanced price representation |

**Pro Tip:** For trend following, use a length of 20-30 to maximize the Hanning window's noise reduction capabilities without introducing excessive lag.

## Calculation and Mathematical Foundation

**Simplified explanation:**
HANMA calculates a weighted average of prices where the weights follow a bell-shaped pattern. The weights are highest in the middle and gradually decrease to zero at both ends, creating a smooth filter that effectively removes random price fluctuations.

**Technical formula:**
The Hanning window weights are calculated as:
w(n) = 0.5 × (1 - cos(2π × n / (N - 1)))

Where:
- n is the position in the window (0 to N-1)
- N is the window size (period)

The final HANMA calculation: HANMA = Σ(Price[i] × Window_Weight[i]) / Σ(Window_Weight[i])

> 🔍 **Technical Note:** The Hanning window provides approximately -32dB of side-lobe attenuation, making it effective at filtering market noise while maintaining signal integrity. It offers a good balance between main-lobe width and side-lobe suppression.

## Interpretation Details

HANMA can be used in various trading strategies:

* **Trend identification:** The direction of HANMA indicates the prevailing trend
* **Signal generation:** Crossovers between price and HANMA generate trade signals
* **Support/resistance levels:** HANMA can act as dynamic support during uptrends and resistance during downtrends
* **Trend strength assessment:** Distance between price and HANMA can indicate trend strength
* **Noise filtering:** Using HANMA to filter noisy price data before applying other indicators

## Limitations and Considerations

* **Market conditions:** Like all moving averages, less effective in choppy, sideways markets
* **Lag factor:** More lag than linear-weighted averages due to center-weighted emphasis
* **Limited adaptability:** Fixed weighting scheme cannot adapt to changing market volatility
* **Main-lobe width:** Moderate main-lobe width affects frequency resolution
* **Complementary tools:** Best used with momentum oscillators or volume indicators for confirmation

## References

* Harris, F.J. "On the Use of Windows for Harmonic Analysis with the Discrete Fourier Transform", Proceedings of the IEEE, 1978
* Ehlers, J.F. "Cycle Analytics for Traders," Wiley, 2013
