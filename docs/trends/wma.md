# Weighted Moving Average (WMA)

The Weighted Moving Average (WMA) is a technical indicator that assigns different weights to price data within the calculation window, with greater emphasis on more recent data. WMA applies a linear weighting scheme to data in FIR window, decreasing linearly as the data gets older.

[Pine Script Implementation of WMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends/wma.pine)

## Mathematical Foundation

### Basic Formula

The WMA calculation applies a linearly decreasing weight to each price point:

WMA = (P₁ × w₁ + P₂ × w₂ + ... + Pₙ × wₙ) / (w₁ + w₂ + ... + wₙ)

Where:
- P₁, P₂, ..., Pₙ are price values in the lookback window (P₁ being the oldest)
- w₁, w₂, ..., wₙ are the weights assigned to each price (w₁ being the smallest weight)
- n is the number of periods (window size)

### Linear Weighting Scheme

In the standard implementation of WMA, weights are assigned in a linear progression:

| Price Point | Weight |
|------------|--------|
| Most recent (Pₙ) | n |
| Second most recent (Pₙ₋₁) | n-1 |
| Third most recent (Pₙ₋₂) | n-2 |
| ... | ... |
| Oldest (P₁) | 1 |

### Denominator Formula

The sum of weights for a period n is calculated as:

Sum of weights = n(n+1)/2

For example, for a 5-period WMA, the sum of weights is 5(5+1)/2 = 15.

## Filter Characteristics

The WMA is a Finite Impulse Response (FIR) filter like the SMA, but with non-uniform weighting:

- Each input affects the output for exactly p periods
- Values within the window have linearly increasing weights
- No "memory" beyond the specified window size
- Less lag than SMA but more than EMA for similar period settings

## Initialization Properties

Similar to the SMA, the WMA has straightforward initialization characteristics:

### Full Window Requirement

WMA requires a minimum of p data points for a complete calculation. For a period of n, the handling of the first n-1 values can be:

1. **Partial Window Calculation**: Calculate weighted averages with available data points until the window is filled
2. **NA Values**: Return "not available" until enough data points exist

### No Convergence Issue

As a FIR filter, WMA does not suffer from the convergence issues of IIR filters like EMA. Once the initial window is filled, WMA immediately produces correctly weighted outputs without bias.

## Window Size Considerations

The window size (period) directly impacts:

1. **Smoothness**: Larger windows produce smoother outputs with more lag
2. **Responsiveness**: Smaller windows respond faster to price changes
3. **Weight Distribution**: The relative difference between highest and lowest weights becomes less significant with larger periods

Common window sizes include:

| Period | Common Applications |
|--------|---------------------|
| 5-10   | Short-term price movements, quick transitions |
| 14-21  | Medium-term trend identification |
| 50-100 | Long-term trend identification |

## Advantages and Disadvantages of SMA

## Advantages of WMA

- **Balanced Responsiveness**: More responsive to recent price changes than SMA, but less prone to whipsaws than EMA
- **Linear Decay**: Predictable and intuitive degradation of influence for older prices
- **No Initialization Bias**: Produces valid outputs as soon as window is filled
- **Simple Weighting Logic**: Easier to understand than exponential weighting
- **Finite Memory**: Guaranteed to "forget" old price data after p periods

## Disadvantages of WMA

- **Still Has Lag**: Though less than SMA, still lags behind price action
- **Abrupt Ending**: The oldest value suddenly drops out of calculation when leaving the window
- **Step Changes**: Linear weighting creates discrete steps in influence
- **Computational Overhead**: More calculations than SMA (though less than some other averages)
- **Less Smooth**: Shows more "ripples" in response to price changes than higher-order averages