# HT_TRENDMODE: Hilbert Transform Trend Mode

[Pine Script Implementation of HT_TRENDMODE](https://github.com/mihakralj/pinescript/blob/main/indicators/dynamics/ht_trendmode.pine)

## Overview and Purpose

The Hilbert Transform Trend Mode (HT_TRENDMODE) is an advanced market state classifier developed by John Ehlers that determines whether the market is currently in a trending state or a cycling (oscillating) state. Published in his book "Cycle Analytics for Traders" (2013), this binary indicator uses the Hilbert Transform and dominant cycle period analysis to provide real-time classification of market behavior.

Unlike traditional trend indicators that measure strength or direction, HT_TRENDMODE focuses on identifying the fundamental nature of price movement: is the market trending in one direction, or is it oscillating in a range? This classification is crucial because different trading strategies and indicators perform optimally in different market states - trend-following strategies excel in trending markets while mean-reversion strategies work better in cycling markets.

## Core Concepts

* **Binary Classification**: Returns 1 for trend mode (directional movement) and 0 for cycle mode (ranging oscillation), providing clear market state identification
* **Hilbert Transform Analysis**: Uses phase and amplitude information from the Hilbert Transform to detect the presence of dominant cycles versus trends
* **Sine Wave Threshold**: Examines the sine wave derived from the dominant cycle phase - weak sine amplitudes indicate trending, strong amplitudes indicate cycling
* **Dominant Cycle Period**: Incorporates HT_DCPERIOD to understand the current market rhythm and adjust detection sensitivity accordingly
* **Adaptive Detection**: Dynamically adjusts to changing market conditions, switching between trend and cycle classification as market behavior evolves

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|----------------|
| Source | hlc3 | Price data to analyze | Use close for end-of-bar signals, hlc3 for smoother intrabar analysis |

**Pro Tip:** HT_TRENDMODE works best when combined with other Ehlers indicators: use HT_DCPERIOD to understand cycle length, HT_TRENDMODE to determine market state, then apply appropriate indicators (trend-following when mode=1, oscillators when mode=0). This creates an adaptive trading system that automatically adjusts to market conditions.

## Calculation and Mathematical Foundation

**Simplified explanation:**
HT_TRENDMODE compares the instantaneous period (derived from phase rate-of-change) with the dominant cycle period. When the instantaneous period is significantly longer than the dominant cycle period (>1.5x), it indicates trending behavior where phase changes slowly. When periods are similar, the market is cycling.

**Technical formula:**

1. **Calculate dominant cycle period** using HT_DCPERIOD:
   ```
   DCPeriod = HT_DCPERIOD(source)
   ```

2. **Compute Hilbert Transform components** (same as HT_DCPERIOD):
   ```
   SmoothPrice = (4×Price + 3×Price[1] + 2×Price[2] + Price[3]) / 10
   Detrender = HT_FIR(SmoothPrice) with adaptive bandwidth
   Q1 = HT_FIR(Detrender)
   I1 = Detrender[3]
   ```

3. **Advance phase by 90 degrees**:
   ```
   jI = HT_FIR(I1)
   jQ = HT_FIR(Q1)
   I2 = I1 - jQ
   Q2 = Q1 + jI
   Smooth I2 and Q2: Value = 0.2×Value + 0.8×Value[1]
   ```

4. **Calculate phase angle**:
   ```
   Re = I2×I2[1] + Q2×Q2[1]
   Im = I2×Q2[1] - Q2×I2[1]
   Smooth Re and Im: Value = 0.2×Value + 0.8×Value[1]
   DCPhase = arctan(Im / Re) + 90°
   Normalize DCPhase to [0, 360°]
   ```

5. **Calculate instantaneous period from phase rate-of-change**:
   ```
   DeltaPhase = DCPhase[1] - DCPhase
   DeltaPhase = max(DeltaPhase, 1.0)
   InstPeriod = 2π / DeltaPhase
   Smooth: InstPeriod = 0.33×InstPeriod + 0.67×InstPeriod[1]
   ```

6. **Determine trend mode by comparing periods**:
   ```
   TrendMode = InstPeriod > 1.5×DCPeriod ? 1 : 0
   ```

> 🔍 **Technical Note:** The 1.5x threshold compares instantaneous period (from phase rate-of-change) with dominant cycle period. When phase changes slowly (large instantaneous period), the market is trending. When phase changes at the expected cycle rate, the market is cycling. The 0.33/0.67 smoothing provides stability while maintaining responsiveness.

## Interpretation Details

HT_TRENDMODE provides binary market state classification with clear trading implications:

* **Trend Mode (Value = 1)**:
  - Market is directional with weak or absent cyclical component
  - Price showing sustained movement in one direction
  - Use trend-following indicators: moving averages, MACD, ADX
  - Employ breakout strategies and momentum approaches
  - Avoid mean-reversion strategies
  - Wider stops and longer holding periods appropriate

* **Cycle Mode (Value = 0)**:
  - Market is oscillating with strong cyclical component
  - Price bouncing between support and resistance
  - Use oscillators: RSI, Stochastic, CCI
  - Employ mean-reversion and range-trading strategies
  - Avoid trend-following and breakout strategies
  - Tighter stops and shorter holding periods appropriate

* **Mode Transitions**:
  - 1→0 (Trend to Cycle): Trend exhaustion, range formation beginning
  - 0→1 (Cycle to Trend): Breakout occurring, new trend developing
  - Rapid oscillation: Transitional period, reduce position size
  - Stable readings: High confidence in current market state

* **Strategy Selection**:
  - Mode = 1: ADX, moving average crossovers, Parabolic SAR, breakouts
  - Mode = 0: RSI divergences, Bollinger Band bounces, Stochastic, support/resistance
  - Use HT_DCPERIOD to optimize indicator periods during cycle mode

## Limitations and Considerations

* **Lag Component**: Requires approximately 50-60 bars for stable operation due to underlying HT_DCPERIOD calculation and smoothing, resulting in mode detection that confirms rather than predicts state changes
* **Binary Nature**: Simple 0/1 output doesn't capture the degree of trending or cycling - a weak trend and strong trend both show as 1, providing no gradation
* **Threshold Sensitivity**: The 0.25 sine amplitude threshold works well for most markets but may need adjustment for highly volatile or very quiet instruments
* **Whipsaw Risk**: During transitional periods between trend and cycle, rapid mode switches can generate false signals and trading whipsaws
* **Market Dependent**: Performs better in liquid markets with clear cycles - may struggle in illiquid or news-driven markets with erratic behavior
* **Complementary Use**: Best used with confirming indicators rather than as sole decision criterion - combine with volume analysis, support/resistance, and other market structure tools

## References

* Ehlers, J. F. (2013). *Cycle Analytics for Traders: Advanced Technical Trading Concepts*. Wiley Trading.
* Ehlers, J. F. (2001). *Rocket Science for Traders: Digital Signal Processing Applications*. Wiley Trading.
* TA-Lib Technical Analysis Library - HT_TRENDMODE implementation
* Ehlers, J. F. "MESA and Trading Market Cycles" - Technical Papers
