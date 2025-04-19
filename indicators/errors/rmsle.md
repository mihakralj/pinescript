# Root Mean Squared Logarithmic Error (RMSLE)

The Root Mean Squared Logarithmic Error implements a specialized error metric that calculates the square root of the mean squared difference between the logarithms of predicted and actual values. RMSLE emphasizes relative errors and is particularly useful for data with exponential growth or when proportional differences are more important than absolute ones.

[Pine Script Implementation of RMSLE](https://github.com/mihakralj/pinescript/blob/main/indicators/errors/rmsle.pine)

## Mathematical Foundation

The RMSLE is calculated by taking the square root of the average of squared differences between the logarithms of two signals plus 1:

RMSLE = √[(1/p) * Σ(log(1 + Y₁) - log(1 + Y₂))²]

RMSLE₍ₙ₎ = √[SMA((log(1 + Y₁₍ₙ₎) - log(1 + Y₂₍ₙ₎))², p)]

Where:

- RMSLE₍ₙ₎ is the current RMSLE value
- Y₁₍ₙ₎, Y₂₍ₙ₎ are the current signal values
- p is the averaging period
- log is the natural logarithm

## Error Characteristics

### Statistical Properties

1. **Non-negativity**: RMSLE is always ≥ 0, with 0 indicating perfect match
2. **Logarithmic Scale**: Measures relative differences rather than absolute ones
3. **Penalty Asymmetry**: Penalizes underestimation more heavily than overestimation
4. **Moderation**: Square root operation moderates the effect of the squared differences

### Response Properties

1. **Sensitivity**:
   - Higher sensitivity to relative differences than absolute ones
   - Penalizes underprediction more heavily than overprediction
   - Reduces the impact of large absolute errors on high-value signals
   - Moderates extreme values through square root transformation

2. **Temporal Behavior**:
   - Moving window provides dynamic relative error tracking
   - Well-suited for signals with exponential or multiplicative growth
   - Responds proportionally across different magnitudes

### Window Considerations

1. **Error Smoothing**: Longer periods provide more stable relative error metrics
2. **Response Time**: Shorter periods track proportional changes more quickly
3. **Memory Usage**: O(p) space complexity for the averaging window

## Advantages and Disadvantages

### Advantages

- **Scale Invariance**: Better for comparing proportional accuracy
- **Growth Pattern Handling**: Suitable for exponentially growing data
- **Relative Error Focus**: Emphasizes percentage-like differences
- **Reduced Dominance**: Prevents large values from dominating the error
- **Underestimation Penalty**: Stronger penalty for underpredicting values

### Disadvantages

- **Unintuitive Units**: Error isn't in the same units as the original data
- **Undefined for Negatives**: Requires positive values in both signals
- **Computational Complexity**: Higher computational cost due to logarithm and square root
- **Parameter Sensitivity**: Adding 1 affects the error scale differently at different magnitudes
- **Not Suitable for Zero Values**: Cannot handle true zero values without the +1 adjustment
