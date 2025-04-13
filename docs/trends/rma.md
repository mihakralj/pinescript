# Wilder's Moving Average (RMA/SMMA)

The Relative Moving Average (RMA), also known as Smoothed Moving Average (SMMA), was developed by J. Welles Wilder Jr. and introduced in his 1978 book "New Concepts in Technical Trading Systems". Wilder created this moving average specifically for calculating his revolutionary technical indicators, most notably the Relative Strength Index (RSI).

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

### Basic Formula

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

RMA is an Infinite Impulse Response (IIR) filter with specific properties:

1. **Infinite Memory**: Each output depends on all previous inputs extending to infinity
2. **Recursive Nature**: Each value depends on the previous calculated value
3. **Slower Decay**: Uses smaller α than EMA, leading to more emphasis on historical values
4. **No Fixed Window**: Unlike FIR filters, there is no fixed calculation window

### Transfer Function Properties

As a smoothed IIR filter, RMA provides:
- Slower response to signal changes than EMA (α = 1/period vs 2/(period+1))
- Approximately -3dB per octave roll-off in frequency domain
- Non-linear phase response due to recursive calculation
- Greater noise reduction than EMA at the cost of increased lag

For example, comparing smoothing factors:
- RMA(14): α = 0.0714
- EMA(14): α = 0.1333

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
