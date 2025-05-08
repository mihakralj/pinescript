# QUANTILE: Quantile

[Pine Script Implementation of QUANTILE](https://github.com/mihakralj/pinescript/blob/main/indicators/statistics/quantile.pine)

## Overview and Purpose

The Quantile indicator calculates the value below which a specific fraction of observations in a dataset fall. Quantiles divide the probability distribution of a variable into continuous intervals with equal probabilities. For example, the 0.25 quantile (or first quartile) is the value below which 25% of the data points are found. The 0.5 quantile is the median.

This implementation calculates the specified quantile over a rolling lookback period using linear interpolation.

## Core Concepts

*   **Rank-Based Value:** Identifies a value based on its rank or position within a sorted dataset, corresponding to a specific fraction of the data.
*   **Data Distribution Insight:** Helps understand the distribution of data within the lookback window. For instance, the 0.25, 0.5, and 0.75 quantiles (quartiles) describe the spread and central tendency.
*   **Rolling Calculation:** The quantile is calculated over a moving window of a fixed length.
*   **Linear Interpolation:** If the exact quantile rank falls between two data points, this method estimates the value by linearly interpolating between them.
*   **NA Handling:** `na` values in the `source` series within the lookback `period` are filtered out before the quantile calculation.

## Common Settings and Parameters

| Parameter       | Default | Function                                                                 | When to Adjust                                                                                                                               |
| :-------------- | :------ | :----------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------- |
| Source          | Close   | The data series to calculate the quantile from.                        | Change to High, Low, Open, HL2, HLC3, another indicator's output, etc., for different analyses.                                              |
| Period          | 14      | The number of bars in the lookback window.                               | Shorter periods make the quantile more sensitive to recent data; longer periods provide a more stable, longer-term quantile value.        |
| Quantile Level  | 0.25     | The quantile to calculate (a value between 0.0 and 1.0). E.g., 0.5 for median, 0.25 for the first quartile, 0.75 for the third quartile. | Adjust to observe different parts of the data distribution. For example, 0.1 and 0.9 quantiles can define a range capturing 80% of the data. |

**Pro Tip:** Plotting multiple quantiles (e.g., 0.1, 0.5, 0.9) can create dynamic channels or bands around the price, similar to Bollinger Bands but based on rank rather than standard deviation.

## Calculation and Mathematical Foundation

**Simplified explanation:**
1.  Collect all valid (non-`na`) numbers from the lookback period.
2.  Sort these numbers from smallest to largest.
3.  Determine the rank (position) that corresponds to the desired quantile level.
4.  If the rank points to an exact data point, that's the quantile value. If it falls between two data points, estimate the value using linear interpolation.

**Technical formula:**
The calculation involves these primary steps:
1.  **Data Collection:** Gather all non-`na` values from the `source` series within the `period`.
2.  **Sorting:** Sort the collected values in ascending order. Let the sorted array be `X` and its size be `N_valid`.
3.  **Rank Calculation:** Determine the 0-indexed rank `k` for the desired `quantile_level` (Q, between 0.0 and 1.0):
    `k = Q * (N_valid - 1)`
4.  **Value Retrieval/Interpolation:**
    *   If `Q = 0.0`, Quantile = `X[0]` (minimum).
    *   If `Q = 1.0`, Quantile = `X[N_valid - 1]` (maximum).
    *   If `k` is an integer, Quantile = `X[k]`.
    *   If `k` is not an integer, let `k_floor = floor(k)` and `k_ceil = ceil(k)`. The quantile is found by linear interpolation:
        `Quantile = X[k_floor] + (k - k_floor) * (X[k_ceil] - X[k_floor])`

> 🔍 **Technical Note on Linear Interpolation:** This method is equivalent to the R type 7 quantile estimation method and is commonly used in statistical software (e.g., Python's `numpy.percentile` with 'linear' interpolation). It ensures that the 0th quantile is the minimum and the 1st quantile (or 100th percentile) is the maximum of the dataset.

## Interpretation Details

*   **Dynamic Support/Resistance:** Lower quantiles (e.g., 0.1, 0.25) can act as dynamic support levels, while upper quantiles (e.g., 0.75, 0.9) can act as dynamic resistance levels.
*   **Volatility Assessment:** The spread between different quantiles (e.g., 0.9 - 0.1, or Interquartile Range: 0.75 - 0.25) can be a measure of data dispersion or volatility over the lookback period.
*   **Outlier Identification:** Values falling outside extreme quantiles (e.g., below 0.05 or above 0.95) might be considered outliers for the given period.
*   **Median (0.5 Quantile):** Provides a robust measure of central tendency, less affected by outliers than the mean.

## Limitations and Considerations

*   **Computational Cost:** Sorting an array of `N` elements typically takes O(N log N) time. This is done on every bar for the lookback window, so it can be more computationally intensive than simple averages for very long periods.
*   **Data Requirements:** Meaningful quantile calculation requires a sufficient number of data points. With very short periods, quantiles can be volatile or less representative.
*   **Choice of Interpolation Method:** While linear interpolation is common, other methods exist. The choice can slightly affect the result, especially for small datasets. This implementation uses the linear interpolation method described.
*   **Edge Quantiles (0.0 and 1.0):** The 0.0 quantile corresponds to the minimum value in the window, and the 1.0 quantile corresponds to the maximum value.

## References

*   Hyndman, R. J., & Fan, Y. (1996). Sample Quantiles in Statistical Packages. *The American Statistician*, *50*(4), 361–365.
*   Wikipedia contributors. (2023). Quantile. In *Wikipedia, The Free Encyclopedia*.
