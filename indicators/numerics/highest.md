# Highest: Highest Value

[Pine Script Implementation of Highest](https://github.com/mihakralj/pinescript/blob/main/indicators/numerics/highest.pine)

## Overview and Purpose

The Highest Value indicator identifies the maximum price (or other data point) reached within a specified lookback period. This fundamental statistical measure serves as an essential building block for many technical analysis tools and trading strategies. By tracking the highest values over time, traders can identify significant price levels, resistance zones, and potential breakout points.

## Core Concepts

* **Price extremes identification:** Highest Value efficiently tracks price peaks, helping identify potential resistance levels and breakout points
* **Market application:** Particularly useful for setting stop-loss levels, recognizing chart patterns, and defining trailing stops based on previous price action
* **Timeframe suitability:** **All timeframes** are effective, with shorter periods (5-20) for identifying immediate resistance levels and longer periods (20-200) for significant historical resistance

Highest Value forms the foundation for numerous technical indicators and trading systems, including Donchian Channels, Price Envelopes, and various trend-following strategies.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Period | 14 | Controls the lookback window for calculation | Decrease for more responsive readings in active markets, increase for identifying significant historical levels |
| Source | Close | Data point used for calculation | Switch to High for true price extremes, or use other price data based on specific strategy requirements |

**Pro Tip:** Using multiple Highest Value periods simultaneously (e.g., 20, 50, and 200) can help identify a hierarchy of resistance levels, with longer-period highs typically representing stronger resistance zones.

## Calculation and Mathematical Foundation

**Simplified explanation:**
The Highest Value indicator scans a specified number of previous bars and identifies the maximum value within that range. As each new bar forms, the indicator updates by dropping the oldest bar from its calculation and adding the newest one, continuously tracking the highest value within the moving window.

**Technical formula:**
Highest(Source, Length) = Maximum value of Source over the past Length bars

Where:

* Source is the price or data series being analyzed (typically Close or High)
* Length is the number of bars in the lookback period

> 🔍 **Technical Note:** The implementation uses a monotonic deque algorithm with a circular buffer for efficiency. This approach maintains O(1) time complexity for each new bar, avoiding the need to scan all values in the lookback period repeatedly.

## Interpretation Details

Highest Value provides valuable insights for various trading applications:

* **Resistance levels:** The highest value over a significant period often acts as a psychological resistance level
* **Breakout trading:** When price breaks above the highest value of recent periods, it often signals bullish momentum
* **Trailing stops:** Using the highest value of the last N bars (offset by some value) can serve as a trailing stop-loss mechanism
* **Volatility assessment:** Comparing current price to recent highest values helps gauge potential upside room

The indicator is most effective when used alongside other technical tools that provide context about market conditions and trend direction.

## Limitations and Considerations

* **Market conditions:** Less predictive during highly volatile or gapping markets where price leaps beyond historical levels
* **Lag factor:** By definition, the indicator looks backward and doesn't predict future price levels
* **False breakouts:** Price briefly exceeding the highest value doesn't always result in sustained momentum
* **Complementary tools:** Best used in conjunction with volume analysis, trend indicators, or support/resistance confirmation

## References

* Wilder, J. W. (1978). New Concepts in Technical Trading Systems. Trend Research.
* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
