# SUPER: SuperTrend Indicator

[Pine Script Implementation of SUPER](https://github.com/mihakralj/pinescript/blob/main/indicators/dynamics/super.pine)

## Overview and Purpose

The SuperTrend indicator is a versatile trend-following tool that combines volatility measurement with price action to identify market direction and generate trading signals. Developed by French trader Olivier Seban in 2009, SuperTrend has become one of the most popular overlay indicators among day traders and swing traders due to its simplicity, visual clarity, and effectiveness in trending markets.

Unlike traditional moving averages that simply smooth price data, SuperTrend dynamically adapts to market volatility through the Average True Range (ATR), creating a responsive support/resistance line that follows price action while filtering out market noise. The indicator plots a single line that changes color as trends shift, providing clear visual cues for trend direction and potential reversal points.

SuperTrend excels in trending markets by keeping traders on the right side of the move while minimizing whipsaws through its volatility-adjusted bands. Its straightforward buy/sell signals and ability to serve as a trailing stop make it particularly valuable for traders seeking a systematic approach to trend following.

## Core Concepts

* **ATR-Based Bands:** Uses Average True Range to create volatility-adjusted upper and lower bands that expand in volatile markets and contract in quiet periods
* **Dynamic Support/Resistance:** The SuperTrend line acts as dynamic support in uptrends and resistance in downtrends, automatically adjusting position as trends change
* **Color-Coded Signals:** Green line below price indicates bullish trend (buy signal), red line above price indicates bearish trend (sell signal)
* **Trend Persistence:** Once a trend is established, the indicator maintains that trend until price definitively breaks through the opposite band
* **Trailing Stop Function:** Can be used as a trailing stop-loss level, with the line following price at a volatility-adjusted distance

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|----------------|
| ATR Period | 10 | Lookback period for volatility calculation | Lower (7-8) for faster response in day trading; higher (14-20) for swing trading to reduce false signals |
| Multiplier | 3.0 | Distance of bands from median price (× ATR) | Lower (2.0-2.5) for tighter stops and more signals; higher (3.5-5.0) for wider stops and stronger trends |
| Source | Close | Price used for trend determination | Close is standard; some traders use HLC3 for smoother signals |

**Pro Tip:** The default settings (10, 3.0) work well for most timeframes and markets. Day traders on 5-15 minute charts often reduce the multiplier to 2.0-2.5 for earlier entries. Swing traders on daily charts may increase to 3.5-4.0 to stay in trends longer and avoid premature exits. In highly volatile markets (cryptocurrencies), consider increasing the multiplier to 4.0-5.0 to prevent whipsaws. Always backtest parameter changes on your specific market and timeframe before trading live.

## Calculation and Mathematical Foundation

**Simplified explanation:**
SuperTrend creates two bands (upper and lower) around price based on volatility (ATR). The indicator follows the lower band during uptrends and switches to the upper band during downtrends. The bands can never move in the opposite direction of the current trend, which creates the "sticky" behavior that keeps traders in trends.

**Technical formula:**

1. Calculate the median price (HL2):
   ```
   HL2 = (High + Low) / 2
   ```

2. Calculate Average True Range (ATR) with exponential smoothing:
   ```
   TR = max(High - Low, |High - Close[1]|, |Low - Close[1]|)
   ATR = EMA(TR, period)
   ```

3. Calculate basic bands:
   ```
   Basic Upper Band = HL2 + (Multiplier × ATR)
   Basic Lower Band = HL2 - (Multiplier × ATR)
   ```

4. Apply persistence rules to final bands:
   ```
   Final Upper Band = Basic UB < Final UB[1] OR Close[1] > Final UB[1] 
                      ? Basic UB : Final UB[1]
   
   Final Lower Band = Basic LB > Final LB[1] OR Close[1] < Final LB[1]
                      ? Basic LB : Final LB[1]
   ```

5. Determine trend and SuperTrend line:
   ```
   Trend = Close > Final UB ? 1 : Close < Final LB ? -1 : Trend[1]
   SuperTrend = Trend == 1 ? Final LB : Final UB
   ```

> 🔍 **Technical Note:** The implementation uses an exponential warmup compensator for the ATR calculation to provide valid values from bar 1. The persistence rules ensure that the upper band can only fall (never rise) and the lower band can only rise (never fall), which forces price to definitively break through a band to trigger a trend change. This prevents rapid oscillations and keeps traders in established trends.

## Interpretation Details

SuperTrend provides multiple layers of actionable information:

* **Primary Trend Identification:**
  - Green line below price = Bullish trend (long positions favored)
  - Red line above price = Bearish trend (short positions favored)
  - Line color change = Potential trend reversal signal

* **Entry Signals:**
  - Buy Signal: When price closes above the red SuperTrend line, triggering a color change to green
  - Sell Signal: When price closes below the green SuperTrend line, triggering a color change to red
  - Strongest signals occur after periods of consolidation or when confirmed by other indicators

* **Position Management:**
  - Use SuperTrend line as trailing stop-loss: Exit longs if price closes below green line; exit shorts if price closes above red line
  - The line automatically adjusts distance based on volatility, tightening in quiet markets and widening in volatile conditions
  - Helps maximize profits in strong trends while limiting losses when trend ends

* **Trend Strength Assessment:**
  - Distance between price and SuperTrend line indicates trend strength
  - Price hugging the line suggests weak trend or potential reversal
  - Large separation indicates strong momentum and confident trend
  - Decreasing distance may warn of trend exhaustion

* **Consolidation Periods:**
  - Frequent color changes (whipsaws) indicate rangebound or choppy market
  - In these conditions, wait for clear breakout or use range-trading strategies instead
  - Consider higher multiplier settings to filter false signals during consolidation

* **Volatility Context:**
  - Wider bands (line farther from price) = Higher volatility, larger position risk
  - Tighter bands = Lower volatility, smaller position risk
  - Adjust position sizing based on current band width

## Limitations and Considerations

* **Lagging Nature:** As a trend-following indicator, SuperTrend confirms trends after they begin, not before. Initial trend moves are captured late, potentially missing 10-20% of the move
* **False Signals in Ranging Markets:** Generates frequent whipsaw signals during sideways or choppy conditions. Best performance occurs in trending markets with clear directional bias
* **No Magnitude Information:** Indicates trend direction but not strength or duration. Cannot distinguish between weak and strong trends without additional analysis
* **Sensitivity Settings Challenge:** Finding optimal ATR period and multiplier requires testing. Too sensitive (low multiplier) generates false signals; too insensitive (high multiplier) misses trend changes
* **Volatility Dependency:** Performance varies with market conditions. May be too reactive in high volatility or too slow in low volatility periods
* **No Profit Targets:** Provides entry and exit signals but no guidance on profit-taking levels. Requires additional tools or predetermined targets for complete strategy
* **Single Timeframe View:** Most effective when confirmed across multiple timeframes. Lower timeframe signals should align with higher timeframe trend
* **Breakout Gaps:** Large gaps at market open can trigger premature signals if gap doesn't reflect true trend change

## References

* Seban, O. (2009). SuperTrend Indicator Development
* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance
* Wilder, J. W. (1978). New Concepts in Technical Trading Systems (ATR methodology)
* Pring, M. J. (2002). Technical Analysis Explained. McGraw-Hill
