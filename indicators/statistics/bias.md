# BIAS: Bias

[Pine Script Implementation of BIAS](https://github.com/mihakralj/pinescript/blob/main/indicators/statistics/bias.pine)

## Overview and Purpose

The Bias indicator measures the deviation of a source series (typically price) from its moving average. It quantifies how far the current value has strayed from its recent mean. This helps traders identify overbought or oversold conditions, gauge the strength of a trend relative to its average, and spot potential mean-reversion opportunities.

Positive BIAS values indicate the source is above its moving average, while negative values indicate it's below. The magnitude of the BIAS suggests the extent of the deviation.

## Core Concepts

*   **Mean Reversion:** BIAS is often used to identify conditions where the price has moved significantly away from its mean and might be due for a correction back towards it.
*   **Trend Strength:** Consistently high positive or low negative BIAS values can indicate a strong, sustained trend.
*   **Overbought/Oversold Levels:** Extreme BIAS readings can signal potential overbought (high positive) or oversold (high negative) market conditions.
*   **Relative Deviation:** Expresses deviation as a ratio, making it comparable across different price levels and securities.

## Common Settings and Parameters

| Parameter | Default | Function                                   | When to Adjust                                                                 |
| :-------- | :------ | :----------------------------------------- | :----------------------------------------------------------------------------- |
| Source    | Close   | Data point used for BIAS calculation.      | Adjust based on analysis focus (e.g., High/Low for range dynamics).            |
| Length    | 20      | Lookback period for the moving average.    | Shorter for more sensitivity to recent price action; longer for smoother BIAS. |

**Pro Tip:** Look for divergences between the source series and BIAS. For example, if price makes a new high but BIAS makes a lower high, it could signal weakening bullish momentum.

## Calculation and Mathematical Foundation

**Simplified explanation:**
BIAS is calculated by taking the difference between the current source value and its Simple Moving Average (SMA), and then dividing this difference by the SMA.

**Technical formula:**

BIAS = ((Source - SMA(Source, Length)) / SMA(Source, Length)) * 100

Where:
*   `Source` is the current value of the input series.
*   `SMA(Source, Length)` is the Simple Moving Average of the `Source` over the specified `Length`.
*   `Length` is the lookback period for the SMA.

> 🔍 **Technical Note:** The Pine Script implementation calculates the Simple Moving Average (SMA) internally using an efficient circular buffer method. This method maintains a running sum and a buffer of recent source values. During the initial warm-up period (fewer bars than the specified `Length`), the SMA is calculated based on the available bars. `na` (Not a Number) source values are treated as zero (`nz(src, 0.0)`) for sum integrity but do not increment the `validCount` if they replace an existing `na` in the buffer, ensuring the divisor accurately reflects the number of actual values. Once the buffer is full, the SMA is calculated using the full `Length`. The BIAS calculation itself then proceeds, handling cases where the calculated `movingAverage` might be `na` or zero to prevent errors.

## Interpretation Details

*   **Positive BIAS:** The source is trading above its moving average. Higher values indicate a greater deviation above the mean.
*   **Negative BIAS:** The source is trading below its moving average. Lower (more negative) values indicate a greater deviation below the mean.
*   **Zero Line:** When BIAS is near zero, the source is trading close to its moving average.
*   **Extreme Readings:** Values significantly above or below historical norms for the specific asset and timeframe can indicate potential overbought or oversold conditions, respectively. These thresholds are often determined empirically.
*   **Trend Confirmation:** In an uptrend, BIAS will generally remain positive. In a downtrend, it will generally remain negative. A shift across the zero line can signal a potential change in trend.

## Limitations and Considerations

*   **Lag:** Since BIAS relies on a moving average, it is a lagging indicator.
*   **Whipsaws:** In choppy or sideways markets, BIAS can generate frequent buy/sell signals that may not be profitable.
*   **Parameter Sensitivity:** The choice of `Length` for the moving average significantly impacts the BIAS values and signals.
*   **No Fixed Thresholds:** "Overbought" or "oversold" levels vary between assets and timeframes and are not universally defined.
*   **Context is Key:** BIAS should be used in conjunction with other indicators and price action analysis for more reliable signals.

## References

*   Colby, R. W. (2003). *The Encyclopedia of Technical Market Indicators*. McGraw-Hill.
*   Pring, M. J. (2002). *Technical Analysis Explained*. McGraw-Hill.
