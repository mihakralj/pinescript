# VR: Volatility Ratio

[Pine Script Implementation of VR](https://github.com/mihakralj/pinescript/blob/main/indicators/volatility/vr.pine)

## Overview and Purpose

The Volatility Ratio (VR) is a technical indicator that measures the current period's true range relative to the average true range over a specified period. It provides traders with insight into whether current market volatility is expanding or contracting compared to recent historical norms. Unlike absolute volatility measures, VR offers a normalized view that makes volatility levels comparable across different market conditions and time periods.

## Core Concepts

*   **Relative Measurement** — Compares current volatility to recent average levels
*   **True Range Foundation** — Uses comprehensive range calculation including gaps
*   **Bias-Corrected ATR** — Implements Wilder's smoothing with initialization compensation
*   **Volatility Context** — Provides immediate context for current market conditions

Market Applications:
*   **Breakout Detection** — Identifies potential volatility expansion signals
*   **Market Regime Analysis** — Distinguishes between quiet and active periods
*   **Risk Assessment** — Helps adjust position sizing based on current volatility context

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|----------------|
| ATR Period | 14 | Lookback period for average true range calculation | Shorter for more sensitive readings; longer for stable baseline |
| Source | OHLC | Required price data for true range calculation | Must have complete OHLC data for accurate results |
| Reference Level | 1.0 | Baseline for normal volatility | Fixed reference point for interpretation |

## Calculation and Mathematical Foundation

**Technical Formula:**

True Range (TR) calculation:
$TR = \max(H-L, |H-C_{prev}|, |L-C_{prev}|)$

where:
* $H$ = Current high
* $L$ = Current low  
* $C_{prev}$ = Previous close

Average True Range with bias correction:
$ATR_{raw} = \frac{ATR_{prev} \times (n-1) + TR}{n}$

$e_{comp} = (1-\alpha) \times e_{comp,prev}$ where $\alpha = \frac{1}{n}$

$ATR_{corrected} = \frac{ATR_{raw}}{1-e_{comp}}$ (when $e_{comp} > \epsilon$)

Volatility Ratio:
$VR = \frac{TR}{ATR_{corrected}}$

> 🔍 **Technical Note:** The bias correction mechanism accelerates ATR convergence during initialization, providing more responsive readings in early periods compared to standard Wilder's smoothing.

## Interpretation Details

*   **Magnitude Analysis:**
    - VR > 1.0 → Current volatility exceeds recent average (expansion)
    - VR < 1.0 → Current volatility below recent average (contraction)
    - VR ≈ 1.0 → Current volatility aligned with recent norms

*   **Threshold Interpretation:**
    - VR > 2.0 → Significant volatility spike, potential breakout
    - VR > 3.0 → Extreme volatility, possible panic or major news
    - VR < 0.5 → Very quiet conditions, possible consolidation
    - VR < 0.3 → Extremely low volatility, market may be coiling

*   **Contextual Analysis:**
    - Rising VR trend → Increasing market stress or momentum
    - Falling VR trend → Calming market conditions
    - Volatile VR readings → Unstable volatility regime

## Applications

*   **Breakout Trading:**
    - High VR signals potential trend continuation
    - Filter entries with volatility confirmation
    - Avoid false breakouts in low VR conditions

*   **Risk Management:**
    - Scale position sizes with VR levels
    - Adjust stop-loss distances based on current volatility
    - Monitor regime changes through VR patterns

*   **Market Timing:**
    - Enter trades during appropriate volatility conditions
    - Avoid trading in extremely quiet or chaotic periods
    - Time entries with volatility expansion signals

## Limitations and Considerations

*   **Data Requirements:**
    - Requires complete OHLC data for accurate true range
    - Gap handling crucial for overnight markets
    - Historical data quality affects baseline accuracy

*   **Computational Aspects:**
    - Bias correction adds complexity but improves accuracy
    - Parameter sensitivity in ATR period selection
    - Real-time vs. historical calculation differences

*   **Market Conditions:**
    - Less effective in markets with structural breaks
    - May lag during rapid regime transitions
    - Requires sufficient history for meaningful baseline

Complementary Indicators:
* ATR (absolute volatility reference)
* Bollinger Band Width (price-based volatility)
* Volume indicators (confirmation)

## References

1. Wilder, J.W. "New Concepts in Technical Trading Systems." Trend Research, 1978.
2. Kaufman, P.J. "Trading Systems and Methods." Wiley, 2013.
