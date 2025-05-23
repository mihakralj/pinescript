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
| Corrected | false | Adjusts internal EMA smoothing factors for potentially faster response. | Set to `true` for a modified TEMA that may react quicker to price changes. `false` uses standard TEMA calculation. |
| Visualization | Line | Display format on charts | Use filled cloud to see divergence from price more clearly |

**Pro Tip:** For optimal trade signals, many professional traders use two TEMAs (e.g., 8 and 21 periods) and look for crossovers, which often provide earlier signals than traditional moving average pairs.

## Calculation and Mathematical Foundation

**Simplified explanation:**
TEMA calculates three levels of EMAs, then combines them using a special formula that amplifies recent price action while reducing lag. This triple-processing approach effectively eliminates much of the delay found in traditional moving averages.

**Technical formula:**
TEMA = 3 × EMA₁ - 3 × EMA₂ + EMA₃

Where:
- EMA₁ = EMA(source, α₁)
- EMA₂ = EMA(EMA₁, α₂)
- EMA₃ = EMA(EMA₂, α₃)

The smoothing factors (α₁, α₂, α₃) are determined as follows:
- Let α_base = 2/(length + 1)
- α₁ = α_base
- If `corrected` is `false`:
  - α₂ = α_base
  - α₃ = α_base
- If `corrected` is `true`:
  - Let r = (1/α_base)^(1/3)
  - α₂ = α_base * r
  - α₃ = α_base * r * r = α_base * r²

The `corrected = true` option implements a variation that uses progressively smaller alpha values for the subsequent EMA calculations. This approach aims to optimize the filter's frequency response and phase lag.

**Alpha Calculation for `corrected = true`:**
- α₁ (alpha_base) = 2/(length + 1)
- r = (1/α₁)^(1/3)  (cube root relationship)
- α₂ = α₁ * r = α₁^(2/3)
- α₃ = α₂ * r = α₁^(1/3)

**Mathematical Rationale for Corrected Alphas:**

1.  **Frequency Response Balance:**
    The standard TEMA (where α₁ = α₂ = α₃) can lead to an uneven frequency response, potentially over-smoothing high frequencies or creating resonance artifacts. The geometric progression of alphas (α₁ > α₁^(2/3) > α₁^(1/3)) in the corrected version aims to create a more balanced filter cascade. Each stage contributes more proportionally to the overall frequency response.

2.  **Phase Lag Optimization:**
    The cube root relationship between the alphas is designed to minimize cumulative phase lag while maintaining smoothing effectiveness. Each subsequent EMA stage has a progressively smaller impact on phase distortion.

3.  **Mathematical Stability:**
    The geometric progression (α₁, α₁^(2/3), α₁^(1/3)) can enhance numerical stability due to constant ratios between consecutive alphas. This helps prevent the accumulation of rounding errors and maintains consistent convergence properties.

**Practical Impact of `corrected = true`:**
This modification aims to achieve:
- Potentially better lag reduction for a similar level of smoothing.
- A more uniform frequency response across different market cycles.
- Reduced overshoot or undershoot in trending conditions.
- Improved signal-to-noise ratio preservation.

Essentially, the cube root relationship in the corrected TEMA attempts to optimize the trade-off between responsiveness and smoothness that can be a challenge with uniform alpha values.

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
