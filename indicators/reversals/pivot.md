# PIVOT: Classic Pivot Points

[Pine Script Implementation of PIVOT](https://github.com/mihakralj/pinescript/blob/main/indicators/reversals/pivot.pine)

## Overview and Purpose

Classic Pivot Points, also known as Standard or Floor Pivot Points, are one of the oldest and most widely used technical indicators in trading. Originally developed by floor traders in the commodity pits before the era of electronic trading, these levels serve as objective price markers that identify potential support and resistance zones throughout the trading day.

The indicator calculates a central pivot point (PP) based on the previous period's high, low, and close, then derives three resistance levels (R1, R2, R3) above the pivot and three support levels (S1, S2, S3) below it. These seven key levels provide traders with predetermined price targets and reversal zones, making them invaluable for day trading, swing trading, and position management.

The universal adoption of classic pivot points across trading platforms and markets has created a self-fulfilling prophecy effect - because so many traders watch and react to these levels, they often become significant turning points in price action.

## Core Concepts

* **Pivot Point (PP):** The central reference level calculated as the average of previous period's high, low, and close
* **Support Levels (S1-S3):** Price levels below PP where buying pressure is expected to emerge
* **Resistance Levels (R1-R3):** Price levels above PP where selling pressure is expected to emerge
* **Timeframe Flexibility:** Can be calculated on daily, weekly, or monthly periods for different trading styles
* **Self-Fulfilling Nature:** Widely watched levels become significant due to collective trader behavior

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Timeframe | Daily | Period for pivot calculation | Use Weekly for swing trading, Monthly for position trading |
| Show PP | True | Display pivot point | Central reference level, always useful |
| Show R1-R3 | True | Display resistance levels | Hide if focusing only on support |
| Show S1-S3 | True | Display support levels | Hide if focusing only on resistance |
| PP Color | Yellow | Pivot point line color | Visual preference |
| Resistance Color | Red | Resistance lines color | Visual preference |
| Support Color | Green | Support lines color | Visual preference |

**Pro Tip:** Daily pivots work best for intraday and day trading (5m to 1H charts). Weekly pivots are ideal for swing trading (4H to Daily charts). Monthly pivots suit position trading (Daily to Weekly charts). The key is matching the pivot timeframe to your trading timeframe - typically use pivots from one timeframe higher than your trading chart.

## Calculation and Mathematical Foundation

**Simplified explanation:**
Classic pivot points calculate a central pivot level from the previous period's price action, then derive support and resistance levels using simple arithmetic based on the price range.

**Technical formula:**

```
Step 1: Calculate Pivot Point (PP)
PP = (High + Low + Close) / 3

Step 2: Calculate First Level Support and Resistance
R1 = 2 × PP - Low
S1 = 2 × PP - High

Step 3: Calculate Second Level Support and Resistance
R2 = PP + (High - Low)
S2 = PP - (High - Low)

Step 4: Calculate Third Level Support and Resistance
R3 = High + 2 × (PP - Low)
S3 = Low - 2 × (High - PP)
```

> 🔍 **Technical Note:** The formula uses the previous period's data (high[1], low[1], close[1]) to calculate levels that remain static throughout the current period. This forward-looking approach using `lookahead=barmerge.lookahead_on` ensures the levels are known at the start of the period and don't repaint. The arithmetic progression ensures each level is equidistant within its respective range.

## Interpretation Details

Classic pivot points provide multiple analytical perspectives for traders:

* **Directional Bias:**
  - Price opens above PP: Bullish bias for the session
  - Price opens below PP: Bearish bias for the session
  - PP acts as the neutral equilibrium level

* **Support and Resistance:**
  - S1, S2, S3: Expected support zones where buyers may emerge
  - R1, R2, R3: Expected resistance zones where sellers may emerge
  - Breaks through levels signal strength in that direction
  - Bounces from levels confirm their validity

* **Price Targets:**
  - From PP: Target R1 in uptrend, S1 in downtrend
  - From R1: Target R2, from S1: Target S2
  - R3/S3 typically represent extreme moves requiring strong momentum

* **Range Trading:**
  - Between S1 and R1: Normal trading range
  - Between S2 and R2: Extended range
  - Beyond R3 or S3: Breakout/breakdown scenario

* **Breakout Confirmation:**
  - Clean break above R1 with retest: Bullish continuation to R2
  - Clean break below S1 with retest: Bearish continuation to S2
  - Failed breaks suggest range-bound conditions

## Limitations and Considerations

* **Static Levels:** Pivot points remain fixed for the entire period and don't adapt to intraday volatility
* **Market Gaps:** Large overnight gaps can make pivot levels less relevant at the open
* **Trending Markets:** Strong trends may ignore pivot levels and move through them quickly
* **Range-Bound Bias:** Most effective in ranging or consolidating markets
* **Timeframe Dependency:** Must match pivot calculation period to trading timeframe appropriately
* **No Volume Information:** Purely price-based, doesn't account for volume or momentum
* **Self-Fulfilling Prophecy:** Effectiveness depends on how many traders are watching the same levels

## References

* Floor Traders' Standard Practice (Pre-1990s)
* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
* Person, J. L. (2004). Candlestick and Pivot Point Trading Triggers. Wiley Trading.
