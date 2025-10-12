# PIVOTCAM: Camarilla Pivot Points

[Pine Script Implementation of PIVOTCAM](https://github.com/mihakralj/pinescript/blob/main/indicators/reversals/pivotcam.pine)

## Overview and Purpose

Camarilla Pivot Points are a sophisticated set of eight intraday support and resistance levels developed by bond trader Nick Scott in 1989. Named after the secret council in the popular role-playing game Vampire: The Masquerade, these levels are designed specifically for short-term trading and provide tightly clustered support and resistance zones around the previous period's closing price.

The Camarilla method uses precise mathematical multipliers (derived from Fibonacci-like calculations) applied to the previous period's range to create four resistance levels (R1-R4) and four support levels (S1-S4). The levels are intentionally close together, making them ideal for scalping and day trading strategies where small price movements are captured repeatedly throughout the day.

What makes Camarilla pivots unique is their focus on mean reversion rather than breakout trading. The system assumes that price will typically stay within the R3-S3 range and revert to the pivot point, with R3 and S3 acting as critical decision points. Breaks beyond R4 or S4 are considered exceptional events signaling strong trend continuation.

## Core Concepts

* **Mean Reversion Focus:** Assumes price returns to PP; R3/S3 are reversal zones
* **Eight Levels:** Most granular pivot system (R1-R4, S1-S4)
* **Tight Clustering:** Levels closely spaced for scalping opportunities
* **R4/S4 Breakout Signals:** Beyond these levels indicates strong trending
* **Intraday Precision:** Designed specifically for short-term, high-frequency trading

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Timeframe | Daily | Period for pivot calculation | Rarely change; designed for daily pivots on intraday charts |
| Show PP | True | Display pivot point | Reference equilibrium level |
| Show R1 (1.0833/12) | True | Display first resistance | Minor resistance, first profit target |
| Show R2 (1.1666/12) | True | Display second resistance | Moderate resistance |
| Show R3 (1.2500/12) | True | **Display third resistance - KEY REVERSAL LEVEL** |
| Show R4 (1.5000/12) | True | Display fourth resistance | **BREAKOUT LEVEL - Trend signal** |
| Show S1 (1.0833/12) | True | Display first support | Minor support, first profit target |
| Show S2 (1.1666/12) | True | Display second support | Moderate support |
| Show S3 (1.2500/12) | True | **Display third support - KEY REVERSAL LEVEL** |
| Show S4 (1.5000/12) | True | **Display fourth support - BREAKOUT LEVEL - Trend signal** |

**Pro Tip:** Camarilla pivots excel in ranging markets with their mean-reversion strategy. **R3 and S3 are the most critical levels** - expect reversals here 80% of the time. When price reaches R3, look to sell; at S3, look to buy. However, if price breaks R4 or S4, **immediately reverse your bias** and trade with the trend - these breakouts often lead to sustained moves. Use 5-minute to 15-minute charts for optimal results, and avoid this system during high-impact news events when mean reversion breaks down.

## Calculation and Mathematical Foundation

**Simplified explanation:**
Camarilla pivots use precise multipliers (fractions of 1/12) applied to the previous day's range, creating tightly spaced levels around the closing price optimized for mean-reversion trading.

**Technical formula:**

```
Step 1: Calculate Pivot Point (PP) - Same as Classic
PP = (High + Low + Close) / 3

Step 2: Calculate Price Range
Range = High - Low

Step 3: Calculate Resistance Levels with Camarilla Multipliers
R1 = Close + Range × (1.0833 / 12) = Close + Range × 0.0903
R2 = Close + Range × (1.1666 / 12) = Close + Range × 0.0972
R3 = Close + Range × (1.2500 / 12) = Close + Range × 0.1042
R4 = Close + Range × (1.5000 / 12) = Close + Range × 0.1250

Step 4: Calculate Support Levels with Camarilla Multipliers
S1 = Close - Range × (1.0833 / 12) = Close - Range × 0.0903
S2 = Close - Range × (1.1666 / 12) = Close - Range × 0.0972
S3 = Close - Range × (1.2500 / 12) = Close - Range × 0.1042
S4 = Close - Range × (1.5000 / 12) = Close - Range × 0.1250
```

> 🔍 **Technical Note:** The Camarilla multipliers (1.0833, 1.1666, 1.2500, 1.5000 divided by 12) create specific percentage offsets from the closing price. R1/S1 are approximately 9% of range, R2/S2 are ~9.7%, R3/S3 are ~10.4%, and R4/S4 are 12.5% of the range. This mathematical precision allows for consistent level spacing regardless of volatility. The levels cluster around Close rather than PP, reflecting the mean-reversion philosophy that price gravitates toward where it last settled.

## Interpretation Details

Camarilla pivots require a specific trading methodology:

* **R3/S3 - Primary Reversal Zones:**
  - **Most important levels in the entire system**
  - Price typically reverses at R3/S3 about 80% of the time
  - **Sell at R3** with stop above R4
  - **Buy at S3** with stop below S4
  - Best risk/reward when price reaches these levels

* **R1/S1 - Profit Targets:**
  - Use as initial profit targets from mean reversion trades
  - Light resistance/support zones
  - Often tested multiple times per day

* **R2/S2 - Intermediate Levels:**
  - Secondary profit targets
  - Can act as support/resistance for pullbacks
  - Less significant than R3/S3

* **R4/S4 - Breakout/Breakdown Levels:**
  - **CRITICAL: Breaks indicate trend, not reversal**
  - Break above R4: Strong bullish trend - go long
  - Break below S4: Strong bearish trend - go short
  - Only ~20% chance of reaching these levels
  - Often leads to sustained moves beyond levels

* **Trading Strategy:**
  1. Wait for price to reach R3 or S3
  2. Look for reversal signals (candlestick patterns, momentum divergence)
  3. Enter counter-trend trade with tight stop beyond R4/S4
  4. Target PP or opposite S1/R1 for profit
  5. If R4/S4 breaks, flip bias and trade with trend

* **Risk Management:**
  - Tight stops (just beyond R4/S4)
  - Multiple smaller trades throughout day
  - Exit at PP or R1/S1 for consistent profits
  - Avoid trading during news events

## Limitations and Considerations

* **Range-Bound Markets Only:** Fails during strong trending conditions
* **Intraday Specific:** Designed for day trading, not swing or position trading
* **Requires Discipline:** Must respect R4/S4 breaks and flip bias immediately
* **False Breakouts:** R4/S4 can be tested and fail, causing whipsaws
* **News Event Risk:** High-impact news renders mean-reversion invalid
* **Scalping Focus:** Requires active monitoring; not passive system
* **Tight Stops:** Frequent stop-outs in volatile conditions
* **Market Dependent:** Works best in forex and futures; less effective in low-liquidity stocks

## References

* Scott, N. (1989). Camarilla Equation development and bond trading methodology.
* Practical application documented in various forex and futures trading forums.
* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
