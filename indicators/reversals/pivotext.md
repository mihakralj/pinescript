# PIVOTEXT: Extended Traditional Pivot Points

[Pine Script Implementation of PIVOTEXT](https://github.com/mihakralj/pinescript/blob/main/indicators/reversals/pivotext.pine)

## Overview and Purpose

Extended Traditional Pivot Points expand upon the classic floor trader pivot system by adding two additional resistance levels (R4, R5) and two additional support levels (S4, S5) beyond the standard R1-R3 and S1-S3. This creates a comprehensive 11-level framework designed to provide reference points for extreme price movements and highly volatile market conditions.

Developed as an enhancement to traditional pivot methodology, the extended system uses the same mathematical principles as classic pivots but extends the range projection multipliers to create outer boundaries at R4/S4 and R5/S5. These additional levels are particularly valuable in trending markets, during high-impact news events, and in volatile instruments like cryptocurrencies where price can move significantly beyond the typical R3/S3 range.

The extended system maintains the same pivot point calculation as classic pivots, ensuring compatibility and familiarity, while providing traders with additional reference levels for setting profit targets, identifying potential reversal zones, and managing risk during extreme market conditions. The R4/S4 and R5/S5 levels often coincide with significant psychological price points and previous period extremes.

## Core Concepts

* **Maximum Coverage:** 11 total levels (PP, R1-R5, S1-S5) for comprehensive analysis
* **Extended Range:** R4/S4 and R5/S5 for extreme movements and volatility
* **Classic Foundation:** Same PP calculation as traditional pivots
* **Volatility Adaptation:** Additional levels scale with previous period's range
* **Extreme Targets:** Outer levels for trending and high-volatility markets

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Timeframe | Daily | Period for pivot calculation | Use Weekly for swing trading, Monthly for position trading |
| Show PP | True | Display pivot point | Central reference level |
| Show R1 | True | Display first resistance | Standard resistance |
| Show R2 | True | Display second resistance | Extended resistance |
| Show R3 | True | Display third resistance | Strong resistance |
| Show R4 | True | Display fourth resistance | **Extreme resistance for volatile conditions** |
| Show R5 | True | Display fifth resistance | **Maximum resistance - rare target** |
| Show S1 | True | Display first support | Standard support |
| Show S2 | True | Display second support | Extended support |
| Show S3 | True | Display third support | Strong support |
| Show S4 | True | Display fourth support | **Extreme support for volatile conditions** |
| Show S5 | True | Display fifth support | **Maximum support - rare target** |

**Pro Tip:** Extended pivots are essential for volatile markets like crypto, forex during major news, or stocks during earnings. R1-R3 and S1-S3 work like classic pivots, but **R4/S4 become critical during 2x+ ATR days** - they often act as final exhaustion points. R5/S5 are reached less than 5% of the time but provide valuable context for "Black Swan" events. In normal conditions, hide R4/R5 and S4/S5 to reduce chart clutter. Enable them during: earnings season, FOMC meetings, NFP releases, or when trading highly volatile instruments. Use R4/S4 as maximum profit targets and R5/S5 as "something is very wrong" signals.

## Calculation and Mathematical Foundation

**Simplified explanation:**
Extended pivots use the same formula as classic pivots for PP, R1-R3, and S1-S3, then add R4/S4 (using 3× range multiplier) and R5/S5 (using 4× range multiplier) for extreme conditions.

**Technical formula:**

```
Step 1: Calculate Pivot Point (PP) - Same as Classic
PP = (High + Low + Close) / 3

Step 2: Calculate Price Range
Range = High - Low

Step 3: Calculate Standard Levels (Same as Classic)
R1 = 2 × PP - Low
S1 = 2 × PP - High
R2 = PP + Range
S2 = PP - Range
R3 = High + 2 × (PP - Low)
S3 = Low - 2 × (High - PP)

Step 4: Calculate Extended Levels (Additional)
R4 = High + 3 × (PP - Low)
S4 = Low - 3 × (High - PP)
R5 = High + 4 × (PP - Low)
S5 = Low - 4 × (High - PP)
```

> 🔍 **Technical Note:** The extended levels (R4/S4 and R5/S5) follow the same mathematical progression as R3/S3 but with higher multipliers. R3/S3 use 2× the relationship between PP and the previous period's extreme, while R4/S4 use 3× and R5/S5 use 4×. This creates exponential spacing: R1 is typically closest to current price, R2 is moderately distant, R3 is significantly distant, R4 is extremely distant, and R5 is at the mathematical maximum extension. These levels often align with multiples of the previous day's range (1×, 2×, 3×, 4×), making them natural targets during range expansion.

## Interpretation Details

Extended pivots provide comprehensive coverage for all market conditions:

* **Standard Levels (R1-R3, S1-S3):**
  - Use exactly like classic pivots
  - R1/S1: First support/resistance, reversal zones
  - R2/S2: Strong support/resistance, breakout targets
  - R3/S3: Extreme support/resistance, rare in normal conditions
  - See Classic Pivot documentation for detailed interpretation

* **Extended Levels - R4/S4 (3× Range):**
  - **Reached during high volatility or strong trends**
  - Approximately 10-15% probability of being reached
  - Often coincides with 2× ATR moves
  - Common during:
    * Earnings announcements
    * Economic data releases (NFP, CPI, FOMC)
    * Geopolitical events
    * Gap-and-go scenarios
  - **Trading at R4/S4:**
    * Consider taking profits on trend trades
    * Watch for exhaustion signals (volume decline, candlestick patterns)
    * Tighten stops as reversal probability increases
    * Expect increased volatility

* **Maximum Levels - R5/S5 (4× Range):**
  - **Rarely reached (< 5% probability)**
  - Indicates exceptional market conditions:
    * Black Swan events
    * Major news surprises
    * Flash crashes or spikes
    * Limit moves in futures
  - **When R5/S5 is reached:**
    * Extreme overbought/oversold
    * High probability of reversal or consolidation
    * Consider closing ALL positions in that direction
    * Wait for price to return inside R4/S4 before re-entering
    * Often marks the high/low of the entire week or month

* **Volatility Assessment:**
  - Normal day: Price stays within R2/S2
  - Active day: Price reaches R3/S3
  - Volatile day: Price reaches R4/S4
  - Extreme day: Price reaches R5/S5

* **Timeframe Considerations:**
  - **Daily pivots with extended levels:**
    * R4/S4: 2-3 times per month
    * R5/S5: Once per month or less
  
  - **Weekly pivots with extended levels:**
    * R4/S4: Major trend moves
    * R5/S5: Monthly extremes
  
  - **Monthly pivots with extended levels:**
    * R4/S4: Quarterly moves
    * R5/S5: Yearly extremes

## Limitations and Considerations

* **Chart Clutter:** 11 levels can be overwhelming; hide outer levels in normal conditions
* **Rare Utility:** R4/S4 and R5/S5 are not used daily; consider toggling visibility
* **Over-Trading Risk:** Too many levels can lead to excessive entry/exit signals
* **Psychological Impact:** Seeing R5/S5 far away may discourage appropriate targets
* **False Precision:** Outer levels have wider "zones" rather than exact prices
* **Market Dependent:** Extended levels more useful in volatile markets (crypto, forex) vs. stable markets (bonds, dividends stocks)
* **Not All Markets:** Some instruments rarely reach R3/S3, making R4/S5 theoretical
* **Calculation Complexity:** More levels = more variables to track and interpret

## References

* Floor traders' pivot point methodology with extended calculations.
* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
* Adapted from standard pivot formulas to include additional range multipliers for extreme conditions.
