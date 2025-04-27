# GWMA: Gaussian-Weighted Moving Average

[Pine Script Implementation of GWMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_FIR/gwma.pine)

## Overview and Purpose

The Gaussian-Weighted Moving Average (GWMA) is a technical indicator that applies the Gaussian (normal) distribution as a weighting function to price data. Inspired by the mathematical principles formalized by Carl Friedrich Gauss in the early 19th century, GWMA was adapted for financial markets in the 1990s as researchers explored statistically optimal smoothing methods. The indicator applies a bell-shaped weighting scheme that gives maximum weight to the center of the lookback period and gradually reduces weight toward both ends, creating a smooth filter with excellent noise reduction properties.

## Core Concepts

* **Bell-curve weighting:** GWMA applies a Gaussian distribution to assign weights to price points, providing statistically optimal smoothing
* **Sigma parameter flexibility:** The width of the bell curve can be adjusted through the sigma parameter to fine-tune filtering characteristics
* **Symmetrical filtering:** The bell-shaped weighting provides balanced filtering with no bias toward recent or older data

The core innovation of GWMA is its implementation of the Gaussian window, which creates a weight distribution with theoretically optimal time-bandwidth product. This makes it particularly effective at separating meaningful price movements from market noise while preserving important trend characteristics. By applying weights that follow the normal distribution, GWMA creates a smooth filter that minimizes both time-domain ripple and frequency-domain side lobes.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 14 | Controls the lookback period | Increase for smoother signals in volatile markets, decrease for responsiveness |
| Sigma | 2.0 | Controls the width of the Gaussian bell curve | Lower values create narrower bell curves with more center emphasis, higher values create wider, flatter distributions |
| Source | close | Price data used for calculation | Consider using hlc3 for a more balanced price representation |

**Pro Tip:** For most trading applications, start with a sigma value between 1.5 and 2.5 - lower values in this range emphasize the center of the window more heavily, while higher values create a more balanced distribution of weights.

## Calculation and Mathematical Foundation

**Simplified explanation:**
GWMA calculates a weighted average of prices where the weights follow a bell curve shape. The center of the lookback period receives the highest weight, and weights gradually decrease toward both the recent and older ends, creating a smooth filter that effectively removes random price fluctuations.

**Technical formula:**
The Gaussian window weights are calculated as:
w(n) = exp(-0.5 × ((n - c) / (σ × N))²)

Where:
- n is the position in the window (0 to N-1)
- c is the center of the window (N-1)/2
- σ (sigma) is the parameter controlling the width of the Gaussian bell curve
- N is the window size (period)

The final GWMA calculation: GWMA = Σ(Price[i] × Window_Weight[i]) / Σ(Window_Weight[i])

> 🔍 **Technical Note:** Smaller sigma values create a more peaked bell curve, emphasizing central values more heavily, while larger sigma values create a wider, flatter curve that distributes weights more evenly across the window.

## Interpretation Details

GWMA can be used in various trading strategies:

* **Trend identification:** The direction of GWMA indicates the prevailing trend
* **Signal generation:** Crossovers between price and GWMA generate trade signals
* **Support/resistance levels:** GWMA can act as dynamic support during uptrends and resistance during downtrends
* **Trend strength assessment:** Distance between price and GWMA can indicate trend strength
* **Sigma optimization:** Different sigma values can be used for different market conditions and trading styles

## Limitations and Considerations

* **Market conditions:** Like all moving averages, less effective in choppy, sideways markets
* **Lag factor:** More lag than linear-weighted averages due to center-weighted emphasis
* **Limited adaptability:** Fixed weighting scheme cannot adapt to changing market volatility
* **Parameter sensitivity:** Finding optimal sigma values may require experimentation for different markets
* **Complementary tools:** Best used with momentum oscillators or volume indicators for confirmation

## References

* Harris, F.J. "On the Use of Windows for Harmonic Analysis with the Discrete Fourier Transform", Proceedings of the IEEE, 1978
* Ehlers, J.F. "Cycle Analytics for Traders," Wiley, 2013
