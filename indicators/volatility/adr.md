# ADR: Average Daily Range

[Pine Script Implementation of ADR](https://github.com/mihakralj/pinescript/blob/main/indicators/volatility/adr.pine)

## Overview and Purpose

The Average Daily Range (ADR) is a volatility indicator that measures the average price movement within a single trading day over a specified period. Unlike complex volatility indicators, ADR provides a straightforward, intuitive measure of market activity expressed in the same units as price (e.g., dollars, pips, points). This makes it particularly valuable for position sizing, stop placement, and identifying potential trading opportunities based on volatility patterns.

The implementation provided offers the flexibility to choose between different averaging methods (SMA, EMA, WMA) to suit various trading styles and market conditions. By quantifying the typical daily price movement, ADR helps traders establish realistic expectations for price action, set appropriate stop-loss and take-profit levels, and adjust their strategies as market volatility expands or contracts over time.

## Core Concepts

* **Daily price range:** Measures the difference between the high and low price for each day
* **Moving average:** Applies selected smoothing method (SMA, EMA, or WMA) to these daily ranges
* **Volatility pattern recognition:** Identifies periods of expanding or contracting volatility
* **Risk management framework:** Provides objective basis for position sizing and stop placement

ADR stands apart from other volatility indicators by focusing exclusively on the intraday price range, making it particularly valuable for day traders and swing traders who need to understand typical daily price movements. Unlike percentage-based measures like Average True Range Percent (ATRP), ADR preserves the absolute price measurement, allowing for direct incorporation into trading rules without additional conversion.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 14 | Number of days to average | Shorter (7-10) for more responsiveness to recent volatility; longer (20-30) for more stable readings |
| Method | SMA (1) | Smoothing method: SMA (1), EMA (2), or WMA (3) | SMA for equal weighting, EMA for more recent bias, WMA for graduated weighting |

**Pro Tip:** Try using different ADR lengths across multiple timeframes. For example, a 7-day ADR on a daily chart helps with short-term position sizing, while a 20-day ADR on a weekly chart provides context for longer-term trades and strategic stop placement.

## Calculation and Mathematical Foundation

**Simplified explanation:**
ADR calculates the high-low range for each day, then averages these ranges over the specified period using the selected smoothing method (SMA, EMA, or WMA).

**Technical formula:**

1. Daily Range = High - Low

2. Averaging methods:
   - SMA: Simple average of ranges over the lookback period
   - EMA: Exponentially weighted average with bias-correction
   - WMA: Weighted average with linearly decreasing weights

> 🔍 **Technical Note:** The implementation uses circular buffers for SMA and WMA calculations, maintaining O(1) computational complexity regardless of the lookback period. For EMA, a bias correction factor is applied to ensure accurate values even during the initialization period, preventing the common "warm-up effect" seen in many EMA implementations.

## Interpretation Details

ADR provides several analytical perspectives:

* **Volatility assessment:** Higher ADR values indicate more volatile market conditions; lower values suggest calmer markets
* **Support/resistance identification:** Adding/subtracting ADR from opening price can identify potential intraday support/resistance levels
* **Trade filters:** Only taking trades when price has moved less than X% of the ADR to avoid chasing moves
* **Stop-loss placement:** Using a percentage of ADR (e.g., 50-100%) as a stop distance for new positions
* **Take-profit targets:** Setting profit targets at multiples of ADR (e.g., 1.0-1.5 × ADR) from entry price
* **Breakout confirmation:** Moves exceeding 150% of ADR might indicate significant breakouts
* **Volatility cycles:** Tracking ADR expansion and contraction over time can identify market regime changes

## Limitations and Considerations

* **Historical bias:** Past volatility doesn't guarantee future volatility patterns
* **Intraday consistency:** A day with a wide range may still have extended quiet periods
* **Gap handling:** ADR only measures intraday range, ignoring overnight gaps that may affect trading risk
* **Time zone dependency:** Different trading sessions (Asian, European, American) may have different typical ranges
* **Special events impact:** ADR may be distorted around news events, earnings, or economic releases
* **Timeframe sensitivity:** ADR on lower timeframes (H1, H4) may produce different values than daily charts
* **Computational lag:** EMA and WMA methods reduce lag compared to SMA but may be more sensitive to recent outliers

## References

* Wilder, J. W. (1978). New Concepts in Technical Trading Systems. Trend Research.
* Williams, L. (1999). Long-Term Secrets to Short-Term Trading. Wiley Trading.
* Schwager, J. D. (1995). Technical Analysis of the Financial Markets. New York Institute of Finance.
* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
