# Deviation-Scaled Moving Average (DSMA)

The Deviation-Scaled Moving Average is an adaptive IIR filter that adjusts its smoothing factor based on market volatility. Introduced in the early 2000s as markets became increasingly electronic and volatile, DSMA gained adoption among algorithmic traders seeking more responsive indicators. It dynamically increases responsiveness during high-deviation periods while maintaining stability during normal conditions. This approach creates a balance between noise reduction in stable markets and quick adaptation during volatile phases, making it particularly useful in modern trading environments with rapidly changing market conditions.

[Pine Script Implementation of DSMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_IIR/dsma.pine)

## Mathematical Foundation

The DSMA calculation uses a dynamically adjusted smoothing factor (α) that scales based on the normalized deviation of the current price from its moving average:

DSMA₍ₙ₎ = α × Price₍ₙ₎ + (1 - α) × DSMA₍ₙ₋₁₎

Where:

- DSMA₍ₙ₎ is the current DSMA value
- Price₍ₙ₎ is the current signal
- DSMA₍ₙ₋₁₎ is the previous DSMA value
- α is the adaptive smoothing factor

### Adaptive Smoothing Factor

The adaptive smoothing factor α is calculated as:

α = min(scale_factor × |filt/rms| × (5/period), 1.0)

Where:

- scale_factor is the base scaling factor (0.01-0.9)
- filt is the filtered deviation from moving average
- rms is the root mean square of filtered deviations
- period is the lookback window size

### Filter Calculation

The filtered deviation (filt) is computed using a second-order IIR filter:

filt₍ₙ₎ = c₁/2 × (zeros₍ₙ₎ + zeros₍ₙ₋₁₎) + b₁ × filt₍ₙ₋₁₎ - a₁² × filt₍ₙ₋₂₎

Where:

- zeros₍ₙ₎ = Price₍ₙ₎ - DSMA₍ₙ₎
- a₁ = exp(-1.414π/period)
- b₁ = 2a₁cos(1.414π/period)
- c₁ = 1 - b₁ + a₁²

## Implementation Details

The Pine Script implementation includes several optimizations:

### 1. Memory Management

- Efficient array usage for deviation history
- Single-pass RMS calculation
- Minimal variable allocation

### 2. Computational Optimization

- Combined filter calculations
- Optimized square root operations
- Reduced redundant calculations

### 3. Numerical Stability

- Protected division operations
- Bounded smoothing factor
- Proper initialization of all variables

## Parameter Selection

Three key parameters control DSMA behavior:

### 1. Period

Controls the lookback window and filter characteristics:

- Smaller values (10-20): More responsive, less stable
- Larger values (25-50): More stable, less responsive
- Typical range: 20-30 for most applications

### 2. Scale Factor

Determines the intensity of volatility adaptation:

- Lower values (0.01-0.3): Subtle adaptation
- Higher values (0.5-0.9): Aggressive adaptation
- Typical range: 0.4-0.7 for balanced response

### 3. Source

Input data selection affects filter behavior:

- Close price: Most common, balanced
- High/Low: More volatile response
- HL2/HLC3: Reduced noise input

## Performance Considerations

### Advantages

1. **Adaptive Response**:
   - Automatically adjusts to market conditions
   - No manual intervention needed
   - Balance between speed and stability

2. **Noise Handling**:
   - Effective filtering during stable periods
   - Intelligent noise reduction
   - Maintains signal clarity

3. **Performance**:
   - Efficient execution
   - Memory efficient
   - Reasonable computational requirements

### Limitations

1. **Complexity**:
   - More complex than simple moving averages
   - Multiple parameters to tune
   - Higher computational requirements

2. **Parameter Sensitivity**:
   - Results vary with parameter selection
   - Requires careful optimization
   - Potential for overfitting

3. **Statistical Considerations**:
   - Assumes normal distribution
   - May lag in extremely volatile conditions
   - Requires sufficient data for accurate deviation calculation
