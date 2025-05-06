# BOP: Balance of Power

[Pine Script Implementation of BOP](https://github.com/mihakralj/pinescript/blob/main/indicators/oscillators/bop.pine)

## Overview and Purpose

The Balance of Power (BOP) oscillator measures the relative strength between buyers and sellers by comparing price changes to trading ranges. Developed as a market strength indicator, BOP quantifies buying and selling pressure by examining the relationship between closing and opening prices within the context of the trading range. This approach provides insights into market control and potential trend changes by normalizing price movements relative to the day's trading activity.

The implementation provided uses an efficient EMA smoothing algorithm with proper warmup handling, ensuring accurate signals from the first available bar while maintaining computational efficiency. By focusing on price relationships rather than absolute values, BOP creates a normalized measure that works consistently across different price scales and market conditions.

## Core Concepts

* **Price position analysis:** Measures where prices close relative to their open within the day's range
* **Range normalization:** Uses the high-low range as a denominator to create comparable readings across different securities
* **Momentum measurement:** Identifies which market participants (buyers or sellers) are controlling price action
* **Trend confirmation:** Helps validate trend strength and potential reversal points through momentum analysis

BOP stands apart from traditional momentum indicators by focusing on the relationship between opening and closing prices relative to the trading range, providing insights into market participant behavior and control.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Smoothing Length | 14 | Period for EMA smoothing | Decrease for more sensitivity, increase for smoother signals |
| MA Type | SMA | Type of moving average for centerline | "Zero" for raw oscillator, "SMA" for trend identification |
| MA Length | 20 | Period for SMA centerline | Adjust based on typical trend duration |

**Pro Tip:** Use the SMA centerline crossovers for trend confirmation, but watch for divergences between BOP and price when the indicator moves in the opposite direction of price, as these often precede reversals.

## Calculation and Mathematical Foundation

**Simplified explanation:**
BOP calculates how much of the day's range was controlled by buyers versus sellers by comparing where the price closed relative to where it opened, normalized by the day's range. A close near the high suggests buyer control, while a close near the low suggests seller control.

**Technical formula:**
BOP = (Close - Open) / (High - Low)

Where:
- If High equals Low (zero range), BOP = 0
- Optional EMA smoothing: EMA(BOP, Length)
- Optional SMA centerline: SMA(BOP, MA_Length)

> 🔍 **Technical Note:** The implementation uses a sophisticated EMA algorithm with proper warmup handling and bias correction, ensuring accurate signals from the start of the data series. The algorithm maintains O(1) computational complexity while providing numerically stable results.

## Interpretation Details

BOP provides several analytical insights:

* **Positive values:** Indicate buying pressure (closes above opens)
* **Negative values:** Indicate selling pressure (closes below opens)
* **Magnitude:** Larger absolute values suggest stronger control by either buyers or sellers
* **Centerline crossovers:** Signal potential trend changes when using SMA option
* **Divergences:** BOP diverging from price can signal potential reversals
* **Trend confirmation:** Consistent positive/negative readings confirm trend direction

## Limitations and Considerations

* **Range dependency:** Requires meaningful high-low range for accurate signals
* **Gap handling:** Does not account for gaps between sessions
* **Smoothing trade-off:** More smoothing reduces noise but increases lag
* **Zero-range bars:** Special handling needed when high equals low
* **Complementary tools:** Best used alongside price action and volume analysis
* **Time frame sensitivity:** More reliable on daily charts where open/close relationship is meaningful

## References

* Elder, A. (2002). Come Into My Trading Room: A Complete Guide to Trading. John Wiley & Sons.
* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
* Kaufman, P. J. (2013). Trading Systems and Methods (5th ed.). Wiley Trading.
