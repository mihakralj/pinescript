# WILLR: Williams %R

[Pine Script Implementation of WILLR](https://github.com/mihakralj/pinescript/blob/main/indicators/momentum/willr.pine)

## Overview and Purpose

Williams %R (Percent Range) is a momentum oscillator developed by Larry Williams. It measures overbought and oversold levels, similar to the Stochastic Oscillator. However, Williams %R is plotted on an upside-down scale, with 0 at the top and -100 at the bottom. Overbought readings are typically above -20, and oversold readings are below -80.

The indicator shows the current closing price in relation to the highest high and lowest low over a lookback period (typically 14 days). It essentially indicates where today's price falls within the recent trading range.

## Core Concepts

*   **Momentum Oscillator:** Measures the speed and change of price movements.
*   **Overbought/Oversold Levels:** Identifies potential price extremes.
    *   Values from -20 to 0 are considered overbought.
    *   Values from -80 to -100 are considered oversold.
*   **Inverse Scale:** Unlike many oscillators, %R uses a negative scale from 0 to -100.
*   **Relationship to Stochastic:** Williams %R is the inverse of the Fast Stochastic Oscillator's %K line, but without its smoothing.

## Common Settings and Parameters

| Parameter | Default | Function                                     | When to Adjust                                                                    |
| :-------- | :------ | :------------------------------------------- | :-------------------------------------------------------------------------------- |
| `len`     | 14      | The lookback period for highs, lows, and close. | Shorter periods make it more sensitive; longer periods make it smoother. Common values range from 5 to 30. |

**Pro Tip:**
*   A 14-period %R is common for daily charts.
*   Shorter periods (e.g., 7-10) can be used for more frequent signals on intraday charts.
*   Longer periods (e.g., 20-28) can be used for weekly charts or to identify longer-term overbought/oversold conditions.
*   Overbought/oversold levels (-20 and -80) can be adjusted based on market volatility or asset characteristics.

## Calculation and Mathematical Foundation

**Simplified explanation:**
Williams %R compares the latest closing price to the highest high and lowest low of a specified lookback period. It shows how the current price stacks up against the total price range of that period.

**Technical formula:**
`%R = ((Highest High in Period - Current Close) / (Highest High in Period - Lowest Low in Period)) * -100`

Where:
*   `Highest High in Period` = The highest price during the lookback period (`len`).
*   `Lowest Low in Period` = The lowest price during the lookback period (`len`).
*   `Current Close` = The most recent closing price.

**Edge Case Handling:**
If `Highest High in Period == Lowest Low in Period` (i.e., the price range is zero, which can happen if prices are flat for the entire period or `len` is 1 and `high == low`):
*   If `Current Close == Highest High in Period`, then `%R = 0`.
*   Otherwise (if `Current Close < Highest High in Period`, which implies `Current Close == Lowest Low in Period`), then `%R = -100`.

The result is always multiplied by -100 to produce values between 0 and -100.

> 🔍 **Technical Note:** The implementation uses `ta.highest(high, len)` and `ta.lowest(low, len)` for efficient calculation of the period's high and low. The final value is clamped between 0 and -100 to ensure consistency.

## Interpretation Details

Williams %R is used to identify potential entry and exit points based on overbought and oversold conditions:

*   **Overbought Conditions:**
    *   When %R moves above -20, the market is considered overbought. This suggests that the price is near the top of its recent trading range and might be due for a pullback.
    *   A sell signal might be considered when %R crosses back below -20 from above.

*   **Oversold Conditions:**
    *   When %R moves below -80, the market is considered oversold. This suggests that the price is near the bottom of its recent trading range and might be due for a rally.
    *   A buy signal might be considered when %R crosses back above -80 from below.

*   **Mid-Line (-50) Crossovers:**
    *   Crossing above -50 can indicate strengthening bullish momentum.
    *   Crossing below -50 can indicate strengthening bearish momentum.

*   **Divergence:**
    *   **Bullish Divergence:** Price makes a new low, but %R makes a higher low (less negative). This can signal weakening selling pressure.
    *   **Bearish Divergence:** Price makes a new high, but %R makes a lower high (more negative, or less close to 0). This can signal weakening buying pressure.

*   **Failure Swings (less common with %R but can be adapted):**
    *   **Bullish:** %R enters oversold, rallies above -80, pulls back but stays above -80, then breaks a prior %R peak.
    *   **Bearish:** %R enters overbought, falls below -20, pulls back but stays below -20, then breaks a prior %R trough.

## Limitations and Considerations

*   **Leading but Prone to Whipsaws:** %R is a leading indicator, meaning it can signal potential reversals before they occur. However, this also makes it prone to false signals (whipsaws), especially in choppy or non-trending markets.
*   **No Trend Direction:** %R does not inherently indicate the direction of the primary trend. It's best used in conjunction with trend-following indicators or analysis.
*   **Can Stay Extreme:** In strong trends, %R can remain in overbought or oversold territory for extended periods. A move into these zones doesn't automatically mean a reversal is imminent. Divergence signals become more critical in such trending markets.
*   **Sensitivity:** Shorter lookback periods make %R very sensitive, leading to more frequent but potentially less reliable signals.
*   **Context is Key:** Always use Williams %R in the context of the broader market environment and alongside other analytical tools.

## References

*   Williams, L. (1979). *How I Made One Million Dollars Last Year Trading Commodities*. Windsor Books.
*   Murphy, J. J. (1999). *Technical Analysis of the Financial Markets*. New York Institute of Finance.
*   Achelis, S. B. (2001). *Technical Analysis from A to Z*. McGraw-Hill.
