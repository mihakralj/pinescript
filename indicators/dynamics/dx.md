# DX: Directional Movement Index

[Pine Script Implementation of DX](https://github.com/mihakralj/pinescript/blob/main/indicators/dynamics/dx.pine)

## Overview and Purpose

The Directional Movement Index (DX) is a technical indicator developed by J. Welles Wilder Jr. in 1978 as a core component of the Average Directional Index (ADX) system. DX measures the strength of directional movement by comparing the positive directional indicator (+DI) to the negative directional indicator (-DI), expressing the result as a percentage. Unlike ADX which smooths DX values, this standalone DX indicator provides an unsmoothed, more responsive measure of trend strength.

DX quantifies how strongly price is moving in one direction versus the other, ranging from 0 to 100. Higher values indicate stronger directional movement (trending), while lower values suggest weak or non-directional price action (ranging). This implementation uses Wilder's smoothing (equivalent to RMA) with warmup compensation to provide accurate values from the first bar.

## Core Concepts

* **Directional strength:** Measures the dominance of one direction over the other
* **Unsmoothed metric:** More responsive than ADX, shows immediate directional changes
* **Normalized scale:** Values from 0-100 regardless of price level or volatility
* **Trend identification:** Distinguishes trending markets from ranging markets
* **Component indicator:** Building block for ADX and ADXR calculations

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Period | 14 | Lookback period for Wilder's smoothing | Lower (7-10) for faster response; higher (20-30) for smoother, less noisy signals |

**Pro Tip:** The standard 14-period setting works well for most timeframes and was Wilder's original recommendation. Consider adjusting based on market characteristics:
- Fast-moving markets: 7-10 periods for quicker signals
- Volatile markets: 20-30 periods to reduce noise
- Position trading: 21-28 periods for longer-term trends
- Day trading: 7-14 periods for intraday responsiveness

## Calculation and Mathematical Foundation

**Simplified explanation:**
DX calculates the percentage difference between +DI and -DI relative to their sum, showing how dominant one direction is over the other.

**Technical formula:**

1. Calculate True Range (TR):
   ```
   TR = max(high - low, abs(high - close[1]), abs(low - close[1]))
   ```

2. Calculate Directional Movement:
   ```
   +DM = (high - high[1] > low[1] - low) and (high - high[1] > 0) ? high - high[1] : 0
   -DM = (low[1] - low > high - high[1]) and (low[1] - low > 0) ? low[1] - low : 0
   ```

3. Apply Wilder's smoothing (RMA with α = 1/period):
   ```
   Smoothed_TR = RMA(TR, period)
   Smoothed_+DM = RMA(+DM, period)
   Smoothed_-DM = RMA(-DM, period)
   ```

4. Calculate Directional Indicators:
   ```
   +DI = 100 * Smoothed_+DM / Smoothed_TR
   -DI = 100 * Smoothed_-DM / Smoothed_TR
   ```

5. Calculate DX:
   ```
   DX = 100 * abs(+DI - -DI) / (+DI + -DI)
   ```

> 🔍 **Technical Note:** This implementation uses Wilder's smoothing (RMA) with warmup compensation, providing accurate DX values from the first bar without the typical initialization lag. The compensation gradually reduces as the smoothing converges, typically within 3-4 times the period length.

## Interpretation Details

DX provides direct insight into directional strength:

* **Value Ranges:**
  - DX < 25: Weak directional movement, ranging or consolidating market
  - DX 25-50: Moderate directional movement, developing trend
  - DX 50-75: Strong directional movement, established trend
  - DX > 75: Very strong directional movement, powerful trend

* **Trend Strength Assessment:**
  - Rising DX: Increasing directional conviction, trend strengthening
  - Falling DX: Decreasing directional conviction, trend weakening
  - DX near 0: No clear direction, balanced +DI and -DI
  - DX near 100: Extreme directional dominance, one-sided movement

* **Market Context:**
  - High DX with +DI > -DI: Strong uptrend
  - High DX with -DI > +DI: Strong downtrend
  - Low DX: Non-trending, choppy, or ranging market
  - DX spikes: Sudden directional shifts or breakouts

* **Compared to ADX:**
  - DX is more volatile and responsive than ADX
  - DX shows immediate directional changes
  - ADX smooths DX to reduce noise (ADX = RMA of DX values)
  - Use DX for early signals, ADX for confirmed trends

## Advantages

1. **Immediate Response:**
   - Reacts faster than ADX to directional changes
   - Shows real-time trend strength without additional smoothing
   - Useful for early trend detection

2. **Normalized Measurement:**
   - Scale from 0-100 works across all instruments
   - Comparable across different price levels and timeframes
   - Easy to set consistent thresholds

3. **Building Block:**
   - Foundation for ADX calculation
   - Can be smoothed further for custom indicators
   - Integrates with other directional indicators

## Limitations and Considerations

* **Higher volatility:** More noise than ADX due to lack of additional smoothing
* **Whipsaw signals:** Can generate false signals in choppy markets
* **No direction:** Only shows strength, not trend direction (use +DI/-DI for direction)
* **Lagging component:** Wilder's smoothing introduces some lag (though less than ADX)
* **Threshold subjectivity:** "Strong" DX levels vary by market and timeframe
* **Range-bound bias:** Very low DX values don't indicate trend direction
* **Requires confirmation:** Best used with price action and other indicators

## Relationship to ADX System

**DX in the Wilder Framework:**
- **DX**: Unsmoothed directional strength (this indicator)
- **ADX**: Smoothed DX (RMA of DX values), shows sustained trend strength
- **ADXR**: Average of current and historical ADX, even smoother trend measure
- **+DI/-DI**: Show trend direction, DX shows strength regardless of direction

**Usage Hierarchy:**
1. Use +DI and -DI to determine trend direction
2. Use DX to assess immediate directional strength
3. Use ADX for confirmed, sustained trend strength
4. Use ADXR for long-term trend assessment

## Trading Applications

* **Trend Confirmation:** DX > 25 confirms directional movement
* **Range Identification:** DX < 25 suggests consolidation or ranging
* **Breakout Detection:** Rising DX from low levels signals potential breakout
* **Trend Exhaustion:** DX > 75 may indicate overextended conditions
* **Filter System:** Use DX to filter trend-following strategies
* **Market Scanner:** Compare DX across multiple instruments to find trending markets

## References

* Wilder, J. W. (1978). New Concepts in Technical Trading Systems. Trend Research.
* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
* Kaufman, P. J. (2013). Trading Systems and Methods (5th ed.). Wiley Trading.
* Pring, M. J. (2002). Technical Analysis Explained (4th ed.). McGraw-Hill.
