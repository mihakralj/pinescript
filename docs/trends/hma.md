# Hull Moving Average (HMA)

The Hull Moving Average (HMA) is a technical indicator developed by Alan Hull to provide significantly reduced lag compared to traditional moving averages while maintaining smoothness in the resulting trend line. It uses weighted moving averages in a unique configuration that emphasizes recent price action and helps eliminate lag.

[Pine Script Implementation of HMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends/hma.pine)

## Mathematical Foundation

### Basic Formula

The HMA is calculated using the four steps:

1. Calculate WMA with period n/2: WMA₁ = WMA(price, n/2)

2. Calculate WMA with period n: WMA₂ = WMA(price, n)

3. Calculate the difference: diff = 2 × WMA₁ - WMA₂

4. Calculate final HMA with sqrt(n): HMA = WMA(diff, √n)

Where:
- n is the period of the HMA
- WMA is the Weighted Moving Average
- price is the input price series
- √n is the square root of n (rounded down)

### Weighted Moving Average Components

Each WMA component uses linear weighting where:
- Most recent price has highest weight
- Weights decrease linearly for older prices
- Sum of weights denominator = n(n+1)/2

## Filter Characteristics

The HMA combines multiple FIR filters (WMAs) in a unique configuration:

- Uses shorter period WMA (n/2) to capture rapid changes
- Uses full period WMA (n) for baseline trend
- Square root period in final WMA balances smoothing and responsiveness
- Difference amplification (2×) helps reduce lag

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
- **Overshooting Tendency**: The aggressive lag reduction can cause significant overshooting during sharp price reversals
- **Amplitude Distortion**: The 2× multiplier in the formula can exaggerate price movements
- **Gap Sensitivity**: More prone to creating gaps in the moving average line during price gaps or market closures
