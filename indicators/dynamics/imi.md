# IMI: Intraday Momentum Index

[Pine Script Implementation of IMI](https://github.com/mihakralj/pinescript/blob/main/indicators/dynamics/imi.pine)

## Overview and Purpose

The Intraday Momentum Index (IMI) is a technical indicator developed by Tushar Chande that combines aspects of RSI with candlestick analysis. Unlike RSI which uses close-to-close price changes, IMI uses intraday price movements (open vs close) to measure momentum. This makes IMI particularly useful for identifying overbought and oversold conditions based on intraday trading behavior.

IMI ranges from 0 to 100 and is interpreted similarly to RSI, with readings above 70 typically indicating overbought conditions and readings below 30 indicating oversold conditions. The key innovation is using the relationship between open and close prices rather than sequential closing prices.

## Core Concepts

* **Intraday focus:** Measures momentum within individual bars (open to close)
* **RSI-like calculation:** Similar formula structure to RSI but different input
* **Candlestick integration:** Implicitly incorporates candlestick body direction
* **Overbought/oversold:** Normalized 0-100 scale with traditional thresholds
* **Mean reversion:** Identifies potential reversal points based on intraday extremes

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Period | 14 | Lookback period for summing gains and losses | Lower (5-10) for faster response; higher (20-30) for smoother, less volatile readings |

**Pro Tip:** The standard 14-period setting works well for most timeframes and matches the traditional RSI period. Consider adjusting based on market characteristics:
- Short-term trading: 5-10 periods for quick signals
- Swing trading: 14-21 periods for balanced signals
- Position trading: 20-30 periods for fewer, stronger signals
- Day trading: Lower periods (7-10) work well on intraday charts

## Calculation and Mathematical Foundation

**Simplified explanation:**
IMI calculates the ratio of upward intraday movement (close > open) to total intraday movement over a specified period.

**Technical formula:**

1. For each bar, calculate gains and losses:
   ```
   If close > open:
       gain = close - open
       loss = 0
   If close < open:
       gain = 0
       loss = open - close
   If close = open:
       gain = 0
       loss = 0
   ```

2. Sum gains and losses over period:
   ```
   Sum_Gains = Σ(gains over period)
   Sum_Losses = Σ(losses over period)
   ```

3. Calculate IMI:
   ```
   IMI = 100 × Sum_Gains / (Sum_Gains + Sum_Losses)
   ```

> 🔍 **Technical Note:** This implementation uses a circular buffer for O(1) per-bar complexity, maintaining running sums of gains and losses. When the sum of gains and losses is zero (rare case), IMI defaults to 50 (neutral).

## Interpretation Details

IMI provides insight into intraday momentum and potential reversal points:

* **Value Ranges:**
  - IMI < 30: Oversold, potential upward reversal
  - IMI 30-45: Weak bearish momentum
  - IMI 45-55: Neutral zone, indecision
  - IMI 55-70: Bullish momentum building
  - IMI > 70: Overbought, potential downward reversal

* **Trading Signals:**
  - **Overbought:** IMI > 70 suggests selling pressure may emerge
  - **Oversold:** IMI < 30 suggests buying pressure may emerge
  - **Divergences:** Price makes new high/low but IMI doesn't confirm
  - **Midline crosses:** IMI crossing 50 indicates momentum shift

* **Compared to RSI:**
  - IMI focuses on intraday movements vs RSI's close-to-close
  - IMI better captures candlestick patterns (bullish/bearish bodies)
  - IMI may be more responsive to gap behavior
  - Both share similar overbought/oversold interpretation

* **Market Context:**
  - Strong trends: IMI can remain overbought/oversold for extended periods
  - Ranging markets: IMI oscillations provide better reversal signals
  - Gap behavior: IMI explicitly captures gap impact through open-close relationship
  - Volume consideration: IMI doesn't incorporate volume (consider adding MFI for volume)

## Advantages

1. **Intraday Sensitivity:**
   - Captures sentiment within individual bars
   - Sensitive to candlestick body size and direction
   - Better reflects intraday trading dynamics

2. **Gap Awareness:**
   - Explicitly incorporates gap behavior (open vs previous close)
   - Useful for markets with frequent gaps (stocks, indices)

3. **Candlestick Integration:**
   - Implicitly considers bullish/bearish candle bodies
   - Complements traditional candlestick pattern analysis

4. **Normalized Scale:**
   - 0-100 range makes interpretation consistent
   - Easy to set threshold levels
   - Comparable across different instruments

## Limitations and Considerations

* **Requires OHLC data:** Cannot be calculated from close-only data
* **Gap sensitivity:** Large gaps can cause extreme readings
* **Trend persistence:** Like RSI, can remain overbought/oversold in strong trends
* **No volume component:** Doesn't consider trading volume (unlike MFI)
* **Timeframe dependent:** May behave differently on various timeframes
* **Whipsaw risk:** Can generate false signals in choppy, ranging markets
* **Not directional:** Shows momentum strength but not trend direction directly

## Relationship to RSI

**Key Differences:**
- **RSI Formula:** 100 × AvgGain / (AvgGain + AvgLoss) where gain/loss = close - previous close
- **IMI Formula:** 100 × SumGain / (SumGain + SumLoss) where gain/loss = close - open
- **RSI:** Uses smoothed (Wilder's) averages
- **IMI:** Uses simple sums over period
- **RSI:** Sequential bar relationships
- **IMI:** Intraday bar relationships

**Usage Comparison:**
1. Use RSI for trend-following analysis across bars
2. Use IMI for intraday momentum and reversal signals
3. Consider using both together for confirmation
4. IMI may be better for gap-prone markets

## Trading Applications

* **Overbought/Oversold:** Primary use - identify potential reversal zones
* **Divergence Trading:** Look for price-IMI divergences for early reversal signals
* **Confirmation Tool:** Confirm candlestick patterns with IMI readings
* **Mean Reversion:** Trade oversold/overbought extremes back to 50
* **Momentum Filter:** Filter trades based on IMI trend direction
* **Multi-timeframe:** Compare IMI across timeframes for confluence
* **Combine with Volume:** Add volume analysis (OBV, MFI) for confirmation

## References

* Chande, T. S., & Kroll, S. (1994). The New Technical Trader. Wiley Trading.
* Achelis, S. B. (2000). Technical Analysis from A to Z (2nd ed.). McGraw-Hill.
* Kaufman, P. J. (2013). Trading Systems and Methods (5th ed.). Wiley Trading.
* Colby, R. W. (2003). The Encyclopedia of Technical Market Indicators (2nd ed.). McGraw-Hill.
