# SQRT: Square Root Transformation

[Pine Script Implementation of SQRT](https://github.com/mihakralj/pinescript/blob/main/indicators/numerics/sqrt.pine)

## Overview and Purpose

The Square Root Transformation (SQRT) indicator applies a mathematical square root function to input data series, providing a non-linear transformation that compresses the scale of larger values while preserving the relative ordering of data points. This transformation is particularly valuable in financial data analysis for normalizing skewed distributions, reducing the impact of outliers, and creating more stable statistical relationships.

## Core Concepts

*   **Non-Linear Compression** — Reduces the relative magnitude of larger values compared to smaller ones
*   **Skewness Reduction** — Transforms right-skewed distributions toward normal distributions
*   **Order Preservation** — Maintains the relative ranking of data points after transformation
*   **Scale Normalization** — Creates more uniform variance across different value ranges

Market Applications:
*   **Data Preprocessing** — Prepares price and volume data for statistical analysis
*   **Volatility Stabilization** — Reduces heteroscedasticity in time series analysis
*   **Outlier Management** — Diminishes the impact of extreme values on calculations

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|----------------|
| Source | Close | Input series for transformation | Use price, volume, or other non-negative data |
| Domain | x ≥ 0 | Mathematical constraint | Cannot process negative values |
| Output Range | [0, ∞) | Transformed value range | Results always non-negative |

## Calculation and Mathematical Foundation

**Technical Formula:**

For input value $x \geq 0$:
$$\text{SQRT}(x) = \sqrt{x}$$

**Properties of Square Root Transformation:**
- **Domain**: $x \in [0, \infty)$
- **Range**: $y \in [0, \infty)$
- **Monotonicity**: Strictly increasing function
- **Concavity**: Concave function (decreasing marginal rate)

**Transformation Effects:**
$$\frac{d}{dx}\sqrt{x} = \frac{1}{2\sqrt{x}}$$

The derivative shows that the rate of change decreases as $x$ increases, creating the compression effect for larger values.

**Variance Stabilization:**
For data with variance proportional to the mean (Poisson-like), the square root transformation provides:
$$\text{Var}(\sqrt{X}) \approx \frac{1}{4}$$

> 🔍 **Technical Note:** The square root transformation is particularly effective for count data and measurements where variance increases with the mean, making it valuable for volume analysis and event-based indicators.

## Interpretation Details

*   **Value Transformation:**
    - Small values (0-1): Transformation increases values (√0.25 = 0.5)
    - Value of 1: Unchanged (√1 = 1)
    - Large values (>1): Transformation compresses values (√100 = 10)

*   **Distribution Effects:**
    - Right-skewed data → More symmetric distribution
    - Outliers have reduced relative impact
    - Variance becomes more stable across value ranges

*   **Scale Interpretation:**
    - Original linear scale replaced with square root scale
    - Percentage changes become non-linear in transformed space
    - Relative differences compressed for larger values

## Applications

*   **Statistical Analysis:**
    - Normalize skewed price or volume distributions
    - Prepare data for regression analysis requiring normality
    - Stabilize variance in time series modeling

*   **Technical Indicators:**
    - Transform volume data for more stable oscillators
    - Create square root-scaled moving averages
    - Develop volatility indicators with reduced outlier impact

*   **Risk Management:**
    - Transform portfolio values for symmetric risk measures
    - Create more stable correlation matrices
    - Develop robust performance metrics

## Limitations and Considerations

*   **Domain Restrictions:**
    - Cannot process negative values (returns `na`)
    - Zero values remain unchanged
    - Requires non-negative input data

*   **Interpretation Challenges:**
    - Non-linear scale requires careful interpretation
    - Percentage changes not directly comparable
    - Back-transformation needed for original scale analysis

*   **Statistical Implications:**
    - Changes the distribution characteristics
    - Alters correlation structures between variables
    - May not be appropriate for all data types

Complementary Transformations:
* Logarithmic transformation (for multiplicative processes)
* Box-Cox transformation (parametric power transformations)
* Z-score normalization (for standardization)

## References

1. Box, G.E.P. and Cox, D.R. "An Analysis of Transformations." *Journal of the Royal Statistical Society*, Series B, 26(2), 1964.
2. Tukey, J.W. "Exploratory Data Analysis." Addison-Wesley, 1977.
