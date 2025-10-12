# PSAR: Parabolic Stop And Reverse (Parabolic SAR)

[Pine Script Implementation of PSAR](https://github.com/mihakralj/pinescript/blob/main/indicators/reversals/psar.pine)

## Overview and Purpose

The Parabolic Stop And Reverse (SAR) is a trend-following indicator that provides entry and exit points, developed by J. Welles Wilder Jr. and introduced in his 1978 seminal work "New Concepts in Technical Trading Systems". The indicator appears as a series of dots placed above or below price bars, creating a parabolic curve that accelerates with the trend.

The Parabolic SAR is designed to identify potential reversals in price direction and provide trailing stop levels. When the SAR is below price, it indicates an uptrend and provides a trailing stop level that rises with price. When the SAR is above price, it indicates a downtrend and provides a trailing stop level that falls with price. The indicator "stops and reverses" when price crosses the SAR level, hence its name.

The unique characteristic of the Parabolic SAR is its acceleration feature - as the trend continues and makes new highs or lows, the SAR accelerates its movement toward price, tightening the stop level. This allows traders to lock in profits as trends mature while giving more room during early trend development.

## Core Concepts

* **Stop and Reverse:** SAR switches from buy to sell (or vice versa) when price crosses the SAR level, always keeping traders in the market
* **Acceleration Factor (AF):** Increases each time a new extreme point is reached, causing SAR to accelerate toward price as trend strengthens
* **Extreme Point (EP):** The highest high in an uptrend or lowest low in a downtrend - the target the SAR moves toward
* **Trailing Stop:** SAR acts as a dynamic trailing stop that moves in the direction of the trend but never reverses
* **Parabolic Movement:** The distance between SAR and price decreases parabolically as trend continues, creating the characteristic curved pattern
* **Binary Signal:** Always provides a clear directional bias - either long (SAR below price) or short (SAR above price)

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|----------------|
| Start AF | 0.02 | Initial acceleration factor when trend begins | Lower (0.01) for slower, more conservative signals; rarely increased |
| AF Increment | 0.02 | Amount AF increases with each new extreme | Lower (0.01) for gentler acceleration; higher (0.03-0.05) for more responsive signals |
| Max AF | 0.20 | Maximum acceleration factor limit | Lower (0.10-0.15) for trending markets to avoid premature exits; higher (0.25-0.30) for volatile markets |

**Pro Tip:** Wilder's original parameters (0.02, 0.02, 0.20) work well for most markets and timeframes. For strongly trending markets like forex or crypto, consider lowering Max AF to 0.10-0.15 to avoid being stopped out of good trends prematurely. For choppy or ranging markets, PSAR may generate excessive whipsaws - use with trend confirmation filters in such conditions.

## Calculation and Mathematical Foundation

**Simplified explanation:**
The Parabolic SAR calculates a trailing stop level that accelerates toward price as the trend continues. It starts with a small acceleration factor that increases each time price makes a new high (uptrend) or low (downtrend), causing the SAR to close in on price faster as the trend matures.

**Technical formula:**

**Initial Setup (First Bar):**
```
If Close > Open:
  Long trend, SAR = Low, EP = High
Else:
  Short trend, SAR = High, EP = Low
AF = Start AF
```

**Each Subsequent Bar:**

```
1. Calculate new SAR:
   SAR_new = SAR_prev + AF × (EP - SAR_prev)

2. Safety Rule (prevent SAR from penetrating prior bars):
   If Long: SAR_new = min(SAR_new, Low[1], Low[2])
   If Short: SAR_new = max(SAR_new, High[1], High[2])

3. Check for Reversal:
   If Long and Low < SAR_new:
     Reverse to Short
     SAR_new = EP
     EP = Low
     AF = Start AF
   
   If Short and High > SAR_new:
     Reverse to Long
     SAR_new = EP
     EP = High
     AF = Start AF

4. Update Extreme Point and Acceleration (if no reversal):
   If Long and High > EP:
     EP = High
     AF = min(AF + AF_Increment, Max AF)
   
   If Short and Low < EP:
     EP = Low
     AF = min(AF + AF_Increment, Max AF)

5. SAR = SAR_new
```

> 🔍 **Technical Note:** The safety rule in step 2 is critical - it prevents the SAR from appearing inside the prior two bars' price ranges, which would cause immediate reversals. The AF resets to Start AF on every reversal, allowing new trends to develop gradually before acceleration begins.

## Interpretation Details

The Parabolic SAR provides multiple layers of analysis:

* **Trend Direction:**
  - SAR below price (dots below candles): Uptrend - long positions
  - SAR above price (dots above candles): Downtrend - short positions
  - Clear, unambiguous directional signal at all times

* **Entry Signals:**
  - Price crosses above SAR: Enter long position
  - Price crosses below SAR: Enter short position
  - SAR reversal provides immediate entry signal
  - No neutral zone - always positioned for next move

* **Trailing Stop Levels:**
  - SAR value is the stop loss for current position
  - Stop automatically trails price in trend direction
  - Stop never moves against the trend
  - Accelerates toward price as trend matures

* **Trend Strength Assessment:**
  - Wide distance between SAR and price: Strong, established trend
  - Narrowing distance: Trend weakening or accelerating into climax
  - Frequent reversals: Ranging or choppy market conditions
  - Long runs without reversal: Sustained trending environment

* **Exit Timing:**
  - Exit long when price crosses below SAR
  - Exit short when price crosses above SAR
  - SAR reversal provides definitive exit signal
  - No discretion required - rule-based exits

* **Risk Management:**
  - Always know your stop level (current SAR value)
  - Stops tighten automatically as profits accumulate
  - Maximum risk defined before entry
  - Protects capital in adverse moves

* **Market Context:**
  - Works best in trending markets (30-40% of time)
  - Struggles in sideways markets (60-70% of time)
  - Multiple quick reversals indicate ranging conditions
  - Combine with trend filters for better performance

## Limitations and Considerations

* **Whipsaw in Ranging Markets:** Generates frequent false signals in sideways markets, as price repeatedly crosses the SAR without establishing a trend - can lead to consecutive losing trades
* **Always in Market:** Forces you to always hold a position (long or short) with no neutral stance - not suitable for all trading strategies or market conditions
* **Late Entries:** In fast-moving trends, reversal signal may occur well after the initial move, missing a significant portion of the trend - optimized for trend following, not early entry
* **No Magnitude Information:** Provides direction but not expected move size or probability - requires additional analysis for position sizing and profit targets
* **Parameter Sensitivity:** Performance varies significantly with different AF settings - what works in one market/timeframe may fail in another
* **Trend Acceleration Paradox:** As trends mature and SAR tightens, increased probability of stop-out even in valid trends - "too successful" trends may self-terminate
* **No Volume Consideration:** Ignores volume and market structure - reversals may occur on low-volume price spikes that lack conviction
* **Two-Bar Lookback Only:** Safety rule uses only two prior bars - can be penetrated in highly volatile markets with large gaps
* **Resets on Reversal:** AF resets to Start AF on every reversal, potentially missing early acceleration in strong counter-trends
* **Best with Filters:** Most profitable when combined with trend strength indicators (ADX, ATR) or market regime filters to avoid ranging periods

## References

* Wilder, J. W. (1978). New Concepts in Technical Trading Systems. Trend Research.
* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
* Pring, M. J. (2002). Technical Analysis Explained (4th ed.). McGraw-Hill.
