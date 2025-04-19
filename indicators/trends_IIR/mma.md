# Modified Moving Average (MMA)

The Modified Moving Average combines a simple moving average with a weighted component to provide a balanced smoothing effect. The weighting scheme emphasizes central values while maintaining overall data representation, delivering improved responsiveness compared to traditional moving averages while preserving stability through its dual-component approach.

[Pine Script Implementation of MMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends/mma.pine)

## Mathematical Foundation

The MMA is calculated by combining two components:

1. Simple Moving Average (SMA) component
2. Weighted component with symmetric weights around the center

MMA = SMA + 6*WeightedSum/((period+1)*period)

Where:

- SMA = (P₁ + P₂ + ... + Pₙ) / n
- WeightedSum = Σ(wᵢ * Pᵢ), where wᵢ = (n - (2i + 1))/2
- n is the number of periods
- Pᵢ are the signal values in the lookback window

### Optimized Implementation

1. Maintains a circular buffer for efficient data management
2. Calculates the simple moving average component (T/period)
3. Computes a weighted sum with symmetric weights around the center
4. Combines both components using the formula above

## Initialization Properties

The MMA requires a minimum of 2 periods before producing its first output. Several initialization characteristics:

1. **Minimum Period**: Must be at least 2 periods
2. **Initial Values**: Uses simple average until enough data points are available
3. **Transition**: Smoothly transitions from simple average to full MMA calculation

## Advantages and Disadvantages of MMA

### Advantages

- **Balanced Smoothing**: Better balance between smoothing and responsiveness
- **Reduced Lag**: More responsive than simple moving average
- **Stability**: Maintains stability through dual-component approach
- **Central Emphasis**: Emphasizes central values while maintaining data representation
- **Smooth Transition**: Gradual transition from simple to weighted calculation

### Disadvantages

- **Computational Overhead**: More complex calculations than simple moving average
- **Parameter Sensitivity**: Performance depends on appropriate period selection
- **Memory Requirements**: Requires storing full period of values
- **Complexity**: More difficult to understand than simple moving averages
- **Initial Values**: Requires minimum of 2 periods for proper calculation
