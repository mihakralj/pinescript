# LinReg: Linear Regression Curve & Slope

[Pine Script Implementation of LinReg & Slope](https://github.com/mihakralj/pinescript/blob/main/indicators/statistics/linreg.pine)

## Overview and Purpose

Linear Regression analysis fits a straight line through a series of data points (like price) over a specified period using the least squares method. The `linreg()` function calculates both the value of this best-fit line at the current bar (the regression value) and the slope of the line.

1. **Regression Value:** Acts as a smoothed trendline that follows the data.
2. **Slope:** Quantifies the rate of change (direction and steepness) of the trend over the lookback period.

The function returns these as a tuple `[value, slope]`, providing insights into the current trend's direction, strength, and expected value based on recent linear movement.

## Core Concepts

* **Trend Following (Value):** The regression value provides a dynamic trendline that adapts to recent price action.
* **Trend Direction & Strength (Slope):** The sign of the slope indicates trend direction (positive for uptrend, negative for downtrend), while its magnitude indicates the strength or steepness.
* **Rate of Change (Slope):** Slope directly measures the average rate of change per bar over the lookback period.
* **Least Squares Method:** The function relies on finding the line that minimizes the sum of the squared differences between the actual data points and the line itself.
* **Time-Weighted:** The calculation inherently considers the time progression within the lookback window.
* **Tuple Return:** The function returns both the calculated regression value and the slope in a single tuple `[value, slope]`.

## Common Settings and Parameters

| Parameter | Default | Function                                     | When to Adjust                                                                 |
| :-------- | :------ | :------------------------------------------- | :----------------------------------------------------------------------------- |
| Period    | 14      | Controls the lookback window for calculation | Decrease for faster response to recent changes, increase for smoother readings |
| Source    | Close   | Data point used for calculation              | Change to High/Low, HL2, HLC3, etc., depending on the desired analysis focus   |

**Pro Tip:** Crossovers between the source price and the regression value can signal potential entry or exit points. A steepening slope can confirm strengthening momentum. Access the tuple elements like `[lrVal, lrSlope] = linreg(source, length)`.

## Calculation and Mathematical Foundation

**Simplified explanation:**
Linear regression finds the straight line (`y = mx + c`) that best represents the source data (`y`) over time (`x`) for the specified period. The `linreg()` function calculates both the `y` value on this line for the most recent `x` (the regression value) and the `m` (slope) of the line.

**Technical formula:**
The line is defined by: `y = intercept + slope * x`

Where:

* `y` is the source series (e.g., price)
* `x` is the time index series (0, 1, 2, ..., Period-1)
* `slope = Cov(x, y) / Var(x)`
* `intercept = Mean(y) - slope * Mean(x)`

The regression value is calculated by plugging the x-value corresponding to the current bar (which is `Period - 1` relative to the start of the window) into the line equation.

> 🔍 **Technical Note:** The Pine Script implementation calculates slope and intercept using rolling sums for efficiency, allowing calculations from the first available bars.

## Interpretation Details

* **Regression Value:**

   * Acts as a dynamic support/resistance level.
   * Its direction indicates the overall trend based on the linear fit.
   * Price crossing above/below the regression value can signal shifts in momentum.

* **Slope Value:**

    * **Positive Slope:** Indicates an upward trend over the lookback period. A larger positive value means a steeper uptrend.
    * **Negative Slope:** Indicates a downward trend. A larger negative value (further from zero) means a steeper downtrend.
    * **Slope near Zero:** Suggests a sideways market or consolidation phase.
    * **Changes in Slope:** Observing the slope's value over time reveals changes in trend momentum.

## Limitations and Considerations

* **Lag:** As a lookback-based indicator, `linreg` has inherent lag, especially with longer periods.
* **Linearity Assumption:** Linear regression assumes a linear trend. It may lag or provide misleading signals during sharp, non-linear market moves (e.g., parabolic rallies or crashes).
* **Outlier Sensitivity:** Extreme price points (outliers) within the lookback period can significantly influence the calculated line and slope.
* **Scale Dependent (Slope):** The absolute value of the slope depends on the scale of the source data. Comparing slope values across different assets requires normalization or careful consideration.
* **Whipsaws:** In choppy or sideways markets, price may frequently cross the regression value, and the slope may oscillate around zero, potentially generating false signals.

## References

* Wikipedia contributors. (2023). Simple linear regression. In Wikipedia, The Free Encyclopedia. Retrieved from [https://en.wikipedia.org/wiki/Simple_linear_regression](https://en.wikipedia.org/wiki/Simple_linear_regression)
