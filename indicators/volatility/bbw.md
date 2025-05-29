# BBW: Bollinger Band Width

[Pine Script Implementation of BBW](https://github.com/mihakralj/pinescript/blob/main/indicators/volatility/bbw.pine)

## Overview and Purpose

Bollinger Band Width (BBW) is a volatility indicator that measures the distance between the upper and lower Bollinger Bands. Developed as a complementary tool to John Bollinger's original Bollinger Bands system, BBW quantifies the width of the price channel created by the bands, providing a direct measurement of market volatility at any given time.

BBW serves as an essential tool for identifying periods of market contraction and expansion. When BBW reaches extremely low levels, it often signals an impending period of increased volatility—a phenomenon known as the "Bollinger Band Squeeze." Conversely, when BBW reaches high levels, it indicates elevated volatility that may precede a period of consolidation.

## Core Concepts

* **Volatility quantification:** BBW provides a numerical representation of current market volatility by measuring the distance between Bollinger Bands
* **Squeeze identification:** Extremely low BBW values often precede significant price movements and breakouts
* **Volatility cycles:** BBW helps identify the natural cycles of market expansion and contraction
* **Relative measurement:** BBW values can be compared across time periods to assess whether current volatility is high or low relative to recent history
* **Breakout prediction:** Periods of low BBW (tight bands) frequently signal impending price breakouts

The core principle behind BBW is that periods of low volatility are typically followed by periods of high volatility, and vice versa. This cyclical nature of volatility makes BBW particularly valuable for anticipating market turning points.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Period | 20 | Lookback period for moving average and standard deviation | Decrease for faster response to volatility changes, increase for smoother readings |
| Source | Close | Price data used for calculation | Consider using HLC3 for more comprehensive price representation |
| StdDev Multiplier | 2.0 | Distance of bands from center line | Increase to capture wider price movements, decrease for tighter analysis |

**Pro Tip:** BBW is most effective when used in conjunction with historical BBW levels. Compare current readings to the lowest 10% of BBW values over the past year to identify potential squeeze conditions.

## Calculation and Mathematical Foundation

**Simplified explanation:**
BBW calculates the standard deviation of prices over a specified period, multiplies it by the chosen multiplier, and then doubles the result to represent the full width between upper and lower bands.

**Technical formula:**
BBW = 2 × (StdDev Multiplier × Standard Deviation of Source over Period)

Where:
- Standard Deviation measures the dispersion of prices from their mean
- StdDev Multiplier typically equals 2.0 (standard Bollinger Band setting)
- The factor of 2 accounts for both upper and lower band distances from the center line

Detailed calculation steps:
1. Calculate the simple moving average of the source over the period
2. Compute the standard deviation of the source over the same period
3. Multiply the standard deviation by the StdDev Multiplier
4. Double the result to get the full band width

> 🔍 **Technical Note:** The implementation uses an optimized single-pass algorithm with circular buffers to calculate both the mean and standard deviation efficiently, avoiding multiple data passes and improving computational performance for longer periods.

## Interpretation Details

BBW provides several key analytical insights:

* **Low BBW Values (Squeeze Conditions):**
  - Indicate periods of low volatility and market consolidation
  - Often precede significant price breakouts or trend changes
  - Suggest that market participants are uncertain about direction
  - Create high-probability setups for breakout trading strategies

* **High BBW Values (Expansion Conditions):**
  - Reflect periods of high volatility and active market participation
  - May indicate the continuation of existing trends
  - Can signal overextension when reaching extreme levels
  - Often followed by periods of consolidation and lower volatility

* **BBW Trends:**
  - Rising BBW: Increasing volatility, potential trend acceleration
  - Falling BBW: Decreasing volatility, possible trend exhaustion
  - Stable BBW: Consistent volatility environment

* **Historical Context:**
  - Compare current BBW to historical percentiles
  - Identify unusually low or high volatility periods
  - Use BBW rankings to assess relative market conditions

## Trading Applications

**Squeeze Trading:**
- Identify periods when BBW reaches historical lows
- Prepare for potential breakouts in either direction
- Use additional indicators to determine breakout direction
- Set stops beyond the opposite band to manage risk

**Volatility Assessment:**
- Monitor BBW trends to gauge market environment changes
- Adjust position sizing based on current volatility levels
- Use BBW to optimize stop-loss placement during different volatility regimes

**Market Timing:**
- Enter positions during low BBW periods (anticipating movement)
- Reduce exposure during extremely high BBW periods (anticipating consolidation)
- Use BBW cycles to time entry and exit points

## Limitations and Considerations

* **Timing uncertainty:** BBW can remain at low levels for extended periods before breakouts occur
* **Direction neutrality:** BBW indicates when movement may occur but not the direction
* **False signals:** Not all squeeze conditions lead to significant price movements
* **Parameter sensitivity:** Different period and multiplier settings can significantly affect readings
* **Market dependency:** Effectiveness varies across different market conditions and asset classes
* **Complementary analysis:** Best used alongside trend and momentum indicators for directional bias

## Comparison with Related Indicators

**BBW vs. ATR:**
- BBW: Relative to price mean, adaptive to current conditions
- ATR: Absolute price ranges, less sensitive to trending behavior

**BBW vs. Standard Deviation:**
- BBW: Multiplied and doubled for band width representation
- StdDev: Raw volatility measure without band context

**BBW vs. VIX (for equity markets):**
- BBW: Historical volatility based on price action
- VIX: Forward-looking implied volatility from options

## References

* Bollinger, J. (2002). Bollinger on Bollinger Bands. McGraw-Hill Education.
* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
* Elder, A. (1993). Trading for a Living. John Wiley & Sons.
* Achelis, S. B. (2000). Technical Analysis from A to Z. McGraw-Hill.
