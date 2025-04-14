# Quadruple Exponential Moving Average (QEMA)

The Quadruple Exponential Moving Average (QEMA) extends the concept of TEMA by applying exponential moving average calculations four times. It further reduces lag compared to TEMA while maintaining signal smoothness, making it particularly effective for early trend detection and rapid market changes.

[Pine Script Implementation of QEMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends/qema.pine)

## Mathematical Foundation

QEMA = 4 × EMA₁ - 6 × EMA₂ + 4 × EMA₃ - EMA₄

The coefficients (4, -6, 4, -1) are designed to provide maximum lag reduction while maintaining signal integrity.

### Smoothing Factors

QEMA uses a progressive smoothing factor system:
- Base α₁ = often calculated as 2 / (period + 1)
- Each subsequent alpha increases by a ratio: α₂ = α₁ × ratio, α₃ = α₂ × ratio, α₄ = α₃ × ratio
- The ratio parameter allows fine-tuning of progressive smoothing (default = φ (golden ratio) ≈ 1.618)

## IIR Filter Characteristics

QEMA is a sophisticated Infinite Impulse Response (IIR) filter that processes data through four EMAs with enhanced lag reduction:

### Transfer Properties (Frequency Domain)

1. **Roll-off Rate**: Approximately -24dB per octave due to quadruple cascade
2. **Frequency Response**:
   - Superior high-frequency attenuation
   - Complex interaction between four EMA stages
3. **Phase Response**: Advanced non-linear response from quadruple IIR
4. **Gain**: Highly variable across frequencies due to 4/6/4/1 weighting:
   - Enhanced pass-through in transition band
   - Exceptional stopband attenuation

### Response Properties (Time Domain)

1. **Impulse Response**:
   - Quadruple infinite memory extent
   - Complex progressive smoothing interactions
   - Strategic stage weighting with ratio progression

2. **Step Response**:
   - Extremely fast rise time
   - Enhanced overshoot control through ratio parameter
   - Quick settling despite increased complexity

3. **Latency Properties**:
   - Minimal lag through quadruple compensation
   - Non-uniform delay across frequencies
   - Superior trend detection capability

## Initialization and Compensation

This implementation uses a sophisticated compensation technique:

1. All four EMA stages use progressive smoothing factors
2. Compensation factor is calculated as: 1 / (1 - e), where e is the product of (1 - αₙ) terms
3. Epsilon threshold (1e-10) prevents division by zero
4. The final QEMA applies compensation to the weighted sum of all EMAs

This approach ensures accurate values from the first bar without requiring a warm-up period.

### Progressive Smoothing

The progressive smoothing system with ratio parameter offers:
- Fine control over each EMA stage's responsiveness
- Optimized balance between lag reduction and noise filtering
- Customizable behavior through ratio adjustment
- Smooth transition between different smoothing levels

## Advantages and Disadvantages

### Advantages

- **Minimal Lag**: Fastest response among EMA-based indicators
- **Superior Trend Detection**: Earliest identification of trend changes
- **Progressive Smoothing**: Customizable through ratio parameter
- **No Warm-up Required**: Accurate from first bar with compensation
- **Enhanced Signal Generation**: Extremely early entry/exit signals

### Disadvantages

- **Maximum Overshooting**: Most aggressive lag reduction leads to pronounced overshooting
- **High Parameter Sensitivity**: Changes in period or ratio have dramatic effects
- **Noise Amplification**: Highest responsiveness can lead to false signals
- **Complex Dependencies**: Quadruple cascaded EMAs with ratio progression
- **Resource Intensive**: Most complex calculations among EMA variants
