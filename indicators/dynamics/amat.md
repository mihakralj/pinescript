# AMAT: Archer Moving Averages Trends

[Pine Script Implementation of AMAT](https://github.com/mihakralj/pinescript/blob/main/indicators/dynamics/amat.pine)

## Overview and Purpose

The Archer Moving Averages Trends (AMAT) indicator is a trend identification system developed by trader Tom Joseph, based on concepts by Mark Whistler (Archer). AMAT uses multiple exponential moving averages (EMAs) to identify the overall trend direction and strength in the market. Unlike simple moving average crossovers, AMAT requires alignment of both the fast and slow moving averages in the same direction to confirm a trend.

The indicator is particularly useful for identifying strong, sustained trends while filtering out weak or choppy price action. AMAT generates clear bullish or bearish signals when both the fast EMA is above/below the slow EMA AND both EMAs are moving in the same direction (rising for bullish, falling for bearish).

## Core Concepts

* **Dual EMA System:** Uses two exponential moving averages (fast and slow) to capture trend direction and momentum
* **Direction Alignment:** Requires both EMAs to be trending in the same direction for a valid signal (both rising or both falling)
* **Position Relationship:** Fast EMA must be above slow EMA for bullish trends, below for bearish trends
* **Trend Confirmation:** Only generates signals when all conditions align, reducing false signals in ranging markets
* **Trend Strength:** Measures the separation between fast and slow EMAs as a percentage to gauge trend intensity

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Fast Period | 10 | Period for the fast EMA | Lower for more sensitivity, higher for smoother signals |
| Slow Period | 50 | Period for the slow EMA | Lower for faster reaction, higher for longer-term trends |
| Source | Close | Price data used for calculation | Consider using hlc3 or ohlc4 for less volatile signals |

**Pro Tip:** The default 10/50 periods work well for daily charts and swing trading. For intraday trading, consider faster settings like 5/20. For position trading or longer timeframes, try 20/100. The key is maintaining a ratio where the slow period is approximately 5x the fast period to capture meaningful trend changes while avoiding excessive whipsaws.

## Calculation and Mathematical Foundation

**Simplified explanation:**
AMAT compares two EMAs and their directional movement. A bullish trend requires: (1) fast EMA above slow EMA, (2) fast EMA rising, and (3) slow EMA rising. A bearish trend requires the opposite conditions.

**Technical formula:**

1. Calculate Fast and Slow EMAs:
   ```
   α_fast = 2 / (fast_period + 1)
   α_slow = 2 / (slow_period + 1)
   
   EMA_fast = α_fast × (price - EMA_fast[1]) + EMA_fast[1]
   EMA_slow = α_slow × (price - EMA_slow[1]) + EMA_slow[1]
   ```

2. Determine Trend Direction:
   ```
   Bullish = EMA_fast > EMA_slow AND 
             EMA_fast > EMA_fast[1] AND 
             EMA_slow > EMA_slow[1]
   
   Bearish = EMA_fast < EMA_slow AND 
             EMA_fast < EMA_fast[1] AND 
             EMA_slow < EMA_slow[1]
   ```

3. Calculate Trend Strength (optional):
   ```
   Strength = |EMA_fast - EMA_slow| / EMA_slow × 100
   ```

4. Assign Trend Value:
   ```
   AMAT = +1 if Bullish
   AMAT = -1 if Bearish
   AMAT =  0 if Neutral (mixed conditions)
   ```

> 🔍 **Technical Note:** The requirement for both EMAs to be moving in the same direction (rising or falling) is what distinguishes AMAT from simple EMA crossovers. This additional filter significantly reduces false signals during sideways or choppy markets, as it requires momentum alignment between both short-term and long-term trends.

## Interpretation Details

AMAT provides clear trend identification through histogram columns and a strength line:

* **Visual Components:**
  - **Green Columns (+1):** Bullish trend signals displayed as green histogram bars
  - **Red Columns (-1):** Bearish trend signals displayed as red histogram bars
  - **Gray Areas (0):** Neutral/no clear trend periods shown as gray or gaps
  - **Yellow Line:** Trend strength percentage showing EMA separation

* **Bullish Signal (+1) - Green Columns:**
  - Fast EMA is above the slow EMA (short-term strength)
  - Fast EMA is rising compared to previous bar (accelerating upward)
  - Slow EMA is rising compared to previous bar (sustained momentum)
  - Interpretation: Strong uptrend with aligned short and long-term momentum
  - Chart behavior: Green columns appear during clear uptrends

* **Bearish Signal (-1) - Red Columns:**
  - Fast EMA is below the slow EMA (short-term weakness)
  - Fast EMA is falling compared to previous bar (accelerating downward)
  - Slow EMA is falling compared to previous bar (sustained decline)
  - Interpretation: Strong downtrend with aligned short and long-term momentum
  - Chart behavior: Red columns appear during clear downtrends

* **Neutral/No Signal (0) - Gray Areas:**
  - Mixed conditions where not all criteria align
  - Example: Fast above slow but one or both EMAs not trending
  - Interpretation: No clear trend, consolidation or transition phase
  - Chart behavior: Gaps or gray areas during sideways markets

* **Trend Strength (Yellow Line):**
  - Formula: |EMA_fast - EMA_slow| / EMA_slow × 100
  - Higher spikes indicate stronger trend separation
  - Low values (< 2%) suggest weak trends or potential reversal
  - High values (> 5%) indicate strong, established trends
  - Provides context for the reliability of trend signals

* **Signal Patterns:**
  - **Sustained green columns:** Extended uptrends with consistent bullish momentum
  - **Sustained red columns:** Extended downtrends with consistent bearish momentum
  - **Intermittent signals:** Choppy markets with frequent trend changes
  - **Strength spikes:** Periods of acceleration in the prevailing trend
  - **Transition from 0 to +1/-1:** New trend potentially forming
  - **Transition from +1 to 0 or -1 to 0:** Trend weakening or ending
  - **Direct flip from +1 to -1 or vice versa:** Strong trend reversal

* **Practical Usage:**
  - Use green columns for entry signals in uptrends
  - Use red columns for entry signals in downtrends
  - Avoid trading during gray/neutral periods (consolidations)
  - Higher strength values confirm trend conviction
  - Watch for strength divergence (weakening strength despite trend continuation)

## Limitations and Considerations

* **Lagging Indicator:** As AMAT uses EMAs and requires multiple confirmations, it inherently lags price action and may enter trends after they've already begun
* **Whipsaws in Ranging Markets:** Even with the directional filter, choppy sideways markets can produce brief false signals as EMAs oscillate
* **No Magnitude Information:** AMAT shows trend direction but doesn't indicate the strength or momentum of price movement within the trend
* **Period Sensitivity:** The fast/slow period selection significantly affects signal frequency and reliability; requires optimization for different markets and timeframes
* **No Reversal Timing:** AMAT identifies when a trend exists but doesn't predict when trends will end or reverse
* **Multiple Bar Confirmation:** Requires sustained conditions across multiple bars, which may delay entry signals compared to simpler indicators

## References

* Joseph, T. (2009). "Archer Moving Averages Trends (AMAT)" Trading Strategy Concepts
* Whistler, M. (2007). "Archer System" Trading Methodology Documentation
* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
* Pring, M. J. (2002). Technical Analysis Explained. McGraw-Hill.
