# CUMMEAN: Cumulative Mean (Average)

[Pine Script Implementation of CUMMEAN](https://github.com/mihakralj/pinescript/blob/main/indicators/statistics/cummean.pine)

## Overview and Purpose

The Cumulative Mean (or running average) calculates the average of all data points in a series from the very first data point up to the current data point. Unlike a rolling mean (Simple Moving Average), which considers a fixed-length window, the cumulative mean incorporates all past data available in its calculation at each step.

This implementation calculates the cumulative mean from the start of the chart history, ignoring any `na` (Not a Number) values.

## Core Concepts

*   **Overall Central Tendency:** Provides the average value of the series, taking into account all historical data from the beginning.
*   **Evolving Average:** The mean updates with each new data point, reflecting the influence of the entire history.
*   **NA Handling:** `na` values in the series are excluded from both the sum and the count, ensuring the average is based only on valid data points.
*   **No Rolling Window:** The calculation window grows with each new bar, encompassing all data from the start.

## Common Settings and Parameters

| Parameter | Default | Function                                         | Notes                                                                              |
| :-------- | :------ | :----------------------------------------------- | :------------------------------------------------------------------------------------------ |
| Source    | Close   | The data series to calculate the cumulative mean from. | Change to High, Low, Open, HL2, HLC3, etc., for different analyses. |
| Period    | 14      | Ignored by this cumulative mean implementation.  | This parameter is present for consistency but does not affect the calculation. The mean is always fully cumulative. |

**Pro Tip:** The cumulative mean is useful for observing how the overall average of a series evolves over its entire lifetime. It can be sensitive to early values in long series.

## Calculation and Mathematical Foundation

**Simplified explanation:**
The cumulative mean at any point in time is calculated by adding up all the valid (non-`na`) numbers in the series from the very first bar to the current bar, and then dividing by how many valid numbers there were in that entire span.

**Technical formula (at bar `t`):**

Cumulative Mean_t = (Σ_{i=1 to t} xᵢ) / n_t

Where:
*   Σ_{i=1 to t} xᵢ is the sum of all valid (non-`na`) values from the first bar up to bar `t`.
*   `n_t` is the count of valid (non-`na`) values from the first bar up to bar `t`.

> 🔍 **Technical Note:** The Pine Script implementation uses `var` variables to maintain a running `cumulative_sum` and `valid_data_count` from the start of the data series. This is an O(1) operation per bar.

## Interpretation Details

*   **Long-Term Baseline:** Shows the average value of the series over its entire history up to the current point.
*   **Stabilization:** Tends to stabilize over time as more data points are included, making it less reactive to recent changes compared to a short-period rolling mean.
*   **Drift Indication:** Significant divergence of current price from a long-standing cumulative mean might indicate a major shift in the series' underlying value or behavior.

## Limitations and Considerations

*   **Sensitivity to Initial Values:** In very long time series, the early values can have a diminishing but persistent effect on the cumulative mean.
*   **Slow to Adapt:** Because it includes all past data, it adapts very slowly to new trends or shifts in the data's central tendency compared to rolling means.
*   **Not for Short-Term Trading Signals:** Generally not suitable for generating short-term trading signals due to its extensive memory of past data.
*   **Stationarity Assumption:** Like any mean, its interpretation is most straightforward for data that is reasonably stationary around some level. For strongly trending series, it will continuously trend as well.

## References

*   Wikipedia contributors. (2023). Moving average (Cumulative moving average). In *Wikipedia, The Free Encyclopedia*.
