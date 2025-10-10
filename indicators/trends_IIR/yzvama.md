# YZVAMA: Yang-Zhang Volatility Adjusted Moving Average

[Pine Script Implementation of YZVAMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_IIR/yzvama.pine)

## Overview and Purpose

The Yang-Zhang Volatility Adjusted Moving Average (YZVAMA) is an advanced adaptive indicator that dynamically adjusts its calculation period based on the percentile rank of short-term Yang-Zhang Volatility (YZV) relative to historical volatility levels. Unlike traditional moving averages with fixed periods or simple volatility ratios, YZVAMA uses percentile ranking to provide context-aware adaptation that responds to both absolute volatility levels and their relative significance within recent market history. This makes YZVAMA particularly effective at distinguishing between normal volatility fluctuations and genuine regime changes.

## Core Concepts

* **Percentile-based adaptation:** Uses statistical ranking rather than raw volatility ratios for more stable adjustment
* **YZV measurement:** Leverages comprehensive Yang-Zhang Volatility that accounts for gaps, overnight moves, and intraday ranges
* **Multi-timeframe volatility:** Compares short-term YZV(3) against longer-term baseline YZV(50) through percentile context
* **Dynamic responsiveness:** Automatically shortens during high-volatility percentiles (fast response) and lengthens during low-volatility percentiles (smooth trending)

The fundamental principle behind YZVAMA is that volatility should be evaluated in relative terms rather than absolute values. A volatility spike that would be extreme in a calm market might be normal in a turbulent market. By using percentile ranking, YZVAMA adapts appropriately to the prevailing volatility regime while still responding to significant changes.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Short YZV Period | 3 | Current volatility measurement window | Keep short (3-5) for rapid volatility detection |
| Long YZV Period | 50 | Baseline volatility measurement window | Increase for more stable baseline reference |
| Percentile Lookback | 100 | Historical window for percentile ranking | Larger values provide more stable rankings |
| Min Length | 5 | Minimum allowed adjusted length | Prevent over-responsiveness in extreme volatility |
| Max Length | 100 | Maximum allowed adjusted length | Cap smoothing during very low volatility |
| Source | close | Price data used for calculation | Consider using hlc3 for smoother input |

**Pro Tip:** The Percentile Lookback window should be significantly larger than the Long YZV Period to provide meaningful statistical context. A ratio of 2:1 or greater (e.g., 100:50) works well for most markets.

## Calculation and Mathematical Foundation

**Simplified explanation:**
YZVAMA calculates short-term YZV(3) to capture immediate volatility, maintains a longer-term YZV(50) baseline, then ranks the current YZV(3) against a rolling window of historical YZV values. High percentile ranks (meaning current volatility is high relative to history) trigger shorter MA periods for faster response. Low percentile ranks (current volatility is low relative to history) trigger longer MA periods for smoother trending.

**Technical formula:**

1. Calculate short-term Yang-Zhang Volatility:
   ```
   YZV_short(t) = sqrt(σ²_o + k·σ²_c + (1-k)·σ²_rs)
   
   where:
   σ²_o = overnight variance
   σ²_c = close-to-close variance
   σ²_rs = Rogers-Satchell intraday variance
   k = 0.34/(1.34 + (n+1)/(n-1))
   ```

2. Calculate percentile rank:
   ```
   Percentile(t) = (Rank(YZV_short(t)) / (N-1)) × 100
   
   where Rank = count of historical YZV values < current YZV
   N = number of valid historical values
   ```

3. Map percentile to adjusted length:
   ```
   Adjusted_Length(t) = Max_Length - (Percentile(t)/100) × (Max_Length - Min_Length)
   ```

4. Calculate YZVAMA:
   ```
   YZVAMA(t) = SMA(Price, Adjusted_Length(t))
   ```

> 🔍 **Technical Note:** The percentile calculation uses simple ranking to avoid interpolation complexity. When YZV_short is at the 95th percentile, it means current volatility exceeds 95% of recent historical values, triggering near-minimum MA length for maximum responsiveness.

## Interpretation Details

YZVAMA can be used in various trading strategies:

* **Adaptive trend following:** YZVAMA automatically adjusts to volatility regimes, staying responsive during volatile trends and smooth during calm markets
* **Volatility regime identification:** When adjusted length approaches Min_Length, the market is in a high-volatility regime; near Max_Length indicates low-volatility conditions
* **Crossover signals:** Price crossovers with YZVAMA generate signals naturally filtered by volatility context - more signals during volatility spikes, fewer during calm periods
* **Multi-asset comparison:** Percentile-based adaptation makes YZVAMA comparable across different assets with varying volatility characteristics
* **Gap-aware trading:** YZV's incorporation of overnight gaps makes YZVAMA particularly effective in markets with significant session breaks

## Practical Applications

* **High percentile (80-100):** Market is experiencing unusually high volatility relative to recent history
  - YZVAMA uses short periods (near Min_Length)
  - Excellent for capturing rapid trend changes
  - Consider wider stops due to increased noise
  - Signals are more frequent but require confirmation

* **Medium percentile (40-60):** Market volatility is typical for recent conditions
  - YZVAMA uses moderate periods
  - Balanced responsiveness and smoothing
  - Standard risk management applies
  - Most reliable signal quality

* **Low percentile (0-20):** Market is experiencing unusually low volatility
  - YZVAMA uses long periods (near Max_Length)
  - Superior smoothing reduces false signals
  - May lag at the start of new trends
  - Consider tighter stops as trends are clearer

* **Percentile transitions:** Rapid shifts in adjusted length signal volatility regime changes
  - Expansion (low to high): Prepare for increased market activity
  - Contraction (high to low): Consolidation or trend maturation likely

## Limitations and Considerations

* **Market conditions:** Like all MA-based indicators, YZVAMA may generate whipsaws during choppy, trendless markets, though less frequently than fixed-period MAs
* **Lagging indicator:** Despite adaptive nature, YZVAMA still lags price action and won't predict reversals
* **Data requirements:** Requires complete OHLC data for accurate YZV calculation; missing data affects both volatility measurement and adaptation
* **Percentile sensitivity:** The Percentile Lookback parameter significantly affects behavior - too short causes erratic adjustments, too long reduces responsiveness
* **Computational intensity:** More complex than simple MAs due to dual YZV calculations, percentile ranking, and adaptive SMA
* **Warm-up period:** Needs sufficient historical data (at least Percentile Lookback bars) for accurate percentile calculations
* **Extreme events:** Black swan events may not have historical precedent in the percentile window, potentially causing delayed response
* **Complementary tools:** Best used with momentum indicators, volume analysis, or other trend confirmation tools

## Comparison with Other Adaptive MAs

**YZVAMA vs VAMA:**
- YZVAMA uses percentile ranking vs VAMA's ratio approach
- More stable adaptation through statistical context
- Better handles extreme volatility events
- YZV more comprehensive than ATR (includes gaps)

**YZVAMA vs KAMA:**
- YZVAMA adapts to volatility context vs efficiency ratio
- More responsive to regime changes
- Better in markets with significant gaps
- YZV provides richer volatility information

**YZVAMA vs VIDYA:**
- Percentile ranking vs standard deviation ratio
- More robust to outliers through ranking
- Dual-timeframe YZV provides better context
- Superior performance in gap-prone markets

## References

1. Yang, S. and Zhang, Q. "Drift-Independent Volatility Estimation Based on High, Low, Open, and Close Prices." *Journal of Business*, 73(3), 2000.
2. Kaufman, Perry J. "Trading Systems and Methods." Wiley, 2013.
3. Chande, Tushar S. and Kroll, Stanley. "The New Technical Trader." Wiley, 1994.
4. Sinclair, E. "Volatility Trading." Wiley, 2013.
