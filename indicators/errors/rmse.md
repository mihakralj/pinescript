# Root Mean Squared Error (RMSE)

The Root Mean Squared Error implements a signal comparison metric that calculates the square root of the average squared differences between two sources. RMSE amplifies the influence of larger errors due to the squaring operation, making it particularly sensitive to outliers while providing a measure in the same units as the original data.

[Pine Script Implementation of RMSE](https://github.com/mihakralj/pinescript/blob/main/indicators/errors/rmse.pine)

## Mathematical Foundation

The RMSE is calculated by taking the square root of the average of squared differences between two signals:

RMSE = √[(1/p) * Σ(Y₁ - Y₂)²]

RMSE₍ₙ₎ = √[SMA((Y₁₍ₙ₎ - Y₂₍ₙ₎)², p)]

Where:

- RMSE₍ₙ₎ is the current RMSE value
- Y₁₍ₙ₎, Y₂₍ₙ₎ are the current signal values
- p is the averaging period

## Error Characteristics

### Statistical Properties

1. **Non-negativity**: RMSE is always ≥ 0, with 0 indicating perfect match
2. **Symmetry**: Equal weight to positive and negative deviations
3. **Squared Scaling**: Larger errors contribute disproportionately more
4. **Original Units**: Results are in the same units as input data

### Response Properties

1. **Sensitivity**:
   - Quadratic increase with error magnitude
   - Higher sensitivity to outliers than linear metrics
   - Larger errors penalized more heavily than smaller ones

2. **Temporal Behavior**:
   - Moving window provides dynamic error tracking
   - Responds more dramatically to sudden large deviations
   - Square root operation moderates extreme values

### Window Considerations

1. **Error Smoothing**: Longer periods provide more stable error metrics
2. **Response Time**: Shorter periods track large deviations more quickly
3. **Memory Usage**: O(p) space complexity for the averaging window

## Advantages and Disadvantages

### Advantages

- **Intuitive Units**: Same units as original signals
- **Outlier Emphasis**: Highlights significant deviations
- **Statistical Foundation**: Well-established error metric in statistics
- **Differentiability**: Smooth gradient for optimization
- **Signal Processing**: Effective for detecting high-energy errors

### Disadvantages

- **Outlier Sensitivity**: Can be dominated by a few large errors
- **Quadratic Penalty**: May overemphasize large deviations
- **Scale Dependency**: Not suitable for comparing across different scales
- **Computational Complexity**: Requires squaring and square root
- **Non-robust**: Not resistant to outliers compared to metrics like MAE
