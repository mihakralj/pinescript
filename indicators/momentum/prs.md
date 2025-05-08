# PRS: Price Relative Strength

[Pine Script Implementation of PRS](https://github.com/mihakralj/pinescript/blob/main/indicators/momentum/prs.pine)

## Overview and Purpose

The Price Relative Strength (PRS) indicator measures the relative performance between two assets by calculating their price ratio. This helps identify which asset is outperforming or underperforming relative to the other. Unlike RSI which measures a single asset's momentum, PRS compares two different assets or securities.

This implementation provides options for smoothing, normalization, and logarithmic scaling to enhance analysis capabilities.

## Core Concepts

* **Ratio-Based:** Shows direct price relationship between assets
* **Relative Performance:** Identifies outperformance/underperformance
* **Trend Following:** Reveals strength of relative trends
* **Cross-Asset Analysis:** Enables comparison across different assets

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Base Asset | close | Primary asset to compare | Your main trading instrument |
| Compare Asset | SPY | Secondary asset for comparison | Benchmark or related asset |
| Smoothing Length | 1 | EMA period for ratio smoothing | Higher for less noise |
| Normalize | false | Convert to percentage change | Enable for easier interpretation |
| Log Scale | false | Use logarithmic scaling | Enable for large value ranges |

**Pro Tip:** Common applications:
- Stock vs Index: Compare stock performance to market
- Currency Pairs: Compare relative currency strength
- Sector Analysis: Compare stock to sector ETF
- Cross-Market: Compare related markets (e.g., Gold vs Silver)

## Calculation and Mathematical Foundation

**Simplified explanation:**
PRS calculates the ratio between two price series and optionally applies smoothing.

**Technical formula:**
1. Calculate Basic Ratio:
   ```
   Ratio = Base_Price / Compare_Price
   ```

2. Optional Normalization:
   ```
   Normalized = 100 * Ratio / Previous_Ratio
   ```

3. Optional Smoothing:
   ```
   Smoothed = EMA(Ratio, smoothing_length)
   ```

4. Optional Log Scale:
   ```
   LogRatio = log(Ratio)
   ```

> 🔍 **Technical Note:** The ratio calculation provides a direct measure of relative performance, while normalization and log scaling help manage different price scales and ranges.

## Interpretation Details

PRS provides multiple analytical perspectives:

* **Basic Ratio:**
  - Rising: Base asset outperforming
  - Falling: Compare asset outperforming
  - Flat: Equal performance

* **Trend Analysis:**
  - Above 1 (or 100): Base asset stronger
  - Below 1 (or 100): Compare asset stronger
  - Slope indicates trend strength

* **Divergence Patterns:**
  - Bullish: Price lower, PRS higher
  - Bearish: Price higher, PRS lower
  - Most effective at extremes

* **Crossover Signals:**
  - Cross above 1: Base asset taking lead
  - Cross below 1: Compare asset taking lead
  - Smoothed line crossovers

## Advantages

1. **Comparison Benefits:**
   - Direct performance comparison
   - Cross-asset analysis
   - Sector rotation insights
   - Portfolio analysis

2. **Trading Applications:**
   - Pair trading signals
   - Relative strength analysis
   - Market rotation timing
   - Portfolio rebalancing

3. **Technical Benefits:**
   - Multiple scaling options
   - Smoothing capability
   - Clear visual signals
   - Flexible comparison

## Limitations and Considerations

* **Scale Differences:** Large price differences can affect visualization
* **Correlation Required:** Assets should have some relationship
* **Market Conditions:** Less useful in non-correlated pairs
* **Time Horizon:** Different timeframes may need different settings
* **Data Availability:** Both assets must have price data

## References

* Kirkpatrick, C. D., & Dahlquist, J. R. (2010). Technical Analysis: The Complete Resource for Financial Market Technicians. FT Press.
* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
* Kaufman, P. J. (2013). Trading Systems and Methods (5th ed.). Wiley Trading.
