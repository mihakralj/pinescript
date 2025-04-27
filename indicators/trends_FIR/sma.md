# SMA: Simple Moving Average

[Pine Script Implementation of SMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_FIR/sma.pine)

## Overview and Purpose

The Simple Moving Average (SMA) is one of the most fundamental and widely used technical indicators in financial analysis. It calculates the arithmetic mean of a selected range of prices over a specified number of periods. Developed in the early days of technical analysis, the SMA provides traders with a straightforward method to identify trends by smoothing price data and filtering out short-term fluctuations. Due to its simplicity and effectiveness, it remains a cornerstone indicator that forms the basis for numerous other technical analysis tools.

## Core Concepts

* **Equal weighting:** SMA gives equal importance to each price point in the calculation period, unlike weighted averages that emphasize certain data points
* **Noise reduction:** Smooths price fluctuations to help identify the underlying trend direction
* **Timeframe flexibility:** Effective across all timeframes, with shorter periods for short-term analysis and longer periods for identifying major trends

The core principle of SMA is its unbiased approach to price data. By treating all prices within the lookback period with equal importance, SMA creates a balanced view of recent market activity. This equal weighting makes the SMA particularly intuitive to understand, as it simply represents the average price over the specified time period.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 20 | Controls the lookback period | Increase for smoother signals in volatile markets, decrease for responsiveness |
| Source | close | Price data used for calculation | Consider using hlc3 for a more balanced price representation |

**Pro Tip:** For trend following strategies, consider using two SMAs with different periods (e.g., 50 and 200) – crossovers between these can identify significant trend changes while filtering out minor fluctuations.

## Calculation and Mathematical Foundation

**Simplified explanation:**
SMA adds up the prices for a specific number of periods and divides by that number. For example, a 10-period SMA adds the last 10 closing prices and divides by 10 to find the average.

**Technical formula:**
The standard calculation: SMA = (P₁ + P₂ + ... + Pₙ) / n

An optimized recursive calculation:
SMA₍ₙ₎ = SMA₍ₙ₋₁₎ + (Pₙ - Pₙ₋ₚ) / p

Where:
- P₁, P₂, ..., Pₙ are price values in the lookback window
- n is the period length
- p is the period

> 🔍 **Technical Note:** The SMA has a precisely defined lag of (n-1)/2 periods, meaning a 21-period SMA lags behind price by 10 bars. This consistent, deterministic lag makes its behavior predictable across all market conditions.

## Interpretation Details

SMA can be used in various trading strategies:

* **Trend identification:** The direction of SMA indicates the prevailing trend
* **Signal generation:** Crossovers between price and SMA generate basic trade signals
* **Support/resistance levels:** SMA can act as dynamic support during uptrends and resistance during downtrends
* **Multiple timeframe analysis:** Using SMAs with different periods can confirm trends across different timeframes
* **Moving average crossovers:** When a shorter-period SMA crosses above a longer-period SMA, it signals a potential uptrend (and vice versa)

## Limitations and Considerations

* **Market conditions:** Less effective in choppy, sideways markets where price oscillates around the average
* **Lag factor:** Significant lag in responding to rapid price changes means SMA will always be late to signal reversals
* **Equal weighting:** Treats recent and older prices equally, which may not reflect current market dynamics
* **Sudden changes:** When a price point leaves the calculation window, it can cause abrupt changes in the SMA
* **Complementary tools:** Best used with momentum oscillators, volume indicators, or other trend confirmation tools

## References

* Edwards, Robert D. and Magee, John. "Technical Analysis of Stock Trends." CRC Press, 2007
* Murphy, John J. "Technical Analysis of the Financial Markets." New York Institute of Finance, 1999
