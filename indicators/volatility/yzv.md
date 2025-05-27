# YZV: Yang-Zhang Volatility

[Pine Script Implementation of YZV](https://github.com/mihakralj/pinescript/blob/main/indicators/volatility/yzv.pine)

## Overview and Purpose

The Yang-Zhang Volatility (YZV) estimator, developed by Shien-Chiang Yang and Qiang Zhang (2000), provides a sophisticated approach to measuring market volatility that accounts for both overnight price gaps and intraday price movements. Unlike simpler volatility measures, YZV remains unbiased in the presence of price drift and optimally combines overnight and trading-period volatility components. This makes it particularly valuable for markets with distinct trading sessions or significant overnight gaps.

## Core Concepts

*   **Component Separation** — Decomposes volatility into overnight jumps and continuous trading
*   **Drift Independence** — Maintains accuracy even with strong price trends
*   **Optimal Weighting** — Uses theoretically derived weights to minimize estimation variance
*   **Bias-Corrected Smoothing** — Implements RMA with initialization compensation

Market Applications:
*   **Risk Assessment** — Superior accuracy in markets with frequent gaps
*   **Options Pricing** — More reliable volatility inputs for derivative models
*   **Regime Detection** — Identifies shifts between continuous and jump-driven volatility

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|----------------|
| Length | 20 | Smoothing period for variance estimates | Shorter for faster response; longer for stability |
| Source | OHLC | Required price data | Must have full OHLC data; cannot use reduced data |
| Scaling | Daily | Output scaling | Annualize (×√252) when comparing to standard volatility measures |

## Calculation and Mathematical Foundation

**Technical Formula:**

Let $P_t$ represent prices at time $t$. Define:
* Overnight return: $r_o = \ln(O_t/C_{t-1})$
* Intraday close return: $r_c = \ln(C_t/O_t)$
* High-low returns: $r_h = \ln(H_t/O_t)$, $r_l = \ln(L_t/O_t)$

Component variances:
1. Overnight: $\sigma^2_o = r_o^2$
2. Close: $\sigma^2_c = r_c^2$
3. Rogers-Satchell: $\sigma^2_{rs} = r_h(r_h-r_c) + r_l(r_l-r_c)$

Yang-Zhang variance:
$\sigma^2_{yz} = \sigma^2_o + k \cdot \sigma^2_c + (1-k) \cdot \sigma^2_{rs}$

where $k = \frac{0.34}{1.34 + \frac{n+1}{n-1}}$ for length $n > 1$

> 🔍 **Technical Note:** The bias-corrected RMA smoothing ensures accurate initialization and faster convergence compared to traditional moving averages, particularly important for the multiple variance components in YZV.

## Interpretation Details

*   **Magnitude Analysis:**
    - Rising YZV → increasing total volatility
    - Falling YZV → decreasing total volatility
    - Compare YZV levels to their own history rather than fixed thresholds

*   **Component Analysis:**
    - High overnight/intraday ratio suggests gap-driven volatility
    - High Rogers-Satchell component indicates active intraday trading
    - Balanced components typical in continuous markets

*   **Comparative Analysis:**
    - YZV vs ATR: YZV typically higher in gapping markets
    - YZV vs Historical Vol: YZV more responsive to regime changes
    - YZV vs Implied Vol: Use for options trading opportunities

## Applications

*   **Risk Management:**
    - Position sizing based on volatility regime
    - Stop-loss adjustment for overnight risk
    - Portfolio allocation optimization

*   **Trading Strategies:**
    - Volatility breakout systems
    - Mean reversion timing
    - Options strategy selection

*   **Market Analysis:**
    - Volatility regime identification
    - Trading session comparison
    - Cross-market correlation studies

## Limitations and Considerations

*   **Data Requirements:**
    - Needs complete OHLC data
    - Missing prices can distort estimates
    - Data quality crucial for overnight gaps

*   **Computational Aspects:**
    - More intensive than simpler measures
    - Multiple variance components increase complexity
    - Requires careful handling of initialization period

*   **Market Conditions:**
    - May overweight gaps in 24/7 markets
    - Less effective in very illiquid markets
    - Assumes reasonable price continuity

Complementary Indicators:
* ATR (pure range perspective)
* Historical Volatility (close-only comparison)
* Volume and Liquidity measures

## References

1. Yang, S. and Zhang, Q. "Drift-Independent Volatility Estimation Based on High, Low, Open, and Close Prices." *Journal of Business*, 73(3), 2000.
2. Sinclair, E. "Volatility Trading." Wiley, 2013.
3. Aït-Sahalia, Y., Fan, J., and Li, Y. "The Leverage Effect Puzzle: Disentangling Sources of Bias at High Frequency." *Journal of Financial Economics*, 109(1), 2013.
