# BUTTER: Butterworth Filter

[Pine Script Implementation of BUTTER](https://github.com/mihakralj/pinescript/blob/main/indicators/filters/butter.pine)

## Overview and Purpose

The Butterworth Filter is a signal processing tool designed to provide maximally flat frequency response in the passband. Developed by British engineer Stephen Butterworth in 1930, it offers traders a means to smooth price data without introducing ripples in the frequency response. This implementation provides a 2nd-order low-pass filter that effectively removes high-frequency market noise while preserving lower-frequency trend components. Compared to other filters, Butterworth offers an optimal compromise between smoothing efficiency and signal fidelity, making it a versatile choice for various market conditions.

## Core Concepts

* **Maximally flat response:** Provides smooth frequency response with no ripples in the passband, ensuring consistent filtering across all frequencies below the cutoff
* **Optimal roll-off:** Offers steeper attenuation of high frequencies than Bessel filters while maintaining better phase characteristics than Chebyshev filters
* **Market application:** Particularly effective for identifying underlying trends in noisy market conditions while introducing minimal waveform distortion

The core innovation of the Butterworth filter is its mathematically optimal balance between opposing design constraints. The filter achieves the flattest possible frequency response in the passband without sacrificing roll-off steepness, providing traders with clean signals that maintain essential trend information while effectively eliminating random market noise.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 14 | Controls the cutoff period | Increase for smoother signals and less noise, decrease for faster response to price changes |
| Source | close | Price data used for calculation | Consider using hlc3 for a more balanced price representation |

**Pro Tip:** The Butterworth filter works particularly well with length settings that match known market cycles - for example, using 10-period settings for short-term trading on daily charts where 2-week cycles are common.

## Calculation and Mathematical Foundation

**Simplified explanation:**
The Butterworth filter calculates a smoothed output by considering both the current price and previous filtered values. It applies carefully calculated coefficients to create a balance between smoothness and responsiveness, effectively removing random fluctuations while preserving important market trends.

**Technical formula:**
Implemented as a 2nd-order IIR filter using the difference equation:

y[n] = (b0 × x[n] + b1 × x[n-1] + b2 × x[n-2] - a1 × y[n-1] - a2 × y[n-2]) / a0

Where coefficients are calculated as:
- omega = 2 × π / length
- alpha = sin(omega) / sqrt(2)
- a0 = 1 + alpha
- a1 = -2 × cos(omega)
- a2 = 1 - alpha
- b0 = (1 - cos(omega)) / 2
- b1 = 1 - cos(omega)
- b2 = (1 - cos(omega)) / 2

> 🔍 **Technical Note:** The Butterworth design is characterized by its maximally flat magnitude response, achieved through a specific polynomial form that places all poles at equal angular spacing on a circle in the s-plane.

## Interpretation Details

The Butterworth filter can be used in various trading strategies:

* **Trend identification:** Reveals underlying price direction by effectively filtering out market noise
* **Signal generation:** Crossovers between price and filtered output generate trade signals with reduced false positives
* **Support/resistance levels:** Creates cleaner dynamic support and resistance levels
* **Multiple timeframe analysis:** Apply filters with different cutoff periods to identify trends of varying durations
* **Divergence detection:** Compare filtered output with momentum oscillators to identify potential reversals

## Limitations and Considerations

* **Phase distortion:** Introduces some non-linear phase response that can affect timing of signals, especially near the cutoff frequency
* **Moderate ringing:** Can exhibit some overshoot when responding to sharp price changes
* **Initialization period:** Requires several bars to stabilize after the start of data
* **Filter order tradeoffs:** 2nd-order implementation balances smoothing and lag, higher orders would increase both
* **Complementary tools:** Best used alongside volume analysis and momentum indicators for confirmation

## References

* Butterworth, S. "On the Theory of Filter Amplifiers," Wireless Engineer, vol. 7, 1930
* Smith, S.W. "The Scientist and Engineer's Guide to Digital Signal Processing," Chapters 19-20
