# TEMA: Triple Exponential Moving Average

[Pine Script Implementation of TEMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_IIR/tema.pine)

## Overview and Purpose

The Triple Exponential Moving Average (TEMA) is an advanced technical indicator designed to significantly reduce the lag inherent in traditional moving averages while maintaining signal quality. Developed by Patrick Mulloy in 1994 as an extension of his DEMA concept, TEMA employs a sophisticated triple-stage calculation process to provide exceptionally responsive market signals.

TEMA's mathematical approach goes beyond standard smoothing techniques by using a triple-cascade architecture with optimized coefficients. This makes it particularly valuable for traders who need earlier identification of trend changes without sacrificing reliability. Since its introduction, TEMA has become a key component in many algorithmic trading systems and professional trading platforms.

## Core Concepts

* **Triple-stage lag reduction:** TEMA uses a three-level EMA calculation with optimized coefficients (3, -3, 1) to dramatically minimize the delay in signal generation
* **Enhanced responsiveness:** Provides significantly faster reaction to price changes than standard EMA or even DEMA, while maintaining reasonable smoothness
* **Strategic signal processing:** Employs mathematical techniques to extract the underlying trend while filtering random price fluctuations
* **Timeframe effectiveness:** Performs well across multiple timeframes, though particularly valued in short to medium-term trading

TEMA achieves its enhanced responsiveness through an innovative triple-cascade architecture that strategically combines three levels of exponential moving averages. This approach effectively removes the lag component inherent in EMA calculations while preserving the essential smoothing benefits.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 12 | Controls sensitivity/smoothness | Increase in choppy markets, decrease in strongly trending markets |
| Source | Close | Data point used for calculation | Change to HL2/HLC3 for more balanced price representation |
| Visualization | Line | Display format on charts | Use filled cloud to see divergence from price more clearly |

**Pro Tip:** For optimal trade signals, many professional traders use two TEMAs (e.g., 8 and 21 periods) and look for crossovers, which often provide earlier signals than traditional moving average pairs.

## Calculation and Mathematical Foundation

**Simplified explanation:**
TEMA calculates three levels of EMAs, then combines them using a special formula that amplifies recent price action while reducing lag. This triple-processing approach effectively eliminates much of the delay found in traditional moving averages.

**Technical formula:**
TEMA = 3 × EMA₁ - 3 × EMA₂ + EMA₃

Where:
- EMA₁ = EMA(source, length)
- EMA₂ = EMA(EMA₁, length)
- EMA₃ = EMA(EMA₂, length)
- All EMAs use the same smoothing factor α = 2/(length + 1)

> 🔍 **Technical Note:** Advanced implementations apply compensation techniques to all three EMA stages, ensuring TEMA values are valid from the first bar without requiring a warm-up period. This compensation corrects initialization bias and prevents calculation errors from compounding through the cascade.

## Interpretation Details

TEMA excels at identifying trend changes significantly earlier than traditional moving averages, making it valuable for both entry and exit signals:

- When price crosses above TEMA, it often signals the beginning of an uptrend
- When price crosses below TEMA, it often signals the beginning of a downtrend  
- The slope of TEMA provides insight into trend strength and momentum
- TEMA crossovers with price tend to occur earlier than with standard EMAs
- When multiple-period TEMAs cross each other, they confirm significant trend shifts
- TEMA works exceptionally well as a dynamic support/resistance level in trending markets

For optimal results, traders often use TEMA in combination with momentum indicators or volume analysis to confirm signals and reduce false positives.

## Limitations and Considerations

* **Market conditions:** The high responsiveness can generate false signals during highly choppy, sideways markets
* **Overshooting:** More aggressive lag reduction leads to more pronounced overshooting during sharp reversals
* **Parameter sensitivity:** Changes in length have more dramatic effects than in simpler moving averages
* **Calculation complexity:** Triple cascaded EMAs make behavior less predictable and more resource-intensive
* **Complementary tools:** Should be used with confirmation tools like RSI, MACD or volume indicators

## References

1. Mulloy, P. (1994). "Smoothing Data with Less Lag," *Technical Analysis of Stocks & Commodities*.
2. Mulloy, P. (1995). "Comparing Digital Filters," *Technical Analysis of Stocks & Commodities*.
3. Kaufman, P. (2013). *Trading Systems and Methods*, 5th Edition. Wiley Trading.
