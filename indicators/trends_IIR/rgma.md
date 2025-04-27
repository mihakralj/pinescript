# RGMA: Recursive Gaussian Moving Average

[Pine Script Implementation of RGMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_IIR/rgma.pine)

## Overview and Purpose

The Recursive Gaussian Moving Average (RGMA) is an advanced technical indicator designed to provide enhanced smoothing with Gaussian-like characteristics while maintaining computational efficiency. While a true Gaussian filter would be symmetric and technically an FIR (Finite Impulse Response) filter, RGMA cleverly approximates these characteristics using recursive IIR (Infinite Impulse Response) techniques.

Unlike standard moving averages, RGMA applies an exponential moving average (EMA) multiple times in sequence, with each pass refining the smoothing effect. This multi-pass approach creates a response curve that approximates a Gaussian distribution, providing superior noise filtering while preserving important trend information. The unique recursive implementation makes it particularly valuable for traders seeking cleaner, smoother trend identification with reasonable computational demands.

## Core Concepts

* **Multi-pass smoothing:** Applies EMA filtering multiple times in sequence, with each pass further refining the smoothing effect
* **Gaussian approximation:** Achieves a bell-shaped response curve similar to a Gaussian filter through cascade filtering
* **Period normalization:** Automatically adjusts the effective period for each pass to maintain consistent overall smoothing
* **Recursive implementation:** Uses each pass's output as the input for the next pass, creating a cascaded filtering effect

RGMA achieves its enhanced smoothing through the central limit theorem principle - as multiple simple filters are cascaded, their combined response tends toward a Gaussian distribution. This creates a moving average with excellent noise rejection while maintaining sensitivity to meaningful price changes.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Period | 14 | Base smoothing period | Increase for longer-term trends, decrease for shorter-term signals |
| Passes | 3 | Number of recursive EMA applications | Increase for smoother output with more lag, decrease for faster response |
| Source | Close | Data point used for calculation | Change to HL2 or HLC3 for more balanced price representation |

**Pro Tip:** Many professional traders find that using 2-4 passes provides the optimal balance between smoothness and responsiveness. The sweet spot is often 3 passes with a period about 15-20% shorter than what you'd use for a regular EMA.

## Calculation and Mathematical Foundation

**Simplified explanation:**
RGMA works by running price through a chain of EMAs, where each EMA takes input from the previous one. This creates a smoother result than a single EMA could provide. The period of each EMA is adjusted to ensure consistent smoothing regardless of how many passes are used.

**Technical formula:**
The RGMA calculation process follows these steps:

1. Adjusted Period Calculation:
   adjusted_period = period / sqrt(passes)

2. Smoothing Factor (Alpha) Calculation:
   alpha = 2.0 / (adjusted_period + 1.0)

3. Recursive EMA Calculation:
   - First Pass: filter[0] = alpha × (source - filter[0]) + filter[0]
   - Subsequent Passes: filter[i] = alpha × (filter[i-1] - filter[i]) + filter[i]

The final RGMA value is the output of the last pass: filter[passes-1]

> 🔍 **Technical Note:** The adjustment of the period by the square root of the number of passes is crucial for maintaining consistent overall smoothing regardless of how many passes are used. Without this adjustment, increasing passes would lead to excessive smoothing. The cascade of EMAs creates a response curve that approaches a Gaussian distribution due to the central limit theorem, providing excellent frequency domain characteristics.

## Interpretation Details

RGMA provides several important insights for traders:

- When price crosses above RGMA, it often signals the beginning of an uptrend
- When price crosses below RGMA, it often signals the beginning of a downtrend
- The slope of RGMA provides insight into trend strength and momentum
- RGMA creates smoother, more reliable support and resistance levels than standard EMAs
- Multiple RGMA lines with different periods create channel-like structures that help identify trend changes

RGMA is particularly valuable for detecting genuine trends in noisy market conditions. Its superior noise filtering capabilities help eliminate false signals while still capturing meaningful price movements. Traders often use RGMA as a dynamic support/resistance reference that filters out minor price fluctuations.

## Limitations and Considerations

* **Market conditions:** Less effective during highly choppy markets where excessive smoothing may mask important short-term signals
* **Lag factor:** Introduces more lag than a single EMA, especially with higher numbers of passes
* **Computational complexity:** Requires more calculations than simple moving averages due to multiple passes
* **Parameter sensitivity:** Requires careful selection of both period and passes to achieve optimal results
* **Complementary tools:** Works best when combined with momentum oscillators or volume indicators for confirmation

## References

1. Ehlers, J. (2001). *Rocket Science for Traders*. John Wiley & Sons.
2. Savitzky, A. & Golay, M.J.E. (1964). "Smoothing and Differentiation of Data by Simplified Least Squares Procedures." *Analytical Chemistry*, 36(8), 1627-1639.
3. Kaufman, P. (2013). *Trading Systems and Methods*, 5th Edition. Wiley Trading.
