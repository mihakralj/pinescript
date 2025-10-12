# PIVOTDEM: DeMark Pivot Points

[Pine Script Implementation of PIVOTDEM](https://github.com/mihakralj/pinescript/blob/main/indicators/reversals/pivotdem.pine)

## Overview and Purpose

DeMark Pivot Points, developed by renowned technical analyst Tom DeMark, represent a minimalist approach to pivot point analysis with only three levels: a pivot point (PP), one resistance (R1), and one support (S1). What makes this method unique is its conditional logic that adjusts the pivot calculation based on the relationship between the opening and closing prices, providing a directional bias built into the formula itself.

Introduced as part of DeMark's broader suite of technical indicators in the 1990s, this method reflects his philosophy of simplicity and trend-following. Rather than providing multiple support and resistance zones like traditional pivot systems, DeMark pivots identify the single most critical level for the upcoming period, making them ideal for traders who prefer clear, unambiguous decision points.

The conditional nature of DeMark pivots means they automatically adjust to market sentiment: bearish closes produce different pivots than bullish closes, creating a system that is inherently trend-aware rather than mean-reverting. This makes DeMark pivots particularly effective in trending markets where directional bias is more important than multiple price levels.

## Core Concepts

* **Conditional Logic:** Different calculations based on Close vs Open relationship
* **Minimalist Design:** Only 3 levels (PP, R1, S1) for clarity
* **Trend Aware:** Built-in directional bias based on previous period's action
* **Open Price Dependency:** Uses opening price unlike most pivot systems
* **Single Decision Point:** PP is the primary reference level

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Timeframe | Daily | Period for pivot calculation | Use Weekly for swing trading, Monthly for position trading |
| Show PP | True | Display pivot point | **Critical decision level - most important** |
| Show R1 | True | Display resistance | Single resistance target above PP |
| Show S1 | True | Display support | Single support target below PP |

**Pro Tip:** DeMark pivots excel in trending markets where a single clear reference level is more valuable than multiple zones. The pivot point (PP) is THE key level - **trade above PP in uptrends, below PP in downtrends**. The conditional calculation automatically adjusts the pivot higher after bullish closes and lower after bearish closes, creating a system that trends with the market. Use R1 and S1 as profit targets rather than reversal zones. This method works particularly well for trend-following strategies on higher timeframes (4H, Daily, Weekly) where you want one clear reference point without the noise of multiple levels.

## Calculation and Mathematical Foundation

**Simplified explanation:**
DeMark pivots use conditional logic to calculate an intermediate value (X) based on whether the previous period closed higher, lower, or equal to its open, then derive PP, R1, and S1 from this adjusted value.

**Technical formula:**

```
Step 1: Calculate Conditional X Value
If Close < Open (Bearish):
    X = High + 2 × Low + Close

If Close > Open (Bullish):
    X = 2 × High + Low + Close

If Close = Open (Neutral):
    X = High + Low + 2 × Close

Step 2: Calculate Pivot Point
PP = X / 4

Step 3: Calculate Resistance and Support
R1 = X / 2 - Low
S1 = X / 2 - High
```

> 🔍 **Technical Note:** The genius of DeMark's method lies in the conditional X calculation. When the previous period closes bearish (Close < Open), the formula weights Low twice, pulling the pivot down. When bullish (Close > Open), High is weighted twice, pushing the pivot up. When neutral (Close = Open), Close is weighted twice. This creates an automatic bias: bullish closes produce higher pivots (more room above, less below), and bearish closes produce lower pivots (more room below, less above). The division by 4 normalizes the calculation, while R1 and S1 are derived from X/2, creating asymmetric levels that reflect the previous period's directional momentum.

## Interpretation Details

DeMark pivots require a trend-following mindset:

* **Pivot Point (PP) - The Only Level That Matters:**
  - **Primary reference for all trading decisions**
  - Price above PP: Bullish bias, look for longs
  - Price below PP: Bearish bias, look for shorts
  - Crossovers of PP signal potential trend changes
  - Most significant level in entire system

* **Directional Bias Built-In:**
  - Bullish previous close → Higher PP → Easier to stay bullish
  - Bearish previous close → Lower PP → Easier to stay bearish
  - PP naturally "trends" with the market

* **R1 - Single Resistance:**
  - Primary profit target for long positions
  - Not typically a reversal level
  - Breakthrough indicates strong uptrend
  - Often reached in trending conditions

* **S1 - Single Support:**
  - Primary profit target for short positions
  - Not typically a reversal level
  - Breakdown indicates strong downtrend
  - Often reached in trending conditions

* **Trading Strategy:**
  - **Trend Following:**
    * Long when price is above PP and rising
    * Short when price is below PP and falling
    * Use R1/S1 as profit targets
  
  - **Breakout Trading:**
    * Break above R1: Strong bullish signal
    * Break below S1: Strong bearish signal
    * PP breaks can signal trend reversals

  - **Avoid Counter-Trend:**
    * Don't fade R1 (selling resistance)
    * Don't fade S1 (buying support)
    * System designed for momentum, not mean reversion

* **Comparison with Classic Pivots:**
  - Fewer levels = clearer decisions
  - Built-in bias vs. neutral reference
  - Better for trending vs. ranging markets
  - Single entry/exit levels vs. multiple zones

## Limitations and Considerations

* **Trending Markets Only:** Less effective in range-bound conditions
* **Limited Levels:** Only 3 levels may miss intermediate support/resistance
* **Open Price Dependency:** Requires reliable opening price data (gaps matter)
* **No R2/R3 Targets:** Limited profit targets in extended moves
* **Conditional Complexity:** Three different formulas can be confusing
* **Less Universal:** Not as widely used as classic pivots; less "self-fulfilling"
* **Pivot Dominance:** Over-reliance on single PP level can be limiting
* **Gap Sensitivity:** Large gaps between close and open affect calculations significantly

## References

* DeMark, T. (1994). The New Science of Technical Analysis. Wiley.
* DeMark, T. (2012). DeMark Indicators. Bloomberg Press.
* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
