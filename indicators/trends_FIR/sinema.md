# SINEMA: Sine Weighted Moving Average

[Pine Script Implementation of SINEMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_FIR/sinema.pine)

## Overview and Purpose

The Sine Weighted Moving Average (SINEMA) is a technical indicator that applies sine wave-based weighting to price data. Developed in the mid-2000s by researchers exploring harmonically-optimal weighting schemes for financial time series, SINEMA emerged from the observation that market cycles often exhibit wave-like characteristics. The indicator gained traction in the 2010s as traders sought moving averages that could better align with natural market rhythms. By using a trigonometric weighting scheme, SINEMA creates a bell-shaped distribution that emphasizes central price points while naturally tapering weight toward both ends, providing effective noise reduction while maintaining important price signals.

## Core Concepts

* **Sine wave weighting:** SINEMA uses a trigonometric function to create a natural bell-shaped weight distribution that aligns with wave-like market behavior
* **Harmonically-aligned filtering:** The sinusoidal weighting scheme potentially synchronizes better with the cyclical nature of market movements
* **Timeframe flexibility:** Works effectively across all timeframes with appropriate period adjustments

The core innovation of SINEMA is its application of sine-based weighting to price data. Unlike simpler moving averages, SINEMA's trigonometric weighting creates a distribution that naturally aligns with the wave-like patterns often observed in market price movements. This creates smooth transitions without abrupt weight changes and maintains perfect boundary conditions with zero endpoint influence.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 14 | Controls the lookback period | Increase for smoother signals in volatile markets, decrease for responsiveness |
| Source | close | Price data used for calculation | Consider using hlc3 for a more balanced price representation |

**Pro Tip:** SINEMA tends to perform well with lengths that match suspected market cycles - try using Fourier analysis or cycle identification tools to determine appropriate length settings for your specific market.

## Calculation and Mathematical Foundation

**Simplified explanation:**
SINEMA calculates a weighted average of prices where the weights follow a sine wave pattern. This creates a bell-shaped curve that gives most importance to prices in the middle of the lookback period and gradually less importance to prices at both ends, creating a smooth filter that effectively reduces market noise.

**Technical formula:**
SINEMA(t) = Σ(P(i) × w(i)) / Σw(i)

Where:
- P(i) = Price at position i
- w(i) = sin(π × (i + 1) / period)
- i ranges from 0 to period-1
- period = lookback window size

> 🔍 **Technical Note:** The sine function naturally creates a bell-shaped weighting curve that reaches maximum at the middle of the period and tapers to zero at the boundaries, providing a smooth transition without the need for additional windowing functions.

## Interpretation Details

SINEMA can be used in various trading strategies:

* **Trend identification:** The direction of SINEMA indicates the prevailing trend
* **Signal generation:** Crossovers between price and SINEMA generate trade signals
* **Support/resistance levels:** SINEMA can act as dynamic support during uptrends and resistance during downtrends
* **Trend strength assessment:** Distance between price and SINEMA can indicate trend strength
* **Cycle analysis:** The sine-based nature of SINEMA makes it particularly useful when analyzing markets with cyclical behavior

## Limitations and Considerations

* **Market conditions:** Like all moving averages, less effective in choppy, sideways markets
* **Fixed weighting scheme:** Cannot adapt weights to changing market conditions like adaptive moving averages
* **Mid-period bias:** Always weights the middle of the period highest, which may not be optimal for all market conditions
* **Computational complexity:** More complex calculations than simple averaging methods
* **Complementary tools:** Best used with momentum oscillators or cycle identification tools for confirmation

## References

* Dayal, B.S. "Trading with Sine Wave Moving Averages." Technical Analysis of Stocks & Commodities, 2011
* Ehlers, J.F. "Cycle Analytics for Traders." Wiley, 2013
