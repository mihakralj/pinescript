# Bandpass Filter (BP)

The Bandpass Filter implements a cascaded highpass and lowpass filter combination to isolate frequency components within a specific range. Based on John Ehlers' research, it effectively removes both high and low-frequency noise while preserving the desired frequency band.

[Pine Script Implementation of BP](https://github.com/mihakralj/pinescript/blob/main/indicators/filters/ehbpf.pine)

## Mathematical Foundation

The filter combines two stages in series:

BP = Lowpass(Highpass(X))

Where:

- Highpass coefficients:
  - a1 = exp(-1.414π/lp)
  - b1 = 2a1 × cos(1.414 × 180/lp)
  - c1 = (1 + c2 - c3)/4
  - c2 = b1
  - c3 = -a1²

- Lowpass coefficients:
  - a2 = exp(-1.414π/up)
  - b2 = 2a2 × cos(1.414 × 180/up)
  - k1 = 1 - k2 - k3
  - k2 = b2
  - k3 = -a2²

### Implementation Details

1. **Coefficient Calculation**:
   - Optimized pole placement
   - Independent period controls
   - Automatic stability enforcement
   - Efficient coefficient updates

2. **Signal Processing**:
   - Two-stage cascade structure
   - Recursive implementation
   - Memory-efficient design
   - Real-time processing capability

## Advantages and Disadvantages

### Advantages

- **Frequency Selectivity**: Precise control over passband
- **Noise Rejection**: Effective removal of unwanted frequencies
- **Phase Response**: Minimal distortion in passband
- **Computational Efficiency**: Optimized two-stage design
- **Flexibility**: Independent control of cutoff frequencies

### Disadvantages

- **Initialization Period**: Requires several bars for startup
- **Parameter Sensitivity**: Performance depends on cutoff selection
- **Complexity**: More complex than single-stage filters
- **Memory Usage**: Requires storing multiple previous values
- **Group Delay**: Higher than single-stage filters
