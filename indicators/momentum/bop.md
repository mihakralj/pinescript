# BOP: Balance of Power

[Pine Script Implementation of BOP](https://github.com/mihakralj/pinescript/blob/main/indicators/momentum/bop.pine)

## Overview and Purpose

The Balance of Power (BOP) indicator measures the relative strength between buyers and sellers by comparing the closing price to the opening price within the context of the trading range. Developed to quantify market pressure, BOP provides insights into which market participants (buyers or sellers) are more aggressively controlling price action. By relating the position of the close relative to the open against the total trading range, BOP creates a normalized measure of buying or selling pressure that oscillates around zero.

The implementation provided uses calculations with optional smoothing to reduce noise while maintaining responsiveness. This approach helps traders identify shifts in market control and potential trend reversals by measuring the relationship between price movement and range, with proper handling of edge cases such as zero-range bars.

## Core Concepts

* **Price position analysis:** Measures where the close is relative to the open within the high-low range
* **Market pressure quantification:** Normalizes buying/selling pressure to a scale that's comparable across different securities
* **Range normalization:** Accounts for volatility by considering the total trading range
* **Optional smoothing:** Provides flexibility to reduce noise while maintaining signal clarity

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Smoothing Length | 14 | Period for smoothing raw BOP values | 0 for no smoothing, increase for less noise but more lag |

**Pro Tip:** While the default 14-period smoothing works well for daily charts, consider using shorter periods (5-10) for intraday trading or longer periods (20-30) for position trading. Using no smoothing (length=0) can be effective for detecting immediate shifts in market pressure.

## Calculation and Mathematical Foundation

**Simplified explanation:**
BOP measures how much of the day's range was controlled by buyers versus sellers by comparing where the price closed relative to where it opened, normalized by the day's range. A close near the high suggests buyer control, while a close near the low suggests seller control.

**Technical formula:**
Raw BOP = (Close - Open) / (High - Low)

Where:
- If High equals Low (zero range), BOP = 0
- Final BOP value is optionally smoothed using EMA(Raw BOP, Length)

> 🔍 **Technical Note:** The implementation includes special handling for zero-range bars and uses an optimized EMA calculation with proper warmup period handling. The algorithm maintains O(1) computational complexity while ensuring accurate smoothing from the first available bar.

## Interpretation Details

BOP provides several analytical perspectives:

* **Market control:** Positive values indicate buyer control, negative values indicate seller control
* **Trend strength:** Greater distance from zero indicates stronger control by either buyers or sellers
* **Momentum shifts:** Changes in BOP direction can signal potential trend reversals
* **Divergence analysis:** BOP diverging from price can indicate weakening trends
* **Range context:** Values are automatically normalized by the trading range
* **Trend confirmation:** Consistent BOP sign confirms trend direction

## Limitations and Considerations

* **Range dependency:** Requires meaningful high-low range for accurate signals
* **Gap handling:** Does not account for gaps between trading sessions
* **Smoothing trade-off:** More smoothing reduces noise but increases lag
* **Time frame sensitivity:** Most effective on time frames that capture complete trading sessions
* **Market type influence:** More reliable in trending markets than in choppy conditions
* **Complementary tool:** Should be used alongside price action and other indicators for confirmation

## References

* Elder, A. (2002). Come Into My Trading Room: A Complete Guide to Trading. John Wiley & Sons.
* Kaufman, P. J. (2013). Trading Systems and Methods (5th ed.). Wiley Trading.
* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
