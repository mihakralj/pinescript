# GEOMEAN: Geometric Mean

[Pine Script Implementation of GEOMEAN](https://github.com/mihakralj/pinescript/blob/main/indicators/statistics/geomean.pine)

## Overview and Purpose

The Geometric Mean is a type of average, usually used for sets of positive numbers, that indicates the central tendency or typical value of a set of numbers by using the product of their values (as opposed to the arithmetic mean which uses their sum). It is defined as the nth root of the product of n numbers. The Geometric Mean is particularly useful when averaging rates of change, growth rates, or ratios, as it tends to dampen the effect of very large values and give more weight to smaller values compared to the arithmetic mean.

This indicator calculates the Geometric Mean for a given input series over a specified lookback period.

## Core Concepts

*   **Product of Values:** Unlike the arithmetic mean, the geometric mean involves multiplying all the values together.
*   **Nth Root:** After multiplying the `n` values, the `n`-th root is taken to find the geometric mean.
*   **Positive Values Required:** The standard definition of geometric mean applies to positive numbers. If any value is zero, the product becomes zero, making the geometric mean zero. If any value is negative, the product might be negative, and taking an even root of a negative number is not defined in real numbers. This implementation requires all input values to be positive.
*   **Logarithmic Calculation:** For computational stability and to avoid potential overflow/underflow issues with large products, the geometric mean is often calculated using logarithms: `GM = exp((1/n) * Σ ln(xᵢ))`. This is the approach used in the Pine Script implementation.

## Common Settings and Parameters

| Parameter       | Type         | Default | Function                                                                                                | When to Adjust                                                                                                                                                              |
| :-------------- | :----------- | :------ | :------------------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Source          | series float | close   | The input data series (e.g., price, ratio). **Must consist of positive values.**                        | Choose the series whose geometric mean you want to measure. Ensure data is strictly positive.                                                                               |
| Lookback Period | simple int   | 14      | The number of bars (sample size `n`) used for calculating the geometric mean. Min 1.                    | A larger period provides a more stable estimate over a longer term but will be less responsive to recent changes. A shorter period is more reactive to shifts in the data.    |

**Pro Tip:** The Geometric Mean is often preferred over the arithmetic mean when analyzing investment returns over multiple periods because it accurately reflects the compound growth rate. For example, if an investment grows by 10% in year 1 and then by 50% in year 2, the geometric mean of the growth factors (1.10 and 1.50) will give the average annual compound growth factor.

## Calculation and Mathematical Foundation

The Geometric Mean (GM) is calculated as follows for a given `source` series and `length`:

1.  **Data Collection:** A window of the most recent `length` data points from `source` is considered.
2.  **Data Validation:** Only positive (`> 0`) and non-`na` values from this window are included in the calculation. Let `n_valid` be the count of such values. If `n_valid` is 0, the geometric mean is `na`.
3.  **Logarithm of Values:** For each valid positive data point `xᵢ`, its natural logarithm `ln(xᵢ)` is calculated.
4.  **Sum of Logarithms:** The sum of these natural logarithms is computed: `Sum_lnX = Σ ln(xᵢ)`.
5.  **Average of Logarithms:** The average of these logarithms is calculated: `Avg_lnX = Sum_lnX / n_valid`.
6.  **Geometric Mean:** The geometric mean is then found by taking the exponent of this average: `GM = exp(Avg_lnX)`.

This is equivalent to the formula: `GM = (x₁ * x₂ * ... * xₙ)^(1/n)`

> 🔍 **Technical Note:**
> *   The implementation strictly requires positive data (`xᵢ > 0`). Non-positive or `na` values in the source series are excluded from the calculation.
> *   Using logarithms helps prevent numerical overflow or underflow that could occur if directly multiplying many numbers, especially if they are very large or very small.
> *   The implementation uses a circular buffer to efficiently update the sum of logarithms as new data points arrive and old ones leave the lookback window.

## Interpreting the Geometric Mean

*   **Value Range:** If all input values are positive, the Geometric Mean will also be positive.
*   **Relationship to Arithmetic Mean:** For any set of positive numbers that are not all equal, the Geometric Mean is always less than the Arithmetic Mean. They are equal only if all numbers in the set are identical.
*   **Sensitivity:** The Geometric Mean is less sensitive to extreme high values than the Arithmetic Mean.
*   **Changes Over Time:**
    *   An **increasing** Geometric Mean suggests that the typical value (in a multiplicative sense) of the source data is rising.
    *   A **decreasing** Geometric Mean suggests that the typical value is falling.

## Common Applications

1.  **Financial Analysis:**
    *   Calculating average investment returns over multiple periods (compound annual growth rate, CAGR).
    *   Averaging financial ratios.
    *   Analyzing growth rates of economic indicators.
2.  **Scientific Data:**
    *   Averaging rates or ratios in various scientific fields.
    *   Used in some biological and environmental studies.
3.  **Index Construction:** Some financial indices use a geometric mean for their calculation.

## Limitations and Considerations

*   **Positive Data Requirement:** The Geometric Mean is mathematically defined for positive numbers. This implementation will return `na` if non-positive values are encountered or if there are no valid positive values in the lookback period.
*   **Zero Values:** If any value in the dataset is zero, the geometric mean is zero (assuming all other values are positive). This implementation filters out non-positive values, so a zero would be excluded.
*   **Volatility:** While useful for growth rates, it might not always be the best measure for highly volatile series where the arithmetic mean might provide a different perspective on central tendency.

## References

*   Wikipedia contributors. (2023). *Geometric mean*. Wikipedia, The Free Encyclopedia. Retrieved from [https://en.wikipedia.org/wiki/Geometric_mean](https://en.wikipedia.org/wiki/Geometric_mean)
*   Kenney, J. F. and Keeping, E. S. (1962). *Mathematics of Statistics, Pt. 1, 3rd ed.* Van Nostrand, Princeton, NJ.
