# VEL: Jurik Velocity

[Pine Script Implementation of VEL](https://github.com/mihakralj/pinescript/blob/main/indicators/momentum/vel.pine)

## Overview and Purpose

Jurik Velocity (VEL) indicator is an advanced momentum oscillator that solves the classic trade-off between smoothness and lag. While traditional momentum indicators either show noisy signals or introduce significant lag when smoothed, VEL achieves exceptional smoothness without sacrificing timing, making it particularly valuable for identifying market reversals and trend changes.

This implementation uses Jurik's JMA (Jurik Moving Average) algorithm to smooth the momentum signal while preserving its responsiveness to price changes. The result is a clean, noise-free momentum indicator that maintains excellent timing characteristics.

## Core Concepts

* **Zero-lag Smoothing:** Uses JMA to remove noise without introducing the lag typical of moving averages
* **Adaptive Behavior:** Automatically adjusts to market volatility
* **Clean Signals:** Eliminates the zig-zagging noise inherent in classic momentum
* **Precise Timing:** Maintains responsiveness despite smoothing
* **Versatile Application:** Effective across different timeframes and markets

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 10 | Lookback period for momentum calculation | Lower for faster signals, higher for longer-term trends |
| Source | Close | Price data used for calculation | Consider using hlc3 for more comprehensive price action |

**Pro Tip:** While the default settings work well for most situations, consider:
- Length 5-8 for intraday trading
- Length 10-15 for daily charts
- Length 20-30 for longer-term analysis
- Increasing Power during high volatility periods
- Adjusting Phase to fine-tune signal timing

## Calculation and Mathematical Foundation

VEL combines two key components:

1. **Raw Momentum Calculation:**
   ```
   raw_momentum = price(t) - price(t-n)
   ```
   Where:
   - price(t) is the current price
   - price(t-n) is the price n periods ago

2. **JMA Smoothing:**
   - Applies adaptive smoothing based on local volatility
   - Uses phase-shifting to minimize lag
   - Maintains sharp response to significant price moves
   - Dampens noise without degrading signal quality

> 🔍 **Technical Note:** The JMA algorithm provides superior smoothing by dynamically adjusting to market conditions. It uses volatility measurements and phase-shifting techniques to achieve smoothness without the lag typically associated with moving averages.

## Interpretation Details

VEL provides clear signals through several key patterns:

* **Zero-line Crossovers:**
  - Crossing above zero indicates positive momentum
  - Crossing below zero indicates negative momentum
  - More reliable due to reduced noise

* **Signal Strength:**
  - Greater distance from zero indicates stronger momentum
  - Convergence toward zero suggests momentum weakening
  - Smooth curves make strength assessment more reliable

* **Divergence Analysis:**
  - Price making new highs while VEL makes lower highs (bearish)
  - Price making new lows while VEL makes higher lows (bullish)
  - Cleaner signals make divergences easier to identify

* **Trend Confirmation:**
  - Consistent readings above/below zero confirm trend
  - Magnitude of readings indicates trend strength
  - Smooth curves reduce false trend change signals

## Limitations and Considerations

* **Adaptive Nature:** May require parameter adjustment across different markets
* **Calculation Complexity:** More computationally intensive than simple momentum
* **Parameter Sensitivity:** Phase and Power settings can significantly affect behavior
* **Market Conditions:** Most effective in trending markets
* **Timeframe Dependency:** Optimal settings vary by timeframe
* **Volume Consideration:** Does not incorporate volume information

## References

* Jurik, M. (2022). "JMA - Jurik Moving Average". Jurik Research.
* Ehlers, J. (2002). "Advanced Digital Filters for Trading". Technical Analysis of Stocks & Commodities.
* Kaufman, P. J. (2013). "Trading Systems and Methods" (5th ed.). Wiley Trading.
* Murphy, J. J. (1999). "Technical Analysis of the Financial Markets". New York Institute of Finance.
