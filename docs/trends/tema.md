# Triple Exponential Moving Average (TEMA)

The Triple Exponential Moving Average (TEMA) is a technical indicator that extends the concept of DEMA by applying exponential moving average calculations three times. Developed by Patrick Mulloy, TEMA further reduces the lag in price action while maintaining smoothness. It's particularly effective in identifying trend changes earlier than traditional moving averages or even DEMA.

[Pine Script Implementation of TEMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends/tema.pine)

## Mathematical Foundation

### Basic Formula

TEMA is calculated using the following formula:

TEMA = 3 × EMA(source) - 3 × EMA(EMA(source)) + EMA(EMA(EMA(source)))

Where:
- EMA(source) is the first exponential moving average of the source price
- EMA(EMA(source)) is the second exponential moving average
- EMA(EMA(EMA(source))) is the third exponential moving average

### Detailed Breakdown

1. Calculate first EMA:
   EMA₁ = EMA(source, period)

2. Calculate second EMA:
   EMA₂ = EMA(EMA₁, period)

3. Calculate third EMA:
   EMA₃ = EMA(EMA₂, period)

4. Apply TEMA formula:
   TEMA = 3 × EMA₁ - 3 × EMA₂ + EMA₃

The coefficients (3 and -3) are designed to effectively eliminate the inherent lag while maintaining a smooth output.

### Smoothing Factor

Like EMA and DEMA, TEMA uses a smoothing factor α calculated as:

α = 2 / (period + 1)

The same α is used for all three EMA calculations to maintain consistency in the smoothing process.

## IIR Filter Characteristics

TEMA employs three cascaded IIR filters (EMAs) combined in a way that significantly reduces lag:

- The first EMA provides basic smoothing
- The second EMA adds depth to the smoothing process
- The third EMA, when combined with the weighted first and second EMAs, creates a sophisticated filter response
- The overall effect provides exceptional responsiveness while maintaining reasonable smoothness

## Initialization and Compensation

This implementation uses compensation techniques for all three EMA stages:

1. First EMA stage is compensated for initialization bias
2. Second EMA stage applies compensation to the output of the first stage
3. Third EMA stage applies compensation to the output of the second stage
4. The final TEMA combines all three compensated EMAs for accurate early values

This triple compensation ensures TEMA values are valid from the first bar without requiring a warm-up period.

### Alpha vs Period

As with other IIR moving averages, TEMA can be fine-tuned using α directly instead of period:
- Provides more precise control over smoothing
- Avoids the discrete steps inherent in period-based calculations
- Allows for more sophisticated optimization in trading strategies

## Advantages and Disadvantages

### Advantages

- **Minimal Lag**: Responds more quickly to price changes than both EMA and DEMA
- **Superior Trend Detection**: Earlier identification of trend changes
- **No Warm-up Required**: With compensation, provides accurate values from first bar
- **Smooth Output**: Despite increased responsiveness, maintains reasonable smoothness
- **Enhanced Signal Generation**: The reduced lag can provide earlier entry/exit signals

### Disadvantages

- **Increased Overshooting**: More aggressive lag reduction leads to more pronounced overshooting during sharp reversals
- **Higher Parameter Sensitivity**: Changes in period/α have more dramatic effects than in simpler moving averages
- **Noise Amplification**: Higher responsiveness can lead to more false signals in volatile markets
- **Complex Dependencies**: Triple cascaded EMAs can compound calculation errors and make behavior less predictable
- **Resource Intensive**: More complex calculations compared to simpler moving averages
