# BETA: Beta Coefficient

[Pine Script Implementation of BETA](https://github.com/mihakralj/pinescript/blob/main/indicators/statistics/beta.pine)

## Overview and Purpose

The Beta coefficient is a crucial risk measurement tool in financial analysis that quantifies the volatility or systematic risk of an individual security or portfolio in comparison to the market as a whole. Originally derived from the Capital Asset Pricing Model (CAPM), Beta measures how sensitive an asset's returns are to movements in the benchmark (typically a market index like the S&P 500). Unlike correlation which is limited to a -1 to +1 range, Beta's magnitude provides valuable insight into relative volatility, making it essential for portfolio construction, risk management, and performance attribution.

The implementation provided uses an optimized algorithm that efficiently calculates returns and their covariance, maintaining computational stability even with extended lookback periods. This makes it particularly useful for real-time trading applications where performance matters.

## Core Concepts

* **Relative volatility:** Quantifies how much an asset's price moves in relation to a benchmark, with values above 1 indicating higher volatility than the benchmark and values below 1 indicating lower volatility
* **Directional risk:** Not only measures magnitude but also direction of risk, with positive Beta indicating the asset tends to move in the same direction as the benchmark and negative Beta indicating opposite movement
* **Systematic risk assessment:** Isolates market risk (systematic) from security-specific risk (unsystematic), helping traders distinguish between diversifiable and non-diversifiable risk
* **Performance benchmark:** Serves as a foundation for evaluating risk-adjusted returns and asset allocation decisions

Beta forms the cornerstone of modern portfolio theory and risk analysis, helping traders identify assets that can either amplify returns during bull markets (high Beta) or provide defensive positions during market downturns (low Beta). The indicator's ability to quantify market sensitivity makes it invaluable for building diversified portfolios with specific risk characteristics.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Period | 14 | Lookback period for return calculation | Shorter for more sensitivity to recent market changes, longer for more stable long-term risk assessment |
| Source 1 | Close | Price data for the security being analyzed | Rarely needs adjustment unless analyzing specific price components |
| Source 2 | Benchmark | Price data for the benchmark (typically market index) | Change to compare against different benchmarks based on your trading strategy |

**Pro Tip:** For pairs trading strategies, try calculating Beta between correlated securities rather than against a broad market index. A significant change in their historical Beta relationship can signal potential mean reversion opportunities.

## Calculation and Mathematical Foundation

**Simplified explanation:**
Beta calculates the relationship between an asset's returns and a benchmark's returns. It divides the covariance of these returns by the variance of the benchmark returns, essentially measuring how much the asset moves for each unit of benchmark movement.

**Technical formula:**

Beta = Covariance(Asset Returns, Benchmark Returns) / Variance(Benchmark Returns)

Where:

* Returns are calculated as (Current Price - Previous Price) / Previous Price
* Covariance measures how the two return series move together
* Variance measures the dispersion of benchmark returns around their mean

> 🔍 **Technical Note:** The implementation uses efficient array-based circular buffers to track returns without growing memory usage over time. It handles missing data gracefully and includes safeguards against division by zero when benchmark variance is negligible, ensuring stability even in unusual market conditions.

## Interpretation Details

Beta provides several analytical perspectives:

* **Beta = 1:** The security moves in tandem with the market (same volatility)
* **Beta > 1:** The security is more volatile than the market (amplified movements)
* **Beta < 1 (but positive):** The security is less volatile than the market (dampened movements)
* **Beta = 0:** The security's movements have no relation to market movements
* **Beta < 0:** The security tends to move in the opposite direction of the market (rare)
* **Magnitude assessment:** A Beta of 2 means the security typically moves twice as much as the benchmark in the same direction
* **Risk evaluation:** Higher Beta typically suggests higher potential returns but with increased downside risk
* **Sector analysis:** Comparing Betas across sector peers can identify relative defensive or aggressive positions

## Limitations and Considerations

* **Past performance disclaimer:** Beta is calculated from historical data and may not predict future relationships
* **Benchmark relevance:** The calculated Beta is only meaningful if the chosen benchmark is relevant to the security being analyzed
* **Non-linear relationships:** Beta assumes a linear relationship between asset and benchmark returns, which may not hold during extreme market conditions
* **Timeframe dependency:** Different calculation periods can yield significantly different Beta values
* **Return distribution assumptions:** Standard Beta calculation assumes normally distributed returns, which is often not the case in financial markets
* **Regime sensitivity:** Beta relationships can change dramatically during market regime shifts (e.g., from low to high volatility environments)
* **Fundamental changes:** Corporate actions or structural market changes can alter Beta characteristics, requiring recalibration

## References

* Sharpe, W. F. (1964). Capital asset prices: A theory of market equilibrium under conditions of risk. The Journal of Finance, 19(3), 425-442.
* Fama, E. F., & French, K. R. (2004). The Capital Asset Pricing Model: Theory and Evidence. Journal of Economic Perspectives, 18(3), 25-46.
* Jacobs, B. I., & Levy, K. N. (2005). Market Neutral Strategies. John Wiley & Sons.
