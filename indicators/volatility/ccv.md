# CCV: Close-to-Close Volatility

[Pine Script Implementation of CCV](https://github.com/mihakralj/pinescript/blob/main/indicators/volatility/ccv.pine)

## Overview and Purpose

Close-to-Close Volatility (CCV) is a statistical measure that quantifies market volatility based on the logarithmic returns between consecutive closing prices. Unlike range-based volatility indicators such as Average True Range (ATR), CCV focuses exclusively on closing prices, making it particularly valuable for assessing the volatility of daily, weekly, or monthly returns—similar to how volatility is measured in academic finance and risk management. The indicator is annualized to provide a standardized volatility metric that can be directly compared across different securities and timeframes.

The implementation provided offers multiple averaging methods (SMA, EMA, WMA) and uses circular buffers for efficient computation, ensuring consistent performance regardless of the lookback period. By calculating the standard deviation of logarithmic returns and annualizing the result, CCV gives traders and investors a real-world volatility estimate that translates directly to expected annual percentage movement, providing an objective framework for position sizing, option pricing, and risk assessment.

## Core Concepts

* **Logarithmic returns:** Uses log(close/close[1]) to measure price changes, providing better statistical properties than simple percentage returns
* **Return variability:** Measures the dispersion of returns around their mean, quantifying the "noise" in price movements
* **Annualization:** Scales the volatility measurement to represent expected annual variation (multiplies by √252 for daily data)
* **Multiple averaging methods:** Offers simple, exponential, and weighted moving averages for different smoothing preferences

CCV stands apart from other volatility indicators by following the classic definition of volatility used in financial theory: the standard deviation of logarithmic returns. This approach allows for direct application in various financial models, including option pricing, Value at Risk (VaR) calculations, and portfolio optimization. The annualized format makes the numbers immediately meaningful—a CCV of 0.20 (or 20%) suggests that prices are expected to fluctuate within a ±20% range over the next year with approximately 68% confidence (one standard deviation).

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 20 | Number of periods for volatility calculation | Shorter for more responsive readings; longer for more stable, trend-focused analysis |
| Method | SMA (1) | Averaging method: SMA (1), EMA (2), or WMA (3) | SMA for equal weighting; EMA for recency bias; WMA for graduated weighting |

**Pro Tip:** Compare CCV against its own historical values rather than absolute levels. A security's "normal" volatility can vary significantly, so identifying when current volatility is high or low relative to its own recent history often provides more actionable insights than comparing against fixed thresholds.

## Calculation and Mathematical Foundation

**Simplified explanation:**
CCV calculates the logarithmic return between consecutive closing prices, computes the standard deviation of these returns over the specified period, and then annualizes the result by multiplying by the square root of 252 (the approximate number of trading days in a year).

**Technical formula:**

1. Calculate logarithmic returns: r_t = ln(close_t / close_{t-1})

2. Compute the standard deviation of returns:
   σ = √[Σ(r_t - r̄)² / n]
   Where:
   - r̄ is the mean of the returns over the period
   - n is the number of observations

3. Annualize the volatility:
   CCV = σ × √252

> 🔍 **Technical Note:** The implementation uses circular buffers for efficient storage and calculation of returns, maintaining O(1) computational complexity regardless of the lookback period. For mean calculation, it maintains a running sum rather than recalculating the entire sum for each bar. The annualization factor of √252 assumes daily data; different timeframes would require different annualization factors (e.g., √52 for weekly data, √12 for monthly).

## Interpretation Details

CCV provides several analytical perspectives:

* **Absolute volatility levels:** Higher CCV values indicate more volatile market conditions with wider expected price swings
* **Volatility regimes:** CCV can help identify shifts between high and low volatility periods (volatility clustering)
* **Risk assessment:** Directly usable for calculating Value at Risk (VaR) or setting position sizes
* **Option pricing input:** Can serve as a volatility input for Black-Scholes or other option pricing models
* **Mean reversion potential:** Extreme CCV readings (historically high or low) often precede mean reversion in volatility
* **Trend strength assessment:** Declining volatility during price advances often indicates healthy trends
* **Pre-event analysis:** Rising CCV ahead of known events (earnings, economic releases) can indicate market uncertainty

## Limitations and Considerations

* **Close-only focus:** Ignores intraday price movements, potentially underestimating true volatility during turbulent markets
* **Lag component:** As a statistical measure based on past returns, CCV is inherently backward-looking
* **Return distribution assumptions:** Standard deviation assumes normally distributed returns, which is often not the case in financial markets
* **Timeframe dependency:** CCV values will differ across timeframes, requiring appropriate annualization factors
* **Gap handling:** Large gaps between closing prices can create temporary spikes in the indicator
* **Mean sensitivity:** The standard deviation calculation is sensitive to outliers, potentially skewing results
* **Parameter dependence:** Results can vary significantly based on length parameter and averaging method
* **Annualization accuracy:** The √252 factor assumes continuous trading days; adjustments may be needed for less liquid markets

## References

* Hull, J. C. (2017). Options, Futures, and Other Derivatives (10th ed.). Pearson.
* Alexander, C. (2008). Market Risk Analysis, Volume II: Practical Financial Econometrics. Wiley.
* Sinclair, E. (2013). Volatility Trading (2nd ed.). John Wiley & Sons.
* Poon, S. H., & Granger, C. W. (2003). Forecasting Volatility in Financial Markets: A Review. Journal of Economic Literature, 41(2), 478-539.
