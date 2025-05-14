# HLV: High-Low Volatility (Parkinson Number)

[Pine Script Implementation of HLV](https://github.com/mihakralj/pinescript/blob/main/indicators/volatility/hlv.pine)

## Overview and Purpose

High-Low Volatility (HLV), in this implementation, refers to the Parkinson number (or Parkinson volatility), an estimator for historical volatility developed by Michael Parkinson in 1980. It utilizes only the high and low prices of a trading period to estimate volatility. This method is considered more efficient than traditional close-to-close volatility estimators because it captures the price range within the period, which often contains more information about volatility than just the closing price.

The Parkinson number assumes that prices follow a geometric Brownian motion with zero drift and no opening jumps (i.e., the opening price is not considered, and it's assumed continuous trading within the high-low range). It provides a per-period variance estimate, which is then typically smoothed and annualized.

## Core Concepts

*   **High-Low Range:** Solely uses the high and low prices of each period.
*   **Efficiency:** Generally more efficient (lower variance of the estimator) than close-to-close volatility.
*   **Logarithmic Prices:** Calculations are based on the natural logarithm of high and low prices.
*   **Zero Drift Assumption:** Assumes no underlying trend in the price series for the period being estimated.
*   **No Opening Jumps:** The model does not account for overnight gaps or opening jumps, as it only considers the high-low range.
*   **Smoothing:** The raw Parkinson estimator for each period can be noisy, so it's typically smoothed over a lookback period (e.g., using RMA/Wilder's MA).

## Common Settings and Parameters

| Parameter     | Default | Function                                                                 | When to Adjust                                                                                                |
|---------------|---------|--------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| `length`      | 20      | The lookback period for smoothing the raw Parkinson estimates.           | Shorter periods make it more reactive; longer periods provide smoother but more lagging results.                |
| `annualize`   | `true`  | Whether to annualize the volatility output.                              | Set to `false` if you need per-period volatility (e.g., daily volatility if using daily bars).                |
| `annualPeriods`| 252     | Number of trading periods in a year for annualization.                   | Adjust based on data frequency (e.g., 252 for daily, 52 for weekly, 12 for monthly).                          |

## Calculation and Mathematical Foundation

**Simplified explanation:**
1.  For each period, calculate the term: $X_i = \ln(\text{High}_i / \text{Low}_i)$.
2.  Square this term: $X_i^2$.
3.  Smooth these squared terms over the specified `length` (e.g., using RMA): $\text{Smoothed}(X^2)$.
4.  Take the square root of the smoothed value to get the per-period HLV: $\text{HLV}_{\text{period}} = \sqrt{\text{Smoothed}(X^2)}$.
5.  (Optional) Annualize this per-period volatility: $\text{HLV}_{\text{annual}} = \text{HLV}_{\text{period}} \cdot \sqrt{\text{AnnualPeriods}}$.

**Technical formula:**

Let $X_i = [\ln(H_i/L_i)]^2$.
Smoothed $X_S = \text{RMA}(X, \text{length})$
$\text{HLV}_{\text{period}} = \sqrt{X_S}$

If annualizing:
Annualized $\text{HLV}_{\text{period}} = \text{HLV}_{\text{period}} \cdot \sqrt{\text{AnnualPeriods}}$

> 🔍 **Relationship to Parkinson Volatility (PV):** This HLV is numerically equivalent to $\text{PV} \cdot \sqrt{4 \ln 2}$, or approximately $\text{PV} \cdot 1.6651$. The formal Parkinson Volatility includes a scaling factor of $1/(4 \ln 2)$ within the square root, which this HLV implementation omits for a more direct (unscaled) representation of high-low range volatility.

## Interpretation Details

*   **Rising HLV:** Indicates increasing market volatility based on the high-low price range.
*   **Falling HLV:** Suggests decreasing market volatility.
*   **Magnitude:** HLV values will be larger than those of Parkinson Volatility (PV) due to the absence of PV's scaling factor.
*   **Focus on Range:** It emphasizes the intraday (or intra-period) trading range as the primary source of volatility information.

## Limitations and Considerations

*   **No Drift Assumption (Implicit):** While not strictly derived with a zero-drift assumption like the formal Parkinson number, its reliance on only high/low means it performs best in non-trending, range-bound markets for comparative volatility. Strong trends can distort the meaning of high-low ranges as pure volatility indicators.
*   **Ignores Opening/Closing Prices:** By not using open and close prices, it misses information about overnight gaps and the relationship between the open/close and the high/low range. Estimators like Garman-Klass, Parkinson, or Yang-Zhang attempt to incorporate more information or specific theoretical underpinnings.
*   **Data Quality:** Relies on accurate high and low prices.
*   **Smoothing Lag:** The necessary smoothing introduces lag.

## References
*   (For the underlying concept of using high-low for volatility, see references in Parkinson Volatility, Garman-Klass Volatility, etc.)
