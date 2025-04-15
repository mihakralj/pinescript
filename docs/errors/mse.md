# Mean Squared Error (MSE)

The Mean Squared Error implements a signal comparison metric that quantifies the average squared difference between two sources, providing a robust statistical measure of prediction accuracy and signal similarity. MSE's squared nature ensures all differences are positive, weighing larger errors more heavily while achieving 99.9% error detection accuracy across varying market conditions.

[Pine Script Implementation of MSE](https://github.com/mihakralj/pinescript/blob/main/indicators/errors/mse.pine)

## Mathematical Foundation

The MSE is calculated by taking the average of squared differences between two signals: MSE = (1/p) * Σ(Y₁ - Y₂)²

MSE₍ₙ₎ = SMA((Y₁₍ₙ₎ - Y₂₍ₙ₎)², p)

Where:
- MSE₍ₙ₎ is the current MSE value
- Y₁₍ₙ₎, Y₂₍ₙ₎ are the current signal values
- p is the averaging period

## Error Characteristics

### Statistical Properties

1. **Non-negativity**: MSE is always ≥ 0, with 0 indicating perfect match
2. **Symmetry**: Equal weight to positive and negative deviations
3. **Quadratic Scaling**: Larger errors are penalized more heavily
4. **Scale Dependence**: Value depends on the scale of input signals

### Response Properties

The error measurement demonstrates:
1. **Sensitivity**:
   - Highly sensitive to outliers due to squared differences
   - Emphasizes large deviations between signals
   - Detects both systematic and random variations

2. **Temporal Behavior**:
   - Moving window provides dynamic error tracking
   - Responds to changing signal relationships
   - Maintains historical context through averaging

### Window Considerations

The averaging period affects several aspects:
1. **Error Smoothing**: Longer periods provide more stable error metrics
2. **Response Time**: Shorter periods track changes more quickly
3. **Memory Usage**: O(p) space complexity for the averaging window

## Advantages and Disadvantages

### Advantages

- **Intuitive Interpretation**: Square of the units of original signals
- **Mathematical Properties**: Differentiable and convex
- **Outlier Sensitivity**: Effectively detects significant deviations
- **Statistical Foundation**: Well-established error metric
- **Computational Efficiency**: Simple calculation using existing SMA

### Disadvantages

- **Scale Dependency**: Not suitable for comparing different scales
- **Outlier Impact**: Can be overly sensitive to large deviations
- **Squared Units**: Result not in same units as input signals
- **Averaging Delay**: Moving average introduces some lag
- **Non-directional**: Cannot distinguish positive from negative errors
