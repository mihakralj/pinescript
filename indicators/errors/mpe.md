# Mean Percentage Error (MPE)

The Mean Percentage Error implements a signal comparison metric that quantifies the average percentage error between actual and predicted values, including error direction, providing insight into forecast bias. MPE's signed percentage nature makes it particularly useful for detecting systematic over or under-prediction in forecasting models.

[Pine Script Implementation of MPE](https://github.com/mihakralj/pinescript/blob/main/indicators/errors/mpe.pine)

## Mathematical Foundation

The MPE is calculated by taking the average of percentage errors: MPE = (100/p) * Σ(Y₁ - Y₂)/Y₁

MPE₍ₙ₎ = SMA((Y₁₍ₙ₎ - Y₂₍ₙ₎)/Y₁₍ₙ₎ * 100, p)

Where:

- MPE₍ₙ₎ is the current MPE value
- Y₁₍ₙ₎ is the actual value
- Y₂₍ₙ₎ is the predicted value
- p is the averaging period

## Error Characteristics

### Statistical Properties

1. **Signed Measure**: MPE can be positive or negative
2. **Asymmetry**: Different treatment of over and under predictions
3. **Scale Independence**: Percentage-based measurement
4. **Unbounded Range**: Values can range from -∞ to +∞

### Response Properties

The error measurement demonstrates:

1. **Sensitivity**:
   - Directional bias indication
   - Higher sensitivity when actual values are small
   - Cancellation of positive and negative errors

2. **Temporal Behavior**:
   - Moving window provides dynamic error tracking
   - Reveals systematic prediction biases
   - Maintains historical context through averaging

### Window Considerations

The averaging period affects several aspects:

1. **Error Smoothing**: Longer periods provide more stable error metrics
2. **Response Time**: Shorter periods track changes more quickly
3. **Memory Usage**: O(p) space complexity for the averaging window

## Advantages and Disadvantages

### Advantages

- **Bias Detection**: Shows systematic over/under prediction
- **Scale Independence**: Suitable for comparing different scales
- **Intuitive Direction**: Clear indication of error direction
- **Statistical Foundation**: Useful for bias analysis
- **Computational Efficiency**: Simple calculation using existing functions

### Disadvantages

- **Zero Handling**: Undefined when actual values are zero
- **Error Cancellation**: Positive and negative errors can offset
- **Outlier Sensitivity**: Heavily affected by small actual values
- **Averaging Delay**: Moving average introduces some lag
- **Infinite Values**: Can produce infinite errors for zero actuals
