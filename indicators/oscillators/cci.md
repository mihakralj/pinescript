# CCI: Commodity Channel Index

[Pine Script Implementation of CCI](https://github.com/mihakralj/pinescript/blob/main/indicators/oscillators/cci.pine)

## Overview and Purpose

The Commodity Channel Index (CCI) is a versatile momentum oscillator developed by Donald Lambert in 1980. Originally designed for commodity trading, it measures an instrument's deviation from its statistical mean. By comparing the current price to an average price and normalizing by mean deviation, CCI helps identify cyclical turns, overbought/oversold conditions, and trend strength. The indicator oscillates above and below a zero line, with readings above +100 or below -100 traditionally signaling extreme conditions.

The implementation provided uses circular buffers for moving average calculations, ensuring optimal performance while properly handling data gaps. This approach maintains O(1) computational complexity regardless of the lookback period, making it particularly suitable for real-time analysis.

## Core Concepts

* **Mean price deviation:** Measures how far price has moved from its statistical average
* **Cyclical identification:** Helps identify overbought and oversold conditions in cyclic markets
* **Trend strength measurement:** Indicates trending conditions through sustained readings
* **Statistical normalization:** Uses mean deviation and 0.015 constant for consistent scaling

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 20 | Lookback period for calculations | Lower for more signals but increased noise, higher for smoother readings |
| Overbought Level | 100 | Upper threshold for extreme conditions | Increase for fewer but stronger signals |
| Oversold Level | -100 | Lower threshold for extreme conditions | Decrease for fewer but stronger signals |

**Pro Tip:** While the default 20-period setting works well for daily charts, consider using 14 periods for more active markets or 30 periods for less volatile instruments. The traditional +100/-100 thresholds can be adjusted to +/-75 for more frequent signals.

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

> 🔍 **Technical Note:** The implementation uses circular buffers to efficiently maintain running sums for the SMA calculation, ensuring O(1) computational complexity per bar. The algorithm properly handles NA values and maintains accurate mean deviation calculations.

## Interpretation Details

CCI provides multiple analytical perspectives:

* **Overbought/Oversold:** Readings above +100 suggest overbought conditions, below -100 suggest oversold
* **Trend strength:** Sustained readings above/below zero indicate trend direction and strength
* **Divergence signals:** CCI diverging from price can signal potential reversals
* **Zero-line crossovers:** Can indicate trend changes when combined with other signals
* **Color coding:** Green for overbought, red for oversold, yellow for neutral conditions

## Limitations and Considerations

* **Scaling sensitivity:** The fixed 0.015 constant may not be optimal for all markets
* **False signals:** Can generate numerous signals in choppy markets
* **Lag component:** Moving average calculations introduce some lag
* **Normalization issues:** May not be perfectly normalized for all market conditions
* **Complementary tools:** Best used alongside trend and volume indicators

## References

* Lambert, D. R. (1980). Commodity Channel Index: Tool for Trading Cyclic Trends. Commodities Magazine.
* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
* Kaufman, P. J. (2013). Trading Systems and Methods (5th ed.). Wiley Trading.
