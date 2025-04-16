# R-squared (Coefficient of Determination)

The R-squared (Coefficient of Determination) implements a statistical measure that represents the proportion of variance in the dependent variable that is predictable from the independent variable(s). Unlike other error metrics that focus on absolute errors, R² quantifies the goodness of fit of a model, providing a scale from 0 to 1 where higher values indicate better predictive performance.

[Pine Script Implementation of R-squared](https://github.com/mihakralj/pinescript/blob/main/indicators/errors/rsquared.pine)

## Mathematical Foundation

The R-squared is calculated by comparing the residual sum of squares to the total sum of squares:

R² = 1 - (Σ(Y₁ - Y₂)² / Σ(Y₁ - Y̅₁)²)

R²₍ₙ₎ = 1 - (SMA((Y₁₍ₙ₎ - Y₂₍ₙ₎)², p) / SMA((Y₁₍ₙ₎ - Y̅₁₍ₙ₎)², p))

Where:

- R²₍ₙ₎ is the current R-squared value
- Y₁₍ₙ₎ represents the actual values
- Y₂₍ₙ₎ represents the predicted values
- Y̅₁₍ₙ₎ represents the mean of actual values over the period
- p is the averaging period

## Error Characteristics

### Statistical Properties

1. **Bounded Range**: R² typically ranges from 0 to 1 (can be negative for poorly fitting models)
2. **Proportional Interpretation**: Directly represents the proportion of explained variance
3. **Scale Independence**: Dimensionless metric allowing cross-dataset comparison
4. **Model Comparison**: Facilitates direct comparison between different predictive models

### Response Properties

1. **Sensitivity**:
   - Values near 1 indicate the model explains most of the variance
   - Values near 0 indicate the model explains little of the variance
   - Can detect how well a model captures the overall pattern rather than just point-by-point accuracy

2. **Temporal Behavior**:
   - Moving window updates both the error and baseline calculations
   - Provides continuous assessment of model fit over time
   - Reflects changing relationships between signals in different market conditions

### Window Considerations

1. **Fit Assessment**: Longer periods provide more stable assessment of model fit
2. **Adaptability**: Shorter periods track changing relationships more quickly
3. **Memory Usage**: O(2p) space complexity due to tracking both residuals and total variance

## Advantages and Disadvantages

### Advantages

- **Intuitive Interpretation**: Easy to understand as a percentage of explained variance
- **Bounded Range**: Fixed scale makes interpretation straightforward
- **Comparative Analysis**: Ideal for comparing different models on the same data
- **Statistical Foundation**: Well-established in statistical modeling
- **Dimensionless**: Not affected by the scale of the original measurements

### Disadvantages

- **Insensitivity to Bias**: High R² can occur even with systematically biased predictions
- **Improvement Assessment**: Adding variables almost always increases R², even with irrelevant predictors
- **Non-linear Relationships**: May not fully capture non-linear dependencies
- **Outlier Sensitivity**: Can be heavily influenced by a few extreme values
- **No Information on Prediction Direction**: Doesn't indicate if predictions are consistently high or low
