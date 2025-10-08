# DPO: Detrended Price Oscillator

[Pine Script Implementation of DPO](https://github.com/mihakralj/pinescript/blob/main/indicators/oscillators/dpo.pine)

## Overview and Purpose

The Detrended Price Oscillator (DPO) is a cyclical indicator designed to eliminate long-term trends from price data, making it easier to identify short-term cycles and overbought/oversold conditions. Unlike momentum oscillators that fluctuate around a moving average, DPO removes the trend component by comparing current price to a displaced (shifted back in time) simple moving average.

The key innovation of DPO is its displacement technique: it shifts the moving average back in time by (period/2 + 1) bars, effectively centering it within the price data. This eliminates the trend and reveals the cyclical component of price movement. DPO is particularly valuable for cycle analysis and identifying potential turning points in markets that exhibit regular cyclical behavior.

## Core Concepts

* **Trend removal:** Eliminates long-term trend by using a displaced moving average
* **Cycle identification:** Highlights short-term price cycles by isolating cyclical component
* **Zero-line oscillation:** Fluctuates above and below zero, indicating position relative to the displaced average
* **Non-predictive:** Unlike other oscillators, DPO is not designed to predict future price movements but to analyze cycles
* **Lag-free cycles:** The displacement technique ensures cycles are shown without phase lag

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Source | Close | Price data used for calculation | Change to analyze different aspects of price action (e.g., HL2 for range focus) |
| Period | 20 | Length for SMA and displacement calculation | Adjust based on the cycle length you want to analyze (shorter for faster cycles) |

**Pro Tip:** The period should match the dominant cycle you're analyzing. For daily charts, try 20-30 periods for intermediate cycles, or 5-10 for short-term cycles. Use longer periods (40-60) on weekly charts for longer-term cycle analysis.

## Calculation and Mathematical Foundation

**Simplified explanation:**
DPO calculates a simple moving average over the specified period, then shifts (displaces) it back in time by roughly half the period plus one bar. The current price is then compared to this displaced average. The result shows how far the current price deviates from the historical average at that point in the cycle.

**Technical formula:**
```
Displacement = Floor(Period / 2) + 1
DPO = Price - SMA(Price, Period)[Displacement]
```

Where:
- Price = Current price (typically Close)
- SMA = Simple Moving Average
- Period = Lookback period for the moving average
- [Displacement] = Historical value from that many bars ago

**Example with Period = 20:**
- Displacement = Floor(20/2) + 1 = 11 bars
- DPO = Current Close - SMA(20)[11]
- This compares today's price to the 20-period average from 11 bars ago

> 🔍 **Technical Note:** The displacement formula (Period/2 + 1) centers the moving average within the data, which is key to DPO's ability to isolate cycles. This shifting prevents the indicator from having predictive qualities and focuses it purely on cycle identification.

## Interpretation Details

DPO provides several analytical perspectives:

* **Cycle peaks/troughs:** Identifies cyclical turning points when DPO reaches extremes
* **Zero-line crossovers:** Crossing above zero indicates price above the displaced average (potential bullish); below zero indicates price below the displaced average (potential bearish)
* **Overbought/Oversold:** Extreme positive values suggest overbought conditions; extreme negative values suggest oversold conditions
* **Cycle length:** The distance between consecutive peaks (or troughs) indicates the cycle length
* **Divergences:** Divergence between DPO and price can signal weakening trends
* **Cycle regularity:** Consistent peaks/troughs suggest reliable cyclical patterns

## Limitations and Considerations

* **Not predictive:** DPO is designed for cycle analysis, not for predicting future price movements
* **Lag inherent:** The displacement means DPO references historical data, creating inherent lag
* **Cycle dependency:** Most effective in markets with clear cyclical patterns; less useful in strongly trending or random markets
* **Period sensitivity:** Performance heavily dependent on choosing a period that matches actual cycle length
* **No trend information:** By design, DPO removes trend information, so it should not be used alone for trend-following strategies
* **Requires complementary tools:** Best used alongside trend-following indicators and other technical analysis tools

## Practical Trading Applications

* **Cycle timing:** Identify regular market cycles to time entries and exits
* **Support/Resistance:** Historical DPO levels can act as support/resistance for future cycles
* **Mean reversion:** Extreme DPO values suggest potential mean reversion opportunities
* **Pattern recognition:** Regular DPO patterns can help predict cycle continuation
* **Multi-timeframe analysis:** Compare DPO across different timeframes to identify nested cycles

## References

* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
* Achelis, S. B. (2000). Technical Analysis from A to Z (2nd ed.). McGraw-Hill.
* Kaufman, P. J. (2013). Trading Systems and Methods (5th ed.). Wiley Trading.
* Ehlers, J. F. (2001). Rocket Science for Traders. John Wiley & Sons.
