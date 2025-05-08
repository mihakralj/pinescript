# MODE: Mode (Most Frequent Value)

[Pine Script Implementation of MODE](https://github.com/mihakralj/pinescript/blob/main/indicators/statistics/mode.pine)

## Overview and Purpose

The Mode is a measure of central tendency that represents the most frequently occurring value in a dataset. Unlike the mean or median, the mode identifies the value that appears most often. In trading, a rolling mode can highlight price levels or indicator values that are repeatedly hit or act as points of congestion over a lookback period.

This implementation calculates the mode of all valid (non-`na`) data points within the specified lookback period. If all values are unique, or if no single value occurs more frequently than others (e.g., multiple values share the same highest frequency but only occur once), it returns `na`.

## Core Concepts

*   **Most Frequent Value:** Identifies the data point that occurs most often in the window.
*   **Data Concentration:** Can indicate levels where price or an indicator tends to cluster.
*   **Rolling Calculation:** The mode is calculated over a moving window of a fixed length.
*   **NA Handling:** `na` values within the lookback period are excluded from the frequency count.
*   **Uniqueness Handling:** Returns `na` if all values in the period are unique (i.e., every value occurs only once and there's more than one distinct value), as no single mode exists in such cases by some definitions. If multiple values share the same highest frequency, this implementation returns the first one encountered.

## Common Settings and Parameters

| Parameter | Default | Function                                         | When to Adjust                                                                              |
| :-------- | :------ | :----------------------------------------------- | :------------------------------------------------------------------------------------------ |
| Source    | Close   | The data series to calculate the mode from.      | Change to High, Low, Open, HL2, HLC3, another indicator's output, etc., for different analyses. |
| Period    | 14      | The number of bars in the lookback window.       | Shorter periods make the mode more sensitive to recent frequent values; longer periods identify more persistent modes. |

**Pro Tip:** The mode is most useful for discrete or categorical data but can be applied to continuous data like price. For price data, it might highlight specific price levels that are frequently revisited. Consider rounding price data to a certain number of decimal places before calculating mode if you want to group very close prices.

## Calculation and Mathematical Foundation

**Simplified explanation:**
To find the mode:
1.  Collect all valid (non-`na`) numbers from the lookback period.
2.  Count how many times each unique number appears.
3.  The number that appears most often is the mode.
4.  If all numbers appear only once (and there's more than one distinct number), or if there's no single most frequent value under certain strict definitions, then no mode is returned (`na`).

**Technical approach:**
The Pine Script implementation uses a `map` data structure to store the frequency of each unique value encountered in the lookback window. It then iterates through these frequencies to find the value associated with the highest frequency.

> 🔍 **Technical Note:** The implementation iterates through the lookback period to populate a frequency map, then iterates through the map's keys to find the mode. The performance depends on the number of unique values within the window and the length of the window. For data with many unique floating-point values (like raw price), the mode might frequently be `na` or change rapidly unless prices cluster at specific levels.

## Interpretation Details

*   **Congestion Levels:** A stable mode over time can indicate a price level that is acting as a point of control or significant interest.
*   **Repeated Test Levels:** If the mode consistently appears near key support or resistance levels, it can reinforce their significance.
*   **Data Distribution Insight:** Can give a quick glance at the most common value, which might differ significantly from mean or median in skewed distributions.

## Limitations and Considerations

*   **Continuous Data:** For continuous data like price, exact matches required for mode calculation might be rare unless prices frequently hit exact ticks. Rounding data or using price bins might yield more meaningful modes for such data.
*   **Multi-modality:** A dataset can have more than one mode (bimodal, trimodal, etc.). This implementation returns the first value encountered that has the maximum frequency. A more sophisticated analysis might list all modes or handle multi-modality differently.
*   **Sensitivity:** The mode can be very sensitive to small changes in data, especially with shorter periods or when frequencies are low.
*   **No Mode:** If all values are unique within the period (and more than one distinct value exists), this implementation returns `na`, indicating no single most frequent value.
*   **Computational Cost:** Using maps and iterations can be more computationally intensive than simple arithmetic averages for very long periods.

## References

*   Wikipedia contributors. (2023). Mode (statistics). In *Wikipedia, The Free Encyclopedia*.
*   Spiegel, M. R., & Stephens, L. J. (2008). *Schaum's Outline of Statistics*. McGraw-Hill.
