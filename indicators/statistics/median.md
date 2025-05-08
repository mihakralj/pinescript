# MEDIAN: Median Value

[Pine Script Implementation of MEDIAN](https://github.com/mihakralj/pinescript/blob/main/indicators/statistics/median.pine)

## Overview and Purpose

The Median is a measure of central tendency that represents the middle value of a dataset when it is sorted. Unlike the mean (average), the median is not skewed by extremely large or small values (outliers) in the dataset. In trading, a rolling median can provide a more robust measure of the typical price or indicator level over a lookback period compared to a simple moving average.

This implementation calculates the median of all valid (non-`na`) data points within the specified lookback period.

## Core Concepts

*   **Central Tendency:** Identifies the middle value of the data, providing a robust measure of the center.
*   **Outlier Resistance:** Less affected by extreme values or outliers compared to the mean.
*   **Rolling Calculation:** The median is calculated over a moving window of a fixed length.
*   **NA Handling:** `na` values within the lookback period are excluded before sorting and finding the median.

## Common Settings and Parameters

| Parameter | Default | Function                                         | When to Adjust                                                                              |
| :-------- | :------ | :----------------------------------------------- | :------------------------------------------------------------------------------------------ |
| Source    | Close   | The data series to calculate the median from.    | Change to High, Low, Open, HL2, HLC3, another indicator's output, etc., for different analyses. |
| Period    | 14      | The number of bars in the lookback window.       | Shorter periods make the median more responsive; longer periods provide a more stable level.   |

**Pro Tip:** Use the median in conjunction with the mean. If the median and mean are significantly different, it suggests the presence of outliers or a skewed distribution in the data over the lookback period.

## Calculation and Mathematical Foundation

**Simplified explanation:**
To find the median:
1.  Collect all valid (non-`na`) numbers from the lookback period.
2.  Sort these numbers from smallest to largest.
3.  If there's an odd number of values, the median is the middle value.
4.  If there's an even number of values, the median is the average of the two middle values.

**Technical formula:**
For a sorted dataset x₁, x₂, ..., xₙ:
*   If `n` is odd, Median = x₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍(n+1)/2₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎
*   If `n` is even, Median = (x₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍n/2₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎ + x₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍₍n/2 + 1₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎₎) / 2

> 🔍 **Technical Note:** The Pine Script implementation collects all non-`na` values from the source series over the lookback period into a dynamic array. This array is then sorted on each bar using `array.sort()`, and the median is determined from the sorted array. For very long lookback periods, the sorting step might have performance implications compared to indicators using O(1) rolling sum techniques.

## Interpretation Details

*   **Robust Trend Line:** The median can act as a trend line that is less affected by brief, sharp price spikes compared to a simple moving average.
*   **Support and Resistance:** Like other moving averages, a rolling median can indicate potential areas of support or resistance.
*   **Skew Detection:** Comparing the median to the mean can give an informal idea of data skewness. If Mean > Median, the data might be skewed to the right (positive skew). If Mean < Median, it might be skewed to the left (negative skew).

## Limitations and Considerations

*   **Computational Cost:** Calculating the median by sorting an array on each bar can be computationally more expensive than simple moving averages, especially for long lookback periods. This might lead to slower script execution.
*   **Lag:** As it uses past data, the median will lag current price action.
*   **Responsiveness:** While robust to outliers, it might not be as smooth as some types of moving averages.

## References

*   Wikipedia contributors. (2023). Median. In *Wikipedia, The Free Encyclopedia*.
*   Tukey, J. W. (1977). *Exploratory Data Analysis*. Addison-Wesley.
