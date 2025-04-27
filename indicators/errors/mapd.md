# MAPD: Mean Absolute Percentage Difference

[Pine Script Implementation of MAPD](https://github.com/mihakralj/pinescript/blob/main/indicators/errors/mapd.pine)

## Overview and Purpose

The Mean Absolute Percentage Difference (MAPD) is a symmetric, scale-independent metric that quantifies the relative difference between two data series. Unlike MAPE which treats one series as the "actual" reference value, MAPD treats both series equally by using their average as the denominator. This approach provides a more balanced measure of relative difference, making it particularly valuable for comparing signals of equal importance, such as different indicators or price series. For traders and analysts, MAPD offers a percentage-based metric for measuring similarity between different instruments, timeframes, or technical indicators without introducing a reference bias.

## Core Concepts

* **Symmetric comparison:** Treats both signals equally without assuming one is the reference "truth"
* **Scale independence:** Expresses differences in percentage terms, allowing comparison across different price ranges
* **Market application:** Particularly useful for measuring similarity between different indicators, instruments, or timeframes

The core innovation of MAPD is its symmetric approach to percentage differences. By using the average of both values in the denominator rather than designating one as the reference, MAPD creates a more balanced measure of relative difference. This makes it especially valuable when comparing signals where neither has clear precedence as the "correct" value, such as when assessing correlation between different instruments or evaluating how closely two indicators track each other.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 14 | Controls the averaging period | Increase for more stable comparison, decrease for more responsive measurement |
| Source 1 | close | First signal for comparison | Any signal you want to compare |
| Source 2 | sma(close,20) | Second signal for comparison | Any signal you want to compare against the first |

**Pro Tip:** When using MAPD to compare different instruments, consider applying it to normalized or z-scored versions of the price series to focus on relative movements rather than absolute differences.

## Calculation and Mathematical Foundation

**Simplified explanation:**
MAPD calculates the percentage difference between two values, but instead of using just one value as the reference point, it uses the average of both. This creates a balanced measure that treats both signals equally and avoids problems when values get close to zero.

**Technical formula:**
MAPD = (100/p) * Σ|Y₁ - Y₂|/((Y₁ + Y₂)/2)

Where:
- Y₁, Y₂ are the signals being compared
- p is the averaging period

> 🔍 **Technical Note:** Using the average of both values in the denominator ensures symmetry - swapping Y₁ and Y₂ produces the exact same result. This property makes MAPD ideal for correlation and similarity studies.

## Interpretation Details

MAPD can be applied in various financial contexts:

* **Correlation analysis:** Measure how closely different instruments or indicators track each other
* **Pair trading:** Quantify the relationship between paired securities
* **Indicator comparison:** Evaluate similarity between different technical indicators
* **Market regime detection:** Identify when relationships between securities change
* **Divergence identification:** Detect when normally correlated instruments begin to separate

## Limitations and Considerations

* **Zero handling:** Undefined when both signals are zero
* **Extreme values:** Can produce very large percentages when values have opposite signs
* **Interpretability range:** Typically interpreted in the 0-100% range, but can exceed 100% in extreme cases
* **Directional blindness:** Does not distinguish between positive and negative differences
* **Complementary metrics:** Best used alongside correlation measures for comprehensive relationship analysis

## References

* Törnqvist, L., Vartia, P., and Vartia, Y. "How Should Relative Changes Be Measured?" The American Statistician, 1985
* Armstrong, J.S. "Long-range Forecasting: From Crystal Ball to Computer," Wiley, 1985
