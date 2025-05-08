# GRANGER: Granger Causality Test

[Pine Script Implementation of GRANGER](https://github.com/mihakralj/pinescript/blob/main/indicators/statistics/granger.pine)

## Overview and Purpose

The Granger Causality Test is a statistical hypothesis test used to determine whether one time series is useful in forecasting another. Specifically, it tests if lagged values of an independent time series (X) have statistically significant power in predicting the current value of a dependent time series (Y), after accounting for the predictive power of lagged values of Y itself.

This implementation calculates the F-Statistic for a Granger causality test with a single lag (p=1). A higher F-Statistic suggests that the past values of series X provide significant information for predicting series Y, beyond what past values of Y already provide.

## Core Concepts

*   **Predictive Causality:** Tests if one time series can forecast another, not necessarily true causation in a philosophical sense.
*   **Lagged Variables:** Uses past (lagged) values of time series to predict current values.
*   **F-Statistic:** The output of the test, used to determine statistical significance.
*   **Restricted vs. Unrestricted Models:** Compares a model where Y is predicted only by its own lags (restricted) against a model where Y is predicted by its own lags and lags of X (unrestricted).

## Common Settings and Parameters

| Parameter  | Default | Function                                                                 | When to Adjust                                                                                                |
| :--------- | :------ | :----------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------ |
| Y Series   | Close   | The dependent time series (the one being predicted).                     | Select the series whose future values you want to test for predictability.                                    |
| X Series Symbol | SPY   | The symbol for the independent time series (defaults to SPY). The script uses the 'close' of this symbol. | Change to any other symbol whose past 'close' values might predict Y.                                       |
| Period     | 20      | Lookback period for calculating regressions and the F-statistic.         | Longer periods provide more data for the regressions but might smooth out recent changes in relationships. Minimum is 4. |
| Lag        | 1       | Number of lags used in the regression. (Fixed at 1 in this implementation) | This implementation is fixed at 1 lag. More advanced versions could allow variable lags.                      |

**Pro Tip:** To test if Y Granger-causes X, simply swap the Y Series and X Series inputs. Compare the F-statistics for both directions (X → Y and Y → X) to understand bidirectional relationships.

## Calculation and Mathematical Foundation

**Simplified explanation:**
The test compares two regression models:
1.  **Restricted Model:** Predicts current Y using only past Y values (e.g., `Y_t = c0 + c1*Y_{t-1}`).
2.  **Unrestricted Model:** Predicts current Y using past Y values AND past X values (e.g., `Y_t = d0 + d1*Y_{t-1} + d2*X_{t-1}`).

If the Unrestricted Model explains significantly more variance in Y than the Restricted Model (i.e., adding past X values improves the prediction), then X is said to Granger-cause Y. The F-statistic quantifies this improvement.

**Technical formula (for 1 lag):**

1.  **Restricted Model Regression:**
    `Y_t = α₀ + α₁*Y_{t-1} + u_t`
    Calculate Sum of Squared Residuals (SSR₁).

2.  **Unrestricted Model Regression:**
    `Y_t = β₀ + β₁*Y_{t-1} + β₂*X_{t-1} + e_t`
    Calculate Sum of Squared Residuals (SSR₂).

3.  **F-Statistic Calculation:**
    `F = ((SSR₁ - SSR₂) / q) / (SSR₂ / (N - k))`
    Where:
    *   `N` = Number of observations (Period)
    *   `q` = Number of lag parameters for X in the unrestricted model (here, q=1 for one lag of X).
    *   `k` = Total number of parameters in the unrestricted model (here, k=3: intercept, lag Y, lag X).

> 🔍 **Technical Note:** The Pine Script implementation calculates Ordinary Least Squares (OLS) coefficients for the regressions using formulas derived from variances and covariances of the involved series. Sums of squared residuals are then computed based on these coefficients. The helper functions for mean, variance, and covariance use efficient circular buffers. The F-statistic is calculated for a single lag (p=1).

## Interpretation Details

*   **F-Statistic Value:** A larger F-statistic indicates stronger evidence that X Granger-causes Y.
*   **Critical Values:** To formally test the hypothesis, the calculated F-statistic is compared against a critical F-value from an F-distribution table (with `q` and `N-k` degrees of freedom) for a chosen significance level (e.g., 5%).
    *   If `Calculated F > Critical F`: Reject the null hypothesis (H₀: X does not Granger-cause Y). Conclude that X Granger-causes Y.
    *   If `Calculated F ≤ Critical F`: Fail to reject the null hypothesis.
*   **Practical Use:** While Pine Script doesn't provide p-values or easy access to F-distribution critical values, traders can observe the relative magnitude of the F-statistic over time or compare it to manually looked-up approximate critical values (some are commented in the script).
*   **Coefficient of X_lag1 (`x_coeff_yx`):** The script also returns the coefficient of the lagged X variable in the unrestricted model. Its sign and magnitude can provide insights into the direction and strength of the lagged influence if causality is deemed significant.

## Limitations and Considerations

*   **Single Lag:** This implementation is limited to a single lag (p=1). Real-world relationships may involve multiple lags.
*   **Stationarity:** Granger causality tests assume that the time series involved are stationary. Non-stationary series can lead to spurious results. Users should ideally test for stationarity before applying this test.
*   **Omitted Variable Bias:** The test only considers the specified X and Y series. If other relevant variables that influence both X and Y are omitted, the results can be misleading.
*   **Instantaneous Causality:** The test focuses on predictive causality from past values. It doesn't capture contemporaneous relationships.
*   **Non-Linear Relationships:** Granger causality primarily tests for linear predictive power.
*   **No P-Values in Pine Script:** Pine Script does not provide built-in functions for p-value calculation from an F-statistic, making formal hypothesis testing within the script difficult. Interpretation often relies on the magnitude of F or comparison to pre-defined thresholds.
*   **Computational Intensity:** Calculating multiple regressions on each bar can be computationally intensive, especially with longer periods.

## References

*   Granger, C. W. J. (1969). Investigating Causal Relations by Econometric Models and Cross-spectral Methods. *Econometrica*, 37(3), 424-438.
*   Hamilton, J. D. (1994). *Time Series Analysis*. Princeton University Press.
*   Enders, W. (2014). *Applied Econometric Time Series*. Wiley.
