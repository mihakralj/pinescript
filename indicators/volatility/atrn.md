# ATRN: Normalized Average True Range

[Pine Script Implementation of ATRN](https://github.com/mihakralj/pinescript/blob/main/indicators/volatility/atrn.pine)

## Overview and Purpose

Normalized Average True Range (ATRN) converts ATR into a percentage of price, allowing direct cross‑instrument and cross‑timeframe volatility comparison. First popularized on futures desks in the late 1990s, ATRN divides ATR by close and expresses the result in percent, preserving Wilder’s volatility logic while removing the scale problem inherent to absolute ATR values. Traders rely on ATRN to rank markets by activity, detect regime shifts, and tune strategy parameters irrespective of symbol price.

## Core Concepts

* **Price‑scaled volatility** — ATR ÷ Close creates unit‑free percentage volatility  
* **Comparability across assets** — enables screening of diverse markets for high or low volatility  
* **Regime detection** — shifts in ATRN identify transitions between quiet and explosive phases  

Market application:  
* **Portfolio allocation** — weight positions inversely to ATRN for volatility parity  
* **Strategy optimization** — adjust breakout thresholds when ATRN rises/falls  
* **Risk alerts** — spike in ATRN signals unusual market stress

Timeframe suitability:  
* **Any timeframe** — normalization offsets absolute‑price bias; intraday for scalping, daily for swing.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 14 | ATR smoothing period | Shorten for fast regimes; lengthen for stability |
| Source | HLC | Data for True Range | Rarely changed |
| Multiplier | 100 | Converts ratio to percentage | Set to 1 for decimal output |

**Pro Tip:** Rank watchlists by 20‑day ATRN to focus on the top 20 % most volatile symbols for breakout strategies.

## Calculation and Mathematical Foundation

**Simplified explanation:**  
Compute ATR as usual, divide by price, multiply by 100 to express as a percent of price.

**Technical formula:**

ATRNₙ = 100 × ATRₙ ⁄ Cᵗ  

ATRₙ = WilderMAₙ(TR)  
TR as defined in standard ATR.

> 🔍 **Technical Note:** Because ATR and price can trend together, ATRN remains mean‑reverting, making it useful for volatility breakout thresholds.

## Interpretation Details

* **High ATRN (> 2 %)** — exceptional volatility; widen stops or reduce size  
* **Low ATRN (< 0.5 %)** — quiet market; favor mean‑reversion or wait for expansion  
* **Rising ATRN** — tightening squeezes are breaking; momentum setups favored  
* **Falling ATRN** — volatility compression; prepare for range‑bound tactics

## Limitations and Considerations

* **Lag from smoothing** — same as ATR  
* **Price jumps** — corporate actions can distort ATRN; adjust for splits/dividends  
* **Percentage still relative** — extreme penny stocks may show inflated ATRN

Complementary tools: Bollinger Bands (volatility envelope), Keltner Channels, ADX.

## References

1. Wilder, J. W. Jr. *New Concepts in Technical Trading Systems*, 1978.  
2. Martin, E. “Volatility as a Percent of Price.” *Futures Magazine*, 2001.
