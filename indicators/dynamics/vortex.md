# VORTEX: Vortex Indicator

[Pine Script Implementation of VORTEX](https://github.com/mihakralj/pinescript/blob/main/indicators/dynamics/vortex.pine)

## Overview and Purpose

The Vortex Indicator (VI) is a technical analysis tool developed by Etienne Botes and Douglas Siepman, introduced in the January 2010 issue of "Technical Analysis of Stocks & Commodities." The indicator is designed to identify the beginning of new trends and confirm the continuation of existing trends by measuring positive and negative trend movement in relation to price volatility.

The Vortex Indicator consists of two oscillating lines: VI+ (positive vortex indicator) and VI- (negative vortex indicator). These lines capture the directional flow of price movement by comparing the current high/low to the previous low/high, normalized by true range. The concept is based on natural vortex movements observed in fluid dynamics and applied to price action.

This implementation uses efficient running sums with circular buffers to achieve O(1) complexity, providing accurate trend signals from the first bar with proper warmup handling.

## Core Concepts

* **Dual Lines:** VI+ measures upward vortex movement, VI- measures downward vortex movement
* **Vortex Movement:** Captures price flow between bars using absolute distance between high/low and prior low/high
* **True Range Normalization:** Divides vortex movements by true range to account for volatility
* **Crossover Signals:** VI+ crossing above VI- indicates uptrend; VI- crossing above VI+ indicates downtrend
* **Trend Strength:** Greater separation between lines indicates stronger trend
* **Natural Price Flow:** Based on principles of vortex behavior in fluid dynamics applied to markets

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|----------------|
| Period | 14 | Lookback period for summing movements and true range | Lower (7-10) for faster signals in volatile markets, higher (21-25) for smoother, longer-term trends |

**Pro Tip:** The default 14-period setting works well across most markets and timeframes, providing a good balance between responsiveness and noise reduction. For day trading, consider 7-10 periods for quicker signals. For swing trading or position trading, use 21-25 periods for more reliable trend identification. The Vortex Indicator works best when combined with other trend confirmation tools, as it can generate false signals during choppy, sideways markets. Watch for strong crossovers with clear separation between VI+ and VI- for the most reliable signals.

## Calculation and Mathematical Foundation

**Simplified explanation:**
The Vortex Indicator measures the relationship between current and prior highs/lows to identify directional movement. It calculates upward movement (high minus prior low) and downward movement (low minus prior high), sums these over a period, and normalizes by true range to create two oscillating lines.

**Technical formula:**

1. Calculate Vortex Movements for current bar:
   ```
   VM+ = |Current High - Prior Low|
   VM- = |Current Low - Prior High|
   ```

2. Calculate True Range (TR) for current bar:
   ```
   TR = max(High - Low, |High - Prior Close|, |Low - Prior Close|)
   ```

3. Sum movements over the period (n):
   ```
   Sum(VM+, n) = VM+(1) + VM+(2) + ... + VM+(n)
   Sum(VM-, n) = VM-(1) + VM-(2) + ... + VM-(n)
   Sum(TR, n) = TR(1) + TR(2) + ... + TR(n)
   ```

4. Calculate normalized Vortex Indicators:
   ```
   VI+ = Sum(VM+, n) / Sum(TR, n)
   VI- = Sum(VM-, n) / Sum(TR, n)
   ```

> 🔍 **Technical Note:** This implementation uses circular buffers to maintain running sums of VM+, VM-, and TR, achieving O(1) computational complexity. The absolute value calculations ensure all movements are positive before summation. Division by zero is prevented by checking if Sum(TR) > 0. The count-based warmup ensures accurate values from the first bar even when the full period hasn't been reached.

## Interpretation Details

The Vortex Indicator provides multiple analytical perspectives for trend identification and confirmation:

* **Trend Direction Identification:**
  - VI+ > VI-: Bullish trend in place (positive vortex movement dominates)
  - VI- > VI+: Bearish trend in place (negative vortex movement dominates)
  - Lines near equal: Trendless, ranging market conditions

* **Crossover Signals:**
  - VI+ crosses above VI-: Bullish signal, potential uptrend beginning
  - VI- crosses above VI+: Bearish signal, potential downtrend beginning
  - Multiple quick crossovers: Market indecision, avoid trading

* **Trend Strength:**
  - Wide separation between lines: Strong, well-defined trend
  - Narrow separation: Weak trend or consolidation
  - VI+ well above 1.0: Very strong bullish momentum
  - VI- well above 1.0: Very strong bearish momentum

* **Entry Signals:**
  - Long: Enter when VI+ crosses above VI- from below
  - Short: Enter when VI- crosses above VI+ from below
  - Confirm with price action and other indicators

* **Exit Signals:**
  - Close long when VI- crosses above VI+
  - Close short when VI+ crosses above VI-
  - Consider partial profits when lines begin converging

* **Divergence Analysis:**
  - Price making higher highs but VI+ making lower highs: Bearish divergence
  - Price making lower lows but VI- making lower lows: Bullish divergence
  - Divergences suggest potential trend exhaustion

* **Reference Level (1.0):**
  - Values above 1.0 indicate strong directional movement
  - Values below 1.0 during trend suggest weakening momentum
  - Both lines below 1.0: Low volatility, consolidation phase

## Limitations and Considerations

* **Lag Component:** Based on summed historical data, inherent lag in signal generation
* **False Signals in Ranges:** Can produce numerous whipsaw signals during sideways markets
* **Requires Confirmation:** Best used with other indicators like moving averages or RSI
* **No Overbought/Oversold:** Doesn't indicate when trends are overextended
* **Crossover Timing:** Signals can occur late after trend has already begun
* **Sensitivity to Period:** Shorter periods = more signals but also more noise
* **Volatility Dependent:** Normalization by TR makes it sensitive to volatility changes
* **Equal Weighting:** All bars in period weighted equally, no decay for older data
* **Trend Following Only:** Designed for trending markets, not effective for range-bound trading
* **Best Conditions:** Most reliable in clearly trending markets with sustained directional movement

## References

* Botes, E., & Siepman, D. (2010). "The Vortex Indicator." Technical Analysis of Stocks & Commodities, January 2010.
* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
