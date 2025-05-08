# PERCENTILE: Percentile

[Pine Script Implementation of PERCENTILE](https://github.com/mihakralj/pinescript/blob/main/indicators/statistics/percentile.pine)

## Overview and Purpose

The Percentile indicator calculates the value below which a given percentage of observations in a dataset fall. For example, the 25th percentile is the value below which 25% of the data points are found. The 50th percentile is equivalent to the Median.

This implementation calculates the specified percentile over a rolling lookback period using linear interpolation.

## Core Concepts

*   **Rank-Based Value:** Identifies a value based on its rank or position within a sorted dataset.
*   **Data Distribution Insight:** Helps understand the distribution of data within the lookback window. For instance, comparing the 25th, 50th, and 75th percentiles can give an idea of data spread and skewness.
*   **Rolling Calculation:** The percentile is calculated over a moving window of a fixed length.
*   **Linear Interpolation:** If the exact percentile rank falls between two data points, this method estimates the value by linearly interpolating between them.
*   **NA Handling:** `na` values in the `source` series within the lookback `period` are filtered out before the percentile calculation.

## Common Settings and Parameters

| Parameter  | Default | Function                                                                 | When to Adjust                                                                                                                               |
| :--------- | :------ | :----------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------- |
| Source     | Close   | The data series to calculate the percentile from.                        | Change to High, Low, Open, HL2, HLC3, another indicator's output, etc., for different analyses.                                              |
| Period     | 14      | The number of bars in the lookback window.                               | Shorter periods make the percentile more sensitive to recent data; longer periods provide a more stable, longer-term percentile value.        |
| Percentile | 50      | The percentile to calculate (0-100). E.g., 50 for median, 25 for Q1, 75 for Q3. | Adjust to observe different parts of the data distribution. For example, 10th and 90th percentiles can define a range capturing 80% of the data. |

**Pro Tip:** Plotting multiple percentiles (e.g., 10th, 50th, 90th) can create dynamic channels or bands around the price, similar to Bollinger Bands but based on rank rather than standard deviation.

## Calculation and Mathematical Foundation

**Simplified explanation:**
1.  Collect all valid (non-`na`) numbers from the lookback period.
2.  Sort these numbers from smallest to largest.
3.  Determine the rank (position) that corresponds to the desired percentile.
4.  If the rank is an exact data point, that's the percentile value. If it falls between two data points, estimate the value using linear interpolation.

**Technical approach:**
The Pine Script implementation performs the following steps:
1.  Collects all valid (non-`na`) data points from the `source` series over the specified `period` into an array.
2.  If there are no valid data points, it returns `na`. If there's only one, it returns that data point.
3.  The array of valid data points is then sorted in ascending order.
4.  The 0-indexed rank `k` corresponding to the target `percentile` (0-100) is calculated using the formula: `rank = (percentile / 100.0) * (number_of_valid_points - 1)`.
5.  Special cases for the 0th percentile (minimum value) and 100th percentile (maximum value) are handled by directly returning the first or last element of the sorted array, respectively.
6.  For other percentiles:
    *   The floor (`k_floor`) and ceiling (`k_ceil`) of the calculated `rank` are determined.
    *   If `k_floor` and `k_ceil` are the same (meaning `rank` is an integer), the value at index `k_floor` in the sorted array is the result.
    *   Otherwise, linear interpolation is performed: `value_at_k_floor + (rank - k_floor) * (value_at_k_ceil - value_at_k_floor)`.

> 🔍 **Technical Note on Linear Interpolation:** For a percentile `P` (0-100) in a sorted array `X` of size `N_valid` (0-indexed), the rank `k = (P/100) * (N_valid - 1)`. If `k` is an integer, `X[k]` is the value. If `k` is not an integer, let `k_floor = floor(k)` and `k_ceil = ceil(k)`. The interpolated value is `X[k_floor] + (k - k_floor) * (X[k_ceil] - X[k_floor])`.

This is the method implemented, a well-established approach often referred to as method R-7 in statistical literature and is commonly used as the default in statistical software like R and Python's NumPy library.

## Interpretation Details

*   **Dynamic Support/Resistance:** Lower percentiles (e.g., 10th, 25th) can act as dynamic support levels, while upper percentiles (e.g., 75th, 90th) can act as dynamic resistance levels.
*   **Volatility Assessment:** The spread between different percentiles (e.g., 90th - 10th) can be a measure of data dispersion or volatility over the lookback period.
*   **Outlier Identification:** Values falling outside extreme percentiles (e.g., below 5th or above 95th) might be considered outliers for the given period.
*   **Median (50th Percentile):** Provides a robust measure of central tendency, less affected by outliers than the mean.

## Limitations and Considerations

*   **Computational Cost:** Sorting an array of `N` elements typically takes O(N log N) time. This is done on every bar for the lookback window, so it can be more computationally intensive than simple averages for very long periods.
*   **Data Requirements:** Meaningful percentile calculation requires a sufficient number of data points. With very short periods, percentiles can be volatile or less representative.
*   **Choice of Interpolation Method:** While linear interpolation is common, other methods exist (e.g., nearest rank). The choice can slightly affect the result, especially for small datasets. This implementation uses the linear interpolation method described in the "Calculation" section, implemented manually.
*   **Edge Percentiles (0th and 100th):** The 0th percentile corresponds to the minimum value in the window, and the 100th percentile corresponds to the maximum value.

## References

*   Hyndman, R. J., & Fan, Y. (1996). Sample Quantiles in Statistical Packages. *The American Statistician*, *50*(4), 361–365.
