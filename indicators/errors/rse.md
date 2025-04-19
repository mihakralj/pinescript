# Relative Squared Error (RSE)

The Relative Squared Error implements a normalized error metric that compares squared prediction errors against a naive baseline model. RSE expresses the sum of squared errors as a proportion of the squared baseline error, where the baseline is typically defined as using the average of the actual values as a constant prediction. This normalization makes RSE particularly useful for comparing model performance across different datasets.

[Pine Script Implementation of RSE](https://github.com/mihakralj/pinescript/blob/main/indicators/errors/rse.pine)

## Mathematical Foundation

The RSE is calculated by dividing the sum of squared errors by the sum of squared baseline errors:

RSE = Σ(Y₁ - Y₂)² / Σ(Y₁ - Y̅₁)²

Where:

- Y₁ represents the actual values
- Y₂ represents the predicted values
- Y̅₁ represents the mean of the actual values over the period
- The summations are calculated over the specified period

In the Pine Script implementation, this is performed using a moving window approach:

RSE₍ₙ₎ = SMA((Y₁₍ₙ₎ - Y₂₍ₙ₎)², p) / SMA((Y₁₍ₙ₎ - Y̅₁₍ₙ₎)², p)

## Error Characteristics

### Statistical Properties

1. **Normalization**: RSE is normalized against a baseline error
2. **Relative Scale**: Value of 1.0 indicates performance equivalent to the baseline
3. **Range**: Typically ranges from 0 to infinity, with lower values being better
4. **Quadratic Penalty**: Larger errors are penalized more heavily due to squaring

### Response Properties

1. **Sensitivity**:
   - Provides context for error interpretation
   - Values below 1.0 indicate better-than-baseline performance
   - Values above 1.0 indicate worse-than-baseline performance
   - Squared terms amplify the effects of larger errors

2. **Temporal Behavior**:
   - Moving window updates both the error and baseline calculations
   - Adapts to changing signal distributions
   - Baseline reference point evolves with the data

### Window Considerations

1. **Baseline Stability**: Longer periods provide more stable baseline calculations
2. **Relativity**: Shows squared error performance relative to a dynamic baseline
3. **Memory Usage**: O(2p) space complexity due to tracking both error and baseline

## Advantages and Disadvantages

### Advantages

- **Contextual Interpretation**: Error is understood in relation to a benchmark
- **Scale Invariance**: Can compare error across different data scales
- **Performance Benchmarking**: Clear indication of model utility
- **Outlier Sensitivity**: Heightened awareness of significant prediction errors
- **Cross-Dataset Comparison**: Facilitates comparison between different time series

### Disadvantages

- **Baseline Dependence**: Performance heavily depends on the baseline choice
- **Unstable for Constant Data**: May approach infinity if actual values are nearly constant
- **Computation Complexity**: Requires maintaining multiple running averages
- **Outlier Vulnerability**: Can be dominated by a few large errors due to squaring
- **Interpretation Challenges**: May be less intuitive than direct error measurements
