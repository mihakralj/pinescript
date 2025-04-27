# AFIRMA: Adaptive Finite Impulse Response Moving Average

[Pine Script Implementation of AFIRMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_FIR/afirma.pine)

## Overview and Purpose

The Adaptive Finite Impulse Response Moving Average (AFIRMA) is a sophisticated moving average that implements multiple digital filter windows borrowed from signal processing theory. It was developed as an application of digital signal processing techniques to financial markets, providing traders with enhanced noise filtering capabilities while preserving important price action signals. AFIRMA offers multiple windowing functions (Hanning, Hamming, Blackman, and Blackman-Harris) that can be selected based on specific market conditions and analysis requirements.

## Core Concepts

* **Multiple window options:** AFIRMA provides four different windowing functions, each with specific spectral characteristics suitable for various market conditions
* **Enhanced noise filtering:** The windowing functions offer superior noise reduction compared to traditional moving averages while preserving important price signals
* **Timeframe adaptability:** Functions effectively across all timeframes, with longer periods providing cleaner signals in higher timeframes

The core innovation of AFIRMA is its implementation of established windowing functions from digital signal processing. These functions shape the frequency response of the filter, allowing for precise control over which price movements are preserved and which are filtered out as noise. Each window type offers unique filtering properties that traders can select based on their analytical needs and market conditions.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 14 | Controls the lookback period | Increase for smoother signals in volatile markets, decrease for responsiveness in trending markets |
| Source | close | Price data used for calculation | Typically left at default; can be changed to hlc3 for more balanced price representation |
| Window Type | Hanning | Determines filter characteristics | Change based on market conditions and desired balance between smoothness and responsiveness |

**Pro Tip:** The Blackman window tends to provide the best balance between noise reduction and signal preservation for most market conditions, while Hanning is preferred for faster response to developing trends.

## Calculation and Mathematical Foundation

**Simplified explanation:**
AFIRMA applies carefully designed weighting patterns (windows) to price data. These windows give different importance to different prices in the lookback period, with the weights determined by mathematical functions that optimize signal processing characteristics.

**Technical formula:**
AFIRMA applies specialized windowing functions to price data:

1. **Hanning Window**: w(k) = 0.50 - 0.50 × cos(2π × k / n)
2. **Hamming Window**: w(k) = 0.54 - 0.46 × cos(2π × k / n)
3. **Blackman Window**: w(k) = 0.42 - 0.50 × cos(2π × k / n) + 0.08 × cos(4π × k / n)
4. **Blackman-Harris Window**: w(k) = 0.35875 - 0.48829 × cos(2π × k / n) + 0.14128 × cos(4π × k / n) - 0.01168 × cos(6π × k / n)

Where:
- k is the position in the window (0 to n-1)
- n is the window size (period)

The final AFIRMA calculation: AFIRMA = Σ(Price[i] × Window_Weight[i]) / Σ(Window_Weight[i])

> 🔍 **Technical Note:** The key advantage of these windowing functions is their ability to minimize "spectral leakage" - a phenomenon in signal processing that can distort the extracted signal.

## Interpretation Details

AFIRMA can be used in various trading strategies:

* **Trend identification:** The direction of AFIRMA indicates the prevailing trend
* **Signal generation:** Crossovers between price and AFIRMA can generate trade signals
* **Trend strength assessment:** The distance between price and AFIRMA can indicate trend strength
* **Filter selection:** Different window types can be used for different market conditions:
  - Hanning for general trend following
  - Hamming for markets with sharp transitions
  - Blackman for noisy markets requiring more smoothing
  - Blackman-Harris for extracting weak trends in choppy conditions

## Limitations and Considerations

* **Market conditions:** Like all moving averages, less effective in ranging or highly volatile markets
* **Lag factor:** All moving averages introduce some lag; AFIRMA's lag varies by window type
* **Complexity:** More parameters to optimize compared to simple moving averages
* **Complementary tools:** Best used with momentum oscillators and volatility measures for confirmation

## References

* Harris, F.J. "On the Use of Windows for Harmonic Analysis with the Discrete Fourier Transform", Proceedings of the IEEE, 1978
* Ehlers, John F. "Cycle Analytics for Traders", Wiley, 2013

