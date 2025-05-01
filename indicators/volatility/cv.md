# CV: Conditional Volatility

[Pine Script Implementation of CV](https://github.com/mihakralj/pinescript/blob/main/indicators/volatility/cv.pine)

## Overview and Purpose

Conditional Volatility (CV) is a volatility model based on the Generalized Autoregressive Conditional Heteroskedasticity (GARCH) framework that captures volatility clustering in financial time series. Unlike simple historical volatility measures, CV recognizes that market volatility tends to be persistent—volatile periods tend to be followed by volatile periods, and calm periods by calm periods. This adaptive approach makes CV particularly valuable for quantifying time-varying risk, option pricing, volatility forecasting, and dynamic position sizing in trading systems.

The implementation provided offers a streamlined GARCH(1,1) model with configurable persistence parameters, enabling traders to capture volatility dynamics without the computational complexity of full maximum likelihood estimation. By explicitly modeling how past market shocks and volatility states influence current volatility expectations, CV provides forward-looking volatility estimates that adapt more quickly to changing market conditions than traditional fixed-window approaches like standard deviation or ATR-based indicators.

## Core Concepts

* **Volatility clustering:** Captures the empirically observed tendency of volatility to cluster, with high volatility periods followed by more high volatility
* **Adaptive estimation:** Dynamically adjusts volatility estimates based on recent market behavior rather than arbitrary fixed windows
* **Shock persistence:** Models how the impact of market shocks decays over time through the alpha parameter
* **Volatility persistence:** Quantifies the "memory" of previous volatility states through the beta parameter

CV stands apart from simple historical volatility measures by incorporating both the magnitude of recent price changes (through alpha) and the persistent memory of past volatility (through beta). This dual-component approach creates a more responsive indicator that can quickly adapt to regime changes while maintaining stability during consistent market conditions, providing a theoretically sound foundation for risk management derived from financial econometrics.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 20 | Initial period for parameter estimation | Shorter for more adaptive behavior; longer for more stable baseline estimates |
| Alpha | 0.2 | Weight on previous squared return (ARCH term) | Higher (0.3-0.4) for more reactive volatility; lower (0.05-0.15) for smoother responses |
| Beta | 0.7 | Weight on previous variance (GARCH term) | Higher (0.8-0.9) for longer volatility memory; lower (0.5-0.6) for quicker forgetting |

**Pro Tip:** The sum of Alpha and Beta represents the persistence of volatility shocks—how long elevated volatility tends to last. For most financial markets, this sum typically falls between 0.85 and 0.98. Values closer to 1.0 indicate very persistent volatility regimes, while lower values suggest quicker mean reversion in volatility. Try setting Alpha+Beta = 0.9 for standard markets and adjust based on the observed volatility persistence.

## Calculation and Mathematical Foundation

**Simplified explanation:**
CV models volatility as having both a long-term component and a reactive component. Each day, the model updates its volatility estimate based on: (1) a constant term representing long-run average volatility, (2) the most recent observed price shock, and (3) the previous day's volatility estimate.

**Technical formula:**

The GARCH(1,1) model is defined as:

σ²ₜ = ω + α × r²ₜ₋₁ + β × σ²ₜ₋₁

Where:
- σ²ₜ is the conditional variance at time t
- ω is the long-run average variance component (calculated as (1-α-β) × long-run variance)
- r²ₜ₋₁ is the squared log return from the previous period
- α is the weight assigned to recent squared returns
- β is the weight assigned to the previous variance estimate
- The final output is annualized by multiplying by √252 and expressing as a percentage

> 🔍 **Technical Note:** The implementation initializes the long-run variance component during the warm-up period by calculating the sample variance of returns. It also employs return capping to prevent extreme outliers from excessively impacting volatility estimates, and includes variance floor protection to maintain numerical stability during calculations.

## Interpretation Details

CV provides several analytical perspectives:

* **Absolute volatility levels:** Higher CV values indicate heightened market risk; lower values suggest calmer conditions
* **Volatility trends:** Increasing CV suggests growing market uncertainty; decreasing CV indicates stabilizing conditions
* **Regime identification:** Sudden shifts in CV often signal transitions between market regimes
* **Relative volatility:** Comparing current CV to its historical range helps contextualize present market conditions
* **Risk-adjusted position sizing:** Inversely scaling position sizes based on CV helps maintain consistent risk exposure
* **Option valuation framework:** Provides dynamic volatility inputs for option pricing models
* **Stop-loss calibration:** Wider stops during high CV periods, tighter stops during low CV periods

## Limitations and Considerations

* **Parameter sensitivity:** Results can vary significantly based on alpha and beta settings
* **Simplification tradeoffs:** The implementation sacrifices some econometric rigor for computational efficiency
* **Log-return assumption:** Uses logarithmic returns which may not be optimal for all asset classes
* **Asymmetry limitations:** Standard GARCH(1,1) treats positive and negative shocks equally, unlike more advanced models (e.g., EGARCH)
* **Volatility targeting:** Does not directly incorporate a target or "normal" volatility level
* **Mean-reversion assumption:** Implicitly assumes volatility will eventually revert to a long-run average
* **Initialization period:** Requires sufficient historical data for reliable parameter estimation
* **Crisis adaptation:** May lag during rapid regime shifts despite its adaptive nature

## References

* Bollerslev, T. (1986). Generalized Autoregressive Conditional Heteroskedasticity. Journal of Econometrics, 31(3), 307-327.
* Engle, R. F. (1982). Autoregressive Conditional Heteroscedasticity with Estimates of the Variance of United Kingdom Inflation. Econometrica, 50(4), 987-1007.
* Alexander, C. (2008). Market Risk Analysis, Volume II: Practical Financial Econometrics. Wiley.
* Poon, S. H., & Granger, C. W. (2003). Forecasting Volatility in Financial Markets: A Review. Journal of Economic Literature, 41(2), 478-539.
* Sinclair, E. (2013). Volatility Trading (2nd ed.). John Wiley & Sons.
