# Lowest: Lowest Value

[Pine Script Implementation of Lowest](https://github.com/mihakralj/pinescript/blob/main/indicators/numerics/lowest.pine)

## Overview and Purpose

The Lowest Value indicator identifies the minimum price (or other data point) reached within a specified lookback period. This fundamental statistical measure serves as an essential component in many technical analysis tools and trading strategies. By tracking the lowest values over time, traders can identify significant price levels, support zones, and potential breakdown points.

## Core Concepts

* **Price extremes identification:** Lowest Value efficiently tracks price valleys, helping identify potential support levels and breakdown points
* **Market application:** Particularly useful for setting take-profit targets, recognizing chart patterns, and defining entry points based on historical price action
* **Timeframe suitability:** **All timeframes** are effective, with shorter periods (5-20) for identifying immediate support levels and longer periods (20-200) for significant historical support

Lowest Value forms the foundation for numerous technical indicators and trading systems, including Donchian Channels, Price Envelopes, and various mean-reversion strategies.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Period | 14 | Controls the lookback window for calculation | Decrease for more responsive readings in active markets, increase for identifying significant historical levels |
| Source | Close | Data point used for calculation | Switch to Low for true price extremes, or use other price data based on specific strategy requirements |

**Pro Tip:** Using multiple Lowest Value periods simultaneously (e.g., 20, 50, and 200) can help identify a hierarchy of support levels, with longer-period lows typically representing stronger support zones.

## Calculation and Mathematical Foundation

**Simplified explanation:**
The Lowest Value indicator scans a specified number of previous bars and identifies the minimum value within that range. As each new bar forms, the indicator updates by dropping the oldest bar from its calculation and adding the newest one, continuously tracking the lowest value within the moving window.

**Technical formula:**
Lowest(Source, Length) = Minimum value of Source over the past Length bars

Where:

* Source is the price or data series being analyzed (typically Close or Low)
* Length is the number of bars in the lookback period

> 🔍 **Technical Note:** The implementation uses a monotonic deque algorithm with a circular buffer for efficiency. This approach maintains O(1) time complexity for each new bar, avoiding the need to scan all values in the lookback period repeatedly.

## Interpretation Details

Lowest Value provides valuable insights for various trading applications:

* **Support levels:** The lowest value over a significant period often acts as a psychological support level
* **Breakdown trading:** When price breaks below the lowest value of recent periods, it often signals bearish momentum
* **Entry signals:** Pullbacks that approach but respect the lowest values of recent periods can offer potential entry points
* **Volatility assessment:** Comparing current price to recent lowest values helps gauge potential downside risk

The indicator is most effective when used alongside other technical tools that provide context about market conditions and trend direction.

## Limitations and Considerations

* **Market conditions:** Less predictive during highly volatile or gapping markets where price plunges beyond historical levels
* **Lag factor:** By definition, the indicator looks backward and doesn't predict future price levels
* **False breakdowns:** Price briefly falling below the lowest value doesn't always result in sustained downward momentum
* **Complementary tools:** Best used in conjunction with volume analysis, trend indicators, or support/resistance confirmation

## References

* Wilder, J. W. (1978). New Concepts in Technical Trading Systems. Trend Research.
* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
