# BLMA: Blackman Moving Average

[Pine Script Implementation of BLMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_FIR/blma.pine)

## Overview and Purpose

The Blackman Moving Average (BLMA) is a technical indicator that applies the Blackman window function from digital signal processing to price data. Developed originally by Ralph Beebe Blackman at Bell Labs in the 1950s as a window function for spectral analysis, the Blackman window was later adapted for financial market analysis as digital signal processing techniques became more widespread in technical analysis. BLMA uses a triple-cosine weighting scheme to create an effective filter that reduces market noise while preserving important price movements.

## Core Concepts

* **Triple-cosine weighting:** BLMA uses a three-term cosine series that creates an optimized weight distribution with excellent frequency domain characteristics
* **Side-lobe suppression:** The Blackman window provides -58dB side-lobe attenuation, effectively filtering out market noise
* **Timeframe flexibility:** Works across multiple timeframes with appropriate period adjustments

The core innovation of BLMA is its ability to filter out market noise through its specialized weighting scheme. Unlike simpler moving averages, the Blackman window's triple-cosine weighting creates a bell-shaped curve that gradually tapers to zero at both ends, minimizing distortion while effectively separating meaningful price movements from random fluctuations.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 14 | Controls the lookback period | Increase for smoother signals in volatile markets, decrease for responsiveness |
| Source | close | Price data used for calculation | Consider using hlc3 for a more balanced price representation |

**Pro Tip:** For trend following, start with longer periods (20-30) to maximize the Blackman window's noise reduction capabilities; for short-term trading, use shorter periods (8-12) but be prepared for increased lag compared to simple moving averages.

## Calculation and Mathematical Foundation

**Simplified explanation:**
BLMA calculates a weighted average of prices where the weights follow a special bell-shaped pattern. The weights are highest in the middle and gradually decrease to zero at both ends, creating a smooth filter that effectively removes random price fluctuations.

**Technical formula:**
The Blackman window weights are calculated as:
w(n) = 0.42 - 0.5 × cos(2πn/(N-1)) + 0.08 × cos(4πn/(N-1))

Where:
- n is the position in the window (0 to N-1)
- N is the window size (period)

The final BLMA calculation: BLMA = Σ(Price[i] × Window_Weight[i]) / Σ(Window_Weight[i])

> 🔍 **Technical Note:** The Blackman window achieves -58dB side-lobe attenuation compared to -42dB in Hamming and -32dB in Hanning windows, making it particularly effective at filtering market noise while maintaining signal integrity.

## Interpretation Details

BLMA can be used in various trading strategies:

* **Trend identification:** The direction of BLMA indicates the prevailing trend
* **Signal generation:** Crossovers between price and BLMA generate trade signals
* **Support/resistance levels:** BLMA can act as dynamic support during uptrends and resistance during downtrends
* **Trend strength assessment:** Distance between price and BLMA can indicate trend strength
* **Noise reduction:** Using BLMA to filter noisy price data before applying other indicators

## Limitations and Considerations

* **Market conditions:** Like all moving averages, less effective in choppy, sideways markets
* **Lag factor:** More lag than simpler moving averages due to center-weighted emphasis
* **Limited adaptability:** Fixed weighting scheme cannot adapt to changing market volatility
* **Main-lobe width:** Wider main lobe than some other windows, potentially affecting sensitivity to rapid changes
* **Complementary tools:** Best used with momentum oscillators or volume indicators for confirmation

## References

* Harris, F.J. "On the Use of Windows for Harmonic Analysis with the Discrete Fourier Transform", Proceedings of the IEEE, 1978
* Ehlers, J.F. "Cycle Analytics for Traders," Wiley, 2013
