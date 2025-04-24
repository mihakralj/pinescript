# Double Exponential Moving Average (DEMA)

## Historical Background

The Double Exponential Moving Average (DEMA) was developed by Patrick Mulloy in 1994 and published in the February issue of Technical Analysis of Stocks & Commodities magazine. Mulloy sought to create a moving average that reduced the lag inherent in traditional EMAs while preserving signal quality.

Since its introduction, DEMA has gained significant popularity among technical analysts and has become a standard component in many trading platforms. It is widely used in algorithmic trading systems where minimizing lag without sacrificing reliability is crucial.

[Pine Script Implementation](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_IIR/dema.pine)

## Core Concepts

DEMA addresses the lag inherent in traditional moving averages while maintaining signal quality through:

- Double-smoothing to reduce noise while preserving trend information
- Strategic coefficient weighting (2× first EMA minus second EMA) to minimize lag
- Balanced approach between responsiveness and stability
- Improved trend detection compared to standard EMA

## Mathematical Foundation

$DEMA = 2 \times EMA(source) - EMA(EMA(source))$

Where:
- $EMA(source)$ is the first exponential moving average of the source signal
- $EMA(EMA(source))$ is the exponential moving average applied to the result of the first EMA

## Calculation Process

1. Calculate first EMA:
   $EMA_1 = EMA(source, period)$

2. Calculate second EMA:
   $EMA_2 = EMA(EMA_1, period)$

3. Apply DEMA formula:
   $DEMA = 2 \times EMA_1 - EMA_2$

The formula works by amplifying the first EMA (multiplying by 2) and then subtracting the second EMA. This mathematical approach reduces lag by compensating for the delay introduced in the smoothing process.

Like EMA, DEMA uses a smoothing factor α calculated as:

$\alpha = \frac{2}{period + 1}$

The same α is used for both EMA calculations to maintain consistency in the smoothing process.

## Technical Implementation

DEMA is a composite Infinite Impulse Response (IIR) filter that processes data through two EMAs with lag reduction. The implementation applies compensation techniques to both EMA stages:

1. First EMA stage is compensated for initialization bias
2. Second EMA stage applies compensation to the output of the first stage
3. The final DEMA combines both compensated EMAs

This approach improves accuracy of early values, reducing the need for extended warm-up periods.

## Advantages and Limitations

### Advantages
- Responds more quickly to price changes than standard EMA
- Follows trends while maintaining reasonable smoothness
- With compensation, provides usable values earlier
- Maintains better signal quality than simple lag-reduction methods
- Based on proven IIR filter principles

### Limitations
- Can overshoot the source signal during sharp reversals
- Small changes in period/α can significantly alter behavior
- Higher responsiveness may introduce noise in sideways markets
- Cascaded EMAs require more computational steps
- More complex to implement correctly than single-stage moving averages

## Sources

1. Mulloy, P. (1994). "Smoothing Data with Faster Moving Averages," *Technical Analysis of Stocks & Commodities*, February.
2. Ehlers, J. (2001). *Rocket Science for Traders*. John Wiley & Sons.
3. Kaufman, P. (2013). *Trading Systems and Methods*, 5th Edition. Wiley Trading.
