# NORMALIZE: Min-Max Scaling (Normalization)

[Pine Script Implementation of NORMALIZE](https://github.com/mihakralj/pinescript/blob/main/indicators/numerics/normalize.pine)

## Overview and Purpose

Min-Max Scaling, often referred to as normalization, is a data preprocessing technique used to rescale numeric features to a fixed range, typically [0, 1] or [-1, 1]. This is achieved by shifting and scaling the values based on the minimum and maximum values observed in the data over a specified lookback period.

In financial analysis, normalization can be useful for:
*   Comparing indicators or price series that operate on different scales.
*   Preparing data for machine learning algorithms that are sensitive to the scale of input features (e.g., Support Vector Machines, K-Nearest Neighbors, neural networks with certain activation functions).
*   Creating bounded oscillators that fluctuate within a defined range, making it easier to identify overbought/oversold conditions or relative strength.

## Core Concepts

*   **Rescaling:** Transforming data from its original range to a new, predefined range.
*   **Lookback Period:** The number of past data points used to determine the current minimum and maximum values for scaling.
*   **Target Range:** The normalized output is always scaled to the range [0, 1].

## Common Settings and Parameters

| Parameter         | Default | Function                                                                 | When to Adjust                                                                                                                               |
| :---------------- | :------ | :----------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------- |
| Source            | Close   | Data point or series to be normalized.                                   | Can be any series, such as price, returns, volume, or another indicator output.                                                              |
| Lookback Length   | 200     | Number of bars to find the min and max values for scaling.               | Shorter lengths make the normalization more sensitive to recent price action; longer lengths provide a more stable, longer-term perspective. |

**Pro Tip:** Normalizing an indicator like RSI or Stochastics (which are already bounded) might not be necessary unless you want to rescale them to a different specific range or combine them with other differently scaled indicators. Normalizing unbounded indicators like Momentum or MACD can be very useful for creating consistent oscillator behavior within the [0, 1] range.

## Calculation and Mathematical Foundation

**Simplified explanation:**
1.  Find the highest and lowest values of the `Source` data over the `Lookback Length`.
2.  For the current `Source` value, determine where it sits proportionally between this min and max. (e.g., if min=10, max=20, and current=15, it's at the 50% mark). This proportion will be a value between 0 and 1.

**Technical formula:**

Normalized Value = (X - X<sub>min</sub>) / (X<sub>max</sub> - X<sub>min</sub>)

Where:
*   `X` is the current value of the `Source` series.
*   `X_min` is the minimum value of the `Source` series over the `Lookback Length`.
*   `X_max` is the maximum value of the `Source` series over the `Lookback Length`.

If `X_max` equals `X_min` (i.e., the range is zero), the `Normalized Value` is 0.0.

**Special Case (X<sub>max</sub> - X<sub>min</sub> = 0):**
If all values within the `Lookback Length` are identical (i.e., `X_max` - `X_min` = 0), the `Source` value `X` must be equal to `X_min` (and `X_max`). In this scenario, the formula `(X - X_min) / (X_max - X_min)` would result in 0/0. The Pine Script implementation handles this by directly outputting `0.0`.

> 🔍 **Technical Note:** The Pine Script `normalize` function determines the minimum (`min_val_in_period`) and maximum (`max_val_in_period`) values of the `src` series over the specified `len` lookback period by iterating through the historical data in a single pass within its own code block. It does not use separate helper functions or the built-in `ta.lowest()`/`ta.highest()` functions for this. It then applies the simplified normalization formula for the [0, 1] range, carefully handling the case where `max_val_in_period - min_val_in_period` is zero to prevent division by zero errors and ensure an output of `0.0`.

## Interpretation Details

*   A value of **1.0** indicates that the current `Source` value is the highest it has been over the `Lookback Length`.
*   A value of **0.0** indicates that the current `Source` value is the lowest it has been over the `Lookback Length` (or that all values in the lookback period were identical).
*   Values between 0 and 1 represent the relative position of the current `Source` value within its range over the lookback period. For example:
    *   Output ≈ 1.0: Source is at or near its recent high.
    *   Output ≈ 0.0: Source is at or near its recent low.
    *   Output ≈ 0.5: Source is midway between its recent high and low.

## Limitations and Considerations

*   **Sensitivity to Lookback Period:** The choice of `Lookback Length` significantly impacts the output. A short period can lead to volatile normalized values, while a very long period might make the indicator slow to react to new price extremes.
*   **Outliers:** Extreme outliers within the lookback window can compress the rest of the data into a small portion of the target range, potentially obscuring finer details.
*   **Non-Stationary Data:** For highly trending or non-stationary data, the min/max values can shift dramatically, causing the normalized output to frequently hit the target boundaries.
*   **Information Loss (Contextual):** While normalization makes comparison easier, it removes information about the absolute magnitude and volatility of the original series.
*   **Warm-up Period:** Requires `Lookback Length` bars to have a full window for min/max calculation. Values during warm-up are based on fewer bars.

## References

*   Han, J., Pei, J., & Kamber, M. (2011). *Data Mining: Concepts and Techniques* (3rd ed.). Morgan Kaufmann. (Chapter 3: Data Preprocessing)
*   Wikipedia contributors. (2023). *Feature scaling*. Wikipedia, The Free Encyclopedia.
