# HLC3: Typical Price

[Pine Script Implementation of HLC3](https://github.com/mihakralj/pinescript/blob/main/indicators/numerics/hlc3.pine)

## Naming Convention

**HLC3** is universally known as **Typical Price** in technical analysis. This is the most widely recognized name across all trading platforms and literature:

- **HLC3**: Programming/library notation (High-Low-Close average of 3)
- **Typical Price**: Standard terminology in technical analysis and trading platforms
- **Average Price**: Alternative descriptive name
- **Pivot Price**: Sometimes used in pivot point calculations

## Overview and Purpose

The HLC3 indicator, commonly known as Typical Price, calculates the arithmetic average of the high, low, and close prices for each bar. This widely-used price transformation provides a representative measure of price action by incorporating the trading range extremes along with the final settlement price. The Typical Price is one of the most popular price series transformations in technical analysis, offering a balanced view that considers both where price traded and where it finished.

This measure is extensively used as an input source for volume-based indicators like Money Flow Index and as a foundation for various momentum and trend indicators. By averaging the high, low, and close, HLC3 creates a comprehensive price representation that reduces the impact of any single price extreme while maintaining sensitivity to both range and directional components.

## Core Concepts

* **Three-component balance:** Combines range extremes with closing price for comprehensive representation
* **Typical value:** Represents a "typical" or representative price for each period
* **Volume indicator foundation:** Commonly used in volume-weighted calculations
* **Range and direction:** Captures both trading range breadth and final directional outcome

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| High | high | High price data | Typically not adjusted, uses standard high price |
| Low | low | Low price data | Typically not adjusted, uses standard low price |
| Close | close | Closing price data | Typically not adjusted, uses standard close price |

**Pro Tip:** HLC3 is the standard input for Money Flow Index (MFI) and many volume-based indicators. Use HLC3 when you want a price measure that balances range information with closing bias, making it ideal for indicators that combine price and volume analysis.

## Calculation and Mathematical Foundation

**Simplified explanation:**
HLC3 (Typical Price) calculates the arithmetic mean of three key price points: high, low, and close, providing the most widely-used balanced price measure.

**Technical formula:**

```
HLC3 = (High + Low + Close) / 3
```

Where:
- High is the highest price reached during the period
- Low is the lowest price reached during the period  
- Close is the closing price at the end of the period

> 🔍 **Technical Note:** This is the standard Typical Price calculation used throughout technical analysis literature and trading platforms. The O(1) complexity calculation is both efficient and deterministic, requiring no historical data.

## Interpretation Details

HLC3 provides several analytical perspectives:

* **Representative price:** Provides a balanced "typical" price for each bar that considers both range and outcome
* **Volume weighting:** Commonly paired with volume for weighted price calculations
* **Smoothing effect:** Creates a naturally smoothed price series compared to using close alone
* **Momentum foundation:** Used as base input for many momentum and flow indicators
* **Range sensitivity:** Responds to full trading range while maintaining closing bias

## Limitations and Considerations

* **Closing bias:** Gives equal weight to close despite it representing a single point versus range extremes
* **Opening omission:** Does not consider where the period started
* **Time-weighted bias:** Assumes equal importance of all three prices regardless of actual time distribution
* **Volume independence:** Does not account for volume traded at different price levels
* **Extreme sensitivity:** Includes high and low extremes that may represent brief spikes

## References

* Chaikin, M. (1980s). Development of Money Flow Index using Typical Price.
* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
* Achelis, S. B. (2000). Technical Analysis from A to Z. McGraw-Hill.
* Kaufman, P. J. (2013). Trading Systems and Methods. John Wiley & Sons.
