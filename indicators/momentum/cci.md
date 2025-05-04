# CCI: Commodity Channel Index

[Pine Script Implementation of CCI](https://github.com/mihakralj/pinescript/blob/main/indicators/momentum/cci.pine)

## Overview and Purpose

The Commodity Channel Index (CCI) is a versatile momentum oscillator developed by Donald Lambert in 1980. Originally designed for commodity trading, CCI measures an instrument's variation from its statistical mean. By comparing the current price to an average price, CCI helps identify cyclical turns, overbought/oversold conditions, and trend strength. The indicator oscillates above and below a zero line, with readings above +100 or below -100 traditionally signaling extreme conditions.

The implementation provided uses circular buffers for simple moving average calculations, ensuring optimal performance while properly handling data gaps. This approach maintains O(1) computational complexity regardless of the lookback period, making it particularly suitable for real-time analysis of high-frequency data while preserving accuracy in mean deviation calculations.

## Core Concepts

* **Mean price deviation:** Measures how far price has moved from its statistical average
* **Cyclical identification:** Helps identify overbought and oversold conditions in cyclic markets
* **Trend strength measurement:** Indicates trending conditions through sustained readings in one direction
* **Statistical foundation:** Based on the assumption that prices are normally distributed around their mean

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 20 | Lookback period for calculations | Lower for more signals but increased noise, higher for smoother readings |

**Pro Tip:** While the default 20-period setting works well for daily charts, consider using 14 periods for more active markets or 30 periods for less volatile instruments. The traditional +100/-100 thresholds can be adjusted to +/-75 for more frequent signals or +/-150 for extreme conditions only.

## Calculation and Mathematical Foundation

**Simplified explanation:**
CCI measures how far price has moved from its average in terms of mean deviation. It first calculates a typical price (TP), then compares how far that TP is from its moving average, scaled by a factor of 0.015 to normalize the indicator.

**Technical formula:**
CCI = (TP - SMA(TP)) / (0.015 × MD)

Where:
- TP (Typical Price) = (High + Low + Close) / 3
- SMA = Simple Moving Average
- MD = Mean Deviation of TP from its SMA
- 0.015 = Constant to normalize the indicator

> 🔍 **Technical Note:** The implementation uses circular buffers to efficiently maintain running sums for the SMA calculation, ensuring O(1) computational complexity per bar. The algorithm properly handles NA values and maintains accurate mean deviation calculations without recalculating entire sums each bar.

## Interpretation Details

CCI provides multiple analytical perspectives:

* **Overbought/Oversold:** Readings above +100 suggest overbought conditions, below -100 suggest oversold
* **Trend strength:** Sustained readings above/below zero indicate trend direction and strength
* **Divergence signals:** CCI diverging from price can signal potential reversals
* **Zero-line crossovers:** Can indicate trend changes when combined with other signals
* **Extreme readings:** Values beyond ±200 often precede significant reversals
* **Trend confirmation:** Direction of CCI movement confirms price trend direction

## Limitations and Considerations

* **Scaling sensitivity:** The fixed 0.015 constant may not be optimal for all markets
* **False signals:** Can generate numerous signals in choppy markets
* **Lag component:** Moving average calculations introduce some lag in signals
* **Normalization issues:** May not be perfectly normalized for all market conditions
* **Timeframe dependency:** Different timeframes require different interpretation approaches
* **Complementary analysis:** Should be used alongside trend and volume indicators for confirmation

## References

* Lambert, D. R. (1980). Commodity Channel Index: Tool for Trading Cyclic Trends. Commodities Magazine.
* Jobman, D. R. (1995). The Handbook of Technical Analysis. McGraw-Hill.
* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
* Kaufman, P. J. (2013). Trading Systems and Methods (5th ed.). Wiley Trading.
