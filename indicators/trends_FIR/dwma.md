# DWMA: Double Weighted Moving Average

[Pine Script Implementation of DWMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_FIR/dwma.pine)

## Overview and Purpose

The Double Weighted Moving Average (DWMA) is a technical indicator that applies weighted averaging twice in sequence to create a smoother signal with enhanced noise reduction. Developed in the late 1990s as an evolution of traditional weighted moving averages, the DWMA was created by quantitative analysts seeking enhanced smoothing without the excessive lag typically associated with longer period averages. By applying a weighted moving average calculation to the results of an initial weighted moving average, DWMA achieves more effective filtering while preserving important trend characteristics.

## Core Concepts

* **Cascaded filtering:** DWMA applies weighted averaging twice in sequence for enhanced smoothing and superior noise reduction
* **Linear weighting:** Uses progressively increasing weights for more recent data in both calculation passes
* **Market application:** Particularly effective for trend following strategies where noise reduction is prioritized over rapid signal response
* **Timeframe flexibility:** Works across multiple timeframes but particularly valuable on daily and weekly charts for identifying significant trends

The core innovation of DWMA is its two-stage approach that creates more effective noise filtering while minimizing the additional lag typically associated with longer-period or higher-order filters. This sequential processing creates a more refined output that balances noise reduction and signal preservation better than simply increasing the length of a standard weighted moving average.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 14 | Controls the lookback period for both WMA calculations | Increase for smoother signals in volatile markets, decrease for more responsiveness |
| Source | close | Price data used for calculation | Consider using hlc3 for a more balanced price representation |

**Pro Tip:** For trend following, use a length of 10-14 with DWMA instead of a single WMA with double the period - this provides better smoothing with less lag than simply increasing the period of a standard WMA.

## Calculation and Mathematical Foundation

**Simplified explanation:**
DWMA first calculates a weighted moving average where recent prices have more importance than older prices. Then, it applies the same weighted calculation again to the results of the first calculation, creating a smoother line that reduces market noise more effectively.

**Technical formula:**
DWMA is calculated by applying WMA twice:

1. First WMA calculation:
   WMA₁ = (P₁ × w₁ + P₂ × w₂ + ... + Pₙ × wₙ) / (w₁ + w₂ + ... + wₙ)

2. Second WMA calculation applied to WMA₁:
   DWMA = (WMA₁₁ × w₁ + WMA₁₂ × w₂ + ... + WMA₁ₙ × wₙ) / (w₁ + w₂ + ... + wₙ)

Where:
- Linear weights: most recent value has weight = n, second most recent has weight = n-1, etc.
- n is the period length

> 🔍 **Technical Note:** The dual-pass approach creates a filter that effectively increases smoothing without the quadratic increase in lag that would come from doubling the period of a single WMA.

## Interpretation Details

DWMA can be used in various trading strategies:

* **Trend identification:** The direction of DWMA indicates the prevailing trend
* **Signal generation:** Crossovers between price and DWMA generate trade signals, though they occur later than with single WMA
* **Support/resistance levels:** DWMA can act as dynamic support during uptrends and resistance during downtrends
* **Trend strength assessment:** Distance between price and DWMA can indicate trend strength
* **Noise filtering:** Using DWMA to filter noisy price data before applying other indicators

## Limitations and Considerations

* **Market conditions:** Less effective in choppy, sideways markets where its lag becomes a disadvantage
* **Lag factor:** More lag than single WMA due to double calculation process
* **Initialization requirement:** Requires more data points for full calculation, showing more NA values at chart start
* **Short-term trading:** May miss short-term trading opportunities due to increased smoothing
* **Complementary tools:** Best used with momentum oscillators or volume indicators for confirmation

## References

* Jurik, M. "Double Weighted Moving Averages: Theory and Applications in Algorithmic Trading Systems", Jurik Research Papers, 2004
* Ehlers, J.F. "Cycle Analytics for Traders," Wiley, 2013
