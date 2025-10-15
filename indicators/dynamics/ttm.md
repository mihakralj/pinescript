# TTM: TTM Trend

[Pine Script Implementation of TTM](https://github.com/mihakralj/pinescript/blob/main/indicators/dynamics/ttm.pine)

## Overview and Purpose

The TTM Trend indicator is part of John Carter's TTM (Trade The Markets) trading system. It's a fast-moving exponential moving average (EMA) designed to identify trend direction and momentum quickly. TTM Trend uses color-coding to provide immediate visual feedback about the current trend direction, making it particularly effective for short-term trading and quick trend identification.

The indicator is commonly used alongside other TTM tools like the TTM Squeeze to create a comprehensive trading system. Its fast response time (default 6-period EMA) makes it ideal for catching early trend changes while filtering out noise through the smoothing effect of the exponential average.

## Core Concepts

* **Fast EMA:** Uses a short period (typically 6 bars) for quick response to price changes
* **Color-Coded Trend:** Visual representation of trend direction through line color changes
* **Momentum Detection:** Identifies when the moving average is rising (bullish) or falling (bearish)
* **Trend Confirmation:** Works with other indicators in the TTM system for complete market analysis
* **Price Source:** Typically uses hlc3 (typical price) for balanced price representation

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Period | 6 | Lookback period for EMA calculation | Lower (3-5) for faster signals, higher (8-10) for smoother trends |
| Source | hlc3 | Price data used for calculation | Consider close for end-of-period signals, ohlc4 for full bar representation |

**Pro Tip:** The default 6-period setting is specifically chosen by John Carter for its balance between responsiveness and reliability. For day trading, stay with 6 or use 5 for even faster signals. For swing trading, consider 8-10 periods. The indicator works best when combined with TTM Squeeze for entry timing and volume confirmation for trend strength.

## Calculation and Mathematical Foundation

**Simplified explanation:**
TTM Trend is a 6-period exponential moving average that changes color based on whether it's rising (green/bullish) or falling (red/bearish).

**Technical formula:**

1. Calculate the Exponential Moving Average:
   ```
   α = 2 / (period + 1)
   EMA = α × (price - EMA[1]) + EMA[1]
   ```

2. Determine Trend Direction:
   ```
   If EMA > EMA[1]: Trend = Bullish (Green)
   If EMA < EMA[1]: Trend = Bearish (Red)
   If EMA = EMA[1]: Trend = Neutral (Gray)
   ```

3. Default Calculation (6-period):
   ```
   α = 2 / (6 + 1) = 0.2857
   EMA = 0.2857 × (price - EMA[1]) + EMA[1]
   ```

> 🔍 **Technical Note:** TTM Trend uses hlc3 (typical price) as the default source rather than close price. This provides a more balanced view of the bar's price action and reduces the impact of closing price manipulation. The 6-period EMA creates a smooth line that responds quickly to trend changes without excessive whipsaws.

## Interpretation Details

TTM Trend provides clear visual trend identification through color-coded signals:

* **Green Line (Bullish Trend):**
  - EMA is rising compared to previous bar
  - Indicates upward momentum
  - Price is generally above the TTM line
  - Entry signal: Buy when line turns green from red
  - Stay long while line remains green

* **Red Line (Bearish Trend):**
  - EMA is falling compared to previous bar
  - Indicates downward momentum
  - Price is generally below the TTM line
  - Entry signal: Sell/short when line turns red from green
  - Stay short while line remains red

* **Gray Line (Neutral):**
  - EMA unchanged from previous bar (rare)
  - Indicates potential consolidation
  - Wait for color change before trading

* **Triangle Markers:**
  - Small triangles appear at trend changes
  - Up triangle (below bar): Trend turned bullish
  - Down triangle (above bar): Trend turned bearish
  - Use as entry/exit alerts

* **Price Relationship:**
  - **Price above green line:** Strong uptrend, optimal long positions
  - **Price below red line:** Strong downtrend, optimal short positions
  - **Price crossing line:** Potential trend weakening or reversal
  - **Whipsaws (frequent color changes):** Sideways market, avoid trading

* **TTM System Integration:**
  - **With TTM Squeeze:** Enter on TTM Trend direction when Squeeze fires
  - **With Volume:** Confirm trend strength with increasing volume
  - **With Support/Resistance:** Use trend direction at key levels
  - **Exit Strategy:** Exit longs when line turns red, shorts when turns green

* **Practical Usage:**
  - **Day Trading:** Quick entries on color changes during market hours
  - **Swing Trading:** Hold positions while color remains consistent
  - **Trend Following:** Ride trends in the direction of line color
  - **Scalping:** Use on lower timeframes (1-5 min) for rapid trades
  - **Risk Management:** Place stops below green line (longs) or above red line (shorts)

## Limitations and Considerations

* **Lagging Indicator:** As an EMA-based tool, it inherently lags price action and confirms trends after they begin
* **Whipsaw Prone:** In choppy, sideways markets, the indicator can change colors frequently causing false signals
* **No Magnitude Information:** Shows trend direction but not strength; strong and weak trends look the same
* **Best with Confluence:** Designed to work within the TTM system, not as a standalone indicator
* **Timeframe Sensitive:** Performance varies significantly across timeframes; requires optimization for each
* **No Overbought/Oversold:** Doesn't indicate when trends are extended or due for reversal
* **Fast Period Noise:** The 6-period default can be too sensitive in volatile markets, generating premature signals

## References

* Carter, J. (2010). "Mastering the Trade" McGraw-Hill.
* Carter, J. "TTM (Trade The Markets) System" - Simpler Trading Educational Materials
* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
* Pring, M. J. (2002). Technical Analysis Explained. McGraw-Hill.
