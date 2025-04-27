# SGMA: Savitzky-Golay Moving Average

[Pine Script Implementation of SGMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_FIR/sgma.pine)

## Overview and Purpose

The Savitzky-Golay Moving Average (SGMA) is a technical indicator that applies polynomial fitting to price data, preserving important features while reducing noise. Originally developed by Abraham Savitzky and Marcel J.E. Golay in 1964 for spectroscopic analysis in chemistry, this filtering method was published in "Analytical Chemistry" and quickly became a standard technique in signal processing. Its application to financial markets began in the 1990s as researchers sought methods that could better preserve trend changes while filtering noise. By fitting local polynomials to price data instead of simple averaging, SGMA creates a smoothed representation that maintains critical features like peaks, valleys, and inflection points that would be attenuated by conventional moving averages.

## Core Concepts

* **Polynomial fitting:** SGMA fits polynomial curves to segments of price data rather than simply averaging them, preserving higher-order moments of the data
* **Feature preservation:** Maintains important price structures such as tops, bottoms, and inflection points that would be smoothed away by traditional moving averages
* **Market application:** Particularly effective for identifying turning points in price action and analyzing trends with rapid changes

The core innovation of SGMA is its ability to filter noise while preserving the underlying structure of price movement. By using least-squares polynomial fitting across sliding windows of data, SGMA creates a moving average that models the actual shape of price action rather than simply averaging it, making it especially valuable for detecting trend changes and analyzing price dynamics.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 21 | Controls the window size (must be odd) | Increase for smoother signals, decrease for more responsiveness |
| Degree | 2 | Sets the polynomial degree | Higher values better preserve features but may fit noise, lower values provide more smoothing |
| Source | close | Price data used for calculation | Consider using hlc3 for a more balanced price representation |

**Pro Tip:** For most trading applications, a polynomial degree of 2 (quadratic) provides a good balance between smoothing and feature preservation, while odd-numbered window sizes like 21 ensure the filter has a well-defined center point.

## Calculation and Mathematical Foundation

**Simplified explanation:**
SGMA fits small polynomial curves to sections of price data, then uses these curves to create smoothed values. This approach is like having mini regression lines constantly adjusting to local price movements, which preserves important price features better than simple averaging.

**Technical formula:**
SGMA = Σ(Price[i] × SG_Coefficient[i]) / Σ(SG_Coefficient[i])

Where SG_Coefficient[i] values are derived from the process of fitting a polynomial of degree d to a window of n points in a least-squares sense. For each window position, a polynomial is fit:
f(x) = c₀ + c₁x + c₂x² + ... + cₚxᵖ

> 🔍 **Technical Note:** SGMA requires an odd window size because the filter is centered on the middle point of each window. The polynomial degree must be less than the window size to avoid overfitting, with degree=2 (quadratic) being a common choice for financial data.

## Interpretation Details

SGMA can be used in various trading strategies:

* **Trend identification:** The direction of SGMA indicates the prevailing trend with better responsiveness to changes
* **Signal generation:** Crossovers between price and SGMA generate trade signals with potentially earlier detection of reversals
* **Support/resistance levels:** SGMA can act as dynamic support/resistance with better adaptation to price structures
* **Turning point detection:** SGMA excels at identifying potential price reversals due to its feature preservation properties
* **Multi-timeframe analysis:** Using SGMAs with different window sizes can confirm trends while preserving key features

## Limitations and Considerations

* **Computational complexity:** More intensive calculations than simple moving averages
* **Parameter selection:** Finding optimal degree and window size combinations requires experimentation
* **Odd-length requirement:** Window size must be odd to ensure a well-defined center point
* **Edge effects:** Performance can degrade near the edges of the data series (start and end)
* **Complementary tools:** Best used with volume indicators and momentum oscillators for confirmation

## References

* Savitzky, A. and Golay, M.J.E. "Smoothing and Differentiation of Data by Simplified Least Squares Procedures," Analytical Chemistry, 1964
* Schafer, R.W. "What Is a Savitzky-Golay Filter?" IEEE Signal Processing Magazine, 2011
