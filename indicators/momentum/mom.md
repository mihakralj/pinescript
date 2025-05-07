# MOM: Momentum

[Pine Script Implementation of MOM](https://github.com/mihakralj/pinescript/blob/main/indicators/momentum/mom.pine)

## Overview and Purpose

The Momentum (MOM) indicator is one of the simplest and most fundamental technical analysis tools, measuring the rate of price change over a specified period. It calculates the difference between the current price and the price n periods ago, providing a direct measure of price velocity. This basic yet powerful concept forms the foundation for many more complex momentum indicators.

This implementation provides a straightforward calculation of price momentum while properly handling data gaps and edge cases. The indicator oscillates above and below zero, with positive values indicating upward momentum and negative values showing downward momentum.

## Core Concepts

* **Price velocity:** Measures the speed of price change over time
* **Zero-line significance:** Crossovers indicate momentum shifts
* **Trend strength:** Greater distance from zero indicates stronger momentum
* **Divergence analysis:** Useful for identifying potential trend reversals
* **Rate of change:** Shows acceleration or deceleration of price movement

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 10 | Lookback period for momentum calculation | Lower for faster signals but more noise, higher for smoother readings |
| Source | Close | Price data used for calculation | Consider using hlc3 for more comprehensive price action |

**Pro Tip:** While the default 10-period setting works well for daily charts, consider using 5-6 periods for intraday trading or 20-25 periods for longer-term analysis. The indicator is particularly effective when used in conjunction with moving averages.

## Calculation and Mathematical Foundation

**Simplified explanation:**
Momentum measures the absolute price change over a specified period. It subtracts the price n periods ago from the current price, showing how much the price has changed in that time.

**Technical formula:**
MOM = Price(t) - Price(t-n)

Where:
- Price(t) is the current price
- Price(t-n) is the price n periods ago
- Result shows absolute price change over n periods

> 🔍 **Technical Note:** The implementation properly handles NA values and ensures accurate momentum calculations even during data gaps or market closures. The simple calculation makes it computationally efficient while remaining effective for trend analysis.

## Interpretation Details

Momentum provides multiple analytical perspectives:

* **Trend Direction:** Positive values indicate upward momentum, negative downward
* **Trend Strength:** Greater distance from zero indicates stronger momentum
* **Zero-line Crossovers:** Signal potential trend changes
* **Divergence Signals:** Momentum diverging from price can indicate potential reversals
* **Rate of Change:** Slope indicates momentum acceleration/deceleration
* **Extreme Readings:** Can identify overbought/oversold conditions

## Limitations and Considerations

* **Scale Dependency:** Values depend on the absolute price, making comparisons across different instruments challenging
* **Lag Component:** Uses historical price data, introducing some inherent lag
* **Noise Sensitivity:** Can generate numerous signals in choppy markets
* **Price Scale Impact:** Higher-priced securities naturally show larger momentum values
* **Complementary Analysis:** Best used alongside trend and volume indicators
* **Timeframe Dependency:** Different timeframes require different interpretation approaches

## References

* Kaufman, P. J. (2013). Trading Systems and Methods (5th ed.). Wiley Trading.
* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
* Pring, M. J. (2002). Technical Analysis Explained. McGraw-Hill.
* Wilder, J. W. (1978). New Concepts in Technical Trading Systems.
