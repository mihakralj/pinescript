# Mean Squared Logarithmic Error (MSLE)

The Mean Squared Logarithmic Error implements a specialized error metric that calculates the squared difference of logarithmic values. MSLE emphasizes relative errors rather than absolute magnitudes, making it particularly suitable for data with exponential growth patterns or cases where proportional differences are more important than absolute ones.

[Pine Script Implementation of MSLE](https://github.com/mihakralj/pinescript/blob/main/indicators/errors/msle.pine)

## Mathematical Foundation

The MSLE is calculated by taking the average of squared differences between the logarithms of two signals plus 1:

MSLE = (1/p) * Σ(log(1 + Y₁) - log(1 + Y₂))²

MSLE₍ₙ₎ = SMA((log(1 + Y₁₍ₙ₎) - log(1 + Y₂₍ₙ₎))², p)

Where:

- MSLE₍ₙ₎ is the current MSLE value
- Y₁₍ₙ₎, Y₂₍ₙ₎ are the current signal values
- p is the averaging period
- log is the natural logarithm

## Error Characteristics

### Statistical Properties

1. **Non-negativity**: MSLE is always ≥ 0, with 0 indicating perfect match
2. **Relative Scale**: Measures relative differences rather than absolute ones
3. **Logarithmic Transformation**: Compresses large values and expands smaller ones
4. **Penalty Asymmetry**: Penalizes underestimation more heavily than overestimation

### Response Properties

1. **Sensitivity**:
   - Higher sensitivity to relative differences than absolute ones
   - Penalizes underprediction more heavily than overprediction
   - Reduces the impact of large absolute errors on high-value signals

2. **Temporal Behavior**:
   - Moving window provides dynamic relative error tracking
   - Well-suited for signals with exponential or multiplicative growth
   - Less affected by sudden large values than squared errors

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
- **Log Computation**: Higher computational cost than simple error metrics
- **Parameter Sensitivity**: Adding 1 affects the error scale differently at different magnitudes
- **Not Suitable for Zero Values**: Cannot handle true zero values without the +1 adjustment
