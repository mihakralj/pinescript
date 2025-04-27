# ADX: Average Directional Movement Index

[Pine Script Implementation of ADX](https://github.com/mihakralj/pinescript/blob/main/indicators/dynamics/adx.pine)

## Overview and Purpose

The Average Directional Movement Index (ADX) is a technical indicator designed to measure the strength of a trend, regardless of its direction. Developed by J. Welles Wilder Jr. and introduced in his 1978 book "New Concepts in Technical Trading Systems," ADX helps traders determine whether a market is trending or trading sideways. Unlike directional indicators that focus on price direction, ADX specifically quantifies trend strength on a scale from 0 to 100, providing traders with a clear measure of when a trend is gaining or losing momentum. This makes it particularly valuable for deciding when trend-following strategies are appropriate versus when range-bound approaches might be more effective.

## Core Concepts

* **Trend strength measurement:** Quantifies the strength of a price trend independent of its direction, helping traders distinguish between trending and non-trending market conditions
* **Directional movement analysis:** Incorporates Positive Directional Indicator (+DI) and Negative Directional Indicator (-DI) to provide additional insight into trend direction
* **Timeframe flexibility:** Works effectively across various timeframes, though traditionally applied to daily charts where trends tend to develop more clearly

The core principle of ADX is its focus on measuring trend strength rather than direction. By analyzing the relationship between price movement and range, ADX creates a normalized measurement of how strongly price is moving in any direction. This focus on strength rather than direction makes it an excellent filter for determining when trend-following strategies are appropriate versus when mean-reversion approaches might work better.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 14 | Controls the smoothing period | Increase for less sensitivity and fewer signals, decrease for more responsiveness |
| Source | Close | Price data used for calculation | Rarely needs adjustment as ADX relies on high/low ranges |
| DI Length | 14 | Period for directional indicators | Typically kept the same as the main length parameter |

**Pro Tip:** The 25 level is widely considered the threshold for identifying meaningful trends - when ADX rises above 25, trend-following strategies tend to perform better, while readings below 20 often indicate range-bound conditions where mean-reversion strategies may be more effective.

## Calculation and Mathematical Foundation

**Simplified explanation:**
ADX first measures price movement in both up and down directions, then compares these movements to the total range to determine how much of the price action is directional versus random. These calculations are smoothed over time to create a consistent measure of trend strength regardless of direction.

**Technical formula:**
ADX is calculated through a multi-stage process:

1. True Range (TR) = max(high - low, |high - previous close|, |low - previous close|)
2. +DM (Directional Movement) = if (high - previous high > previous low - low) and (high - previous high > 0) then high - previous high else 0
3. -DM = if (previous low - low > high - previous high) and (previous low - low > 0) then previous low - low else 0
4. +DI = 100 × RMA(+DM, length) / RMA(TR, length)
5. -DI = 100 × RMA(-DM, length) / RMA(TR, length)
6. DX = 100 × |+DI - -DI| / (+DI + -DI)
7. ADX = RMA(DX, length)

Where RMA is Wilder's smoothing method, equivalent to an EMA with alpha = 1/length

> 🔍 **Technical Note:** ADX is particularly effective at identifying the beginning and end of trends. Rising ADX indicates increasing trend strength, while falling ADX suggests the trend is weakening, regardless of whether prices are moving up or down.

## Interpretation Details

ADX can be used in various trading strategies:

* **Trend identification:** ADX values above 25 generally indicate a trending market, while values below 20 suggest a ranging market
* **Trend strength assessment:** Higher ADX values indicate stronger trends, with readings above 50 signaling extremely strong trending conditions
* **Trend exhaustion:** When ADX reaches extreme levels (above 50) and then begins to decline, it may signal potential trend exhaustion
* **Entry filter:** Using ADX as a filter to only take trend-following trades when ADX is above 25
* **Strategic approach selection:** Switching between trend-following strategies (when ADX is high) and range-bound strategies (when ADX is low)
* **Directional bias:** When used with +DI and -DI, crossovers can suggest potential trend direction changes

## Limitations and Considerations

* **Lagging indicator:** ADX responds after trends have already established, potentially missing early trend development
* **False signals:** Can occasionally produce false signals during volatile market conditions
* **Smoothing effect:** The extensive smoothing creates significant lag in identifying trend changes
* **No directional indication:** By itself, ADX doesn't indicate trend direction, only strength
* **Complementary tools:** Best used alongside price action analysis and other indicators for confirmation

## References

* Wilder, J. Welles. "New Concepts in Technical Trading Systems," Trend Research, 1978
* Murphy, John J. "Technical Analysis of the Financial Markets," New York Institute of Finance, 1999
