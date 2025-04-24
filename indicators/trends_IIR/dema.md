# Double Exponential Moving Average (DEMA)

The Double Exponential Moving Average is a dual-stage IIR filter that reduces lag compared to standard EMAs. Developed by Patrick Mulloy in 1994 and published in the February issue of Technical Analysis of Stocks & Commodities magazine, DEMA quickly gained popularity among technical analysts. It achieves lag reduction through a mathematical approach that applies a second EMA to the first EMA result, then uses these values in a formula designed to minimize delay while preserving signal quality. Since its introduction, DEMA has become a standard component in many trading platforms and is widely used in algorithmic trading systems.

[Pine Script Implementation of DEMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_IIR/dema.pine)

## Mathematical Foundation

DEMA = 2 × EMA(source) - EMA(EMA(source))

Where:

- EMA(source) is the first exponential moving average of the source signal
- EMA(EMA(source)) is the exponential moving average applied to the result of the first EMA

### Calculation Process

1. Calculate first EMA:
   EMA₁ = EMA(source, period)

2. Calculate second EMA:
   EMA₂ = EMA(EMA₁, period)

3. Apply DEMA formula:
   DEMA = 2 × EMA₁ - EMA₂

The formula works by amplifying the first EMA (multiplying by 2) and then subtracting the second EMA. This mathematical approach reduces lag by compensating for the delay introduced in the smoothing process.

### Smoothing Factor

Like EMA, DEMA uses a smoothing factor α calculated as:

α = 2 / (period + 1)

The same α is used for both EMA calculations to maintain consistency in the smoothing process.

## Technical Characteristics

DEMA is a composite Infinite Impulse Response (IIR) filter that processes data through two EMAs with lag reduction. Its behavior can be analyzed in both frequency and time domains.

### Initialization and Compensation

This implementation applies compensation techniques to both EMA stages:

1. First EMA stage is compensated for initialization bias
2. Second EMA stage applies compensation to the output of the first stage
3. The final DEMA combines both compensated EMAs

This approach improves accuracy of early values, reducing the need for extended warm-up periods.

### Alpha vs Period

As with EMA, DEMA can be fine-tuned using α directly instead of period:

- Provides more precise control over smoothing
- Avoids the discrete steps inherent in period-based calculations
- Allows for more sophisticated optimization in trading strategies

## Performance Considerations

### Advantages

- **Reduced Lag**: Responds more quickly to price changes than standard EMA
- **Improved Trend Tracking**: Follows trends while maintaining reasonable smoothness
- **Minimal Warm-up**: With compensation, provides usable values earlier
- **Signal Quality**: Maintains better signal quality than simple lag-reduction methods
- **Established Method**: Based on proven IIR filter principles

### Limitations

- **Overshooting**: Can overshoot the source signal during sharp reversals
- **Parameter Sensitivity**: Small changes in period/α can significantly alter behavior
- **Noise Handling**: Higher responsiveness may introduce noise in sideways markets
- **Calculation Complexity**: Cascaded EMAs require more computational steps

