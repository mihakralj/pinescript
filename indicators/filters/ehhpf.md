# Highpass Filter (HP)

The Highpass Filter implements an optimized filter design that effectively removes low-frequency components while preserving high-frequency signals. Based on John Ehlers' research, it provides precise control over the cutoff frequency with minimal phase distortion.

[Pine Script Implementation of HP](https://github.com/mihakralj/pinescript/blob/main/indicators/filters/ehhpf.pine)

## Mathematical Foundation

The filter is constructed using optimized coefficients in a second-order structure:

HP = c1(X - 2X₁ + X₂) + c2×HP₁ + c3×HP₂

Where:

- a1 = exp(-1.414π/length)
- b1 = 2a1 × cos(1.414 × 180/length)
- c1 = (1 + c2 - c3)/4
- c2 = b1
- c3 = -a1²
- HP₁, HP₂ are the previous filter outputs

## Filter Characteristics

### Implementation Details

1. **Coefficient Calculation**:
   - Automatic pole placement
   - Length-dependent optimization
   - Stable coefficient bounds
   - Efficient parameter tuning

2. **Signal Processing**:
   - Recursive IIR structure
   - Optimized memory usage
   - Real-time capability
   - Numerical stability safeguards

## Advantages and Disadvantages

### Advantages

- **Trend Removal**: Effective elimination of low frequencies
- **Sharp Cutoff**: Clear separation of frequency components
- **Phase Response**: Minimal distortion in passband
- **Computational Efficiency**: Few operations per sample
- **Numerical Stability**: Well-conditioned calculations

### Disadvantages

- **Startup Time**: Requires several periods for initialization
- **Parameter Dependency**: Performance tied to length selection
- **DC Bias**: May introduce baseline shifts
- **Memory Need**: Requires two previous outputs
- **Edge Effects**: Sensitive to sudden level changes
