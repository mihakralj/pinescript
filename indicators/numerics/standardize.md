# STANDARDIZE: Standardization (Z-score)

[Pine Script Implementation of STANDARDIZE](https://github.com/mihakralj/pinescript/blob/main/indicators/numerics/standardize.pine)

## Overview and Purpose

Standardization, often referred to as Z-score normalization, is a data preprocessing technique that rescales data to have a mean of 0 and a standard deviation of 1. The resulting values, known as Z-scores, indicate how many standard deviations an individual data point is from the mean of the dataset (or a rolling sample of it).

This indicator calculates and plots the Z-score for a given input series over a specified lookback period. It is a fundamental tool for statistical analysis, outlier detection, and preparing data for certain machine learning algorithms.

## Core Concepts

*   **Standardization:** The process of transforming data to fit a standard normal distribution (or more generally, to have a mean of 0 and standard deviation of 1).
*   **Z-score (Standard Score):** A dimensionless quantity that represents the number of standard deviations by which a data point deviates from the mean of its sample.
    The formula for a Z-score is:
    `Z = (x - μ) / σ`
    Where:
    *   `x` is the individual data point (e.g., current value of the source series).
    *   `μ` (mu) is the mean of the sample (calculated over the lookback period).
    *   `σ` (sigma) is the standard deviation of the sample (calculated over the lookback period).
*   **Mean (μ):** The average value of the data points in the sample.
*   **Standard Deviation (σ):** A measure of the amount of variation or dispersion of a set of values. A low standard deviation indicates that the values tend to be close to the mean, while a high standard deviation indicates that the values are spread out over a wider range.

## Common Settings and Parameters

| Parameter       | Type         | Default | Function                                                                                                | When to Adjust                                                                                                                                                              |
| :-------------- | :----------- | :------ | :------------------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Source          | series float | close   | The input data series (e.g., price, volume, indicator values).                                          | Choose the series you want to standardize.                                                                                                                                  |
| Lookback Period | int          | 20      | The number of bars (sample size) used for calculating the mean (μ) and standard deviation (σ). Min 2.   | A larger period provides more stable estimates of μ and σ but will be less responsive to recent changes. A shorter period is more reactive. `minval` is 2 because `ta.stdev` requires it. |

**Pro Tip:** Z-scores are excellent for identifying anomalies or extreme values. For instance, applying Standardization to trading volume can help quickly spot days with unusually high or low activity relative to the recent norm (e.g., Z-score > 2 or < -2).

## Calculation and Mathematical Foundation

The Z-score is calculated for each bar as follows, using a rolling window defined by the `Lookback Period`:

1.  **Calculate Mean (μ):** The simple moving average (`ta.sma`) of the `Source` data over the specified `Lookback Period` is calculated. This serves as the sample mean `μ`.
    `μ = ta.sma(Source, Lookback Period)`
2.  **Calculate Standard Deviation (σ):** The standard deviation (`ta.stdev`) of the `Source` data over the same `Lookback Period` is calculated. This serves as the sample standard deviation `σ`.
    `σ = ta.stdev(Source, Lookback Period)`
3.  **Calculate Z-score:**
    *   If `σ > 0`: The Z-score is calculated using the formula:
        `Z = (Current Source Value - μ) / σ`
    *   If `σ = 0`: This implies all values in the lookback window are identical (and equal to the mean). In this case, the Z-score is defined as 0, as the current source value is also equal to the mean.
    *   If `σ` is `na` (e.g., insufficient data in the lookback period), the Z-score is `na`.

> 🔍 **Technical Note:**
> *   The `Lookback Period` must be at least 2 for `ta.stdev` to compute a valid standard deviation.
> *   The Z-score calculation uses the sample mean and sample standard deviation from the rolling lookback window.

## Interpreting the Z-score

*   **Magnitude and Sign:**
    *   A Z-score of **0** means the data point is identical to the sample mean.
    *   A **positive Z-score** indicates the data point is above the sample mean. For example, Z = 1 means the point is 1 standard deviation above the mean.
    *   A **negative Z-score** indicates the data point is below the sample mean. For example, Z = -1 means the point is 1 standard deviation below the mean.
*   **Typical Range:** For data that is approximately normally distributed (bell-shaped curve):
    *   About 68% of Z-scores fall between -1 and +1.
    *   About 95% of Z-scores fall between -2 and +2.
    *   About 99.7% of Z-scores fall between -3 and +3.
*   **Outlier Detection:** Z-scores significantly outside the -2 to +2 range, and especially outside -3 to +3, are often considered outliers or extreme values relative to the recent historical data in the lookback window.
*   **Volatility Indication:** When applied to price, large absolute Z-scores can indicate moments of high volatility or significant deviation from the recent price trend.

The indicator plots horizontal lines at ±1, ±2, and ±3 standard deviations to help visualize these common thresholds.

## Common Applications

1.  **Outlier Detection:** Identifying data points that are unusual or extreme compared to the rest of the sample. This is a primary use in financial markets for spotting abnormal price moves, volume spikes, etc.
2.  **Comparative Analysis:** Allows for comparison of scores from different distributions that might have different means and standard deviations. For example, comparing the Z-score of returns for two different assets.
3.  **Feature Scaling in Machine Learning:** Standardizing features to have a mean of 0 and standard deviation of 1 is a common preprocessing step for many machine learning algorithms (e.g., SVMs, logistic regression, neural networks) to improve performance and convergence.
4.  **Creating Normalized Oscillators:** The Z-score itself can be used as a bounded (though not strictly between -1 and +1) oscillator, indicating how far the current price has deviated from its moving average in terms of standard deviations.
5.  **Statistical Process Control:** Used in quality control charts to monitor if a process is within expected statistical limits.

## Limitations and Considerations

*   **Assumption of Normality for Probabilistic Interpretation:** While Z-scores can always be calculated, the probabilistic interpretations (e.g., "68% of data within ±1σ") strictly apply to normally distributed data. Financial data is often not perfectly normal (e.g., it can have fat tails).
*   **Sensitivity of Mean and Standard Deviation to Outliers:** The sample mean (μ) and standard deviation (σ) used in the Z-score calculation can themselves be influenced by extreme outliers within the lookback period. This can sometimes mask or exaggerate the Z-score of other points.
*   **Choice of Lookback Period:** The Z-score is highly dependent on the `Lookback Period`. A short period makes it very sensitive to recent fluctuations, while a long period makes it smoother and less responsive. The appropriate period depends on the analytical goal.
*   **Stationarity:** For time series data, Z-scores are calculated based on a rolling window. This implicitly assumes some level of local stationarity (i.e., the mean and standard deviation are relatively stable within the window).

## References

*   Wikipedia contributors. (2023). *Standard score*. Wikipedia, The Free Encyclopedia. Retrieved from [https://en.wikipedia.org/wiki/Standard_score](https://en.wikipedia.org/wiki/Standard_score)
*   NIST/SEMATECH e-Handbook of Statistical Methods, "Measures of Scale", available at [https://www.itl.nist.gov/div898/handbook/prc/section1/prc122.htm](https://www.itl.nist.gov/div898/handbook/prc/section1/prc122.htm) (Discusses Standard Deviation)
