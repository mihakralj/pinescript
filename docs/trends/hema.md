# Hull Exponential Moving Average (HEMA)

The Hull Exponential Moving Average (HEMA) is an advanced technical indicator that adapts Alan Hull's original methodology by replacing Weighted Moving Averages (WMAs) with Exponential Moving Averages (EMAs). This adaptation maintains the lag reduction principles of the original Hull Moving Average while leveraging the superior noise-filtering properties of exponential weighting.

[Pine Script Implementation of HEMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends/hema.pine)

## Mathematical Foundation

### Basic Formula

HEMA is calculated using these steps:

1. Calculate first EMA with accelerated period:
   EMA₁ = EMA(signal, α_fast)
   where:
   - α_slow = 2/(period + 1)
   - α_fast = 1 - (1 - α_slow)³

2. Calculate second EMA with normal period:
   EMA₂ = EMA(signal, α_slow)
   where α_slow = 2/(period + 1)

3. Calculate weighted difference:
   diff = (1+ln(2)) × EMA₁ - ln(2) × EMA₂

4. Calculate final HEMA:
   HEMA = EMA(diff, α_final)
   where αfinal = 2/√(1 + (2/α_slow) - 1)

## IIR Filter Characteristics

HEMA is a composite Infinite Impulse Response (IIR) filter that processes data through multiple EMAs with sophisticated lag reduction. Its behavior can be analyzed in both frequency and time domains:

### Transfer Properties (Frequency Domain)

The frequency domain characteristics of HEMA include:
1. **Roll-off Rate**: Approximately -20dB per decade, smoother than HMA
2. **Frequency Response**:
   - Smoother high-frequency attenuation curve
   - Superior stopband rejection of noise
   - Minimal passband ripple
3. **Phase Response**: Non-linear phase shift increases with frequency
4. **Gain**: Controlled by logarithmically-derived coefficients:
   - Enhanced signal preservation in passband
   - Improved noise attenuation in stopband

### Response Properties (Time Domain)

The time domain characteristics demonstrate:
1. **Impulse Response**:
   - Infinite response tail (theoretically)
   - Exponential decay for past signals
   - Faster initial response than standard EMAs

2. **Step Response**:
   - Reduced rise time compared to traditional EMAs
   - Controlled overshoot compared to HMA
   - Graceful approach to new levels

3. **Latency Properties**:
   - Enhanced responsiveness through cubic acceleration
   - More consistent group delay across frequencies
   - Reduced overshooting at trend reversals

## Initialization Properties

This implementation uses sophisticated error compensation techniques:
1. Compensates for initialization bias using scaling factors
2. Adapts compensation during initial periods
3. Includes epsilon protection against division by zero
4. Automatically adjusts based on available data points

### Early Value Handling

1. **Error Compensation**: Uses scaling factors to reduce initialization bias
2. **Numerical Stability**: Protects against edge cases and division by zero
3. **Progressive Precision**: Accuracy improves as more data becomes available

## Advantages and Disadvantages

### Advantages

- **Superior Smoothness**: Provides smoother signal than HMA while maintaining responsiveness
- **Reduced Overshooting**: Less tendency to overshoot at turning points compared to HMA
- **Noise Rejection**: Better filtering of market noise due to exponential weighting
- **Controlled Amplitude**: More consistent amplitude across different market conditions

### Disadvantages

- **Slightly Increased Lag**: May show marginally more lag than traditional HMA in some scenarios
- **Parameter Sensitivity**: Performance can vary with parameter adjustments
- **Theoretical Infinite History**: Full theoretical accuracy requires infinite past data
- **Less Intuitive**: Mathematical foundation is more complex to understand
