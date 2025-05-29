# BBWN: Bollinger Band Width Normalized

[Pine Script Implementation of BBWN](https://github.com/mihakralj/pinescript/blob/main/indicators/volatility/bbwn.pine)

## Overview and Purpose

Bollinger Band Width Normalized (BBWN) is a sophisticated volatility indicator that transforms the raw Bollinger Band Width into a normalized scale ranging from 0.0 to 1.0. Unlike BBWP which uses percentile ranking, BBWN applies min-max normalization to map the current BBW value within its historical range, providing a linear scaling that preserves the relative magnitude of volatility changes while ensuring consistent interpretation across different securities and time periods.

BBWN offers a mathematically precise approach to volatility normalization by using the actual minimum and maximum BBW values observed over a specified lookback period. This creates a bounded scale where 0.0 represents the lowest volatility observed in the historical range, 1.0 represents the highest, and values in between represent proportional positions within this range.

## Core Concepts

* **Min-max normalization:** BBWN scales current BBW linearly between the minimum and maximum historical values, preserving relative distances
* **Bounded scale:** Always produces values between 0.0 and 1.0, making interpretation consistent across all market conditions
* **Linear relationship:** Unlike percentile ranking, maintains proportional relationships between volatility levels
* **Extreme sensitivity:** Reacts immediately when new historical extremes are established
* **Range preservation:** Maintains the relative magnitude of volatility changes within the normalized space

The key advantage of BBWN is its linear scaling property, which means that a change from 0.2 to 0.4 represents the same absolute increase in normalized volatility as a change from 0.6 to 0.8, making it particularly useful for systematic trading strategies and quantitative analysis.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Period | 20 | Lookback period for Bollinger Band calculations | Decrease for faster volatility response, increase for smoother BBW readings |
| Source | Close | Price data used for calculation | Consider using HLC3 for more comprehensive price representation |
| StdDev Multiplier | 2.0 | Distance of bands from center line | Increase to capture wider price movements, decrease for tighter analysis |
| Lookback Period | 252 | Historical period for min-max normalization | Adjust based on timeframe: 252 for daily, 20-50 for shorter periods |

**Pro Tip:** BBWN values below 0.2 indicate volatility in the lowest 20% of the historical range (potential squeeze), while values above 0.8 indicate volatility in the highest 20% of the range (potential overextension).

## Calculation and Mathematical Foundation

**Simplified explanation:**
BBWN calculates the current Bollinger Band Width, then normalizes it using min-max scaling based on the historical range of BBW values over the specified lookback period.

**Technical formula:**
1. Calculate BBW = 2 × (StdDev Multiplier × Standard Deviation of Source over Period)
2. Find Historical Min = Minimum BBW value over Lookback Period
3. Find Historical Max = Maximum BBW value over Lookback Period
4. BBWN = (Current BBW - Historical Min) / (Historical Max - Historical Min)

**Detailed calculation steps:**
1. Compute current Bollinger Band Width using standard deviation method
2. Maintain a circular buffer of historical BBW values over the lookback period
3. Track the minimum and maximum values within the historical buffer
4. Apply min-max normalization formula to scale current BBW to [0,1] range
5. Handle edge cases where min equals max by returning 0.5

> 🔍 **Technical Note:** The implementation uses dual circular buffers with efficient min-max tracking. When new values are added to the historical buffer, the algorithm updates the minimum and maximum values by scanning the entire buffer, ensuring accuracy while maintaining reasonable performance. The normalization handles edge cases where the historical range is zero by defaulting to 0.5.

## Interpretation Details

BBWN provides precise volatility positioning within historical context:

* **Extreme Low Values (0.0-0.2):**
  - Current volatility is near historical minimums
  - Strong squeeze conditions with very low market volatility
  - High probability of impending volatility expansion
  - Optimal conditions for breakout anticipation strategies

* **Low-Medium Values (0.2-0.4):**
  - Volatility below historical average but not extreme
  - Moderate squeeze conditions
  - Potential for volatility increases
  - Suitable for cautious position building

* **Medium Values (0.4-0.6):**
  - Volatility near historical average
  - Balanced market conditions
  - No extreme volatility signals
  - Normal trading environment

* **Medium-High Values (0.6-0.8):**
  - Volatility above historical average
  - Elevated but not extreme market activity
  - Potential for volatility plateau or slight decrease
  - Consider tightening risk management

* **Extreme High Values (0.8-1.0):**
  - Current volatility near historical maximums
  - Extreme market conditions
  - High probability of volatility contraction
  - Optimal conditions for volatility fade strategies

## Trading Applications

**Systematic Volatility Trading:**
- Use BBWN thresholds (e.g., <0.2 for entries, >0.8 for exits) in systematic strategies
- Apply linear position sizing based on BBWN levels
- Implement volatility mean reversion strategies using BBWN extremes

**Risk Management:**
- Scale position sizes inversely with BBWN levels
- Adjust stop-loss distances based on current volatility position
- Modify trade frequency based on volatility environment

**Market Timing:**
- Enter long volatility positions when BBWN < 0.3
- Enter short volatility positions when BBWN > 0.7
- Use BBWN trends to time market entries and exits

**Portfolio Management:**
- Adjust portfolio volatility targets based on BBWN readings
- Rebalance more frequently during high BBWN periods
- Increase diversification when BBWN indicates extreme conditions

## Signal Combinations

**Strong Squeeze Signals:**
- BBWN below 0.1 for multiple consecutive periods
- BBWN making new lows while price consolidates
- Volume declining concurrent with falling BBWN

**Volatility Breakout Confirmation:**
- BBWN rising rapidly from extreme lows (0.0-0.2)
- Price breaking key levels while BBWN increases
- Volume expansion accompanying BBWN increases

**Overextension Warnings:**
- BBWN above 0.9 with price at extremes
- BBWN remaining elevated (>0.8) for extended periods
- Divergence between price momentum and BBWN levels

## Advantages Over Other Volatility Measures

**BBWN vs. BBWP:**
- BBWN: Linear scaling preserves relative volatility relationships
- BBWP: Percentile ranking may compress or expand volatility differences

**BBWN vs. Raw BBW:**
- BBWN: Normalized scale enables cross-market and cross-timeframe comparison
- BBW: Absolute values require manual scaling and interpretation

**BBWN vs. Z-Score Normalization:**
- BBWN: Bounded [0,1] scale with clear extreme levels
- Z-Score: Unbounded scale that may produce outliers

## Limitations and Considerations

* **Range dependency:** Results change when new historical extremes are established
* **Lookback sensitivity:** Different lookback periods can produce significantly different scaling
* **Edge case handling:** May produce misleading readings when historical range is very small
* **Extreme event impact:** Single extreme events can distort the normalization for extended periods
* **Linear assumption:** Assumes equal importance of all volatility levels within the range
* **Historical bias:** Based on past data which may not predict future volatility patterns

## Advanced Applications

**Quantitative Strategy Development:**
- Use BBWN as input for machine learning volatility models
- Implement systematic volatility trading based on BBWN thresholds
- Create volatility-adjusted position sizing algorithms

**Multi-Timeframe Analysis:**
- Compare BBWN across different timeframes for confirmation
- Use longer-term BBWN for strategic positioning, shorter-term for tactical entries
- Identify timeframe alignment for higher-probability setups

**Volatility Clustering:**
- Identify periods of persistent low or high BBWN readings
- Analyze transition patterns between volatility regimes
- Develop regime-dependent trading strategies

## References

* Bollinger, J. (2002). Bollinger on Bollinger Bands. McGraw-Hill Education.
* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
* Pardo, R. (2008). The Evaluation and Optimization of Trading Strategies. John Wiley & Sons.
* Chan, E. (2009). Quantitative Trading: How to Build Your Own Algorithmic Trading Business. John Wiley & Sons.
* Kaufman, P. (2013). Trading Systems and Methods, 5th Edition. Wiley Trading.
