# Symmetric Mean Absolute Percentage Error (SMAPE)

The Symmetric Mean Absolute Percentage Error implements a percentage-based error metric that overcomes limitations of traditional MAPE by using a symmetrical formula. SMAPE treats over-predictions and under-predictions equally, while constraining results to a range of 0-200%, making it more stable and appropriate for comparing prediction accuracy across different scales.

[Pine Script Implementation of SMAPE](https://github.com/mihakralj/pinescript/blob/main/indicators/errors/smape.pine)

## Mathematical Foundation

The SMAPE is calculated by taking the average of absolute differences divided by the sum of absolute values:

SMAPE = (200%/p) * Σ|Y₁ - Y₂| / (|Y₁| + |Y₂|)

SMAPE₍ₙ₎ = SMA(200% * |Y₁₍ₙ₎ - Y₂₍ₙ₎| / (|Y₁₍ₙ₎| + |Y₂₍ₙ₎|), p)

Where:

- SMAPE₍ₙ₎ is the current SMAPE value (in percentage)
- Y₁₍ₙ₎, Y₂₍ₙ₎ are the current signal values
- p is the averaging period

## Error Characteristics

### Statistical Properties

1. **Bounded Range**: SMAPE values are constrained between 0% and 200%
2. **Symmetry**: Equal treatment of over-predictions and under-predictions
3. **Scale Independence**: Results expressed as percentages allow cross-scale comparison
4. **Zero Handling**: Improved stability when either actual or predicted values are close to zero

### Response Properties

1. **Sensitivity**:
   - Provides relative error perspective
   - Balanced sensitivity across different magnitudes
   - Less biased than asymmetric percentage errors
   - More stable when values approach zero

2. **Temporal Behavior**:
   - Moving window provides dynamic error tracking
   - Percentage basis makes trending errors more apparent
   - Maintains consistent interpretation across different value ranges

### Window Considerations

1. **Error Smoothing**: Longer periods provide more stable percentage error metrics
2. **Response Time**: Shorter periods track relative changes more quickly
3. **Memory Usage**: O(p) space complexity for the averaging window

## Advantages and Disadvantages

### Advantages

- **Intuitive Interpretation**: Results expressed as easy-to-understand percentages
- **Bounded Range**: Fixed boundaries make interpretation straightforward
- **Symmetry**: Equal treatment of overestimation and underestimation
- **Scale Independence**: Facilitates comparison across different data ranges
- **Zero Robustness**: More stable than MAPE when values approach zero

### Disadvantages

- **Asymptotic Behavior**: Approaches 200% when either actual or predicted value is zero
- **Undefined for Dual Zeros**: Formula becomes undefined when both values are exactly zero
- **Interpretation Ambiguity**: Same value can result from different error patterns
- **Information Loss**: Like most relative metrics, obscures the absolute magnitude
- **Inverted Range**: Higher values (up to 200%) indicate worse performance
