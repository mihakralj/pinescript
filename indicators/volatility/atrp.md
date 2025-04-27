# ATRP: Average True Range Percent

[Pine Script Implementation of ATRP](https://github.com/mihakralj/pinescript/blob/main/indicators/volatility/atrp.pine)

## Overview and Purpose

Average True Range Percent (ATRP) scales Wilder’s ATR by the instrument’s closing price and expresses the result in percent. This simple normalization, introduced by system developers in the 1990s, makes raw volatility directly comparable between stocks, futures, crypto, or forex pairs regardless of price level. ATRP is a quick gauge of relative turbulence, useful for watchlist filtering, stop calibration, and regime analysis.

## Core Concepts

* **Percent‑based volatility** — ATR ÷ Close × 100 removes price bias  
* **Cross‑market comparability** — rank symbols or timeframes by identical metric  
* **Volatility regime shifts** — rising/falling ATRP flags transitions between quiet and explosive phases  

Market application:  
* **Asset selection** — trade high‑ATRP symbols for breakout systems  
* **Risk scaling** — size positions inversely to ATRP for equal‑volatility weighting  
* **Stop setting** — trail price by *k × ATRP %* of price

Timeframe suitability:  
* **All frames** — from 1‑minute scalps to weekly swing, normalization adapts automatically.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 14 | ATR smoothing window | Shorten for reactive scalping; lengthen for macro view |
| Source | HLC | Price set for True Range | Usually left unchanged |
| Multiplier | 100 | Percent conversion factor | Use 1 for fractional form |

**Pro Tip:** Plot a 50‑period SMA of ATRP and trade breakouts only when current ATRP is above its average—this filters low‑energy setups.

## Calculation and Mathematical Foundation

**Simplified explanation:**  
Measure ATR volatility, divide by current close, then multiply by 100 to obtain percentage movement per bar.

**Technical formula:**

ATRPₙ = 100 × ATRₙ ⁄ Cᵗ  

ATRₙ = WilderMAₙ(TR)  
TRᵗ = max( Hᵗ − Lᵗ, |Hᵗ − Cᵗ⁻¹|, |Lᵗ − Cᵗ⁻¹| )

> 🔍 **Technical Note:** Because both numerator (ATR) and denominator (Close) can trend, ATRP often exhibits mean‑reverting behavior suitable for volatility breakout thresholds.

## Interpretation Details

* **High ATRP (> 2 %)** — market is hot; favor momentum and wide stops  
* **Low ATRP (< 0.5 %)** — dull environment; lean toward mean‑reversion or stay flat  
* **Surging ATRP** — volatility ignition; confirms breakout strength  
* **Diverging price vs. ATRP** — shrinking ATRP during trend warns of exhaustion

## Limitations and Considerations

* **Lag from smoothing** — volatile spikes reflected gradually  
* **Corporate actions** — splits/dividends distort percent values; use adjusted data  
* **Micro‑priced assets** — pennies inflate ATRP; apply floor filter

Complementary tools: ADX for trend validation, Bollinger Band Width, and Keltner Channel ATR bands.

## References

1. Wilder, J. W. Jr. *New Concepts in Technical Trading Systems*, 1978.  
2. Schwager, J. *Technical Analysis*, 1996.
