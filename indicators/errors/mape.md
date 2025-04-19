# Mean Absolute Percentage Error (MAPE)

The Mean Absolute Percentage Error implements a signal comparison metric that quantifies the average percentage error between actual and predicted values, providing a scale-independent measure of prediction accuracy. MAPE's percentage-based nature ensures relative error measurement, making it particularly useful for forecasting and trend analysis.

[Pine Script Implementation of MAPE](https://github.com/mihakralj/pinescript/blob/main/indicators/errors/mape.pine)

## Mathematical Foundation

The MAPE is calculated by taking the average of absolute percentage errors: MAPE = (100/p) * Σ|Y₁ - Y₂|/Y₁

MAPE₍ₙ₎ = SMA(|Y₁₍ₙ₎ - Y₂₍ₙ₎|/Y₁₍ₙ₎ * 100, p)

Where:

- MAPE₍ₙ₎ is the current MAPE value
- Y₁₍ₙ₎ is the actual value
- Y₂₍ₙ₎ is the predicted value
- p is the averaging period

## Error Characteristics

### Statistical Properties

1. **Non-negativity**: MAPE is always ≥ 0, with 0 indicating perfect prediction
2. **Asymmetry**: Different treatment of over and under predictions
3. **Scale Independence**: Percentage-based measurement
4. **Unbounded Range**: Values can exceed 100% for large errors

### Response Properties

The error measurement demonstrates:

1. **Sensitivity**:
   - Proportional to relative errors
   - Higher sensitivity to errors when actual values are small
   - More weight on negative errors than positive ones

2. **Temporal Behavior**:
   - Moving window provides dynamic error tracking
   - Responds to changing prediction accuracy
   - Maintains historical context through averaging

### Window Considerations

The averaging period affects several aspects:

1. **Error Smoothing**: Longer periods provide more stable error metrics
2. **Response Time**: Shorter periods track changes more quickly
3. **Memory Usage**: O(p) space complexity for the averaging window

## Advantages and Disadvantages

### Advantages

- **Scale Independence**: Suitable for comparing different scales
- **Intuitive Interpretation**: Results in percentage values
- **Forecasting Focus**: Well-suited for prediction evaluation
- **Statistical Foundation**: Widely used in forecasting applications
- **Computational Efficiency**: Simple calculation using existing functions

### Disadvantages

- **Zero Handling**: Undefined when actual values are zero
- **Asymmetric Penalties**: Different treatment of over/under predictions
- **Outlier Sensitivity**: Heavily affected by small actual values
- **Averaging Delay**: Moving average introduces some lag
- **Infinite Values**: Can produce infinite errors for zero actuals
