# Endpoint Moving Average (EPMA)

The Endpoint Moving Average (EPMA) is a modified version of the Exponential Moving Average (EMA) that places additional emphasis on recent price movements. By applying increased weight to the endpoint (most recent) values, EPMA provides faster response to new price trends while maintaining the smoothing characteristics of traditional moving averages.

[Pine Script Implementation of EPMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends/epma.pine)

## Mathematical Foundation

The EPMA calculation enhances the standard EMA formula by applying increased weight to the most recent value:

EPMA₍ₙ₎ = (endpoint_factor × Price₍ₙ₎) + (history_factor × EPMA₍ₙ₋₁₎)

Where:
- EPMA₍ₙ₎ is the current EPMA value
- Price₍ₙ₎ is the current signal
- EPMA₍ₙ₋₁₎ is the previous EPMA value
- endpoint_factor = endpoint_weight × α
- history_factor = 1 - endpoint_factor

### Smoothing Factors

The EPMA uses two key factors in its calculation:

1. Base smoothing factor (α):
   α = (2 × endpoint_weight) / (period + endpoint_weight)

2. Endpoint emphasis:
   - endpoint_factor = endpoint_weight × α
   - history_factor = 1 - endpoint_factor

This dual-factor approach provides:
- Stronger emphasis on recent price movements
- Controlled decay of historical values
- Smoother transitions between values

## IIR Filter Characteristics

Like EMA, EPMA is an Infinite Impulse Response (IIR) filter with modified characteristics that enhance its responsiveness to recent price movements. The filter's behavior can be analyzed in both frequency and time domains:

### Transfer Properties (Frequency Domain)

The frequency domain characteristics of EPMA include:
1. **Roll-off Rate**: Steeper than standard EMA (-6dB/octave), due to endpoint emphasis
2. **Frequency Response**: Enhanced high-frequency pass-through compared to EMA
3. **Phase Response**: Non-linear, with increased lead at signal transitions
4. **Gain**: Variable based on endpoint weight, higher at transition frequencies

### Response Properties (Time Domain)

The time domain characteristics demonstrate:
1. **Impulse Response**:
   - Faster initial reaction to price changes
   - Steeper decay of historical values
   - Infinite response length (IIR nature)

2. **Step Response**:
   - Quicker rise time than standard EMA
   - Potential overshoot with higher endpoint weights
   - Faster settling time to steady state

3. **Convergence Properties**:
   - Shorter initialization period than EMA
   - Faster adaptation to trend changes
   - Dynamic response scaling with endpoint weight

## Initialization and Compensation

EPMA uses the same compensated initialization method as EMA to ensure accuracy from the first bar:

### Compensation Formula

EPMA₍corrected₎ = EPMA₍raw₎ / (1 - compensation)

Where:
- EPMA₍raw₎ is the standard EPMA calculation starting from zero
- Compensation starts at 1.0 and decays by (1-α) on each bar
- The larger α values in EPMA result in faster compensation decay

## Configuration Parameters

EPMA introduces an additional parameter compared to standard EMA:

### Endpoint Weight (1.0 - 3.0)

The endpoint weight parameter provides fine control over recent price emphasis:
- 1.0: Equivalent to standard EMA behavior
- 1.5 (default): Balanced between responsiveness and smoothing
- 2.0: Double emphasis on recent prices
- 3.0: Maximum emphasis, highly responsive to price changes

### Period (≥1)

The period parameter works in conjunction with endpoint weight:
- Default: 20 bars (optimal for most trading scenarios)
- Shorter periods (1-10): Quick response, best with lower endpoint weights
- Longer periods (20+): Smoother output, can handle higher endpoint weights
- The final smoothing effect combines both parameters

## Advantages and Disadvantages

### Advantages

- **Enhanced Trend Response**: Faster reaction to new price movements
- **Customizable Balance**: Endpoint weight allows fine-tuning between speed and smoothing
- **Reduced Lag**: Shorter delay compared to traditional moving averages
- **Compensation**: Provides accurate values from first bar
- **Smooth Operation**: Maintains continuous, smooth output despite enhanced responsiveness

### Disadvantages

- **Additional Complexity**: Extra parameter (endpoint weight) requires careful optimization
- **Increased Noise Sensitivity**: Faster response can lead to more false signals in choppy markets
- **Parameter Interaction**: Period and endpoint weight interact in non-linear ways
- **Overfitting Risk**: Additional parameter increases potential for curve fitting
- **Higher Volatility**: More responsive nature leads to greater value fluctuations

## Usage Guidelines

1. **Parameter Selection**:
   - Start with endpoint weight of 1.5 for balanced response
   - Adjust period first, then fine-tune endpoint weight
   - Lower periods benefit from lower endpoint weights

2. **Market Conditions**:
   - Higher endpoint weights work better in trending markets
   - Reduce endpoint weight in ranging or volatile markets
   - Consider market volatility when selecting parameters

3. **Signal Generation**:
   - Use crossing signals with caution due to increased responsiveness
   - Consider confirmation from other indicators
   - Monitor for whipsaws in choppy conditions

4. **Optimization**:
   - Test various endpoint weights across different market conditions
   - Balance between responsiveness and false signals
   - Consider using with longer periods to offset increased sensitivity
