# HARMEAN: Harmonic Mean

[Pine Script Implementation of HARMEAN](https://github.com/mihakralj/pinescript/blob/main/indicators/statistics/harmean.pine)

## Overview and Purpose

The Harmonic Mean is a type of average, typically used for sets of rates (e.g., speeds). It is calculated as the reciprocal of the arithmetic mean of the reciprocals of the observations. The Harmonic Mean is most appropriate for situations when the average of rates is desired. It is one of the three Pythagorean means (along with arithmetic and geometric means).

This indicator calculates the Harmonic Mean for a given input series over a specified lookback period, requiring all input values to be positive.

## Core Concepts

*   **Reciprocal of Averages:** The Harmonic Mean is the number of observations divided by the sum of their reciprocals.
*   **Rate Averaging:** It is particularly useful for averaging rates, such as speeds (distance per unit of time). For example, if you travel a certain distance at one speed and the same distance again at another speed, the harmonic mean of the two speeds gives your average speed over the total distance.
*   **Positive Values Required:** The standard definition and this implementation require all input values to be strictly positive. Zero or negative values would make reciprocals undefined or lead to misleading results.
*   **Sensitivity to Small Values:** The Harmonic Mean gives less weight to large values and more weight to small values. This means it is heavily influenced by the smallest values in the dataset.

## Common Settings and Parameters

| Parameter       | Type         | Default | Function                                                                                                | When to Adjust                                                                                                                                                              |
| :-------------- | :----------- | :------ | :------------------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Source          | series float | close   | The input data series (e.g., price, ratio). **Must consist of positive values.**                        | Choose the series whose harmonic mean you want to measure. Ensure data is strictly positive.                                                                                |
| Lookback Period | simple int   | 14      | The number of bars (sample size `n`) used for calculating the harmonic mean. Min 1.                     | A larger period provides a more stable estimate over a longer term but will be less responsive to recent changes. A shorter period is more reactive to shifts in the data.    |

**Pro Tip:** When dealing with ratios like P/E (Price-to-Earnings) ratios for a portfolio, if you want to find the average P/E ratio of the portfolio where each stock has an equal dollar investment, the harmonic mean of the individual P/E ratios is appropriate.

## Calculation and Mathematical Foundation

The Harmonic Mean (HM) is calculated as follows for a given `source` series and `length`:

1.  **Data Collection:** A window of the most recent `length` data points from `source` is considered.
2.  **Data Validation:** Only positive (`> 0`) and non-`na` values from this window are included in the calculation. Let `n_valid` be the count of such values. If `n_valid` is 0, the harmonic mean is `na`.
3.  **Reciprocals:** For each valid positive data point `xᵢ`, its reciprocal `1/xᵢ` is calculated.
4.  **Sum of Reciprocals:** The sum of these reciprocals is computed: `Sum_Reciprocals = Σ (1/xᵢ)`.
5.  **Harmonic Mean:** The harmonic mean is then calculated as: `HM = n_valid / Sum_Reciprocals`.

The formula is: `HM = n / ( (1/x₁) + (1/x₂) + ... + (1/xₙ) )`

> 🔍 **Technical Note:**
> *   The implementation strictly requires positive data (`xᵢ > 0`). Non-positive or `na` values in the source series are excluded.
> *   A check is in place to avoid division by zero if `Sum_Reciprocals` is zero or extremely close to zero (which could happen if `n_valid` is positive but all `xᵢ` are extremely large).
> *   The implementation uses a circular buffer to efficiently update the sum of reciprocals.

## Interpreting the Harmonic Mean

*   **Value Range:** If all input values are positive, the Harmonic Mean will also be positive.
*   **Relationship to Other Means:** For any set of positive numbers that are not all equal, the Harmonic Mean is always the smallest of the three Pythagorean means (Harmonic ≤ Geometric ≤ Arithmetic). They are equal only if all numbers in the set are identical.
*   **Emphasis on Smaller Values:** The Harmonic Mean is heavily weighted by smaller numbers. A very small value in the dataset can significantly lower the harmonic mean.
*   **Changes Over Time:**
    *   An **increasing** Harmonic Mean suggests that the typical rate or ratio (in the harmonic sense) of the source data is rising, often implying that smaller values are becoming less frequent or larger.
    *   A **decreasing** Harmonic Mean suggests that the typical rate is falling, often influenced by the presence of smaller values.

## Common Applications

1.  **Finance:**
    *   Averaging ratios like P/E ratios when considering an equally weighted portfolio.
    *   Calculating the average cost of shares purchased over time (dollar-cost averaging).
2.  **Physics and Engineering:**
    *   Averaging speeds or rates (e.g., average speed for a round trip of equal distances at different speeds).
    *   Calculating equivalent resistance of parallel resistors.
3.  **Other Sciences:**
    *   Used in various situations where an average of rates is needed.

## Limitations and Considerations

*   **Positive Data Requirement:** Strictly requires positive values. It cannot be used with zero or negative numbers.
*   **Sensitivity to Small Values:** Can be disproportionately affected by very small values in the dataset. If one of the values is close to zero, the harmonic mean will also be close to zero, regardless of other larger values.
*   **Not Suitable for All Averages:** It's not a general-purpose average. Its use is specific to situations where averaging rates or ratios is appropriate. Using it in other contexts can be misleading.

## References

*   Wikipedia contributors. (2023). *Harmonic mean*. Wikipedia, The Free Encyclopedia. Retrieved from [https://en.wikipedia.org/wiki/Harmonic_mean](https://en.wikipedia.org/wiki/Harmonic_mean)
*   Kenney, J. F. and Keeping, E. S. (1962). *Mathematics of Statistics, Pt. 1, 3rd ed.* Van Nostrand, Princeton, NJ.
