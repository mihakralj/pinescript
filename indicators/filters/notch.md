# NOTCH: Notch Filter

[Pine Script Implementation of NOTCH](https://github.com/mihakralj/pinescript/blob/main/indicators/filters/notch.pine)

## Overview and Purpose

The Notch Filter is a specialized band-stop filter designed to selectively remove a specific frequency component from price data while leaving other frequencies relatively unaffected. Unlike lowpass or highpass filters that cut off entire frequency ranges, the notch filter targets a narrow frequency band centered around a specified period length. This makes it particularly valuable for eliminating cyclical noise, periodic artifacts, or unwanted oscillations that can obscure the underlying trend in financial time series.

The implementation provided uses a second-order IIR (Infinite Impulse Response) design with configurable bandwidth, offering an efficient solution for removing specific cycles from price data. This approach is especially useful for eliminating known market periodicity (such as daily, weekly, or monthly cycles), isolating trend components by removing oscillations, or preparing data for further analysis by cleaning specific frequency artifacts.

## Core Concepts

* **Frequency targeting:** Precisely removes a specific frequency component while preserving the rest of the signal
* **Period specification:** Allows direct specification of the cycle period to be removed in bars
* **Bandwidth control:** Adjustable bandwidth parameter determines how wide a frequency range is attenuated
* **IIR design:** Uses a second-order IIR filter structure for computational efficiency and minimal phase distortion

The notch filter stands apart from general smoothing filters by its surgical precision in targeting specific cycles. Rather than attempting to remove all high-frequency components or average out price movements, it specifically targets and attenuates oscillations with a particular period. This makes it valuable for specialized technical analysis applications where the analyst has identified a specific cycle that needs to be removed to better expose the underlying market structure.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Period | 14 | The period of the cycle to remove (center frequency of the notch) | Set to match the exact periodicity you want to eliminate from the data |
| Bandwidth | 0.3 | Relative width of the notch (0-1) | Narrower values (0.1-0.2) for precise removal; wider values (0.3-0.5) for removing a broader frequency range |
| Source | Close | Price data used for filtering | Modify to filter different aspects of price action |

**Pro Tip:** To identify the dominant cycle period to target with the notch filter, first analyze your price series with spectral analysis tools or cycle indicators. Once you've identified the period of the unwanted oscillation, set the notch filter's period parameter to match it exactly for optimal removal.

## Calculation and Mathematical Foundation

**Simplified explanation:**
The notch filter creates a frequency response with a deep "notch" at the target frequency. It processes the input signal through a carefully designed recursive filter that applies specific weights to the current and past input values, as well as past output values, to selectively cancel out the targeted frequency component.

**Technical formula:**

The second-order IIR notch filter uses the following difference equation:

y[n] = b₀x[n] + b₁x[n-1] + b₂x[n-2] - a₁y[n-1] - a₂y[n-2]

Where the coefficients are calculated as:

1. ω₀ = 2π/period (normalized center frequency)
2. BW = bandwidth × ω₀ (bandwidth in radians)
3. r = (1 - tan(BW/2))/(1 + tan(BW/2)) (pole radius controlling notch width)
4. b₀ = (1 + α)/2, b₁ = -cos(ω₀), b₂ = (1 - α)/2 (numerator coefficients)
5. a₁ = -2r×cos(ω₀), a₂ = r² (denominator coefficients)

Where α controls the notch depth and β = cos(ω₀) controls the notch position.

> 🔍 **Technical Note:** The implementation uses a parametric approach that maps the period and bandwidth parameters to the filter coefficients in a numerically stable way. Special care is taken to avoid potential instabilities at very low or very high frequencies, ensuring robust performance across a wide range of parameter settings.

## Interpretation Details

The notch filter provides several analytical perspectives:

* **Cycle removal:** Eliminates specific oscillatory components that might be masking the primary trend
* **Trend isolation:** By removing dominant cycles, the underlying trend direction becomes more apparent
* **Phase information:** Comparing filtered and original data can reveal phase relationships between different market components
* **Harmonic analysis:** Sequentially applying multiple notch filters at different frequencies can identify which cycles contribute most significantly to price action
* **Noise reduction:** Targeted removal of known artifacts (e.g., end-of-day patterns) can improve signal quality
* **Pattern clarity:** Some chart patterns become more visible when specific periodic noise is removed

## Limitations and Considerations

* **Parameter sensitivity:** Results highly dependent on precise period and bandwidth settings
* **Transient response:** May produce temporary artifacts at the beginning of the data or after abrupt changes
* **Phase effects:** Can introduce some phase shifts in the vicinity of the notch frequency
* **Multiple cycles:** If multiple periodicities exist, requires separate notch filters for each
* **Computational complexity:** More resource-intensive than simple moving averages
* **Warm-up requirement:** Needs several bars of data (typically 2× the period) for optimal performance
* **Non-stationary challenges:** Fixed notch frequency assumes the targeted cycle is stationary in frequency

## References

* Oppenheim, A. V., & Schafer, R. W. (2010). Discrete-Time Signal Processing (3rd ed.). Pearson.
* Smith, S. W. (1997). The Scientist and Engineer's Guide to Digital Signal Processing. California Technical Publishing.
* Antoniou, A. (2018). Digital Signal Processing: Signals, Systems, and Filters (2nd ed.). McGraw-Hill Education.
* Ehlers, J. F. (2013). Cycle Analytics for Traders. John Wiley & Sons.
