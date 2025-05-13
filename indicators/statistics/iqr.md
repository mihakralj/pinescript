# IQR: Interquartile Range

[Pine Script Implementation of IQR](https://github.com/mihakralj/pinescript/blob/main/indicators/statistics/iqr.pine)

## Overview and Purpose

The Interquartile Range (IQR) is a measure of statistical dispersion, representing the spread of the middle 50% of a dataset. It is calculated as the difference between the 75th percentile (Q3, or the third quartile) and the 25th percentile (Q1, or the first quartile).

The IQR is a robust measure of variability, meaning it is less sensitive to outliers than the standard deviation or range. It is widely used in descriptive statistics and for identifying potential outliers in data. This indicator calculates and plots the IQR for a given input series over a specified lookback period.

## Core Concepts

*   **Percentile:** A measure indicating the value below which a given percentage of observations in a group of observations falls. For example, the 25th percentile is the value below which 25% of the data may be found.
*   **Quartiles:** Values that divide a dataset into four equal parts.
    *   **Q1 (First Quartile):** The 25th percentile. It separates the lowest 25% of data from the highest 75%.
    *   **Q2 (Second Quartile):** The 50th percentile, also known as the median. It splits the data into two equal halves.
    *   **Q3 (Third Quartile):** The 75th percentile. It separates the lowest 75% of data from the highest 25%.
*   **Interquartile Range (IQR):** The difference between the third quartile (Q3) and the first quartile (Q1).
    `IQR = Q3 - Q1`
    It represents the range within which the central 50% of the data lies.

## Common Settings and Parameters

| Parameter       | Type         | Default | Function                                                                 | When to Adjust                                                                                                                               |
| :-------------- | :----------- | :------ | :----------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------- |
| Source          | series float | close   | The input data series (e.g., price, returns, indicator values).          | Choose the series for which you want to measure dispersion.                                                                                  |
| Lookback Period | int          | 20      | The number of bars (sample size) used for calculating Q1 and Q3. Min 2. | A larger period provides more stable estimates of quartiles and IQR but will be less responsive to recent changes. A shorter period is more reactive. |

**Pro Tip:** The IQR is often used to define outlier "fences". For example, mild outliers might be defined as values below `Q1 - 1.5 * IQR` or above `Q3 + 1.5 * IQR`. Extreme outliers might use a factor of 3 instead of 1.5.

## Calculation and Mathematical Foundation

The IQR is calculated as follows for a given `source` series and `length`:

1.  **Identify Q1:** The first quartile (25th percentile) of the data in the lookback window of `length` bars is determined. This implementation uses linear interpolation for percentile calculation (`ta.percentile_linear_interpolation`).
2.  **Identify Q3:** The third quartile (75th percentile) of the data in the lookback window of `length` bars is determined, also using linear interpolation.
3.  **Calculate IQR:** The Interquartile Range is the difference between Q3 and Q1:
    `IQR = Q3 - Q1`

> 🔍 **Technical Note:** The `ta.percentile_linear_interpolation(source, length, percentage)` function in Pine Script is used for calculating the quartiles. The choice of percentile calculation method (e.g., linear interpolation, nearest rank) can slightly affect the Q1, Q3, and thus IQR values, especially with small or discrete datasets. The `minval` for `Lookback Period` is 2, as percentiles are not well-defined for a single data point.

## Interpreting the Interquartile Range

*   **Magnitude:**
    *   A **larger IQR** indicates that the middle 50% of the data points are spread out over a wider range, implying higher variability or dispersion in the dataset.
    *   A **smaller IQR** indicates that the middle 50% of the data points are clustered more closely together, implying lower variability or dispersion.
*   **Volatility:** In financial markets, a higher IQR for price changes or returns can suggest higher volatility, while a lower IQR can suggest lower volatility or consolidation.
*   **Comparison:** The IQR can be compared over time or across different assets. An increasing IQR might signal rising volatility, while a decreasing IQR might signal calming volatility.

The indicator also provides options to plot Q1 and Q3, which can help visualize the range itself.

## Common Applications

1.  **Volatility Assessment:** Used as a measure of market volatility. A widening IQR can indicate increasing price dispersion.
2.  **Outlier Detection (Box Plots):** IQR is a key component in constructing box plots and identifying potential outliers. Values significantly below Q1 or above Q3 (e.g., by 1.5 * IQR) are often flagged.
3.  **Descriptive Statistics:** Provides a robust measure of the spread of a distribution, less affected by extreme values than standard deviation.
4.  **Risk Management:** Can help in understanding the typical range of price movements, excluding extreme outliers, for setting stop-losses or take-profits.
5.  **Comparing Distributions:** Useful for comparing the dispersion of different datasets or the same dataset at different times.

## Limitations and Considerations

*   **Not a Directional Indicator:** IQR measures dispersion (volatility) but does not provide information about the direction of price trends.
*   **Sensitivity to Lookback Period:** The calculated IQR value is dependent on the chosen `Lookback Period`. Shorter periods will make the IQR more responsive to recent data, while longer periods will smooth it out.
*   **Interpretation Context:** While IQR indicates the spread of the central 50% of data, it doesn't provide information about the tails of the distribution beyond Q1 and Q3, unlike measures like kurtosis or examining extreme values directly.
*   **Data Type:** Best suited for continuous or at least ordinal data where percentiles are meaningful.

## References

*   Wikipedia contributors. (2023). *Interquartile range*. Wikipedia, The Free Encyclopedia. Retrieved from [https://en.wikipedia.org/wiki/Interquartile_range](https://en.wikipedia.org/wiki/Interquartile_range)
*   NIST/SEMATECH e-Handbook of Statistical Methods, "Interquartile Range (IQR)", available at [https://www.itl.nist.gov/div898/handbook/prc/section1/prc16.htm](https://www.itl.nist.gov/div898/handbook/prc/section1/prc16.htm)
