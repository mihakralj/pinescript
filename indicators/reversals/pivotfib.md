# PIVOTFIB: Fibonacci Pivot Points

[Pine Script Implementation of PIVOTFIB](https://github.com/mihakralj/pinescript/blob/main/indicators/reversals/pivotfib.pine)

## Overview and Purpose

Fibonacci Pivot Points combine the traditional pivot point methodology with Fibonacci retracement ratios to create support and resistance levels that align with natural market behavior patterns. By integrating the mathematically significant Fibonacci sequence (0.382, 0.618, 1.000) into pivot point calculations, this indicator provides levels that often coincide with psychological turning points in price action.

Developed as an enhancement to classic pivot points, Fibonacci pivots are particularly effective in trending and volatile markets where price movements tend to respect Fibonacci ratios. The central pivot point remains calculated the same way as classic pivots, but the support and resistance levels are derived using Fibonacci multipliers applied to the previous period's price range, creating a more natural spacing of levels.

Traders favor Fibonacci pivot points for their precision in identifying potential reversal zones and their effectiveness in markets that exhibit strong directional movement. The 61.8% level (R2/S2) is especially significant as it represents the Golden Ratio, often acting as a crucial decision point in trending markets.

## Core Concepts

* **Fibonacci Ratios:** Uses 38.2%, 61.8%, and 100% ratios derived from the Fibonacci sequence
* **Golden Ratio (61.8%):** The most significant Fibonacci level, often the strongest support/resistance
* **Natural Spacing:** Levels correspond to natural market retracement patterns
* **Trending Market Strength:** Particularly effective in trending and volatile conditions
* **Psychological Levels:** Fibonacci ratios align with collective trader psychology

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Timeframe | Daily | Period for pivot calculation | Use Weekly for swing trading, Monthly for position trading |
| Show PP | True | Display pivot point | Central reference level |
| Show R1 (38.2%) | True | Display first resistance | Minor resistance level |
| Show R2 (61.8%) | True | Display second resistance | **Golden Ratio - Key level** |
| Show R3 (100%) | True | Display third resistance | Full range resistance |
| Show S1 (38.2%) | True | Display first support | Minor support level |
| Show S2 (61.8%) | True | Display second support | **Golden Ratio - Key level** |
| Show S3 (100%) | True | Display third support | Full range support |

**Pro Tip:** The R2/S2 levels (61.8% Golden Ratio) are the most significant in Fibonacci pivots and often act as strong turning points. In trending markets, price frequently retraces to the 61.8% level before continuing the trend. Use R1/S1 (38.2%) for shallow retracements in strong trends, and R3/S3 (100%) as extreme targets in volatile conditions. Fibonacci pivots work exceptionally well in forex and crypto markets where Fibonacci-based trading is prevalent.

## Calculation and Mathematical Foundation

**Simplified explanation:**
Fibonacci pivot points calculate the same central pivot as classic pivots, then apply Fibonacci ratios (0.382, 0.618, 1.000) to the previous period's range to determine support and resistance levels.

**Technical formula:**

```
Step 1: Calculate Pivot Point (PP) - Same as Classic
PP = (High + Low + Close) / 3

Step 2: Calculate Price Range
Range = High - Low

Step 3: Calculate Resistance Levels using Fibonacci Ratios
R1 = PP + 0.382 × Range  (38.2% retracement)
R2 = PP + 0.618 × Range  (61.8% Golden Ratio)
R3 = PP + 1.000 × Range  (100% range projection)

Step 4: Calculate Support Levels using Fibonacci Ratios
S1 = PP - 0.382 × Range  (38.2% retracement)
S2 = PP - 0.618 × Range  (61.8% Golden Ratio)
S3 = PP - 1.000 × Range  (100% range projection)
```

> 🔍 **Technical Note:** The Fibonacci ratios (0.382, 0.618, 1.000) are derived from the Fibonacci sequence where each number is the sum of the two preceding ones. The Golden Ratio (0.618) is the most powerful, representing the point at which natural retracements often occur. These ratios create levels that respect the mathematical harmony found throughout nature and markets, making them psychologically significant to traders worldwide.

## Interpretation Details

Fibonacci pivot points provide enhanced analytical capabilities compared to classic pivots:

* **Golden Ratio Significance (R2/S2):**
  - Most critical support/resistance levels
  - Often acts as the final retracement point before trend continuation
  - Break of R2: Strong bullish signal, target R3
  - Break of S2: Strong bearish signal, target S3

* **Shallow Retracements (R1/S1):**
  - Minor support/resistance in strong trends
  - 38.2% is typical retracement in momentum-driven markets
  - Holding above S1 or below R1 indicates trend strength

* **Full Range Projection (R3/S3):**
  - Extreme targets requiring exceptional volatility
  - Often coincides with previous session's high/low
  - Breaking R3/S3 signals potential trend reversal or acceleration

* **Directional Bias:**
  - Price above PP: Bullish, target Fibonacci resistance levels
  - Price below PP: Bearish, target Fibonacci support levels
  - PP acts as dynamic equilibrium

* **Trend Confirmation:**
  - Uptrend: Higher lows at S1 or S2 levels
  - Downtrend: Lower highs at R1 or R2 levels
  - Breaks against trend at Golden Ratio suggest reversal

* **Entry Strategies:**
  - Buy at S1/S2 with confirmation in uptrend
  - Sell at R1/R2 with confirmation in downtrend
  - Use R2/S2 as final decision points

## Limitations and Considerations

* **Trending Market Bias:** Less effective in choppy, range-bound conditions
* **Volatility Dependency:** Requires sufficient range for meaningful levels
* **Learning Curve:** More complex interpretation than classic pivots
* **Golden Ratio Emphasis:** Over-reliance on 61.8% can lead to missed opportunities at other levels
* **Market Psychology:** Effectiveness depends on collective Fibonacci awareness
* **Timeframe Matching:** Must use appropriate pivot period for trading style
* **Not Always Better:** Classic pivots may be more effective in ranging markets

## References

* Fibonacci, Leonardo (1202). Liber Abaci (Book of Calculation)
* Fischer, R. (1993). Fibonacci Applications and Strategies for Traders. Wiley.
* Pesavento, L. (1997). Fibonacci Ratios with Pattern Recognition. Traders Press.
* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
