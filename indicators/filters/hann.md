# HANN: Hann FIR Filter

[Pine Script Implementation of HANN](https://github.com/mihakralj/pinescript/blob/main/indicators/filters/hann.pine)

## Overview and Purpose

The Hann FIR Filter implements smoothing using a Hann window, a common windowing function used in digital signal processing to reduce spectral leakage. It applies weights derived from a raised cosine function, providing a smooth tapering at the window's edges. This helps in reducing discontinuities when analyzing finite segments of data, making it effective for noise reduction and trend identification in financial time series. This implementation provides an O(n) convolution.

## Core Concepts

* **Hann window weights:** Uses weights from the formula `0.5 * (1 - cos(2πk/(N-1)))` for smooth tapering.
* **FIR (Finite Impulse Response):** The filter's output depends only on a finite number of past and/or current input samples.
* **Adjustable length:** The `len` parameter controls the window size, affecting the smoothness and responsiveness.
* **Market application:** Useful for general-purpose smoothing, noise reduction, and as a component in more complex indicators.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length (`len`) | 10 | Controls the size of the Hann window and thus the FIR filter. | Increase for stronger smoothing (more lag), decrease for more responsiveness (less smoothing). |
| Source | close | Price data used for calculation. | Consider using hlc3 for a more balanced price representation, or other series as needed. |

**Pro Tip:** A length of 10-20 often provides a good balance. Experiment to find what best suits the asset and timeframe.

## Calculation and Mathematical Foundation

**Simplified explanation:**
The filter creates a window of weights that are applied to the recent price data. These weights are highest in the middle of the window and taper off to zero at the ends, following the shape of a Hann window. Each filtered value is a weighted average of prices within this window.

**Technical formula:**
The Hann window coefficients are calculated as:

w(k) = 0.5 * (1 - cos(2πk / (N - 1)))

Where:
- k is the index from 0 to N-1
- N is the length (`len`) of the window

The filtered output y\[n] is computed through convolution:

y\[n] = Σ (w_k * x\[n-k]) / Σ w_k
(where the sum is over k from 0 to N-1, and x is the input series `src`)

> 🔍 **Technical Note:** The implementation adapts for initial bars by using `p = math.min(bar_index + 1, len)`, ensuring output from the first bar. The weights are normalized by `currentWeightSum` which accounts for `na` values in the source.

## Interpretation Details

The Hann FIR filter can be used similarly to other moving averages or smoothing filters:

* **Trend identification:** Smoothed output can help clarify the underlying price direction.
* **Noise reduction:** Reduces short-term fluctuations to reveal more significant price movements.
* **Baseline for oscillators:** Can be used as a smoothed input for other indicators.
* **Component in strategies:** Its general-purpose nature makes it a candidate for various trading systems.

## Limitations and Considerations

* **Lag:** Like all causal FIR filters, it introduces lag, which increases with the `len` parameter.
* **Fixed window shape:** The Hann window has a predefined shape; other windowing functions (e.g., Hamming, Gaussian) might be preferable for specific types of signal characteristics.
* **Edge effects:** While adaptive for initial bars, the filter's characteristics are most stable once `bar_index + 1 >= len`.
* **Computational cost:** O(n) complexity, where n is the `len`.

## References

* Hann function - Wikipedia: https://en.wikipedia.org/wiki/Hann_function
* Window function - Wikipedia: https://en.wikipedia.org/wiki/Window_function
* Smith, S.W. "The Scientist and Engineer's Guide to Digital Signal Processing," Chapter 9 (Windowing).
