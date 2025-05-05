# Kurtosis: Distribution Shape Measure

[Pine Script Implementation of Kurtosis](https://github.com/mihakralj/pinescript/blob/main/indicators/statistics/kurtosis.pine)

## Overview and Purpose

Kurtosis is a statistical measure that quantifies the shape or "tailedness" of a probability distribution relative to a normal distribution. In financial markets, kurtosis helps traders assess the frequency and magnitude of outlier events in price movement. A high kurtosis indicates a distribution with heavier tails and a sharper peak, suggesting more frequent extreme price movements than would be expected in a normal distribution.

This indicator helps traders understand the nature of volatility in an asset, distinguishing between markets with steady, predictable movements versus those prone to sudden, extreme price jumps. By measuring the fourth moment of a distribution, kurtosis provides insights into risk characteristics that aren't captured by simpler measures like standard deviation.

## Core Concepts

* **Tail Risk Assessment:** Measures the likelihood of outlier events or "black swans" in price data
* **Distribution Shape Analysis:** Quantifies whether price movements follow normal patterns or exhibit more extreme behavior
* **Risk Profiling:** Helps identify assets with hidden risks that may not be apparent from traditional volatility measures
* **Statistical Anomaly Detection:** Highlights periods when market behavior deviates significantly from historical patterns

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
| :-------- | :------ | :------- | :------------ |
| Period | 14 | Controls the lookback window for calculation | Shorter periods (8-10) capture recent distribution changes, longer periods (30+) reveal persistent statistical properties |
| Source | Close | Data point used for calculation | Change to returns (close/close[1]-1) for more traditional financial kurtosis analysis |

**Pro Tip:** Monitor changes in kurtosis rather than absolute values - a sudden increase may signal a fundamental change in market dynamics and increased tail risk.

## Calculation and Mathematical Foundation

**Simplified explanation:**
Kurtosis measures how much of a distribution's variance comes from infrequent extreme deviations, as opposed to frequent moderate deviations. It quantifies the "peakedness" of a distribution and the weight of its tails relative to a normal distribution.

**Technical formula:**
Excess Kurtosis = [n × Σ(x-μ)⁴/(σ⁴)] - 3

Where:

* n is the number of data points (period)
* x represents the source values
* μ is the mean of the source values
* σ is the standard deviation
* The subtraction of 3 makes this excess kurtosis (0 for normal distribution)

> 🔍 **Technical Note:** The Pine Script implementation efficiently calculates kurtosis by tracking the first four moments of the distribution using dynamic arrays. The algorithm uses a rolling window approach, adding new values and removing old ones in O(1) time, making it computationally efficient even for large lookback periods.

## Interpretation Details

Kurtosis provides unique insights into market behavior:

* **Positive Values (Leptokurtic):** Indicate a distribution with heavy tails - more frequent outliers than expected in normal markets
* **Near Zero (Mesokurtic):** Suggests price movements approximate a normal distribution
* **Negative Values (Platykurtic):** Reveal a distribution with light tails - fewer extreme moves than expected
* **Trend Analysis:** Rising kurtosis during a trend suggests increasing risk of sharp reversals
* **Market Regime Detection:** Significant changes in kurtosis often precede shifts in volatility regimes

## Limitations and Considerations

* **Sample Size Requirements:** Requires sufficient data (minimum 4 bars, preferably more) to produce statistically meaningful results
* **Interpretation Complexity:** Less intuitive than simpler indicators like standard deviation or average true range
* **Delayed Signals:** Major changes in kurtosis often appear only after significant market events have occurred
* **Sensitivity to Outliers:** A single extreme value can dramatically impact kurtosis readings
* **Mathematical Limitations:** As a fourth-order moment, it amplifies measurement errors and noise
* **Context Dependency:** Should be interpreted alongside other measures like skewness and standard deviation

## References

* Mandelbrot, B. (1963). The Variation of Certain Speculative Prices. The Journal of Business, 36(4), 394-419.
* Cont, R. (2001). Empirical Properties of Asset Returns: Stylized Facts and Statistical Issues. Quantitative Finance, 1, 223-236.
