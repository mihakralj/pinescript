# WMA: Weighted Moving Average

[Pine Script Implementation of WMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_FIR/wma.pine)

## Overview and Purpose

The Weighted Moving Average (WMA) is a technical indicator that applies progressively increasing weights to more recent price data. Emerging in the early 1950s during the formative years of technical analysis, WMA gained significant adoption among professional traders through the 1970s as computational methods became more accessible. The approach was formalized in Robert Colby's 1988 "Encyclopedia of Technical Market Indicators," establishing it as a staple in technical analysis software. Unlike the Simple Moving Average (SMA) which gives equal weight to all prices, WMA assigns greater importance to recent prices, creating a more responsive indicator that reacts faster to price changes while still providing effective noise filtering.

## Core Concepts

* **Linear weighting:** WMA applies progressively increasing weights to more recent price data, creating a recency bias that improves responsiveness
* **Market application:** Particularly effective for identifying trend changes earlier than SMA while maintaining better noise filtering than faster-responding averages like EMA
* **Timeframe flexibility:** Works effectively across all timeframes, with appropriate period adjustments for different trading horizons

The core innovation of WMA is its linear weighting scheme, which strikes a balance between the equal-weight approach of SMA and the exponential decay of EMA. This creates an intuitive and effective compromise that prioritizes recent data while maintaining a finite lookback period, making it particularly valuable for traders seeking to reduce lag without excessive sensitivity to price fluctuations.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 14 | Controls the lookback period | Increase for smoother signals in volatile markets, decrease for responsiveness |
| Source | close | Price data used for calculation | Consider using hlc3 for a more balanced price representation |

**Pro Tip:** For most trading applications, using a WMA with period N provides better responsiveness than an SMA with the same period, while generating fewer whipsaws than an EMA with comparable responsiveness.

## Calculation and Mathematical Foundation

**Simplified explanation:**
WMA calculates a weighted average of prices where the most recent price receives the highest weight, and each progressively older price receives one unit less weight. For example, in a 5-period WMA, the most recent price gets a weight of 5, the next most recent a weight of 4, and so on, with the oldest price getting a weight of 1.

**Technical formula:**
WMA = (P₁ × w₁ + P₂ × w₂ + ... + Pₙ × wₙ) / (w₁ + w₂ + ... + wₙ)

Where:
- Linear weights: most recent value has weight = n, second most recent has weight = n-1, etc.
- The sum of weights for a period n is calculated as: n(n+1)/2
- For example, for a 5-period WMA, the sum of weights is 5(5+1)/2 = 15

> 🔍 **Technical Note:** Unlike EMA which theoretically considers all historical data (with diminishing influence), WMA has a finite memory, completely dropping prices that fall outside its lookback window. This creates a cleaner break from outdated market conditions.

## Interpretation Details

WMA can be used in various trading strategies:

* **Trend identification:** The direction of WMA indicates the prevailing trend with greater responsiveness than SMA
* **Signal generation:** Crossovers between price and WMA generate trade signals earlier than with SMA
* **Support/resistance levels:** WMA can act as dynamic support during uptrends and resistance during downtrends
* **Moving average crossovers:** When a shorter-period WMA crosses above a longer-period WMA, it signals a potential uptrend (and vice versa)
* **Trend strength assessment:** Distance between price and WMA can indicate trend strength

## Limitations and Considerations

* **Market conditions:** Still suboptimal in highly volatile or sideways markets where enhanced responsiveness may generate false signals
* **Lag factor:** While less than SMA, still introduces some lag in signal generation
* **Abrupt window exit:** The oldest price suddenly drops out of calculation when leaving the window, potentially causing small jumps
* **Step changes:** Linear weighting creates discrete steps in influence rather than a smooth decay
* **Complementary tools:** Best used with volume indicators and momentum oscillators for confirmation

## References

* Colby, Robert W. "The Encyclopedia of Technical Market Indicators." McGraw-Hill, 2002
* Murphy, John J. "Technical Analysis of the Financial Markets." New York Institute of Finance, 1999
* Kaufman, Perry J. "Trading Systems and Methods." Wiley, 2013
