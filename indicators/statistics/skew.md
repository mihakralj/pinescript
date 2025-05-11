# SKEW: Skewness

[Pine Script Implementation of SKEW](https://github.com/mihakralj/pinescript/blob/main/indicators/statistics/skew.pine)

## Overview and Purpose

Skewness is a statistical measure that describes the asymmetry of a probability distribution around its mean. In financial markets, it's used to understand the distribution of returns or price changes. A positive skewness indicates a distribution with an asymmetric tail extending towards more positive values (right-skewed), while a negative skewness indicates a tail extending towards more negative values (left-skewed). A value of zero suggests a perfectly symmetrical distribution (like a normal distribution).

Understanding skewness can help traders and analysts assess the likelihood of extreme positive or negative outcomes and the general shape of return distributions.

## Core Concepts

*   **Asymmetry Measurement:** Quantifies the degree to which a distribution deviates from perfect symmetry.
*   **Tail Risk Indication:**
    *   **Negative Skew (Left Skew):** Suggests that large negative returns (crashes, drawdowns) are more likely or more pronounced than large positive returns. The left tail is longer or fatter.
    *   **Positive Skew (Right Skew):** Suggests that large positive returns (rallies, spikes) are more likely or more pronounced than large negative returns. The right tail is longer or fatter.
*   **Distribution Shape:** Provides insight into the shape of the data's distribution beyond just its mean and variance.
*   **Normal Distribution Comparison:** A normal distribution has a skewness of 0. Values deviating from 0 indicate non-normality.

## Common Settings and Parameters

| Parameter | Default | Function                                      | When to Adjust                                                                                                |
| :-------- | :------ | :-------------------------------------------- | :------------------------------------------------------------------------------------------------------------ |
| Source    | Close   | Data point used for skewness calculation.     | Typically applied to returns (e.g., `close - close[1]`) or percentage changes rather than raw price levels. |
| Length    | 20      | Lookback period for the calculation. Must be > 2. | Shorter periods are more responsive but noisier; longer periods provide a more stable but lagging measure.    |

**Pro Tip:** When analyzing asset returns, a persistent negative skew might suggest a higher probability of sudden, sharp losses compared to gains of similar magnitude. This is a common characteristic of equity market returns.

## Calculation and Mathematical Foundation

**Simplified explanation:**
Skewness is calculated by taking the average of the cubed deviations from the mean, and then normalizing this by the cubed standard deviation.

**Technical formula (Population Skewness - Fisher-Pearson coefficient g1):**

g₁ = E[((X - μ) / σ)³] = μ₃ / σ³

Where:
*   `X` is the random variable (source data).
*   `μ` (mu) is the mean of `X`.
*   `σ` (sigma) is the standard deviation of `X`.
*   `E` denotes the expectation operator.
*   `μ₃` (mu-3) is the third central moment: E[(X - μ)³].

The Pine Script implementation calculates:
1.  The rolling mean (average) of the `Source` over the `Length`.
2.  The rolling variance (average of squared deviations from the mean).
3.  The rolling standard deviation (square root of variance).
4.  The rolling third central moment (average of cubed deviations from the mean).
5.  Skewness = (Third Central Moment) / (Standard Deviation)³.

> 🔍 **Technical Note:** The Pine Script implementation uses efficient rolling calculations for the mean, variance, and the third central moment. It initializes sums and buffers for each of these components. `na` values in the source are handled by `nz(src)` for sum calculations to maintain integrity, and deviations (`dev`) will be `na` if `src` is `na`. The squared and cubed deviations also use `nz()` before summing. During the warm-up period (fewer bars than `Length`), calculations are based on the available data points. Division by zero is handled for standard deviation and its cube, typically resulting in a skewness of 0 if the standard deviation is zero (no dispersion). A minimum `Length` of 3 is enforced as skewness is undefined for fewer points.

## Interpretation Details

*   **Skewness ≈ 0:** The distribution is approximately symmetrical around the mean.
*   **Skewness > 0 (Positive Skew / Right Skew):**
    *   The right tail is longer or fatter than the left tail.
    *   The bulk of the values are concentrated on the left side of the distribution, with extreme positive outliers.
    *   Mean > Median > Mode (for unimodal distributions).
    *   In finance: Suggests a greater probability of small losses and a small probability of large gains.
*   **Skewness < 0 (Negative Skew / Left Skew):**
    *   The left tail is longer or fatter than the right tail.
    *   The bulk of the values are concentrated on the right side of the distribution, with extreme negative outliers.
    *   Mean < Median < Mode (for unimodal distributions).
    *   In finance: Suggests a greater probability of small gains and a small probability of large losses (e.g., "crash risk").

**General Guidelines for Magnitude:**
*   If skewness is between -0.5 and 0.5, the data are fairly symmetrical.
*   If skewness is between -1 and -0.5 (negative skewed) or between 0.5 and 1 (positive skewed), the data are moderately skewed.
*   If skewness is less than -1 (negative skewed) or greater than 1 (positive skewed), the data are highly skewed.

## Limitations and Considerations

*   **Sensitivity to Outliers:** Skewness is sensitive to extreme values (outliers) because it involves cubed deviations.
*   **Sample Size:** Skewness estimates can be unreliable with small sample sizes (`Length`).
*   **Stationarity:** Assumes the underlying statistical properties of the series are relatively stable over the `Length`.
*   **Interpretation Context:** Skewness should be interpreted in the context of the specific asset and market conditions. What's "high" or "low" can vary.
*   **Not a Predictive Tool on its Own:** Skewness describes historical distribution characteristics; it doesn't directly predict future price movements but can inform risk assessment.
*   **Warm-up Period:** Requires `Length` bars to provide a calculation based on the full period. Values during warm-up are based on fewer bars.

## References

*   Joanes, D. N., & Gill, C. A. (1998). Comparing measures of sample skewness and kurtosis. *Journal of the Royal Statistical Society: Series D (The Statistician)*, 47(1), 183-189.
*   Bacon, D. W. (2012). *Practical Portfolio Performance Measurement and Attribution*. Wiley.
