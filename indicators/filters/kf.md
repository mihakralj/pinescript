# KF: Kalman Filter

[Pine Script Implementation of KF](https://github.com/mihakralj/pinescript/blob/main/indicators/filters/kf.pine)

## Overview and Purpose

The Kalman Filter is a recursive optimal estimator that efficiently processes noisy data to produce accurate estimates of unknown variables. In financial markets, it serves as an adaptive filter that continuously updates its estimates based on new measurements, weighing them against its internal model predictions. Unlike conventional moving averages that apply fixed weights, the Kalman Filter dynamically adjusts its responsiveness through its "Kalman gain," which determines how much weight to give new measurements versus the model's predictions.

The implementation provided offers a simplified yet powerful version of the Kalman Filter that balances computational efficiency with real-time adaptability. By modeling price movement as a process with inherent noise and measurement uncertainty, it can extract underlying signals from market data more effectively than traditional filters. This approach is particularly valuable for tracking price trends in volatile markets, where distinguishing genuine price movements from random fluctuations is challenging.

## Core Concepts

* **State estimation:** Maintains and continuously updates an internal model of the system's state (price value)
* **Prediction-correction cycle:** Alternates between predicting the next state and correcting that prediction using new measurements
* **Adaptive Kalman gain:** Automatically adjusts the filter's responsiveness based on the relative uncertainty in predictions versus measurements
* **Uncertainty management:** Explicitly accounts for both process noise (market volatility) and measurement noise (price reporting inaccuracies)

The Kalman Filter stands apart from other technical indicators through its foundation in statistical estimation theory. Rather than simply averaging past values with predetermined weights, it intelligently adapts to changing market conditions by continuously evaluating its own uncertainty estimates. This probabilistic approach allows it to respond quickly to significant price changes while filtering out random noise.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Process Noise (Q) | 0.01 | Controls how much the filter expects the market to change between observations | Increase during volatile periods for faster response; decrease in stable markets for smoother output |
| Measurement Noise (R) | 0.1 | Represents expected noise level in the price data | Increase when price data contains spikes or artifacts; decrease when price data is reliable |
| Source | Close | Price data used for filtering | Modify to filter different aspects of price action |

**Pro Tip:** The ratio between Q and R is more important than their absolute values. A Q/R ratio of approximately 0.1 provides a good balance for most markets. During trending periods, increase this ratio slightly to make the filter more responsive to new price movements.

## Calculation and Mathematical Foundation

**Simplified explanation:**
The Kalman Filter proceeds in two steps: predict and update. In the prediction step, it projects its current estimate forward in time. In the update step, it incorporates a new measurement to refine this prediction, with the Kalman gain determining how much to trust the measurement versus the prediction.

**Technical formula:**

1. Prediction step:
   - x̂ₙ⁻ = x̂ₙ₋₁ (predicted state equals previous state)
   - Pₙ⁻ = Pₙ₋₁ + Q (predicted error covariance increases by process noise)

2. Update step:
   - Kₙ = Pₙ⁻/(Pₙ⁻ + R) (calculate Kalman gain)
   - x̂ₙ = x̂ₙ⁻ + Kₙ(zₙ - x̂ₙ⁻) (update state estimate)
   - Pₙ = (1 - Kₙ)Pₙ⁻ (update error covariance)

Where:
- x̂ₙ is the filtered value at time n
- Pₙ is the estimation error covariance
- zₙ is the measurement (observed price)
- Q is the process noise covariance
- R is the measurement noise covariance
- Kₙ is the Kalman gain

> 🔍 **Technical Note:** The implementation uses a simplified one-dimensional Kalman Filter with a constant velocity model. This provides good performance for most financial time series while remaining computationally efficient. The filter initializes with the first valid measurement to provide immediate useful output without requiring a warm-up period.

## Interpretation Details

The Kalman Filter provides several analytical perspectives:

* **Trend detection:** The filtered output reveals the underlying trend by removing random fluctuations
* **Change point identification:** Significant deviations between the filter's predictions and new measurements can signal trend changes
* **Dynamic support/resistance:** The filter can function as adaptive support in uptrends and resistance in downtrends
* **Noise quantification:** The gap between raw price and filtered output offers insight into market noise levels
* **Momentum assessment:** The rate of change in the filter's output indicates trend strength
* **Divergence analysis:** When price makes new extremes but the filtered line doesn't confirm, it may signal potential reversals

## Limitations and Considerations

* **Parameter sensitivity:** Results can vary significantly based on noise parameter settings
* **Model assumptions:** Assumes a particular underlying model (constant velocity) which may not match all market conditions
* **Lag component:** Inherently introduces some lag, though typically less than comparable smoothing indicators
* **Single-dimension limitation:** The implementation tracks only price level, not higher-order derivatives like velocity or acceleration
* **Regime adaptability:** May need parameter adjustments when market regime changes (e.g., from trending to ranging)
* **Initialization bias:** First few values may be less reliable until the filter stabilizes
* **Computational complexity:** More resource-intensive than simple moving averages, though the optimized implementation minimizes this concern

## References

* Kalman, R. E. (1960). A New Approach to Linear Filtering and Prediction Problems. Journal of Basic Engineering, 82(1), 35-45.
* Welch, G., & Bishop, G. (2006). An Introduction to the Kalman Filter. University of North Carolina at Chapel Hill.
* Chan, E. P. (2013). Algorithmic Trading: Winning Strategies and Their Rationale. John Wiley & Sons.
* Javaheri, A. (2015). Inside Volatility Filtering: Secrets of the Skew. John Wiley & Sons.
