# CMF: Chaikin Money Flow

[Pine Script Implementation of CMF](https://github.com/mihakralj/pinescript/blob/main/indicators/volume/cmf.pine)

## Overview and Purpose

The Chaikin Money Flow (CMF) is a volume-weighted momentum oscillator developed by Marc Chaikin to measure the amount of Money Flow Volume over a specific period. Unlike other volume indicators that focus solely on volume changes, CMF incorporates both price position and volume to evaluate buying and selling pressure. By analyzing where a security closes within its daily range and weighting this by volume, CMF provides insights into the direction and intensity of money flow.

CMF oscillates above and below a zero line, with positive values indicating accumulation (buying pressure) and negative values indicating distribution (selling pressure). The indicator is particularly effective for confirming price trends, identifying potential reversals, and spotting divergences between price action and underlying buying/selling pressure.

## Core Concepts

* **Money Flow Multiplier:** Evaluates where price closes within its range to determine buying or selling bias
* **Money Flow Volume:** Combines the multiplier with volume to determine directional volume pressure
* **Accumulation/Distribution:** Positive CMF values suggest accumulation (buyers in control), while negative values suggest distribution (sellers in control)
* **Multi-timeframe analysis:** Functions effectively across all timeframes, though commonly used on daily charts

CMF provides a normalized reading between -1 and +1, with extreme readings near these boundaries indicating potentially unsustainable buying or selling pressure. The zero line serves as a key reference point, with crossovers signaling potential shifts in market control between buyers and sellers.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 20 | Lookback period for CMF calculation | Shorter for more sensitivity/signals, longer for stronger trend focus |
| High Source | High | Price data for range calculation | Rarely needs adjustment |
| Low Source | Low | Price data for range calculation | Rarely needs adjustment |
| Close Source | Close | Price data for position within range | Rarely needs adjustment |
| Volume Source | Volume | Volume data for weighting | Consider adjusting when analyzing unusual volume characteristics |

**Pro Tip:** While the 20-period setting is standard, try 21 periods for alignment with the number of trading days in a month, which can provide a clearer picture of monthly money flow patterns.

## Calculation and Mathematical Foundation

**Simplified explanation:**
CMF calculates a Money Flow Multiplier (MFM) that measures where price closes within its range. This multiplier is then applied to volume to get Money Flow Volume (MFV). The CMF value is the sum of Money Flow Volume divided by the sum of volume over the specified period.

**Technical formula:**

1. Money Flow Multiplier (MFM) = ((Close - Low) - (High - Close)) / (High - Low)
2. Money Flow Volume (MFV) = MFM × Volume
3. CMF = Sum(MFV, Length) / Sum(Volume, Length)

> 🔍 **Technical Note:** When the price closes in the upper half of its range, MFM is positive; when it closes in the lower half, MFM is negative. The implementation handles edge cases where High equals Low by setting MFM to 0, preventing division by zero errors.

## Interpretation Details

CMF provides several types of analytical signals:

* **Zero line crossovers:** Crossing above zero indicates a shift to net buying pressure; crossing below zero indicates a shift to net selling pressure
* **Sustained readings:** Values remaining positive/negative for extended periods confirm strong bullish/bearish conditions
* **Magnitude analysis:** Stronger readings (closer to +1 or -1) indicate more intense buying or selling pressure
* **Divergences:** When price makes a new high/low but CMF fails to confirm, it suggests potential weakness in the current trend
* **Trend confirmation:** CMF should align with the price trend; misalignment may signal weakening momentum
* **Support/resistance tests:** CMF can help gauge the strength of buying/selling pressure during tests of significant price levels

## Limitations and Considerations

* **Volume dependency:** Less reliable in markets with inconsistent or manipulated volume data
* **Complementary analysis:** Works best when combined with price action analysis and other technical indicators
* **Range-bound markets:** May generate conflicting signals during prolonged consolidation periods
* **Spikes handling:** Extreme volume events may temporarily distort readings
* **Periodicity sensitivity:** Different timeframes may require adjustment of the lookback period
* **False signals:** Like many oscillators, CMF can generate false signals, particularly in choppy market conditions

## References

* Chaikin, M. (1982). Money Flow Analysis.
* Pring, M. J. (2002). Technical Analysis Explained. McGraw-Hill.
* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
