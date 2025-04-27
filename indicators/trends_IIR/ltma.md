# LTMA: Linear Time Moving Average

[Pine Script Implementation of LTMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_IIR/ltma.pine)

## Overview and Purpose

The Linear Time Moving Average (LTMA) is a weighted technical indicator that applies linearly increasing weights to price data based on recency. Not to be confused with linear regression-based moving averages, LTMA is specifically a time-weighted average where the weight increases linearly with time recency. Unlike simple moving averages that weight all prices equally, or exponential moving averages that weight prices geometrically, LTMA assigns weights that increase in a straight-line fashion from oldest to newest data points.

This unique weighting approach creates a moving average that emphasizes recent price action while still considering older data, providing a balance between responsiveness and stability. By applying greater importance to more recent prices in a gradual, linear manner, LTMA offers traders a smooth representation of price trends that responds more quickly to recent changes than an SMA without the potential overreaction of an EMA.

## Core Concepts

* **Linear weighting:** Applies weights that increase linearly from oldest to newest data points, with the most recent price receiving the highest weight
* **Time-proportional importance:** Assigns importance to each price point proportional to its recency, creating a balanced view of recent price action
* **Smooth transition:** Creates smoother transitions between price regimes than simple averages while avoiding excessive jumpiness
* **Trend representation:** Provides a natural representation of the current price trajectory by emphasizing the most recent market activity

LTMA achieves its linear weighting by assigning each price a weight directly proportional to its position in the lookback window. For a period of N, the most recent price receives a weight of N, the second most recent a weight of N-1, and so on, with the oldest price receiving a weight of 1. This creates a straight-line gradient of importance based purely on time recency, not trend calculation, that smoothly emphasizes recent market activity.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Period | 10 | Controls the lookback window | Increase for longer-term trends, decrease for shorter-term signals |
| Source | Close | Data point used for calculation | Change to HL2 or HLC3 for more balanced price representation |

**Pro Tip:** When transitioning from SMA to LTMA, many traders find that using approximately 80% of their typical SMA period for LTMA provides comparable smoothing with improved responsiveness (e.g., LTMA(16) instead of SMA(20)).

## Calculation and Mathematical Foundation

**Simplified explanation:**
LTMA works by calculating a weighted average of prices where the weights increase linearly with recency. The most recent price has the highest weight (equal to the period), and each older price has a progressively smaller weight, decreasing by 1 for each bar back in time.

**Technical formula:**
LTMA = ∑(Price(i) × Weight(i)) / ∑Weight(i)

Where:
- Price(i) is the price i bars ago
- Weight(i) = (Period - i) for i from 0 to Period-1
- The denominator ∑Weight(i) normalizes the result

For a period of N, the sum of weights equals N(N+1)/2, which is used for normalization.

> 🔍 **Technical Note:** This implementation handles missing data (NA values) gracefully by adjusting both the weighted sum and total weight accordingly. This ensures the indicator produces valid results even with gaps in the data or at the beginning of a series before a full period's worth of data is available.

## Interpretation Details

LTMA provides several key insights for traders:

- When price crosses above LTMA, it often signals the beginning of an uptrend
- When price crosses below LTMA, it often signals the beginning of a downtrend
- The slope of LTMA provides insight into trend strength and momentum
- LTMA creates dynamic support and resistance levels during trending markets
- Multiple LTMA lines with different periods can identify potential reversal zones

LTMA is particularly effective for medium-term trend following strategies, where its linear weighting provides a balanced view of recent price action. It responds more quickly to price changes than SMA but avoids the whipsaws that can occur with EMA, making it suitable for identifying genuine trend changes while filtering out minor fluctuations.

## Limitations and Considerations

* **Market conditions:** Like all moving averages, less effective during extended sideways or choppy markets
* **Lag factor:** While more responsive than SMA, still exhibits some lag during sharp price movements
* **Intermediate responsiveness:** Less responsive than exponential or adaptive moving averages during strong trends
* **Computational requirements:** Requires storing and processing the full lookback period, unlike recursive moving averages
* **Complementary tools:** Works best when combined with momentum oscillators or volume indicators for confirmation

## References

1. Kaufman, P. (2013). *Trading Systems and Methods*, 5th Edition. Wiley Trading.
2. Murphy, J.J. (1999). *Technical Analysis of the Financial Markets*. New York Institute of Finance.
3. Pring, M.J. (2002). *Technical Analysis Explained*, 4th Edition. McGraw-Hill.
