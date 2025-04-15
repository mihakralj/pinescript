# Mean Absolute Error (MAE)

The Mean Absolute Error implements a signal comparison metric that quantifies the average absolute difference between two sources, providing a straightforward statistical measure of prediction accuracy and signal similarity. MAE's linear nature ensures equal weighting of all errors, making it less sensitive to outliers while maintaining high error detection accuracy across varying market conditions.

[Pine Script Implementation of MAE](https://github.com/mihakralj/pinescript/blob/main/indicators/errors/mae.pine)

## Mathematical Foundation

The MAE is calculated by taking the average of absolute differences between two signals: MAE = (1/p) * Σ|Y₁ - Y₂|

MAE₍ₙ₎ = SMA(|Y₁₍ₙ₎ - Y₂₍ₙ₎|, p)

Where:
- MAE₍ₙ₎ is the current MAE value
- Y₁₍ₙ₎, Y₂₍ₙ₎ are the current signal values
- p is the averaging period

## Error Characteristics

### Statistical Properties

1. **Non-negativity**: MAE is always ≥ 0, with 0 indicating perfect match
2. **Symmetry**: Equal weight to positive and negative deviations
3. **Linear Scaling**: All errors contribute proportionally
4. **Scale Dependence**: Value depends on the scale of input signals

### Response Properties

The error measurement demonstrates:
1. **Sensitivity**:
   - Linear sensitivity to deviations
   - Equal weighting of all error magnitudes
   - Robust to outliers compared to squared errors

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

- **Intuitive Interpretation**: Same units as original signals
- **Outlier Robustness**: Less sensitive to extreme deviations
- **Linear Scaling**: Proportional error weighting
- **Statistical Foundation**: Well-established error metric
- **Computational Efficiency**: Simple calculation using absolute values

### Disadvantages

- **Scale Dependency**: Not suitable for comparing different scales
- **Gradient Issues**: Non-differentiable at zero error
- **Averaging Delay**: Moving average introduces some lag
- **Non-directional**: Cannot distinguish positive from negative errors
- **Less Sensitive**: May miss subtle pattern changes
