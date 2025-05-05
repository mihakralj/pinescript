# COINTEGRATION: Engle-Granger Cointegration Test

[Pine Script Implementation of COINTEGRATION](https://github.com/mihakralj/pinescript/blob/main/indicators/statistics/cointegration.pine)

## Overview and Purpose

Cointegration is a statistical property of time series that measures the degree to which two or more series share a common stochastic trend. Unlike correlation, which captures short-term co-movement, cointegration identifies pairs of securities that maintain a long-term equilibrium relationship despite both being non-stationary. This property forms the foundation of pairs trading, relative value strategies, and statistical arbitrage in financial markets by helping identify pairs that are expected to revert to their historical relationship after temporary deviations.

The implementation provided uses the Engle-Granger methodology, which tests for cointegration by examining the residuals from a linear regression between the two series. It calculates the Augmented Dickey-Fuller (ADF) test statistic to evaluate whether these residuals are stationary, which would indicate cointegration. More negative ADF values suggest stronger evidence of cointegration, indicating a more reliable mean-reverting relationship that traders can potentially exploit.

## Core Concepts

* **Long-term equilibrium:** Identifies pairs of securities that maintain a stable relationship over time, despite individual price movements
* **Mean reversion potential:** Provides statistical evidence for whether price divergences are likely to correct back toward a historical relationship
* **Stationarity testing:** Applies rigorous statistical tests to distinguish genuine cointegration from spurious correlations
* **Regression-based approach:** Uses linear regression to establish the relationship and tests residuals for stationarity

Cointegration analysis offers a more robust foundation for pairs trading than simple correlation analysis, as it specifically targets the characteristic that makes such strategies profitable—the tendency of related securities to maintain a long-term equilibrium relationship. By identifying pairs that are truly cointegrated, traders can establish positions with greater confidence that divergences represent temporary market inefficiencies rather than fundamental changes in the relationship.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Period | 20 | Lookback period for regression and ADF test | Longer periods (40-100) for more stable long-term relationships, shorter (10-20) for more responsive signals |
| Source A | High | First time series for cointegration analysis | Typically the security you want to trade |
| Source B | Low | Second time series for cointegration analysis | Typically the hedge or paired security |

**Pro Tip:** Try testing cointegration using logarithmic prices rather than raw prices for certain asset classes like stocks. Log transformation can help stabilize variance and better capture percentage-based relationships, which are often more economically meaningful than absolute price differences.

## Calculation and Mathematical Foundation

**Simplified explanation:**
The Engle-Granger method first estimates the equilibrium relationship between two series using linear regression. It then tests whether the residuals (deviations from this relationship) are stationary using the Augmented Dickey-Fuller test. If the residuals are stationary, the series are considered cointegrated.

**Technical formula:**

1. Run a regression: Series_A = α + β × Series_B + residuals
2. Calculate the ADF test statistic on the residuals:
   - Estimate regression: Δresiduals(t) = γ × residuals(t-1) + error
   - ADF statistic = γ / SE(γ)

Where:
- Δresiduals(t) represents the first difference of residuals
- γ is the coefficient on the lagged residual term
- SE(γ) is the standard error of γ

> 🔍 **Technical Note:** The implementation uses an optimized single-pass algorithm that handles calculations efficiently while maintaining robustness to dirty data. The ADF test formulated here focuses on the lagged level term without additional lagged difference terms, providing a computationally efficient approximation suitable for real-time trading applications.

## Interpretation Details

The cointegration test provides several analytical insights:

* **ADF statistic interpretations:**
  * Values below -3.0: Strong evidence of cointegration (highly significant)
  * Values between -3.0 and -1.95: Moderate evidence of cointegration
  * Values above -1.95: Weak or no evidence of cointegration (not significant)

* **Trading applications:**
  * Entry signals: When cointegrated pairs diverge significantly, enter positions expecting mean reversion
  * Position sizing: More negative ADF values may justify larger position sizes due to higher statistical confidence
  * Stop loss placement: Less cointegrated pairs may require tighter stops due to higher uncertainty in mean reversion
  * Strategy selection: Strongly cointegrated pairs (ADF < -3.5) are candidates for pure statistical arbitrage, while moderately cointegrated pairs may require additional confirmation signals

* **Time-varying analysis:** Track the ADF statistic over time to identify periods when the cointegration relationship strengthens or weakens

## Limitations and Considerations

* **Not all mean-reverting pairs are cointegrated:** Some pairs may exhibit mean-reverting behavior due to factors other than cointegration
* **Regime changes:** Cointegration relationships can break down during market regime shifts or fundamental changes in the securities' relationship
* **Sample size requirements:** Reliable cointegration testing typically requires substantial data history (100+ observations)
* **Lookback period sensitivity:** Results can vary significantly based on the testing period chosen
* **Multiple testing bias:** Testing many pairs increases the chance of finding spurious cointegration relationships by random chance
* **Non-linear relationships:** The Engle-Granger method only tests for linear cointegration and may miss more complex relationships
* **Critical values vary:** Formal hypothesis testing requires comparing the ADF statistic to appropriate critical values based on sample size

## References

* Engle, R. F., & Granger, C. W. J. (1987). Co-integration and error correction: Representation, estimation, and testing. Econometrica, 55(2), 251-276.
* Chan, E. P. (2013). Algorithmic Trading: Winning Strategies and Their Rationale. John Wiley & Sons.
* Alexander, C. (2001). Market Models: A Guide to Financial Data Analysis. John Wiley & Sons.
* Vidyamurthy, G. (2004). Pairs Trading: Quantitative Methods and Analysis. John Wiley & Sons.
