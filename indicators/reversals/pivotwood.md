# PIVOTWOOD: Woodie's Pivot Points

[Pine Script Implementation of PIVOTWOOD](https://github.com/mihakralj/pinescript/blob/main/indicators/reversals/pivotwood.pine)

## Overview and Purpose

Woodie's Pivot Points are a variation of traditional pivot points developed by trader Ken Woodie, designed to place greater emphasis on the closing price by giving it double weight in the pivot point calculation. This modification reflects the belief that closing prices are the most important data points in price action, representing the final consensus of value for a given period.

Introduced in the early 2000s through Woodie's CCI (Commodity Channel Index) trading room, this method has gained popularity among active intraday traders who value the closing price as the most significant price level. The weighted formula produces a pivot point that is more responsive to closing price action, making it particularly effective for traders who focus on price acceptance levels and closing strength.

Woodie's method maintains the same R1-R3 and S1-S3 structure as classic pivots but shifts these levels based on the adjusted pivot point, creating support and resistance zones that are more aligned with where price actually closed rather than the simple average of the day's range.

## Core Concepts

* **Weighted Close:** Closing price receives 2x weight in pivot calculation versus high and low
* **Price Acceptance:** Emphasizes where price actually settled, not just the range
* **Closing Strength:** Reflects the importance of final price consensus
* **Intraday Focus:** Particularly effective for day trading and scalping
* **Dynamic Levels:** Pivots shift more with closing price changes than classic method

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Timeframe | Daily | Period for pivot calculation | Use Weekly for swing trading, Monthly for position trading |
| Show PP | True | Display pivot point | Central weighted reference level |
| Show R1 | True | Display first resistance | First target above pivot |
| Show R2 | True | Display second resistance | Extended target |
| Show R3 | True | Display third resistance | Extreme resistance |
| Show S1 | True | Display first support | First support below pivot |
| Show S2 | True | Display second support | Extended support |
| Show S3 | True | Display third support | Extreme support |

**Pro Tip:** Woodie's pivots work exceptionally well for intraday trading because they emphasize closing prices, which represent true price acceptance. When today's close is strong (near the high), tomorrow's pivot point will be higher than classic pivots, signaling underlying bullish sentiment. Conversely, weak closes (near the low) produce lower pivot points, indicating bearish undertones. Combine with CCI (Woodie's preferred indicator) for enhanced signal confirmation.

## Calculation and Mathematical Foundation

**Simplified explanation:**
Woodie's pivot points weight the closing price twice as heavily as the high and low, producing a pivot point that is more responsive to where price actually closed rather than the midpoint of the range.

**Technical formula:**

```
Step 1: Calculate Pivot Point (PP) with Weighted Close
PP = (High + Low + 2 × Close) / 4

Step 2: Calculate Resistance Levels
R1 = 2 × PP - Low
R2 = PP + (High - Low)
R3 = High + 2 × (PP - Low)

Step 3: Calculate Support Levels
S1 = 2 × PP - High
S2 = PP - (High - Low)
S3 = Low - 2 × (High - PP)
```

> 🔍 **Technical Note:** The key difference from classic pivots is in Step 1, where Close is weighted 2:1 versus High and Low. This shifts the pivot point in the direction of the close. If Close is near High, PP moves higher; if Close is near Low, PP moves lower. This creates a bias that reflects the previous period's directional strength, making Woodie's pivots more "dynamic" than classic pivots while maintaining the same resistance and support calculation structure.

## Interpretation Details

Woodie's pivots provide enhanced directional bias based on closing strength:

* **Pivot Point Bias:**
  - Close near High → PP above classic pivot → Bullish bias built-in
  - Close near Low → PP below classic pivot → Bearish bias built-in
  - Close at midpoint → PP similar to classic pivot → Neutral

* **Directional Trading:**
  - Price above PP: Trade long, target R1, R2, R3
  - Price below PP: Trade short, target S1, S2, S3
  - PP acts as dynamic sentiment gauge

* **R1/S1 Significance:**
  - Most commonly tested levels in Woodie's method
  - Often act as profit targets for intraday moves
  - Breaks of R1/S1 signal strong momentum

* **R2/S2 as Trend Confirmation:**
  - Reaching R2: Strong uptrend, momentum continuation likely
  - Reaching S2: Strong downtrend, momentum continuation likely
  - Failure to reach R2/S2: Potential reversal signal

* **R3/S3 Extreme Levels:**
  - Rare to reach in normal conditions
  - Indicate exceptional volatility or strong trending
  - Often coincide with previous period's high/low

* **Comparison with Classic Pivots:**
  - When Woodie's PP > Classic PP: Bullish undertone (strong close)
  - When Woodie's PP < Classic PP: Bearish undertone (weak close)
  - Divergence between methods provides sentiment insight

## Limitations and Considerations

* **Closing Price Dependency:** Extremely sensitive to where price closes relative to range
* **Gap Behavior:** Large overnight gaps can produce misleading initial pivots
* **Trend Bias:** Introduces directional bias that may not always be warranted
* **Whipsaw Risk:** Can give false signals during choppy, range-bound markets
* **Less Universal:** Not as widely recognized as classic pivots; less "self-fulfilling"
* **Intraday Focused:** Best for day trading; less effective for longer timeframes
* **Requires Context:** Should be used with other indicators (especially CCI per Woodie's methodology)

## References

* Woodie, K. (2000s). Woodie's CCI Trading Room methodology.
* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
* Trading methodology documented through Woodie's CCI forums and educational materials.
