# ALLIGATOR: Williams Alligator

[Pine Script Implementation of ALLIGATOR](https://github.com/mihakralj/pinescript/blob/main/indicators/dynamics/alligator.pine)

## Overview and Purpose

The Williams Alligator is a technical indicator developed by legendary trader Bill Williams to help identify trending markets and determine optimal entry and exit points. Introduced in his book "Trading Chaos" (1995), the Alligator uses three smoothed moving averages set at Fibonacci-based periods to visualize market behavior through the metaphor of an alligator's feeding patterns.

The indicator is built on Williams' philosophy that financial markets trend only 15-30% of the time, with the remaining 70-85% consisting of sideways or ranging movements. The Alligator helps traders identify when markets "awaken" from dormant, non-trending periods and begin to trend strongly. The three lines represent the alligator's jaw, teeth, and lips, which open and close based on market dynamics.

This implementation uses Wilder's smoothed moving average (SMMA/RMA) with proper warmup compensation to provide accurate values from the first bar, following the original Williams specifications.

## Core Concepts

* **Three Smoothed Lines:** Uses three SMMA lines with different periods (13, 8, 5) based on Fibonacci sequences
* **Forward Shifting:** Each line is shifted forward by a specific number of bars (8, 5, 3) to provide predictive signals
* **Jaw (Blue Line):** 13-period SMMA shifted 8 bars forward - represents the slowest, longest-term trend
* **Teeth (Red Line):** 8-period SMMA shifted 5 bars forward - represents medium-term price movements
* **Lips (Green Line):** 5-period SMMA shifted 3 bars forward - represents the fastest, shortest-term trend
* **Alligator Behavior:** Lines converging = sleeping (ranging), lines diverging = feeding (trending)

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|----------------|
| Source | HLC3 | Price data used for calculation | Use close for more responsive signals, hlc3 (default) for smoother behavior |
| Jaw Period | 13 | Lookback for blue line | Increase for longer-term trends, decrease for faster response |
| Jaw Offset | 8 | Forward shift for blue line | Adjust to match market volatility and timeframe |
| Teeth Period | 8 | Lookback for red line | Modify to adjust medium-term sensitivity |
| Teeth Offset | 5 | Forward shift for red line | Tune for specific market characteristics |
| Lips Period | 5 | Lookback for green line | Change for short-term responsiveness |
| Lips Offset | 3 | Forward shift for green line | Adjust for desired signal timing |

**Pro Tip:** The default Fibonacci-based settings (13/8, 8/5, 5/3) work well across most markets and timeframes. For highly volatile markets, consider slightly increasing all periods proportionally. For intraday trading, you might use shorter periods like 8/5, 5/3, 3/2. Always maintain the Fibonacci relationships for optimal performance. The forward shifts help anticipate trend changes and reduce lag inherent in moving averages.

## Calculation and Mathematical Foundation

**Simplified explanation:**
The Alligator calculates three smoothed moving averages (SMMA/RMA) with progressively shorter periods, then shifts each forward in time. The relationship between these shifted averages reveals trend strength and direction.

**Technical formula:**

1. Calculate SMMA (Smoothed Moving Average, equivalent to RMA):
   ```
   SMMA(i) = (SMMA(i-1) * (n-1) + Price(i)) / n
   
   Or equivalently with alpha = 1/n:
   SMMA(i) = alpha * (Price(i) - SMMA(i-1)) + SMMA(i-1)
   ```

2. Apply to three different periods:
   ```
   Jaw = SMMA(Close, 13) shifted forward 8 bars
   Teeth = SMMA(Close, 8) shifted forward 5 bars
   Lips = SMMA(Close, 5) shifted forward 3 bars
   ```

3. Forward shifting means plotting values from past bars:
   ```
   PlottedJaw(i) = Jaw(i - 8)
   PlottedTeeth(i) = Teeth(i - 5)
   PlottedLips(i) = Lips(i - 3)
   ```

> 🔍 **Technical Note:** This implementation uses Wilder's SMMA (equivalent to RMA) with alpha = 1/period, and includes exponential warmup compensation to provide accurate values from the first bar. The forward shifting is implemented using historical reference operators [offset], which effectively "looks back" by the offset amount to create the forward shift effect on the chart.

## Interpretation Details

The Williams Alligator provides multiple analytical perspectives based on line relationships and behavior:

* **Alligator Sleeping (Lines Intertwined):**
  - All three lines converging or crossing each other
  - Market is ranging, consolidating, or moving sideways
  - Low profitability period - avoid trading or wait for awakening
  - Often occurs 70-85% of the time according to Williams

* **Alligator Awakening (Lines Beginning to Separate):**
  - Lines starting to diverge and separate from each other
  - Market transitioning from range to trend
  - Early signal to prepare for potential trend
  - Watch for clear separation before entering

* **Alligator Eating (Lines Widely Separated):**
  - All three lines clearly separated and moving in same direction
  - Strong trending market - optimal trading conditions
  - Lips (green) farthest from Jaw (blue) indicates strong trend
  - Stay with trend until lines begin to converge

* **Trend Direction:**
  - Bullish: Lips > Teeth > Jaw (green above red above blue) with price above all lines
  - Bearish: Jaw > Teeth > Lips (blue above red above green) with price below all lines
  - Lines act as dynamic support/resistance during trends

* **Entry Signals:**
  - Long: Price crosses above all three lines when they're beginning to separate
  - Short: Price crosses below all three lines when they're beginning to separate
  - Confirm with other indicators or price patterns for best results

* **Exit Signals:**
  - Lines beginning to converge (alligator closing mouth)
  - Price crossing back through all three lines
  - Lips crossing Teeth or Jaw (line crossovers signal trend weakness)
  - When alligator "falls asleep" again (lines intertwining)

* **Line Crossovers:**
  - Lips crossing Teeth: Early warning of trend change
  - Teeth crossing Jaw: Confirmation of trend change
  - Multiple crossovers in quick succession: Market indecision

## Limitations and Considerations

* **Lag Component:** Uses smoothed moving averages which inherently lag price action, especially the Jaw line
* **Ranging Markets:** Can generate false signals during choppy, sideways markets when alligator is sleeping
* **Whipsaws:** Multiple crossovers during transitions between sleeping and eating states can cause losses
* **Timeframe Dependency:** Effectiveness varies by timeframe; works best on higher timeframes (4H, daily)
* **Trend-Only Indicator:** Designed specifically for trending markets, not effective in ranges
* **No Overbought/Oversold:** Doesn't indicate when trends are overextended or due for reversal
* **Requires Confirmation:** Best used with additional indicators like fractals, oscillators, or volume
* **Fixed Parameters:** Standard Fibonacci periods may not suit all markets or conditions
* **Forward Shifting Confusion:** The forward-shifted plotting can be confusing for beginners
* **Best Conditions:** Most reliable in strongly trending markets with clear directional movement

## References

* Williams, B. (1995). Trading Chaos: Maximize Profits with Proven Technical Techniques. Wiley.
* Williams, B. (2004). New Trading Dimensions: How to Profit from Chaos in Stocks, Bonds, and Commodities. Wiley.
* Wilder, J. W. (1978). New Concepts in Technical Trading Systems. (for SMMA/RMA methodology)
