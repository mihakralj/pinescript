# ZScore: Statistical Deviation Measure

[Pine Script Implementation of ZScore](https://github.com/mihakralj/pinescript/blob/main/indicators/statistics/zscore.pine)

## Overview and Purpose

Z-Score is a statistical measurement that describes a value's relationship to the mean of a group of values, measured in terms of standard deviations from the mean. In financial markets, Z-Score helps traders identify when prices have moved abnormally far from their recent average, potentially indicating overbought or oversold conditions.

This indicator expresses price action in units of standard deviation, providing a normalized view of market movements regardless of the underlying instrument's price scale or volatility characteristics. By quantifying how unusual current price levels are relative to recent history, Z-Score offers objective entry and exit signals based on statistical extremes.

## Core Concepts

* **Statistical Normalization:** Converts price movements into standard deviation units, allowing comparison across different assets and timeframes
* **Mean Reversion Signals:** Identifies potential reversal points when prices deviate significantly from their statistical average
* **Volatility-Adjusted Analysis:** Automatically adapts to changing market volatility conditions
* **Outlier Detection:** Highlights abnormal price movements that may signal important market events or trading opportunities

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
| :-------- | :------ | :------- | :------------ |
| Period | 14 | Controls the lookback window for statistical calculation | Lower (8-10) for more responsive signals, higher (20+) for more stable readings with fewer false signals |
| Source | Close | Data point used for calculation | Change to other price points (High/Low/Open) or derived values depending on analysis focus |

**Pro Tip:** Z-Score values beyond +/-2 occur only about 5% of the time in normally distributed data, making these levels effective for identifying potential mean reversion opportunities.

## Calculation and Mathematical Foundation

**Simplified explanation:**
Z-Score measures how many standard deviations a current value is from the mean of recent values. It does this by calculating the average and standard deviation of prices over a specified period, then expressing the current price as a deviation from that average in standardized units.

**Technical formula:**
Z-Score = (Current Value - Mean) / Standard Deviation

Where:
* Current Value is the most recent data point
* Mean is the average of values over the lookback period
* Standard Deviation is the square root of variance over the lookback period

> 🔍 **Technical Note:** The Pine Script implementation uses efficient dynamic arrays to maintain a rolling window of values, allowing for O(1) time complexity calculations per bar. It also includes proper handling of edge cases like zero standard deviation and insufficient data during warmup periods.

## Interpretation Details

Z-Score readings provide statistical context for price movements:

* **Positive Values:** Indicate the current price is above the mean, with higher values showing greater deviation
* **Negative Values:** Indicate the current price is below the mean, with lower values showing greater deviation
* **Magnitude Guidelines:**
  * Values between -1 and +1: Price is within one standard deviation of the mean (statistically normal behavior)
  * Values between -2 and +2: Price is within two standard deviations (encompasses ~95% of typical movement)
  * Values beyond -2 or +2: Price is exhibiting statistically rare behavior, suggesting potential mean reversion
* **Divergences:** When price makes new highs/lows but Z-Score fails to confirm, it may indicate weakening momentum

## Limitations and Considerations

* **Non-Normal Distributions:** Financial markets often exhibit non-normal distributions with fat tails, making extreme Z-Score values more common than statistical theory would predict
* **Changing Volatility:** During volatility regime changes, Z-Score can generate delayed signals as it adapts to new conditions
* **Setting Dependency:** Results vary significantly based on chosen period length - requiring calibration for different instruments
* **Context Sensitivity:** What constitutes an "extreme" Z-Score may differ across market regimes and asset classes
* **Mean Selection:** Using simple mean assumes price behavior is symmetric around the average, which may not always be true
* **Warmup Period:** Requires at least two bars of data to begin calculation, with full statistical validity requiring more samples

## References

* Taleb, N. N. (2007). The Black Swan: The Impact of the Highly Improbable. Random House.
* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
