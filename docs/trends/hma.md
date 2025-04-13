# Hull Moving Average (HMA)

The Hull Moving Average (HMA) is a technical indicator developed by Alan Hull to provide significantly reduced lag compared to traditional moving averages while maintaining smoothness in the resulting trend line. It uses weighted moving averages in a unique configuration that emphasizes recent signal action and helps eliminate lag.

[Pine Script Implementation of HMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends/hma.pine)

## Mathematical Foundation

### Basic Formula

The HMA is calculated using the four steps:

1. Calculate WMA with period n/2: WMA₁ = WMA(signal, n/2)

2. Calculate WMA with period n: WMA₂ = WMA(signal, n)

3. Calculate the difference: diff = 2 × WMA₁ - WMA₂

4. Calculate final HMA with sqrt(n): HMA = WMA(diff, √n)

Where:
- n is the period of the HMA
- WMA is the Weighted Moving Average
- signal is the input signal series
- √n is the square root of n (rounded down)

### Weighted Moving Average Components

Each WMA component uses linear weighting where:
- Most recent signal has highest weight
- Weights decrease linearly for older signals
- Sum of weights denominator = n(n+1)/2

## FIR Filter Characteristics

The HMA is a composite Finite Impulse Response (FIR) filter that processes data through multiple stages. Its behavior can be analyzed in both frequency and time domains:

### Transfer Properties (Frequency Domain)

The frequency domain characteristics of HMA include:
1. **Roll-off Rate**: Approximately -24dB per octave roll-off
2. **Frequency Response**:
   - Enhanced high-frequency pass-through from period-halving
   - Improved noise reduction in stopband
3. **Phase Response**: Non-linear due to multi-stage processing
4. **Gain**: Variable across frequencies due to 2× amplification

### Response Properties (Time Domain)

The time domain characteristics demonstrate:
1. **Impulse Response**:
   - Multi-scale processing through different periods
   - Zero response outside component windows
   - Complex interaction between WMA stages

2. **Step Response**:
   - Faster rise time than traditional MAs
   - Potential overshoot due to lag reduction
   - Quick settling to new levels

3. **Latency Properties**:
   - Reduced lag through period-halving
   - Variable delay across frequencies
   - Enhanced momentum through 2× amplification

## Initialization Properties

- First WMA needs n/2 periods
- Second WMA needs n periods
- Final WMA needs √n periods
- Full calculation is available after n periods

### Early Value Handling

1. **Partial Window Calculation**: Can calculate with available data points
2. **NA Values**: Return "not available" until minimum data requirements met
3. **Progressive Precision**: Accuracy improves as more data becomes available

## Advantages and Disadvantages

### Advantages

- **Minimal Lag**: Significantly less lag than traditional moving averages
- **Noise Reduction**: Maintains smooth output despite increased responsiveness
- **Early Signal Generation**: Faster response to trend changes
- **Built-in Momentum**: The 2× multiplier helps capture momentum
- **Self-Correcting**: Multiple timeframe inputs help confirm trends

### Disadvantages

- **Potential Whipsaws**: Higher responsiveness can lead to false signals in choppy markets
- **Non-Traditional Periods**: Square numbers as optimal periods may not align with traditional analysis periods
- **Overshooting Tendency**: The aggressive lag reduction can cause significant overshooting during sharp signal reversals
- **Amplitude Distortion**: The 2× multiplier in the formula can exaggerate signal movements
- **Gap Sensitivity**: More prone to creating gaps in the moving average line during signal gaps or market closures
