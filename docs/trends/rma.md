# Wilder's Moving Average (RMA/SMMA)

The wildeR (Relative) Moving Average (RMA), also known as Smoothed Moving Average (SMMA), was developed by J. Welles Wilder Jr. and introduced in his 1978 book "New Concepts in Technical Trading Systems". Wilder created this moving average specifically for calculating his revolutionary technical indicators, most notably the Relative Strength Index (RSI).

[Pine Script Implementation of RMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends/rma.pine)

## Historical Context and Purpose

Wilder needed a moving average that would be more responsive than SMA but less volatile than EMA for his technical indicators. His solution was to use a modified exponential moving average with a specific smoothing factor of 1/period, which became known as RMA. This smoothing factor creates a more stable line that reduces noise while maintaining sensitivity to signal changes.

### Primary Applications

RMA is a core component in several of Wilder's indicators:
- Relative Strength Index (RSI)
- Average True Range (ATR)
- Average Directional Index (ADX)
- Directional Movement Index (DMI)

## Mathematical Foundation

The RMA calculation uses Wilder's specific smoothing approach:

RMA₍ₙ₎ = (RMA₍ₙ₋₁₎ × (period - 1) + Price₍ₙ₎) / period

Where:
- RMA₍ₙ₎ is the current RMA value
- RMA₍ₙ₋₁₎ is the previous RMA value
- Price₍ₙ₎ is the current signal
- period is the lookback period

### Optimized Formula

The formula can be rewritten in terms of alpha (α = 1/period):

RMA₍ₙ₎ = α × Price₍ₙ₎ + (1 - α) × RMA₍ₙ₋₁₎

This form shows RMA as a specific case of exponential smoothing where α = 1/period.

## IIR Filter Characteristics

RMA is an Infinite Impulse Response (IIR) filter that processes data through recursive calculation with Wilder's specific smoothing. Its behavior can be analyzed in both frequency and time domains:

### Transfer Properties (Frequency Domain)

The frequency domain characteristics of RMA include:
1. **Roll-off Rate**: Approximately -3dB per octave, gentler than EMA
2. **Frequency Response**:
   - Enhanced noise reduction compared to EMA
   - Smoother attenuation curve
3. **Phase Response**: Non-linear due to recursive calculation
4. **Gain**: More conservative than EMA due to smaller α:
   - RMA(14): α = 0.0714
   - EMA(14): α = 0.1333 (for comparison)

### Response Properties (Time Domain)

The time domain characteristics demonstrate:
1. **Impulse Response**:
   - Infinite memory extent
   - Slower exponential decay than EMA
   - Greater emphasis on historical values

2. **Step Response**:
   - More gradual transition than EMA
   - Minimal overshoot characteristics
   - Longer settling time than EMA

3. **Smoothing Properties**:
   - Enhanced noise reduction
   - Increased lag compared to EMA
   - Consistent smoothing behavior

## Initialization Methods

### 1. SMA Initialization (Traditional)

Traditionally, RMA is initialized using SMA for the first period's worth of data. This approach:
- Provides a reasonable starting point
- Creates a discontinuity when switching from SMA to RMA
- Requires waiting for a full period before getting meaningful values

### 2. Compensated Initialization (this Implementation)

This implementation uses the same compensation technique as our EMA implementation:
1. Starts calculation from first bar with zero initialization
2. Tracks the influence of missing history through a compensation factor
3. Adjusts the raw RMA value based on this compensation
4. Gradually reduces compensation as more data becomes available

### The Compensation Formula

The corrected RMA is calculated as:

RMA₍corrected₎ = RMA₍raw₎ / (1 - compensation)

Where:
- RMA₍raw₎ is the standard RMA calculation
- Compensation decays by (1-α) each bar
- α = 1/period (Wilder's smoothing factor)

## Advantages and Disadvantages

### Advantages

- **Stability**: Smoother than EMA, reducing noise in technical indicators
- **Memory Efficient**: Only needs previous value, not entire lookback period
- **Consistency**: Works well with Wilder's technical indicators
- **No Warm-up**: With compensation, provides accurate values from first bar
- **Smooth Transition**: Avoids initialization discontinuities

### Disadvantages

- **More Lag**: Slower to respond to signal changes than EMA
- **Limited Usage**: Primarily used in Wilder's indicators
- **Fixed Smoothing**: Less flexible than EMA in terms of smoothing factor
- **Recursive Nature**: Calculation errors compound over time
- **Historical Dependency**: Each value depends on all previous values
