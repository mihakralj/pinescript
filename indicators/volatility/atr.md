# ATR: Average True Range

[Pine Script Implementation of ATR](https://github.com/mihakralj/pinescript/blob/main/indicators/volatility/atr.pine)

## Overview and Purpose

Created by J. Welles Wilder Jr. and first published in *New Concepts in Technical Trading Systems* (1978), the Average True Range (ATR) measures pure price volatility without regard to direction. By extending the classic daily range to include overnight gaps it delivers a realistic estimate of how far the market can move in a single bar. Traders use ATR for volatility‑adjusted stops, position sizing, breakout validation, and market selection across all asset classes.

## Core Concepts

* **True Range expansion** — captures intraday movement *and* gaps to quantify total bar volatility  
* **Direction‑agnostic measurement** — focuses on magnitude, avoiding bullish/bearish bias  
* **Adaptive smoothing** — Wilder’s moving average damps noise while reacting to volatility bursts  

Market application:  

* **Risk management** — dynamic stops / Kelly‑style position sizing  
* **Volatility filters** — trade only when ATR exceeds a threshold  
* **Breakout confirmation** — high ATR supports range expansions

Timeframe suitability:  

* **Daily to intraday (≥ 5 m)** — smoothing offsets lower‑frame noise; longer frames give macro context

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 14 | Smoothing period (Wilder MA) | Shorten for faster response; lengthen for stability |
| Source | HLC | Price series used in True Range | Rarely changed; adjust only with non‑standard data feeds |
| Multiplier | 1 | Scales ATR for stops/targets | Increase for whipsaw‑prone symbols; decrease for tight risk |

**Pro Tip:** A trailing stop at 1.5–2 × ATR below the recent swing low (up‑trends) balances staying power with risk control.

## Calculation and Mathematical Foundation

**Simplified explanation:**  
Measure the greatest distance price could have travelled during the bar (including gaps) and average this range over *n* periods.

**Technical formula:**

ATRₙ = WilderMAₙ(TR)  

TRᵗ = max( Hᵗ − Lᵗ, |Hᵗ − Cᵗ⁻¹|, |Lᵗ − Cᵗ⁻¹| )

where H, L, C are high, low, close; *t* is current bar; *n* is Length.

> 🔍 **Technical Note:** Wilder’s MA is equivalent to an EMA with α = 1 / *n*, so ATR reaches ≈ 86 % of a volatility shock after *n* bars.

## Interpretation Details

* **Rising ATR** → volatility expansion; supports momentum and breakout trades  
* **Falling ATR** → contraction; expect consolidation or mature trends  
* **Volatility stop:** trail price by *k × ATR*; expand in volatile phases, tighten in calm periods  
* **Filter:** ignore signals when ATR is below its own long‑term average to avoid dull markets

## Limitations and Considerations

* **Lag:** smoothing delays reaction to abrupt moves  
* **No directional bias:** requires trend or momentum confirmation  
* **Extreme bars:** isolated spikes inflate ATR for several periods  
* **Cross‑asset comparison:** raw ATR is absolute; normalize (NATR) or express as % of price

Complementary tools: ADX (trend strength), moving averages (direction), volume indicators (confirm volatility spikes).

## References

1. Wilder, J. W. Jr. *New Concepts in Technical Trading Systems*. Trend Research, 1978.  
2. Kaufman, P. J. *Trading Systems and Methods*. Wiley, 2019.
