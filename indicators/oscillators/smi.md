# SMI: Stochastic Momentum Index

[Pine Script Implementation of SMI](https://github.com/mihakralj/pinescript/blob/main/indicators/oscillators/smi.pine)

## Overview and Purpose

The Stochastic Momentum Index (SMI) is a momentum oscillator developed by William Blau that enhances the traditional Stochastic oscillator by measuring the distance of the current close from the midpoint of the high-low range, rather than from the extremes. This fundamental difference creates a zero-centered oscillator that provides clearer directional bias and more refined momentum analysis.

Unlike traditional Stochastic which measures position relative to the range extremes (0-100 scale), SMI measures position relative to the range center (-100 to +100 scale), making trend direction immediately apparent through the zero line. The indicator applies sophisticated double exponential smoothing to reduce noise while maintaining sensitivity to momentum shifts, making it particularly effective for identifying trend changes and divergence patterns.

## Core Concepts

* **Midpoint reference system:** Uses the center of the high-low range as its baseline, providing a natural zero-centered scale that immediately indicates bullish (positive) or bearish (negative) momentum
* **Double smoothing process:** Applies exponential moving averages twice to create the %K line, reducing false signals while preserving responsiveness to meaningful price movements
* **Zero-line dynamics:** The zero line serves as a critical reference point for momentum direction changes and trend identification
* **Enhanced divergence detection:** The midpoint reference and smoothing combination makes SMI particularly sensitive to momentum shifts before they become evident in price action

SMI's mathematical approach of referencing the range midpoint rather than extremes provides a more balanced view of price momentum, while the dual calculation methods (Blau vs. Chande/Kroll) offer flexibility for different market conditions and trading styles.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| %K Period | 10 | Lookback period for high/low range calculation | Lower (5-8) for faster signals in active markets, higher (15-20) for smoother signals in ranging markets |
| %K Smooth | 3 | First smoothing period for raw SMI values | Lower values increase responsiveness, higher values reduce noise |
| %D Smooth | 3 | Second smoothing period for signal line | Adjust based on desired signal line sensitivity |
| Method | Blau | Calculation method selection | Blau for responsiveness, Chande/Kroll for smoother signals |

**Pro Tip:** SMI's zero-centered scale makes it excellent for divergence analysis - watch for price making new highs/lows while SMI fails to confirm, often indicating momentum exhaustion and potential reversal points.

## Calculation and Mathematical Foundation

**Simplified explanation:**
SMI calculates where the current closing price sits relative to the midpoint of the recent high-low range, then applies double smoothing to create reliable momentum signals. The indicator offers two calculation methods with different smoothing approaches.

**Technical formulas:**

**Blau Method (Original):**
```
Range Midpoint = (Highest High + Lowest Low) / 2
Half Range = (Highest High - Lowest Low) / 2
Raw SMI = 100 × (Close - Midpoint) / Half Range
%K = EMA(EMA(Raw SMI, %K Smooth), %K Smooth)
%D = EMA(%K, %D Smooth)
```

**Chande/Kroll Method (Alternative):**
```
Numerator = Close - Midpoint
Denominator = Half Range
Smoothed Numerator = EMA(EMA(Numerator, %K Smooth), %K Smooth)
Smoothed Denominator = EMA(EMA(Denominator, %K Smooth), %K Smooth)
%K = 100 × Smoothed Numerator / Smoothed Denominator
%D = EMA(%K, %D Smooth)
```

Where:
* Highest High and Lowest Low are calculated over the %K Period
* EMA is the Exponential Moving Average
* The Blau method smooths the ratio, while Chande/Kroll smooths the components separately

> 🔍 **Technical Note:** The implementation uses compensated EMA calculations that provide accurate values from the first bar through sophisticated warm-up compensation. Each EMA stage maintains individual compensators (e₁, e₂, e₃) that track convergence independently, with a unified warmup control that continues until the slowest EMA converges (e > 1e-10). This ensures mathematical precision throughout the calculation chain while optimizing performance by eliminating compensation overhead after the brief warmup period.

## Interpretation Details

SMI offers several powerful approaches to momentum analysis:

* **Zero-line analysis:** Values above zero indicate bullish momentum (price above range midpoint), while values below zero indicate bearish momentum (price below range midpoint)
* **Signal line crossovers:** When %K crosses above %D, it suggests strengthening momentum in the current direction; when %K crosses below %D, it suggests weakening momentum
* **Extreme readings:** Values above +40 may indicate overbought conditions, while values below -40 may indicate oversold conditions, though strong trends can maintain extreme readings
* **Divergence patterns:** SMI's enhanced sensitivity makes it excellent for identifying when price and momentum diverge, often preceding significant reversals
* **Method selection:** Blau method provides more responsive signals for trending markets, while Chande/Kroll method offers smoother signals for choppy or high-volatility conditions

The choice between calculation methods depends on market conditions: use Blau for immediate responsiveness in trending markets, or Chande/Kroll for stability in volatile or range-bound markets.

## Limitations and Considerations

* **Method complexity:** Dual calculation methods add complexity compared to basic oscillators; traders must understand when to use each approach
* **Zero-line familiarity:** Requires understanding of zero-centered dynamics, which differs from traditional 0-100 oscillators
* **Parameter sensitivity:** Performance varies significantly with different smoothing periods and calculation methods
* **Market condition dependency:** Blau method may be too responsive in choppy markets, while Chande/Kroll may lag in fast-moving trends
* **Complementary analysis:** Most effective when combined with trend indicators or volume studies for confirmation of signals
* **Timeframe considerations:** Shorter timeframes may require Blau method for responsiveness, while longer timeframes may benefit from Chande/Kroll smoothing

## References

* Blau, W. (1995). *Momentum, Direction and Divergence*. John Wiley & Sons.
* Chande, T. S., & Kroll, S. (1994). *The New Technical Trader*. John Wiley & Sons.
