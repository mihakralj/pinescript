# Linear Trend Moving Average (LTMA)

## Introduction

The Linear Trend Moving Average (LTMA) is a type of moving average designed to project the linear trend of price data over a specified period. Unlike traditional moving averages that primarily smooth price, LTMA focuses on identifying and extending the current linear regression trend, potentially offering insights into future price direction based on recent momentum.

*Note: Specific historical background for LTMA might vary or be less documented than more common indicators. This section provides a conceptual introduction.*

[Pine Script Implementation](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_IIR/ltma.pine)

## Core Concepts

LTMA is built upon the principles of linear regression applied to price data:

- **Trend Projection**: Calculates the linear regression line over a lookback period.
- **Endpoint Focus**: Uses the endpoint of the calculated regression line as the moving average value.
- **Reduced Lag**: Aims to reduce lag compared to simple moving averages by focusing on the current trend's trajectory.
- **Predictive Element**: Implicitly projects where the price might head if the current linear trend continues.

## Mathematical Foundation

The LTMA is typically derived from the linear regression formula y = mx + c, calculated over a specific period N.

The value of the LTMA at time t is the value of the regression line at the end of the period (i.e., at x = N or the current bar).

Linear Regression Line: LR(t) = Intercept + Slope * (N - 1)
(Calculation details might vary based on specific implementations)

Where:

- Intercept and Slope are calculated using the least squares method over the past N data points.
- N is the lookback period.

The LTMA value represents the projected value on the regression line for the current bar.

## Calculation Process

1. **Define Period**: Select the lookback period N.
2. **Calculate Linear Regression**: For the most recent N data points (e.g., closing prices), calculate the slope and intercept of the best-fit linear regression line.
3. **Determine LTMA Value**: Calculate the value of the regression line at the current point in time (the end of the N period window). This value is the LTMA for the current bar.
4. **Repeat**: Repeat the calculation for each new bar, using a moving window of N periods.

## Advantages and Limitations

### Advantages

- **Trend Clarity**: Provides a clear visualization of the current linear trend.
- **Reduced Lag**: Often less laggy than SMAs, especially in established trends.
- **Potential Predictive Quality**: Offers a projection based on the current rate of change.
- **Smoother than Price**: Still provides some smoothing compared to raw price action.

### Limitations

- **Whipsaws in Ranging Markets**: Like many trend-following indicators, can produce false signals in sideways markets.
- **Sensitivity to Outliers**: Linear regression can be sensitive to significant outliers within the lookback period.
- **Assumption of Linearity**: Assumes the recent trend is linear, which may not always hold true.
- **Parameter Dependent**: The choice of the lookback period N significantly impacts its behavior.
