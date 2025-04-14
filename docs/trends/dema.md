# Double Exponential Moving Average (DEMA)

The Double Exponential Moving Average (DEMA) is a technical indicator designed to reduce the lag inherent in traditional moving averages in exchange for the risk of overshooting. Created by Patrick Mulloy, DEMA applies the EMA calculation twice in a way that minimizes lag while maintaining smoothness. It's particularly useful in trending markets where traditional moving averages might be too slow to react to signal changes.

[Pine Script Implementation of DEMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends/dema.pine)

## Mathematical Foundation

DEMA = 2 × EMA(source) - EMA(EMA(source))

Where:
- EMA(source) is the first exponential moving average of the source signal
- EMA(EMA(source)) is the exponential moving average applied to the result of the first EMA

### Detailed Breakdown

1. Calculate first EMA:
   EMA₁ = EMA(source, period)

2. Calculate second EMA:
   EMA₂ = EMA(EMA₁, period)

3. Apply DEMA formula:
   DEMA = 2 × EMA₁ - EMA₂

The multiplication by 2 and subtraction of the second EMA effectively reduces lag by eliminating the inherent delay present in the smoothing process.

### Smoothing Factor

Like EMA, DEMA uses a smoothing factor α calculated as:

α = 2 / (period + 1)

The same α is used for both EMA calculations to maintain consistency in the smoothing process.

## IIR Filter Characteristics

DEMA is a composite Infinite Impulse Response (IIR) filter that processes data through two EMAs with lag reduction. Its behavior can be analyzed in both frequency and time domains:

### Transfer Properties (Frequency Domain)

The frequency domain characteristics of DEMA include:
1. **Roll-off Rate**: Steeper than single EMA due to cascaded filtering
2. **Frequency Response**:
   - Enhanced high-frequency pass-through from lag reduction
   - Complex interaction between cascaded EMAs
3. **Phase Response**: Non-linear due to dual IIR stages
4. **Gain**: Variable across frequencies due to 2× amplification:
   - Boosted response in transition band
   - Enhanced attenuation in stopband

### Response Properties (Time Domain)

The time domain characteristics demonstrate:
1. **Impulse Response**:
   - Infinite memory extent from both EMAs
   - Complex interaction between cascaded stages
   - Enhanced response to recent changes

2. **Step Response**:
   - Faster rise time than single EMA
   - Potential overshoot from lag reduction
   - Quicker settling to new levels

3. **Latency Properties**:
   - Reduced lag through 2× compensation
   - Variable delay across frequencies
   - More responsive to trend changes

## Initialization and Compensation

This implementation uses the same compensation technique as the EMA for both stages of calculation:

1. First EMA stage is compensated for initialization bias
2. Second EMA stage applies compensation to the output of the first stage
3. The final DEMA combines both compensated EMAs for accurate early values

This dual compensation ensures DEMA values are valid from the first bar without requiring a warm-up period.

### Alpha vs Period

As with EMA, DEMA can be fine-tuned using α directly instead of period:
- Provides more precise control over smoothing
- Avoids the discrete steps inherent in period-based calculations
- Allows for more sophisticated optimization in trading strategies

## Advantages and Disadvantages

### Advantages

- **Reduced Lag**: Responds more quickly to signal changes than standard EMA
- **Better Trend Tracking**: More effective at following trends while maintaining smoothness
- **No Warm-up Required**: With compensation, provides accurate values from first bar
- **Smooth Output**: Despite increased responsiveness, maintains smoother output than similar lag-reduction techniques
- **Mathematically Sound**: Based on well-understood IIR filter principles

### Disadvantages

- **Overshooting**: The mechanism that reduces lag will cause overshooting the source signal during sharp reversals or volatile periods.
- **Parameter Sensitivity**: Small changes in period/α can have amplified effects
- **Noise in Volatile Markets**: Higher responsiveness can lead to more noise in sideways markets
- **Multiple IIR Dependencies**: Cascaded EMAs can compound any calculation errors
