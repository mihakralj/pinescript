# TWAP: Time Weighted Average Price

[Pine Script Implementation of TWAP](https://github.com/mihakralj/pinescript/blob/main/indicators/volume/twap.pine)

## Overview and Purpose

The Time Weighted Average Price (TWAP) is a trading benchmark that represents the average price a security has traded at over a specified time period, with each price weighted equally by time rather than volume. TWAP calculates a simple arithmetic mean of all prices observed during the session, making it fundamentally different from volume-weighted benchmarks like VWAP. Originally developed for algorithmic trading execution, TWAP is used to spread large orders evenly over time to minimize market impact and achieve fair average execution prices. This implementation provides comprehensive timeframe support with session resets ranging from 1-minute intervals to annual periods, accommodating everything from high-frequency execution strategies to long-term position analysis.

## Core Concepts

* **Time weighting:** Each price observation receives equal weight regardless of trading volume, providing a true time-based average
* **Execution benchmark:** Primarily used to evaluate whether trades were executed at better or worse prices than the time-based average
* **Market impact minimization:** Spreading orders evenly over time helps avoid moving the market against large positions
* **Algorithmic trading:** Core metric for TWAP execution algorithms that slice orders into equal time intervals

TWAP provides a pure time-based view of average price, making it ideal for evaluating execution quality when the goal is to trade evenly over a time period rather than matching volume patterns.

## TWAP vs VWAP: Key Differences

| Aspect | TWAP | VWAP |
|--------|------|------|
| **Weighting** | Equal weight per time interval | Weighted by volume |
| **Formula** | Sum(Prices) / Count(Prices) | Sum(Price × Volume) / Sum(Volume) |
| **Use Case** | Even time distribution | Volume-based distribution |
| **Execution Strategy** | Split order equally over time | Match market volume patterns |
| **Market Impact** | Spreads impact evenly | Concentrates on high-volume periods |
| **Calculation** | Simpler (no volume needed) | Complex (volume-dependent) |
| **Best For** | Time-based execution | Volume-following execution |

**Example:** If you need to buy 10,000 shares over 2 hours:
- **TWAP strategy**: Buy ~83 shares per minute (10,000 / 120 minutes) regardless of volume
- **VWAP strategy**: Buy more during high-volume periods, less during low-volume periods

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Source | ohlc4 | Price point used for calculation | ohlc4 provides balanced representation; consider close for end-of-period focus |
| Session Reset | 1D | When to reset TWAP calculation | Select based on execution timeframe and trading strategy |

### Session Reset Options

This implementation provides comprehensive timeframe support for TWAP reset periods:

**Minute-based resets:**
- 1m, 2m, 3m, 5m, 10m, 15m, 30m, 45m - For ultra-short-term execution and scalping

**Hour-based resets:**
- 1H, 2H, 3H, 4H - For intraday execution strategies and session-based trading

**Day/Week/Month resets:**
- 1D (Daily) - Most common for institutional execution benchmarking
- 1W (Weekly) - For swing trading and weekly execution evaluation
- 1M (Monthly) - For long-term position building and monthly performance

**Extended period resets:**
- 3M, 6M, 12M - For strategic position accumulation and quarterly/annual benchmarks

**Special options:**
- Never - Cumulative TWAP from the first available bar (entire dataset)

**Pro Tip:** Most TWAP execution algorithms use intraday resets (1H, 4H, 1D) to match their execution window. For evaluating execution quality, match the TWAP period to your actual execution timeframe. Shorter periods (15m, 30m) are useful for evaluating rapid execution, while longer periods (1D, 1W) better suit patient accumulation strategies.

## Calculation and Mathematical Foundation

**Simplified explanation:**
TWAP calculates the simple arithmetic mean of all prices observed during a session. Each bar's price is added to a running sum, a counter tracks the number of observations, and TWAP is the sum divided by the count. Unlike VWAP, trading volume has no influence on the calculation.

**Technical formula:**
TWAP = Σ(Prices) / n

Where:
- Σ(Prices) = Sum of all price observations in the period
- n = Number of price observations (bar count)

**Wikipedia formula (generalized):**
TWAP = Σ(Pⱼ × Tⱼ) / Σ(Tⱼ)

Where:
- Pⱼ = Price at time j
- Tⱼ = Time interval duration
- For equal time intervals (typical in chart data), this simplifies to the arithmetic mean

**Implementation approach:**
```
Session start: Reset sum and count
For each new bar in session:
1. Add current price to cumulative sum
2. Increment observation counter
3. TWAP = Cumulative Sum / Counter
```

> 🔍 **Technical Note:** This implementation uses persistent variables to maintain the cumulative sum and count across the session. The algorithm resets both values when the session reset condition triggers based on the selected timeframe (from 1-minute to 12-month intervals, or never for cumulative calculation). The calculation is volume-independent and treats each time period equally, providing a pure time-weighted average.

## Interpretation Details

TWAP provides multiple analytical and execution perspectives:

* **Execution benchmark:** Compare your executed price to TWAP to evaluate execution quality (beat TWAP = good, worse than TWAP = poor)
* **Trend indication:** Price consistently above TWAP suggests buying pressure; below suggests selling pressure
* **Fair value reference:** TWAP represents the "fair" time-weighted price for the session
* **Algorithmic trading:** TWAP algorithms aim to execute at or better than the TWAP price
* **Support/resistance:** Like VWAP, TWAP can act as dynamic support in uptrends and resistance in downtrends
* **Mean reversion:** Significant deviations from TWAP may indicate potential reversion opportunities

## Trading Applications

### TWAP Execution Algorithm

The primary use of TWAP is in algorithmic execution:

1. **Order slicing:** Divide large order into equal-sized pieces
2. **Time distribution:** Execute pieces at regular time intervals
3. **Price evaluation:** Compare executed prices against TWAP benchmark
4. **Performance measurement:** Calculate slippage relative to TWAP

**Example:** To buy 100,000 shares using a 2-hour TWAP strategy:
- Time window: 10:00 AM - 12:00 PM (120 minutes)
- Slice size: 833 shares per minute
- Execution: Buy 833 shares every minute
- Benchmark: Compare average execution price to 2-hour TWAP

### TWAP vs Market Timing

- **TWAP advantages:** Predictable, reduces market impact, simple to execute
- **TWAP limitations:** Ignores volume patterns, may trade during illiquid periods
- **Best for:** Large orders, illiquid securities, when stealth is important

## Limitations and Considerations

* **Volume ignorance:** TWAP doesn't account for trading volume, potentially executing during illiquid periods
* **Market impact:** While spreading orders helps, TWAP can still move thin markets
* **Price trends:** In strong trends, TWAP may consistently lag, resulting in poor execution
* **Session sensitivity:** Different reset periods produce significantly different values
* **Information leakage:** Predictable execution patterns can be exploited by predatory traders
* **Urgency tradeoff:** TWAP sacrifices urgency for price improvement; not suitable when immediate execution is critical
* **Market conditions:** Works best in stable, liquid markets; less effective during volatile periods or news events
* **Complementary tools:** Best used alongside market microstructure analysis, volume profile, and real-time market impact models

## TWAP Execution Strategies

### Basic TWAP
- Equal order slices at equal time intervals
- Most straightforward implementation
- Minimal complexity

### Adaptive TWAP
- Adjust slice sizes based on real-time market conditions
- Accelerate during favorable prices
- Decelerate during adverse moves

### Percentage of Volume (POV) Hybrid
- Combine TWAP time distribution with volume targeting
- Participate at X% of market volume within TWAP intervals
- Balances time-based and volume-based execution

## References

* Berkowitz, S.A., Logue, D.E., Noser, E.A. (1988). "The Total Cost of Transactions on the NYSE." Journal of Finance, 43(1), 97-112.
* Kissell, R., Glantz, M. (2003). "Optimal Trading Strategies." AMACOM.
* Almgren, R., Chriss, N. (2001). "Optimal Execution of Portfolio Transactions." Journal of Risk, 3, 5-39.
* Perold, A.F. (1988). "The Implementation Shortfall: Paper versus Reality." Journal of Portfolio Management, 14(3), 4-9.
* Wikipedia: [Time-weighted average price](https://en.wikipedia.org/wiki/Time-weighted_average_price)

## See Also

* [VWAP](/indicators/volume/vwap.md) - Volume Weighted Average Price
* [VWMA](/indicators/volume/vwma.md) - Volume Weighted Moving Average
* [OBV](/indicators/volume/obv.md) - On Balance Volume
