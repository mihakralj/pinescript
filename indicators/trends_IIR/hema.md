# HEMA: Hull Exponential Moving Average

[Pine Script Implementation of HEMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_IIR/hema.pine)

## Overview and Purpose

The Hull Exponential Moving Average (HEMA) is an experimental technical indicator that combines concepts from both Hull Moving Average (HMA) and Exponential Moving Average (EMA). While the traditional Hull Moving Average uses Weighted Moving Averages (WMA) in its calculation, HEMA replaces these with strategically configured EMAs to create a responsive yet smooth trend indicator.

HEMA applies a multi-stage approach where it calculates two EMAs with different speeds, combines them using logarithmic coefficients, and then applies a final EMA smoothing pass. This creates a moving average that responds quickly to genuine price changes while maintaining effective noise filtering capabilities. The algorithm's unique alpha acceleration and logarithmic weighting create a distinctive balance between responsiveness and smoothness.

## Core Concepts

* **Cubic alpha acceleration:** Uses a cubic function to accelerate the alpha parameter for the fast EMA component, creating enhanced responsiveness
* **Logarithmic coefficient distribution:** Applies natural logarithm-based weightings to combine the fast and slow components
* **Hull-inspired methodology:** Follows the Hull Moving Average concept of combining differently-weighted components but uses EMAs instead of WMAs
* **Optimized final smoothing:** Applies a mathematically derived final alpha that maintains the balance between smoothness and responsiveness

HEMA achieves its performance through a three-stage process that first calculates fast and slow EMAs, then combines them with logarithmic coefficients, and finally applies an optimized EMA smoothing to the result. The cubic acceleration of the fast alpha creates rapid response to price changes, while the logarithmic weighting and final smoothing prevent excessive noise and overshooting.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Period | 10 | Base smoothing period | Increase for longer-term trends, decrease for shorter-term signals |
| Source | Close | Data point used for calculation | Change to HL2 or HLC3 for more balanced price representation |

**Pro Tip:** When transitioning from HMA to HEMA, many traders find that a slightly longer period (approximately 15-20% longer) provides comparable responsiveness with improved smoothness. For example, if you typically use HMA(8), try HEMA(10) for similar performance with reduced noise.

## Calculation and Mathematical Foundation

**Simplified explanation:**
HEMA works by calculating two EMAs—one accelerated and one standard—then combines them using specially calculated coefficients. This combined value is then smoothed with a final EMA that uses an optimized alpha value. The result is a moving average that shows price trends clearly while filtering out market noise.

**Technical formula:**
1. Calculate standard alpha for EMA: αSlow = 2/(period + 1)
2. Calculate accelerated alpha for fast EMA: αFast = 1 - (1 - αSlow)³
3. Calculate the optimized final alpha: αFinal = 2/(√((2/αSlow) - 1) + 1)
4. Calculate the two EMAs:
   - EMASlow = Standard EMA with αSlow
   - EMAFast = Accelerated EMA with αFast
5. Calculate weighted difference: diff = (1 + ln(2)) × EMAFast - ln(2) × EMASlow
6. Apply final smoothing: HEMA = EMA of diff with αFinal

> 🔍 **Technical Note:** The coefficient values (approximately 1.693 and 0.693) are derived from natural logarithm properties (ln(2) ≈ 0.693). This logarithmic weighting creates a balanced combination that enhances responsiveness while maintaining a smooth output. The cubic acceleration of αFast means that for shorter periods, the fast component responds dramatically faster than the slow component, while for longer periods, the difference is less pronounced.

## Interpretation Details

HEMA provides several key insights for traders:

- When price crosses above HEMA, it often signals the beginning of an uptrend
- When price crosses below HEMA, it often signals the beginning of a downtrend
- The slope of HEMA provides insight into trend strength and momentum
- HEMA creates smooth dynamic support and resistance levels during trends
- Multiple HEMA lines with different periods can identify potential reversal zones

HEMA is particularly effective for trend following strategies where both responsiveness and noise reduction are important. It provides earlier signals than traditional EMAs while exhibiting less whipsaw than standard HMA in choppy market conditions. The indicator excels at identifying the underlying trend direction while filtering out minor price fluctuations.

## Limitations and Considerations

* **Experimental nature:** As an experimental indicator, HEMA may behave differently from established moving averages in certain market conditions
* **Lag characteristics:** While designed to reduce lag, HEMA may exhibit slightly more lag than HMA in some scenarios
* **Mathematical complexity:** The multi-stage calculation with specialized alpha parameters makes the behavior less intuitive to understand
* **Parameter sensitivity:** Performance can vary significantly with different period settings
* **Complementary tools:** Works best when combined with volume analysis or momentum indicators for confirmation

## References

1. Hull, A. (2005). "Hull Moving Average," *Technical Analysis of Stocks & Commodities*.
