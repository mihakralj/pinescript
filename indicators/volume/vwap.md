# VWAP: Volume Weighted Average Price

[Pine Script Implementation of VWAP](https://github.com/mihakralj/pinescript/blob/main/indicators/volume/vwap.pine)

## Overview and Purpose

The Volume Weighted Average Price (VWAP) is a trading benchmark that gives the average price a security has traded at throughout the session, based on both volume and price. VWAP is calculated by taking the cumulative total of price multiplied by volume, divided by the cumulative total volume from the session start. Originally developed for institutional trading, VWAP serves as a benchmark to determine whether a security is trading above or below its average price weighted by trading activity. This implementation provides comprehensive timeframe support with session resets ranging from 1-minute intervals to annual periods, accommodating everything from scalping strategies to long-term position analysis.

## Core Concepts

* **Volume weighting:** Prices with higher volume have greater influence on the average, reflecting actual market activity more accurately than simple price averages
* **Market application:** Widely used as a benchmark for trade execution quality, trend identification, and support/resistance levels
* **Timeframe suitability:** Effective on all timeframes, with intraday charts most common for traditional VWAP analysis

VWAP provides a more realistic view of average price than simple moving averages because it accounts for the actual trading activity at each price level. This makes it particularly valuable for understanding where the majority of trading volume occurred.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Source | hlc3 | Price point used for calculation | hlc3 provides balanced representation; consider close for end-of-period focus |
| Session Reset | 1D | When to reset VWAP calculation | Select based on trading strategy and analysis timeframe |

### Session Reset Options

This implementation provides comprehensive timeframe support for VWAP reset periods:

**Minute-based resets:**
- 1m, 2m, 3m, 5m, 10m, 15m, 30m, 45m - For scalping and ultra-short-term analysis

**Hour-based resets:**
- 1H, 2H, 3H, 4H - For intraday swing trading and session-based analysis

**Day/Week/Month resets:**
- 1D (Daily) - Traditional VWAP, most common for institutional benchmarking
- 1W (Weekly) - For swing trading and weekly trend analysis
- 1M (Monthly) - For position trading and monthly performance evaluation

**Extended period resets:**
- 3M, 6M, 12M - For long-term trend analysis and quarterly/annual benchmarks

**Special options:**
- Never - Cumulative VWAP from the first available bar (entire dataset)

**Pro Tip:** Traditional institutional VWAP uses daily resets (1D). For algorithmic trading, shorter resets (1H, 4H) can provide more responsive benchmarks. Longer resets (1W, 1M) are valuable for identifying major support/resistance levels based on volume-weighted price action over extended periods.

## Calculation and Mathematical Foundation

**Simplified explanation:**
VWAP calculates the cumulative average price weighted by volume from the session start. Each price point is multiplied by its corresponding volume, these products are accumulated, then divided by the total accumulated volume to get the session-based volume-weighted average.

**Technical formula:**
VWAP = Σ(Price × Volume) / Σ(Volume)

For a session-based implementation:
```
Session start: Reset sums to zero
For each new bar in session:
1. Add current price×volume to cumulative sum
2. Add current volume to cumulative volume sum
3. VWAP = Cumulative(Price×Volume) / Cumulative(Volume)
```

> 🔍 **Technical Note:** This implementation uses persistent variables to maintain cumulative sums across the session. The algorithm resets sums when the session reset condition is triggered based on the selected timeframe (from 1-minute to 12-month intervals, or never for cumulative calculation). Zero volume bars are handled gracefully without affecting the calculation, maintaining the previous VWAP value when no trading activity occurs.

## Interpretation Details

VWAP provides multiple analytical perspectives:

* **Trend identification:** When price is above VWAP, it suggests bullish sentiment; below suggests bearish sentiment
* **Support/resistance:** VWAP often acts as dynamic support in uptrends and resistance in downtrends
* **Execution benchmark:** Institutional traders use VWAP to evaluate trade execution quality
* **Reversal signals:** Significant deviations from VWAP may indicate potential mean reversion opportunities
* **Volume confirmation:** Strong moves accompanied by volume that pulls VWAP in the same direction confirm trend strength

## Limitations and Considerations

* **Volume dependency:** Effectiveness depends on consistent volume data; low volume periods may produce less reliable signals
* **Session sensitivity:** Different session reset periods (daily, weekly, monthly) can produce significantly different values and interpretation
* **Early session reliability:** VWAP is less reliable early in the session when limited volume data is available
* **Market structure:** More effective in liquid markets with consistent volume patterns throughout the session
* **Session gaps:** Price gaps at session open may cause initial VWAP distortion until sufficient volume accumulates
* **Complementary tools:** Best used alongside momentum indicators, price action analysis, and volume profile tools for comprehensive market analysis

## References

* Berkowitz, S.A., Logue, D.E., Noser, E.A. (1988). "The Total Cost of Transactions on the NYSE." Journal of Finance, 43(1), 97-112.
* Kissell, R., Glantz, M. (2003). "Optimal Trading Strategies." AMACOM.
* Almgren, R., Chriss, N. (2001). "Optimal Execution of Portfolio Transactions." Journal of Risk, 3, 5-39.
