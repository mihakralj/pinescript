# HL2: Midprice (High-Low Average)

[Pine Script Implementation of HL2](https://github.com/mihakralj/pinescript/blob/main/indicators/numerics/hl2.pine)

## Naming Convention

**HL2** is also known as **Median Price** in technical analysis literature. The term "median" here refers to the middle point between high and low, though mathematically it's the arithmetic mean (average) of the two extremes. This naming convention is widely adopted across trading platforms:

- **HL2**: Common in Pine Script and many programming libraries
- **Median Price**: Standard terminology in traditional technical analysis
- **Midprice**: Financial mathematics terminology
- **High-Low Average**: Descriptive name emphasizing the calculation method

## Overview and Purpose

The HL2 indicator, also known as Midprice or High-Low Average, calculates the simple average of the high and low prices for each bar. This price transformation represents the midpoint of the bar's trading range and provides a less extreme measure of price than using either the high or low alone. HL2 is particularly useful as a smoothed price series that filters out the closing bias while maintaining sensitivity to the full range of price action within each period.

This fundamental price transformation is widely used as an input source for other technical indicators, moving averages, and oscillators. By averaging the high and low, HL2 creates a balanced representation of price that is less susceptible to manipulation than the close price alone, making it valuable for analysis in markets with significant intrabar volatility.

## Core Concepts

* **Range midpoint:** Represents the exact center of each bar's price range, providing a balanced price measure
* **Closing bias elimination:** Removes the emphasis on closing prices, focusing instead on the full trading range
* **Volatility sensitivity:** Responds to the full extent of price movement within each period
* **Price smoothing:** Creates a naturally smoothed price series by averaging extremes

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| High | high | High price data | Typically not adjusted, uses standard high price |
| Low | low | Low price data | Typically not adjusted, uses standard low price |

**Pro Tip:** HL2 is particularly effective as a source input for moving averages and oscillators in volatile markets, as it reduces the impact of closing price manipulation while maintaining responsiveness to price action. Consider using HL2 instead of close prices for indicators in markets with wide intrabar ranges.

## Calculation and Mathematical Foundation

**Simplified explanation:**
HL2 calculates the arithmetic mean of the high and low prices, representing the midpoint of each bar's trading range.

**Technical formula:**

```
HL2 = (High + Low) / 2
```

Where:
- High is the highest price reached during the period
- Low is the lowest price reached during the period

> 🔍 **Technical Note:** This calculation is computationally efficient with O(1) complexity, requiring only a single addition and division per bar. The formula is deterministic and requires no historical data, making it suitable for real-time analysis.

## Interpretation Details

HL2 provides several analytical perspectives:

* **Balanced price measure:** Represents the true center of each bar's range, unbiased by opening or closing positions
* **Range visualization:** Shows the midpoint around which price oscillated during each period
* **Smoothing effect:** Creates a naturally smoother price series than close prices, reducing noise
* **Volume-independent:** Unlike VWAP, HL2 is not influenced by volume distribution
* **Support/Resistance:** HL2 often acts as a natural support or resistance level within each bar

## Limitations and Considerations

* **Time-weighted bias:** Gives equal weight to high and low regardless of how long price stayed at those levels
* **Volume ignorance:** Does not account for the volume traded at different price levels
* **Gap sensitivity:** Can show sudden jumps on bars with large gaps between consecutive ranges
* **No trend indication:** Simply represents price position without directional information
* **Extreme sensitivity:** Captures extreme highs and lows that may represent brief spikes rather than sustained levels

## References

* Kaufman, P. J. (2013). Trading Systems and Methods. John Wiley & Sons.
* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
* Achelis, S. B. (2000). Technical Analysis from A to Z. McGraw-Hill.
