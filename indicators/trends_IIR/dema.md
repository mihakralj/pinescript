# DEMA: Double Exponential Moving Average

[Pine Script Implementation of DEMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_IIR/dema.pine)

## Overview and Purpose

The Double Exponential Moving Average (DEMA) is a technical indicator designed to reduce the inherent lag of traditional moving averages while maintaining signal quality. Developed by Patrick Mulloy in 1994 and published in the February issue of Technical Analysis of Stocks & Commodities magazine, DEMA has become a popular tool for traders seeking more responsive trend identification.

DEMA accomplishes lag reduction by applying a formula that doubles the impact of the most recent data while filtering out excessive noise. This makes it particularly valuable in markets where traditional moving averages might be too slow to react to important price changes.

## Core Concepts

* **Lag reduction:** DEMA significantly reduces the delay in signal generation compared to standard EMAs, allowing for earlier identification of trend changes
* **Signal quality preservation:** Despite its increased responsiveness, DEMA maintains reasonable smoothness by using double-smoothing techniques
* **Strategic weighting:** Uses a mathematical formula (2× first EMA minus second EMA) that strategically amplifies recent price action while dampening noise
* **Timeframe suitability:** Most effective in short to medium timeframes where quick reaction to price changes is critical

DEMA achieves its enhanced responsiveness by essentially removing the lag component inherent in the EMA calculation itself, making it approximately twice as responsive as a standard EMA of the same length.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 14 | Controls sensitivity/smoothness | Increase in choppy markets, decrease in trending markets |
| Source | Close | Data point used for calculation | Change to High/Low for volatility focus, or use HL2/HLC3 for balanced price representation |
| Color threshold | 0 | Determines bullish/bearish visualization | Adjust based on instrument's typical momentum characteristics |

**Pro Tip:** Many professional traders use multiple DEMA lengths simultaneously (e.g., 9, 14, 21) to identify potential support/resistance levels where these lines converge or diverge.

## Calculation and Mathematical Foundation

**Simplified explanation:**
DEMA works by calculating two EMAs, then applying a formula that doubles the weight of the first EMA and subtracts the second EMA to reduce lag. This mathematical approach effectively removes the delay component while preserving most of the smoothing benefits.

**Technical formula:**
DEMA = 2 × EMA(source, length) - EMA(EMA(source, length), length)

Where:
- EMA(source, length) is the first exponential moving average of the price data
- EMA(EMA(source, length), length) is the second-order EMA (EMA of the first EMA)
- The smoothing factor α = 2/(length + 1) is used for both EMA calculations

> 🔍 **Technical Note:** DEMA can be understood as a composite Infinite Impulse Response (IIR) filter that employs compensation techniques to both EMA stages, which improves accuracy of early values and reduces warm-up periods.

## Interpretation Details

DEMA excels at identifying trend changes earlier than traditional moving averages, making it valuable for both entry and exit signals. Its primary advantages include:

- Earlier trend change detection compared to standard EMAs
- Cleaner signals during trending markets than simple moving averages
- Reduced whipsaws compared to other lag-reduction techniques
- Effective for both trend identification and dynamic support/resistance levels

For optimal results, traders typically use DEMA crossovers with price, multiple DEMA crossovers, or DEMA slope changes as actionable signals. The indicator performs particularly well in markets with clear trending behavior.

## Limitations and Considerations

* **Market conditions:** Performs poorly in highly choppy, sideways markets where the enhanced responsiveness can generate false signals
* **Lag factor:** While reduced compared to standard EMAs, some lag remains and can still be problematic in extremely volatile conditions
* **Overshooting:** Can overshoot the source signal during sharp reversals, potentially giving false reversal signals
* **Parameter sensitivity:** Small changes in length can significantly alter behavior, requiring careful optimization
* **Complementary tools:** Should be used alongside momentum indicators (RSI, MACD) or volume indicators for confirmation

## References

1. Mulloy, P. (1994). "Smoothing Data with Faster Moving Averages," *Technical Analysis of Stocks & Commodities*, February.
2. Kaufman, P. (2013). *Trading Systems and Methods*, 5th Edition. Wiley Trading.
