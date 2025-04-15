# Huber Loss

The Huber Loss implements a hybrid signal comparison metric that combines the best properties of Mean Squared Error (MSE) and Mean Absolute Error (MAE). It behaves quadratically for small errors and linearly for large errors, providing robustness against outliers while maintaining sensitivity to small deviations. This adaptive behavior makes it particularly effective for financial signal analysis across varying market conditions.

[Pine Script Implementation of Huber Loss](https://github.com/mihakralj/pinescript/blob/main/indicators/errors/huber.pine)

## Mathematical Foundation

The Huber Loss uses a threshold (δ) to switch between quadratic and linear behavior:

For |Y₁ - Y₂| ≤ δ: Loss = 0.5(Y₁ - Y₂)² = MSE
For |Y₁ - Y₂| > δ: Loss = δ|Y₁ - Y₂| - 0.5δ² = MAE

Where:
- Y₁, Y₂ are the signal values being compared
- δ (delta) is the threshold parameter
- The final value is averaged over period p using SMA

The delta parameter (δ) has a widely accepted default value in statistics:
- δ = 1.345 is the standard choice in statistical applications
- This value provides 95% statistical efficiency for normally distributed data
- Makes Huber loss behave like MSE for errors ≤ 1.345 and like MAE for larger errors

## Error Characteristics

### Statistical Properties

1. **Non-negativity**: Always ≥ 0, with 0 indicating perfect match
2. **Symmetry**: Equal weight to positive and negative deviations
3. **Adaptive Scaling**: Quadratic for small errors, linear for large ones
4. **Scale Dependence**: Value depends on the scale of input signals
5. **Differentiability**: Smooth transition between regimes

### Response Properties

The error measurement demonstrates:
1. **Sensitivity**:
   - Quadratic response to small deviations for precision
   - Linear response to large deviations for robustness
   - Adaptive behavior based on error magnitude
   
2. **Temporal Behavior**:
   - Moving window provides dynamic error tracking
   - Responds to changing signal relationships
   - Maintains historical context through averaging

## Advantages and Disadvantages

### Advantages

- **Robustness**: Less sensitive to outliers than MSE
- **Precision**: More sensitive to small errors than MAE
- **Adaptivity**: Combines benefits of both MSE and MAE
- **Differentiability**: Smooth transition between regimes
- **Flexibility**: Adjustable threshold parameter

### Disadvantages

- **Scale Dependency**: Not suitable for comparing different scales
- **Parameter Tuning**: Requires appropriate delta selection
- **Averaging Delay**: Moving average introduces some lag
- **Non-directional**: Cannot distinguish positive from negative errors
- **Complexity**: More complex computation than MSE or MAE
