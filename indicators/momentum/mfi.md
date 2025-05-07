# MFI: Money Flow Index

[Pine Script Implementation of MFI](https://github.com/mihakralj/pinescript/blob/main/indicators/momentum/mfi.pine)

## Overview and Purpose

The Money Flow Index (MFI) is a volume-weighted momentum oscillator that measures buying and selling pressure. Often called the volume-weighted RSI, it incorporates both price and volume data to identify overbought or oversold conditions. Developed by Gene Quong and Avrum Soudack, MFI provides insights into the amount of money flowing in and out of a security by considering both price movements and trading volume.

This implementation uses circular buffers for efficient calculation of money flows, maintaining O(1) computational complexity regardless of the lookback period. The algorithm properly handles data gaps and maintains accurate flow calculations without recalculating entire sums each bar.

## Core Concepts

* **Volume integration:** Combines price and volume data for comprehensive market analysis
* **Money flow measurement:** Tracks the flow of money into and out of a security
* **Overbought/oversold identification:** Helps identify potential price reversals
* **Trend confirmation:** Validates price trends with volume support
* **Divergence analysis:** Useful for identifying potential trend reversals

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 14 | Lookback period for money flow calculation | Lower for more signals but increased noise, higher for smoother readings |

**Pro Tip:** While the default 14-period setting works well for daily charts, consider using 10 periods for more active markets or 20 periods for longer-term analysis. The traditional 80/20 thresholds can be adjusted to 90/10 for extreme conditions or 70/30 for more frequent signals.

## Calculation and Mathematical Foundation

**Simplified explanation:**
MFI calculates the ratio of positive to negative money flow over a specified period. It first determines typical price and multiplies it by volume to get raw money flow. This is then classified as positive or negative based on price direction, and the ratio is converted to an oscillator between 0 and 100.

**Technical formula:**
1. Typical Price = (High + Low + Close) / 3
2. Raw Money Flow = Typical Price × Volume
3. Money Flow Ratio = Positive Money Flow / Negative Money Flow
4. MFI = 100 - (100 / (1 + Money Flow Ratio))

Where:
- Positive Money Flow = Sum of Raw Money Flow when Typical Price increases
- Negative Money Flow = Sum of Raw Money Flow when Typical Price decreases

> 🔍 **Technical Note:** The implementation uses circular buffers to maintain running sums of positive and negative money flows, ensuring O(1) computational complexity per bar. The algorithm properly handles NA values and maintains accurate flow calculations without recalculating entire sums each bar.

## Interpretation Details

MFI provides multiple analytical perspectives:

* **Overbought/Oversold:** Readings above 80 suggest overbought, below 20 suggest oversold
* **Trend Direction:** Values above 50 indicate bullish momentum, below 50 bearish
* **Divergence Signals:** MFI diverging from price can signal potential reversals
* **Volume Confirmation:** High readings with strong volume confirm trend strength
* **Failure Swings:** Reversals that fail to reach previous extremes can signal trend changes
* **Centerline Crossovers:** Crossing above/below 50 can confirm trend changes

## Limitations and Considerations

* **Volume Dependency:** Requires reliable volume data for accurate signals
* **False Signals:** Can generate numerous signals in choppy markets
* **Market Type Sensitivity:** More effective in trending markets than ranging ones
* **Timeframe Dependency:** Different timeframes require different interpretation approaches
* **Volume Distortions:** Unusual volume spikes can temporarily distort readings
* **Complementary Analysis:** Should be used alongside price action and other indicators

## References

* Quong, G., & Soudack, A. (1989). "The Money Flow Index." Technical Analysis of Stocks & Commodities.
* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
* Kaufman, P. J. (2013). Trading Systems and Methods (5th ed.). Wiley Trading.
* DeMark, T. R. (1994). The New Science of Technical Analysis. John Wiley & Sons.
