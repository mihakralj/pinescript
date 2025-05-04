# Stoch: Stochastic Oscillator

[Pine Script Implementation of Stoch](https://github.com/mihakralj/pinescript/blob/main/indicators/oscillators/stoch.pine)

## Overview and Purpose

The Stochastic Oscillator is a momentum indicator that compares a security's closing price to its price range over a specific period. Developed by George Lane in the late 1950s, this indicator helps traders identify potential trend reversals by measuring the momentum of price movements. It operates on the principle that during uptrends, prices tend to close near their highs, and during downtrends, prices tend to close near their lows.

By tracking the position of the current close relative to the recent trading range, the Stochastic Oscillator provides insights into overbought and oversold conditions, as well as potential momentum shifts before they become evident in price action. It consists of two lines: %K (the main line) and %D (the signal line), which oscillate between 0 and 100.

## Core Concepts

* **Range Position:** Measures where the current closing price is positioned relative to the high-low range over a specified period, expressed as a percentage.
* **Momentum Shifts:** Identifies when price momentum may be changing before actual price reversals occur.
* **Overbought/Oversold:** Provides clear threshold levels (typically 80 and 20) to identify potential market extremes.
* **Signal Line Crossovers:** Generates trading signals when the fast %K line crosses the slower %D line.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
| :-------- | :------ | :------- | :------------ |
| K Length | 14 | Period for calculating the %K line | Lower (5-9) for more signals but increased noise, higher (20+) for fewer but more reliable signals |
| D Smooth | 3 | Smoothing period for the %D signal line | Lower values increase responsiveness, higher values reduce false signals |

**Pro Tip:** Use divergences between the Stochastic Oscillator and price for powerful signals - when price makes a new high but the oscillator fails to make a new high, it often indicates weakening momentum that may precede a reversal.

## Calculation and Mathematical Foundation

**Simplified explanation:**
The Stochastic Oscillator calculates where the current closing price sits relative to the highest high and lowest low over a specified period. If the close is near the high, the value approaches 100; if near the low, it approaches 0.

**Technical formula:**
%K = 100 × (Close - Lowest Low(K Length)) / (Highest High(K Length) - Lowest Low(K Length))
%D = SMA(%K, D Smooth)

Where:

* Close is the most recent closing price
* Lowest Low(K Length) is the lowest low over the K Length period
* Highest High(K Length) is the highest high over the K Length period
* SMA is the Simple Moving Average

> 🔍 **Technical Note:** The Pine Script implementation uses efficient dynamic arrays with deque operations for tracking highest highs and lowest lows, providing optimal performance with O(1) time complexity per bar. The algorithm carefully handles edge cases like equal highs/lows and maintains proper buffer management.

## Interpretation Details

The Stochastic Oscillator offers several approaches to market analysis:

* **Overbought/Oversold:** Readings above 80 suggest overbought conditions where prices may reverse down; readings below 20 suggest oversold conditions where prices may reverse up.
* **%K/%D Crossovers:** When %K crosses above %D, it's often considered a bullish signal; when %K crosses below %D, it's considered a bearish signal.
* **Divergences:** When price makes new highs/lows but the oscillator fails to confirm with corresponding extremes, it suggests potential reversal points.
* **Centerline Crosses:** Movements above or below the 50 level can indicate the general market direction and momentum strength.
* **Pattern Recognition:** Double tops or bottoms in the oscillator often precede significant price movements.

## Limitations and Considerations

* **Range-Bound Effectiveness:** Works best in sideways, range-bound markets; may generate false signals during strong trends.
* **Lagging Component:** Contains some inherent lag due to its smoothing components.
* **Sensitivity to Settings:** Results vary significantly based on parameter choices - what works in one market may not work in another.
* **False Signals:** Can remain in overbought/oversold territory for extended periods during strong trends, leading to premature signals.
* **Complementary Analysis:** Should be used with other technical tools like trend indicators or volume studies for confirmation.
* **Period Selection:** Shorter periods increase sensitivity but generate more noise; longer periods reduce false signals but decrease responsiveness.

## References

* Lane, G. C. (1984). Lane's Stochastics. Technical Analysis of Stocks and Commodities, 2(3).
* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
