# Mean Absolute Scaled Error (MASE)

The Mean Absolute Scaled Error implements a signal comparison metric that quantifies prediction accuracy by scaling the error against a benchmark MAE, providing a unit-free measure of forecast accuracy. MASE's scaled nature makes it particularly robust for comparing forecasts across different scales and seasonality patterns.

[Pine Script Implementation of MASE](https://github.com/mihakralj/pinescript/blob/main/indicators/errors/mase.pine)

## Mathematical Foundation

The MASE is calculated by scaling the MAE against the average in-sample MAE: MASE = MAE / ((1/p) * Σ|Y₍ᵢ₎ - Y₍ᵢ₋₁₎|)

MASE₍ₙ₎ = SMA(|Y₁₍ₙ₎ - Y₂₍ₙ₎|, p) / SMA(|Y₁₍ₙ₎ - Y₁₍ₙ₋₁₎|, p)

Where:
- MASE₍ₙ₎ is the current MASE value
- Y₁₍ₙ₎ is the actual value
- Y₂₍ₙ₎ is the predicted value
- Y₁₍ₙ₋₁₎ is the previous actual value
- p is the averaging period

## Error Characteristics

### Statistical Properties

1. **Non-negativity**: MASE is always ≥ 0, with 0 indicating perfect prediction
2. **Symmetry**: Equal weight to positive and negative deviations
3. **Scale Independence**: Unit-free measurement
4. **Interpretability**: Values < 1 indicate better than naive forecast

### Response Properties

The error measurement demonstrates:
1. **Sensitivity**:
   - Proportional to scaled errors
   - Robust against outliers and zero values
   - Equal weighting of over and under predictions

2. **Temporal Behavior**:
   - Moving window provides dynamic error tracking
   - Adapts to changing volatility patterns
   - Maintains historical context through averaging

### Window Considerations

The averaging period affects several aspects:
1. **Error Smoothing**: Longer periods provide more stable error metrics
2. **Response Time**: Shorter periods track changes more quickly
3. **Memory Usage**: O(p) space complexity for the averaging window

## Advantages and Disadvantages

### Advantages

- **Scale Independence**: Suitable for comparing different scales
- **Interpretable Scale**: Clear benchmark against naive forecast
- **Outlier Robustness**: Less sensitive to extreme values
- **Statistical Foundation**: Well-suited for seasonal data
- **Zero Handling**: Well-defined for zero values

### Disadvantages

- **Complexity**: More complex calculation than simple error measures
- **Benchmark Dependency**: Relies on quality of naive forecast
- **Averaging Delay**: Moving average introduces some lag
- **Computation Cost**: Requires additional historical data
- **Interpretation**: Less intuitive than percentage errors
