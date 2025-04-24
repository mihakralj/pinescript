# Triple Exponential Moving Average (TEMA)

## Historical Background

The Triple Exponential Moving Average (TEMA) was developed by Patrick Mulloy in 1994 as an extension of his DEMA concept. Published shortly after his work on DEMA, TEMA represented Mulloy's effort to further reduce lag while maintaining signal quality through a more sophisticated mathematical approach.

TEMA quickly gained popularity among technical analysts seeking maximum lag reduction. Its adoption has grown significantly in algorithmic trading systems and professional trading platforms. The indicator's elegant mathematical approach to lag reduction has influenced numerous advanced moving averages in technical analysis.

[Pine Script Implementation](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_IIR/tema.pine)

## Core Concepts

TEMA addresses the lag inherent in traditional moving averages through:

- Triple-cascade architecture for maximum lag reduction
- Strategic coefficient optimization (3, -3, 1) to minimize lag
- Balanced approach between responsiveness and stability
- Superior trend detection compared to EMA and DEMA

## Mathematical Foundation

TEMA = 3 × EMA(source) - 3 × EMA(EMA(source)) + EMA(EMA(EMA(source)))

Where:
- EMA(source) is the first exponential moving average of the source signal
- EMA(EMA(source)) is the second exponential moving average
- EMA(EMA(EMA(source))) is the third exponential moving average

## Calculation Process

1. Calculate first EMA:
   EMA_1 = EMA(source, period)

2. Calculate second EMA:
   EMA_2 = EMA(EMA_1, period)

3. Calculate third EMA:
   EMA_3 = EMA(EMA_2, period)

4. Apply TEMA formula:
   TEMA = 3 × EMA_1 - 3 × EMA_2 + EMA_3

The coefficients (3 and -3) are designed to effectively eliminate the inherent lag while maintaining a smooth output.

Like EMA and DEMA, TEMA uses a smoothing factor α calculated as:

α = 2/(period + 1)

The same α is used for all three EMA calculations to maintain consistency in the smoothing process.

## Implementation Details

TEMA implementation uses compensation techniques for all three EMA stages:

1. First EMA stage is compensated for initialization bias
2. Second EMA stage applies compensation to the output of the first stage
3. Third EMA stage applies compensation to the output of the second stage
4. The final TEMA combines all three compensated EMAs for accurate early values

This triple compensation ensures TEMA values are valid from the first bar without requiring a lengthy warm-up period.

## Advantages and Limitations

### Advantages
- Responds more quickly to signal changes than both EMA and DEMA
- Earlier identification of trend changes
- With compensation, provides accurate values from first bar
- Despite increased responsiveness, maintains reasonable smoothness
- The reduced lag can provide earlier entry/exit signals

### Limitations
- More aggressive lag reduction leads to more pronounced overshooting during sharp reversals
- Changes in period/α have more dramatic effects than in simpler moving averages
- Higher responsiveness can lead to more false signals in volatile markets
- Triple cascaded EMAs can compound calculation errors and make behavior less predictable
- More complex calculations compared to simpler moving averages

## Sources

1. Mulloy, P. (1994). "Smoothing Data with Less Lag," *Technical Analysis of Stocks & Commodities*.
2. Ehlers, J. (2001). *Rocket Science for Traders*. John Wiley & Sons.
3. Kaufman, P. (2013). *Trading Systems and Methods*, 5th Edition. Wiley Trading.
4. Mulloy, P. (1995). "Comparing Digital Filters," *Technical Analysis of Stocks & Commodities*.
