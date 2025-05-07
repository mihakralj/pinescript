# CMO: Chande Momentum Oscillator

[Pine Script Implementation of CMO](https://github.com/mihakralj/pinescript/blob/main/indicators/momentum/cmo.pine)

## Overview and Purpose

The Chande Momentum Oscillator (CMO), developed by Tushar Chande, is a technical momentum indicator that measures the strength and direction of price momentum. Unlike other momentum indicators that use simple differences or ratios, CMO compares the sum of recent gains to the sum of recent losses, providing a unique perspective on market momentum. The indicator oscillates between +100 and -100, with readings above +50 or below -50 indicating potential overbought or oversold conditions.

This implementation uses circular buffers for efficient calculation of sums, maintaining O(1) computational complexity regardless of the lookback period. The algorithm properly handles data gaps and maintains accurate momentum calculations without recalculating entire sums each bar.

## Core Concepts

* **Momentum measurement:** Compares upward and downward price movements to gauge momentum strength
* **Zero-line significance:** Crossovers indicate potential trend changes
* **Extreme readings:** Values near +/-50 suggest overbought/oversold conditions
* **Trend confirmation:** Direction and slope confirm price trend strength
* **Divergence analysis:** Useful for identifying potential trend reversals

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 14 | Lookback period for momentum calculation | Lower for more signals but increased noise, higher for smoother readings |
| Source | Close | Price data used for calculation | Consider using hlc3 for more comprehensive price action |

**Pro Tip:** While the default 14-period setting works well for daily charts, consider using 10 periods for more active markets or 20 periods for longer-term analysis. The traditional +/-50 thresholds can be adjusted to +/-40 for more frequent signals or +/-60 for extreme conditions only.

## Calculation and Mathematical Foundation

**Simplified explanation:**
CMO measures the ratio of upward price changes to total price changes over a specified period, scaled to oscillate between +100 and -100. It does this by comparing the sum of up-moves to the sum of down-moves.

**Technical formula:**
CMO = 100 × (SUM_up - SUM_down) / (SUM_up + SUM_down)

Where:
* SUM_up = Sum of upward price changes over the period
* SUM_down = Sum of downward price changes over the period
* Result is scaled to range from +100 to -100

> 🔍 **Technical Note:** The implementation uses circular buffers to maintain running sums of up and down moves, ensuring O(1) computational complexity per bar. The algorithm properly handles NA values and maintains accurate momentum calculations without recalculating entire sums each bar.

## Interpretation Details

CMO provides multiple analytical perspectives:

* **Trend Direction:** Positive values indicate upward momentum, negative values downward momentum
* **Trend Strength:** Greater distance from zero indicates stronger momentum
* **Overbought/Oversold:** Readings above +50 or below -50 suggest extreme conditions
* **Zero-line Crossovers:** Can signal potential trend changes
* **Divergence Signals:** CMO diverging from price can indicate potential reversals
* **Rate of Change:** Slope of CMO line indicates momentum acceleration/deceleration

## Limitations and Considerations

* **Lag Component:** As with all momentum indicators, CMO has some inherent lag
* **False Signals:** Can generate numerous signals in choppy markets
* **Scaling Issues:** Fixed +/-100 scale may not be optimal for all markets
* **Timeframe Dependency:** Different timeframes require different interpretation approaches
* **Complementary Analysis:** Should be used alongside trend and volume indicators
* **Market Conditions:** Most effective in trending markets, less reliable in ranging conditions

## References

* Chande, T. S., & Kroll, S. (1994). The New Technical Trader. John Wiley & Sons.
* Chande, T. S. (1992). "Adapting Moving Averages to Market Volatility." Technical Analysis of Stocks & Commodities.
