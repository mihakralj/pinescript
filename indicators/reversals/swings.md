# SWINGS: Swing High/Low Detection

[Pine Script Implementation of SWINGS](https://github.com/mihakralj/pinescript/blob/main/indicators/reversals/swings.pine)

## Overview and Purpose

Swing High/Low Detection identifies significant price reversal points in financial markets by recognizing local peaks (swing highs) and troughs (swing lows). Developed as a core concept in technical analysis, swing points form the foundation of market structure analysis, trend identification, and support/resistance level determination.

A swing high occurs when a price peak is surrounded by lower prices on both sides, while a swing low occurs when a price trough is flanked by higher prices. These pivot points represent key moments where price momentum shifts, making them critical for understanding market behavior and identifying potential trading opportunities.

The indicator uses a configurable lookback period to determine how many bars must be lower/higher on each side to confirm a swing point. This flexibility allows traders to adjust sensitivity based on timeframe and market conditions - shorter periods detect more frequent but potentially less significant swings, while longer periods identify major structural pivots.

## Core Concepts

* **Swing High Detection:** A price peak where both the preceding and following bars (within the lookback period) have lower highs, confirming local resistance
* **Swing Low Detection:** A price trough where both the preceding and following bars (within the lookback period) have higher lows, confirming local support
* **Lookback Period:** The number of bars on each side of a potential pivot required to confirm it as a valid swing point
* **Market Structure:** Higher highs and higher lows indicate uptrends; lower highs and lower lows indicate downtrends
* **Pivot Confirmation:** Swings are confirmed retrospectively (after the lookback period completes), creating a natural lag in detection

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Lookback | 5 | Number of bars on each side required to confirm swing | Lower (2-3) for intraday/scalping; higher (10-20) for swing trading and position trading |
| Source High | high | Price series for swing high detection | Use close for less noise, high for true extremes |
| Source Low | low | Price series for swing low detection | Use close for less noise, low for true extremes |

**Pro Tip:** The lookback period significantly affects signal quality versus frequency. For day trading on 5-minute charts, use lookback of 2-4 bars to catch quick reversals. For daily charts and swing trading, use 5-10 bars to filter out noise. For weekly charts identifying major structural pivots, consider 10-20 bars. Markets with higher volatility may benefit from larger lookback periods to avoid false signals.

## Calculation and Mathematical Foundation

**Simplified explanation:**
The algorithm examines each bar and checks if it forms a local extremum by comparing it to surrounding bars. A swing high requires that the center bar's high is greater than all highs within the lookback period before and after it. Similarly, a swing low requires the center bar's low to be less than all lows in the surrounding period.

**Technical formula:**

For a bar at position `i` with lookback period `n`:

**Swing High Detection:**
```
A swing high is confirmed at bar i-n when:
high[i-n] > high[i-n-1] AND
high[i-n] > high[i-n-2] AND
...
high[i-n] > high[i-n-n] AND
high[i-n] > high[i-n+1] AND
high[i-n] > high[i-n+2] AND
...
high[i-n] > high[i]
```

**Swing Low Detection:**
```
A swing low is confirmed at bar i-n when:
low[i-n] < low[i-n-1] AND
low[i-n] < low[i-n-2] AND
...
low[i-n] < low[i-n-n] AND
low[i-n] < low[i-n+1] AND
low[i-n] < low[i-n+2] AND
...
low[i-n] < low[i]
```

> 🔍 **Technical Note:** The implementation uses an efficient O(n) rolling window approach to check all bars within the lookback period. Swing points are detected `n` bars after they occur due to the need to confirm that subsequent bars don't invalidate the pivot. This creates inherent lag but ensures reliability.

## Interpretation Details

Swing highs and lows provide multiple analytical perspectives:

* **Trend Identification:**
  - Uptrend: Series of higher swing highs AND higher swing lows
  - Downtrend: Series of lower swing highs AND lower swing lows
  - Sideways: Swing highs and lows remain within a defined range
  - Trend break occurs when the pattern of higher/lower pivots is violated

* **Support and Resistance:**
  - Swing highs act as resistance levels where price previously reversed downward
  - Swing lows act as support levels where price previously reversed upward
  - Multiple tests of same swing level increase its significance
  - Broken swing levels often flip roles (resistance becomes support and vice versa)

* **Market Structure:**
  - Break of Structure (BOS): Price breaks above previous swing high (bullish) or below previous swing low (bearish)
  - Change of Character (CHOCH): Failure to create new swing high in uptrend or new swing low in downtrend
  - These patterns signal potential trend reversals or continuations

* **Entry and Exit Signals:**
  - Enter long on break above swing high (breakout strategy)
  - Enter short on break below swing low (breakdown strategy)
  - Place stop-loss orders just beyond swing points to limit risk
  - Use swing points to define risk-reward ratios for trade management

* **Price Targets:**
  - Measure distance between swing high and low to project targets
  - Equal-leg moves: expect similar distance in next trend leg
  - Fibonacci extensions from swing points provide potential target zones

## Limitations and Considerations

* **Confirmation Lag:** Swing points are identified retrospectively after `n` bars, meaning they appear `n` bars after the actual pivot occurred. This lag can delay entries and exits.
* **False Signals in Choppy Markets:** During consolidation or ranging markets, many small swings may form that don't lead to significant moves, generating noise.
* **Subjectivity:** Different lookback periods produce different swing points, leading to varying interpretations of market structure across timeframes.
* **No Predictive Power Alone:** Swing points identify what has happened, not what will happen. They must be combined with other analysis for directional bias.
* **Lookback Selection Impact:** Too small a lookback creates excessive signals and noise; too large misses important pivots and increases lag significantly.
* **Not Suitable for Trending Markets:** In strong trends with minimal pullbacks, swing detection may produce few signals or miss the trend entirely.

## References

* Investopedia. (2024). "Swing Low Definition." Technical Analysis Concepts.
* LuxAlgo. (2024). "Swing Highs and Lows: Basics for Traders." TradingView Technical Analysis.
* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
* Elder, A. (1993). Trading for a Living. John Wiley & Sons.
