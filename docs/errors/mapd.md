# Mean Absolute Percentage Difference (MAPD)

The Mean Absolute Percentage Difference implements a signal comparison metric that quantifies the average percentage difference between two sources, providing a scale-independent measure of prediction accuracy and signal similarity. MAPD's percentage-based nature ensures relative error measurement, making it suitable for comparing signals of different magnitudes.

[Pine Script Implementation of MAPD](https://github.com/mihakralj/pinescript/blob/main/indicators/errors/mapd.pine)

## Mathematical Foundation

The MAPD is calculated by taking the average of absolute percentage differences between two signals: MAPD = (100/p) * Σ|Y₁ - Y₂|/((Y₁ + Y₂)/2)

MAPD₍ₙ₎ = SMA(|Y₁₍ₙ₎ - Y₂₍ₙ₎|/((Y₁₍ₙ₎ + Y₂₍ₙ₎)/2) * 100, p)

Where:
- MAPD₍ₙ₎ is the current MAPD value
- Y₁₍ₙ₎, Y₂₍ₙ₎ are the current signal values
- p is the averaging period

## Error Characteristics

### Statistical Properties

1. **Non-negativity**: MAPD is always ≥ 0, with 0 indicating perfect match
2. **Symmetry**: Equal weight to positive and negative deviations
3. **Scale Independence**: Percentage-based measurement
4. **Bounded Range**: Values typically between 0% and 100%

### Response Properties

The error measurement demonstrates:
1. **Sensitivity**:
   - Proportional to relative differences
   - Equal weighting of percentage deviations
   - Robust across different signal magnitudes

2. **Temporal Behavior**:
   - Moving window provides dynamic error tracking
   - Responds to changing signal relationships
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
- **Symmetric**: Treats both signals equally
- **Statistical Foundation**: Well-established relative error metric
- **Computational Efficiency**: Simple calculation using existing functions

### Disadvantages

- **Zero Handling**: Undefined when both signals are zero
- **Outlier Sensitivity**: Can be affected by very small values
- **Averaging Delay**: Moving average introduces some lag
- **Non-directional**: Cannot distinguish positive from negative errors
- **Range Limitation**: May exceed 100% in extreme cases
