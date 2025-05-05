# ENTROPY: Shannon Information Entropy

[Pine Script Implementation of ENTROPY](https://github.com/mihakralj/pinescript/blob/main/indicators/statistics/entropy.pine)

## Overview and Purpose

Shannon Entropy is a fundamental concept in information theory that quantifies the amount of uncertainty or randomness in a data series. In financial markets, entropy serves as a powerful complexity measure that helps traders identify periods of order versus disorder, potentially signaling regime changes or upcoming volatility shifts. Unlike momentum oscillators that focus on directional movement, entropy objectively measures the information content and predictability within price action.

The implementation provided uses an optimized algorithm that normalizes entropy to a 0-1 range, making it intuitive to interpret across different securities and timeframes. High entropy values indicate disorganized, random market behavior with many possible states (high uncertainty), while low entropy suggests more predictable, structured price action with fewer states (higher certainty).

## Core Concepts

* **Information content:** Measures the average unpredictability of price movements, helping identify random versus structured markets
* **Normalized range:** Values between 0 (complete order/predictability) and 1 (maximum randomness/unpredictability)
* **Regime detection:** Identifies transitions between ordered and chaotic market states
* **Non-directional indicator:** Focuses on complexity and structure rather than bullish/bearish bias

Entropy serves as a versatile tool for quantifying market randomness, offering insights complementary to traditional technical indicators. By measuring the distribution of price changes rather than their direction or magnitude, it provides a unique perspective on market conditions that can be valuable for timing trades, adjusting risk exposure, and detecting changes in market dynamics.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 14 | Lookback period for entropy calculation | Shorter for more sensitivity to recent changes, longer for more stable readings |
| Source | Close | Price data used for entropy calculation | Can be modified to analyze different aspects of price action |
| Bins | Auto (Min 2, Max 100) | Number of divisions for probability distribution | Automatically scaled based on data points available; rarely needs manual adjustment |

**Pro Tip:** Try comparing entropy across multiple timeframes. When entropy is high on shorter timeframes but low on longer ones, it often indicates temporary market noise within a structured larger trend—potentially offering strategic mean-reversion opportunities.

## Calculation and Mathematical Foundation

**Simplified explanation:**
Entropy divides the price range into multiple bins (categories), calculates the probability of values falling into each bin, and then measures the information content of this probability distribution. More uniform distributions (many equally likely states) have higher entropy than concentrated distributions (few dominant states).

**Technical formula:**

Shannon Entropy = -∑(p(x) * log(p(x)))

Where:
- p(x) is the probability of a price falling in bin x
- The sum is over all bins with non-zero probability
- The result is normalized by dividing by log(number of bins)

> 🔍 **Technical Note:** The implementation dynamically adjusts the number of bins based on available data points, providing optimal resolution of the probability distribution. It uses a single-pass algorithm for performance efficiency and handles missing data gracefully through proper normalization.

## Interpretation Details

Entropy provides several analytical insights:

* **High entropy (0.8-1.0):** Indicates chaotic, random market conditions with low predictability—often associated with range-bound markets, high volatility, or transitional periods
* **Medium entropy (0.4-0.8):** Suggests balanced market conditions with moderate predictability—typically seen during normal trading with mixed signals
* **Low entropy (0.0-0.4):** Signals ordered, predictable market behavior—often correlates with strong trends or accumulation/distribution phases
* **Increasing entropy:** May indicate a breakdown of existing market structure or an upcoming volatility expansion
* **Decreasing entropy:** Suggests emerging order or consolidation, potentially preceding a new trend
* **Entropy divergence:** When price makes new extremes but entropy doesn't confirm, it may signal unsustainable price action

## Limitations and Considerations

* **Lagging nature:** Like all statistical measures, entropy describes past conditions and may lag significant market changes
* **Normalization effects:** The 0-1 normalization makes cross-security comparison possible but may obscure some internal dynamics
* **Bin sensitivity:** Results can be influenced by the number of bins used, though the adaptive bin sizing helps mitigate this
* **Complementary tool:** Works best when combined with directional indicators, as entropy itself is direction-agnostic
* **Timeframe dependency:** Different timeframes may show different entropy characteristics for the same security
* **Warm-up period:** Requires a full lookback period of data before producing meaningful results

## References

* Shannon, C. E. (1948). A Mathematical Theory of Communication. Bell System Technical Journal, 27, 379-423.
* Pincus, S. M. (1991). Approximate entropy as a measure of system complexity. Proceedings of the National Academy of Sciences, 88(6), 2297-2301.
* Gençay, R., & Gradojevic, N. (2010). Crash of '87—Was it Expected? Aggregate Market Fears and Long-Range Dependence. Journal of Empirical Finance, 17(2), 270-282.
* Philippatos, G. C., & Wilson, C. J. (1972). Entropy, market risk, and the selection of efficient portfolios. Applied Economics, 4(3), 209-220.
