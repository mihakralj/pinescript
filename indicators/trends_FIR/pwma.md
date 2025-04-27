# PWMA: Pascal Weighted Moving Average

[Pine Script Implementation of PWMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_FIR/pwma.pine)

## Overview and Purpose

The Pascal Weighted Moving Average (PWMA) is a technical indicator that applies binomial coefficients from Pascal's triangle as a weighting scheme for price data. Developed in the early 2000s as mathematicians explored natural weighting schemes for financial time series, PWMA emerged from research into binomial distributions and their applications to market data. The indicator uses the mathematical properties of Pascal's triangle to create a bell-shaped weighting distribution that emphasizes central price points while naturally tapering weight toward both older and more recent data points, creating an effective filter with excellent noise reduction properties.

## Core Concepts

* **Binomial coefficient weighting:** PWMA uses Pascal's triangle to assign weights to price points, providing a mathematically optimal weighting scheme
* **Bell-shaped distribution:** The natural distribution of binomial coefficients creates a symmetrical bell-shaped curve that emphasizes central price data
* **Timeframe flexibility:** Works effectively across all timeframes with appropriate period adjustments

The core innovation of PWMA is its application of the binomial theorem to create a weight distribution that follows natural statistical principles. Unlike simple or linear weighted moving averages, PWMA's weighting scheme based on Pascal's triangle creates a symmetrical bell-shaped curve that provides balanced emphasis on central data points with perfect symmetry for zero phase distortion.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 14 | Controls the lookback period | Increase for smoother signals in volatile markets, decrease for responsiveness |
| Source | close | Price data used for calculation | Consider using hlc3 for a more balanced price representation |

**Pro Tip:** When using PWMA for trend identification, consider using even numbers for the length parameter, as this creates a perfectly symmetrical weighting distribution with no single central point.

## Calculation and Mathematical Foundation

**Simplified explanation:**
PWMA calculates a weighted average of prices where the weights follow the same pattern as the numbers in Pascal's triangle. This creates a bell-shaped weighting scheme that gives most importance to prices in the middle of the lookback period and gradually less importance to prices at the beginning and end of the period.

**Technical formula:**
PWMA = Σ(Price[i] × C(n-1,i)) / Σ(C(n-1,i))

Where:
- C(n-1,i) is the binomial coefficient "n-1 choose i" 
- n is the period length
- The binomial coefficient represents the number of ways to choose i items from n-1 items

> 🔍 **Technical Note:** For computational stability, especially with larger period values, the implementation uses a recurrence relation to calculate binomial coefficients: C(n,k) = C(n,k-1) × (n-k+1) / k, rather than using the factorial formula which can cause overflow issues.

## Interpretation Details

PWMA can be used in various trading strategies:

* **Trend identification:** The direction of PWMA indicates the prevailing trend
* **Signal generation:** Crossovers between price and PWMA generate trade signals
* **Support/resistance levels:** PWMA can act as dynamic support during uptrends and resistance during downtrends
* **Trend strength assessment:** Distance between price and PWMA can indicate trend strength
* **Noise filtering:** Using PWMA to filter noisy price data before applying other indicators

## Limitations and Considerations

* **Market conditions:** Like all moving averages, less effective in choppy, sideways markets
* **Computational complexity:** Requires calculation of binomial coefficients, which is more complex than simpler averaging methods
* **Fixed weighting scheme:** Cannot adapt to changing market conditions like adaptive moving averages
* **Moderate lag:** While balanced, still introduces some lag during rapid price movements
* **Complementary tools:** Best used with momentum oscillators or volume indicators for confirmation

## References

* Kaufman, P.J. "Trading Systems and Methods." Wiley, 2013
* Mulloy, P. "Smoothing Techniques for More Accurate Signals." Technical Analysis of Stocks & Commodities, 1994
