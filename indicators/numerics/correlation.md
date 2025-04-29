# CORRELATION: Pearson's Correlation Coefficient

[Pine Script Implementation of CORRELATION](https://github.com/mihakralj/pinescript/blob/main/indicators/numerics/correlation.pine)

## Overview and Purpose

The Pearson's Correlation Coefficient is a statistical measure that quantifies the linear relationship between two variables. In financial markets, correlation analysis helps traders understand how different securities, price components, or indicators move in relation to each other. The coefficient ranges from -1 to +1, with +1 indicating a perfect positive correlation (variables move in lockstep), -1 indicating a perfect negative correlation (variables move in opposite directions), and 0 indicating no linear relationship.

The implementation provided uses an efficient single-pass algorithm with circular buffers that maintains O(1) computational complexity regardless of the lookback period. This optimized approach makes it suitable for real-time trading applications where performance is critical, even with large datasets or when analyzing multiple correlation pairs simultaneously.

## Core Concepts

* **Relationship strength:** Measures how strongly two data series are related, with values closer to +/-1 indicating stronger relationships
* **Directionality:** Indicates whether variables move in the same direction (positive correlation) or opposite directions (negative correlation)
* **Linear dependency:** Focuses specifically on linear relationships between variables, serving as the foundation for more complex statistical analyses
* **Normalized measurement:** Unlike covariance, correlation is normalized to the range [-1, +1], making it easier to interpret and compare relationships across different data pairs

Correlation analysis forms the basis for many trading strategies, including pairs trading, portfolio diversification, and market regime identification. By understanding which assets move together or in opposition, traders can construct more robust portfolios and identify potential trading opportunities arising from temporary deviations in established relationships.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Period | 14 | Lookback period for calculation | Shorter for more sensitivity to recent changes, longer for more stable long-term relationship assessment |
| Source 1 | High | First data series to analyze | Adjust based on which relationship you want to examine |
| Source 2 | Low | Second data series to analyze | Adjust based on which relationship you want to examine |

**Pro Tip:** Try analyzing correlation between an asset and its sector index over multiple timeframes. When correlation breaks down on shorter timeframes but remains intact on longer timeframes, it often signals a temporary deviation that may present mean-reversion opportunities.

## Calculation and Mathematical Foundation

**Simplified explanation:**
Correlation measures how much two variables change together relative to how much they change individually. It calculates the covariance between the variables and then normalizes this value by dividing by the product of their standard deviations.

**Technical formula:**

Correlation(X, Y) = Covariance(X, Y) / (σₓ × σᵧ)

Where:
- Covariance(X, Y) is the covariance between X and Y
- σₓ is the standard deviation of X
- σᵧ is the standard deviation of Y

> 🔍 **Technical Note:** The implementation uses a computationally efficient combined calculation of covariance and variances in a single pass through the data. It maintains circular buffers to efficiently track values within the lookback window, handling NA values gracefully and preventing memory leaks regardless of how long the script runs.

## Interpretation Details

Correlation provides several analytical insights:

* **Strong positive correlation (0.7 to 1.0):** Assets tend to move in the same direction with similar magnitudes; useful for confirming trends or identifying potential substitutes
* **Moderate positive correlation (0.3 to 0.7):** Assets generally move in the same direction but with less consistency
* **Weak or no correlation (-0.3 to 0.3):** Little to no reliable relationship between assets; useful for diversification
* **Moderate negative correlation (-0.7 to -0.3):** Assets tend to move in opposite directions with some consistency
* **Strong negative correlation (-1.0 to -0.7):** Assets consistently move in opposite directions; valuable for hedging strategies
* **Correlation changes:** Shifts in established correlation patterns often signal changing market regimes or potential trading opportunities
* **Rolling correlation analysis:** Evaluating how correlation evolves over time provides insight into the stability of relationships

## Limitations and Considerations

* **Linear relationship focus:** Only measures linear relationships, missing more complex nonlinear dependencies
* **Outlier sensitivity:** Can be disproportionately influenced by extreme values
* **Causation disclaimer:** Correlation does not imply causation; two variables may move together without directly influencing each other
* **Time-varying nature:** Correlations between assets are not static and can change significantly during different market conditions
* **Timeframe dependency:** Correlations often vary across different timeframes (e.g., daily vs. monthly)
* **Sample size requirements:** Requires a sufficient number of data points to produce statistically reliable results
* **Mean reversion assumptions:** Strategies based on correlation often assume relationships will revert to historical norms, which isn't always true

## References

* Pearson, K. (1895). Notes on regression and inheritance in the case of two parents. Proceedings of the Royal Society of London, 58, 240-242.
* Markowitz, H. (1952). Portfolio Selection. The Journal of Finance, 7(1), 77-91.
* Vidyamurthy, G. (2004). Pairs Trading: Quantitative Methods and Analysis. John Wiley & Sons.
* Lo, A. W. (2001). Risk Management for Hedge Funds: Introduction and Overview. Financial Analysts Journal, 57(6), 16-33.
