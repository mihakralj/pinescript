# Mean Error (ME)

The Mean Error implements a basic signal comparison metric that calculates the average difference between two sources without taking the absolute value. Unlike MAE, it accounts for the direction of error, allowing positive and negative errors to cancel each other out. This provides insight into systematic bias in predictions rather than just error magnitude.

[Pine Script Implementation of ME](https://github.com/mihakralj/pinescript/blob/main/indicators/errors/me.pine)

## Mathematical Foundation

The ME is calculated by taking the average of all differences between two signals: ME = (1/p) * Σ(Y₁ - Y₂)

ME₍ₙ₎ = SMA(Y₁₍ₙ₎ - Y₂₍ₙ₎, p)

Where:

- ME₍ₙ₎ is the current ME value
- Y₁₍ₙ₎, Y₂₍ₙ₎ are the current signal values
- p is the averaging period

## Error Characteristics

### Statistical Properties

1. **Sign-sensitive**: ME can be positive, negative, or zero
2. **Zero-centered**: Perfect balance of positive and negative errors results in ME = 0
3. **Cancellation Effect**: Positive and negative errors can offset each other
4. **Scale Dependence**: Value depends on the scale of input signals

### Response Properties

1. **Directional Sensitivity**:
   - Distinguishes between overestimation and underestimation
   - Reveals systematic bias in prediction models
   - Can be zero even with substantial errors if they balance out

2. **Temporal Behavior**:
   - Moving window provides dynamic error tracking
   - Indicates shifting bias over time
   - Can cross zero when prediction bias changes direction

### Window Considerations

1. **Error Smoothing**: Longer periods provide more stable bias assessment
2. **Bias Detection**: Shows persistent directional errors over the window
3. **Memory Usage**: O(p) space complexity for the averaging window

## Advantages and Disadvantages

### Advantages

- **Bias Detection**: Reveals systematic over/under estimation
- **Direction Awareness**: Distinguishes positive from negative errors
- **Zero-Centering**: Indicates balance point between over/under prediction
- **Statistical Foundation**: Simple, direct error metric
- **Computational Efficiency**: Minimal calculation requirements

### Disadvantages

- **Error Cancellation**: Can mask large errors if they balance out
- **Scale Dependency**: Not suitable for comparing different scales
- **Outlier Sensitivity**: Extreme values can heavily influence the result
- **Ambiguous Interpretation**: Small ME can result from either small errors or cancelling large errors
- **Limited Error Magnitude**: Doesn't directly measure prediction accuracy
