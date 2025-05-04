# LIN: Linear Transformation

[Pine Script Implementation of LIN](https://github.com/mihakralj/pinescript/blob/main/indicators/numerics/linear.pine)

## Overview and Purpose

The Linear Transformation indicator applies a configurable linear function to price data, enabling flexible scaling and shifting operations while maintaining the underlying pattern structure. Unlike simple offset adjustments, this transformation uses a formula that centers the scaling around the data's moving average, allowing for more sophisticated visual comparisons and overlays. This approach is particularly valuable for comparative analysis, normalization of different securities, and creating custom indicators that require rescaled inputs.

The implementation provided uses the formula y = a*(x - sma) + sma + b, which first scales deviations from the moving average by factor a, then shifts the entire series by constant b. This preserves the series' mean while allowing independent control of its amplitude and vertical position. The efficient algorithm maintains performance even with long lookback periods for the internal SMA calculation.

## Core Concepts

* **Mean-centered scaling:** Amplifies or dampens deviations from the moving average without shifting the mean position
* **Vertical translation:** Independently controls the vertical positioning of the transformed series
* **Pattern preservation:** Maintains the shape and temporal relationships of the original data
* **Visual normalization:** Enables direct visual comparison between series with different scales and ranges

Linear transformation serves as a fundamental building block for many analytical techniques in technical analysis. By properly rescaling data, analysts can overlay multiple securities, create custom oscillators, or normalize inputs for more complex indicators. This transformation bridges the gap between raw price data and the standardized inputs often required for advanced technical analysis.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Source | Close | Price data to transform | Change to analyze different aspects of price action |
| SMA Period | 200 | Lookback period for internal moving average calculation | Increase for more stable centering; decrease for more responsive centering |
| Scale (a) | 2.0 | Amplitude factor for deviations from the mean | Increase to amplify movements; decrease to dampen them |
| Offset (b) | 20.0 | Vertical displacement of the entire series | Adjust to position the transformed series on the chart |

**Pro Tip:** When comparing two securities with different price ranges, try setting scale factor 'a' to the ratio of their average true ranges (ATRs) to create proportional volatility. Then adjust offset 'b' to align their mean prices for direct visual comparison.

## Calculation and Mathematical Foundation

**Simplified explanation:**
The linear transformation first calculates a moving average of the input data, then applies a scaling factor to the deviations from this average, and finally adds an offset to the entire series.

**Technical formula:**

y = a × (x - SMA) + SMA + b

Where:
- x is the source value
- SMA is the simple moving average of the source
- a is the scaling factor
- b is the offset value

> 🔍 **Technical Note:** The implementation efficiently maintains a circular buffer of price values to calculate the SMA without recalculating the entire sum each time, maintaining O(1) time complexity regardless of the SMA period. This approach ensures predictable performance even with very long lookback periods.

## Interpretation Details

Linear transformation provides several analytical perspectives:

* **Amplitude analysis:** By adjusting the scaling factor 'a', deviations from the mean can be amplified (a > 1) or dampened (0 < a < 1)
* **Reversal effects:** Negative scaling factors (a < 0) can invert the pattern, useful for creating inverse correlations
* **Normalization:** Setting appropriate scale and offset values can normalize diverse data series to a common range
* **Overlap studies:** Multiple transformed series can be overlaid to directly compare their relative movements
* **Mean-reversion visualization:** The mean-centered scaling highlights deviations from the average, emphasizing mean-reverting behavior
* **Channel creation:** Applying different offsets to the same scaled series can create custom price channels

## Limitations and Considerations

* **Linearity constraints:** Cannot transform non-linear relationships without distortion
* **Scale preservation:** Does not preserve the absolute magnitudes of the original data
* **Moving average lag:** The internal SMA calculation introduces lag in the transformation reference point
* **Parameter sensitivity:** Results depend heavily on the chosen scale and offset parameters
* **Interpretation complexity:** Transformed values require mental conversion back to the original scale for accurate interpretation
* **Statistical impact:** Changes the distribution properties of the data, potentially affecting statistical analysis
* **Warmup period:** Requires sufficient historical data to establish a reliable SMA

## References

* Hyndman, R. J., & Athanasopoulos, G. (2018). Forecasting: Principles and Practice. OTexts.
* Box, G. E. P., Jenkins, G. M., Reinsel, G. C., & Ljung, G. M. (2015). Time Series Analysis: Forecasting and Control. John Wiley & Sons.
* Pring, M. J. (2002). Technical Analysis Explained. McGraw-Hill.
* Kirkpatrick, C. D., & Dahlquist, J. R. (2010). Technical Analysis: The Complete Resource for Financial Market Technicians. FT Press.
