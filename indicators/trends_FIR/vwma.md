# Volume Weighted Moving Average (VWMA)

The Volume Weighted Moving Average incorporates volume into the weighting scheme, providing a measure of the average price over a period, weighted by volume. This can be useful for identifying trends that are supported by significant volume.

[Pine Script Implementation of VWMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_FIR/vwma.pine)

## Mathematical Foundation

The VWMA calculation applies a volume-weighted weight to each data point:

VWMA = (P₁ × V₁ × w₁ + P₂ × V₂ × w₂ + ... + Pₙ × Vₙ × wₙ) / (V₁ × w₁ + V₂ × w₂ + ... + Vₙ × wₙ)

Where:

- P₁, P₂, ..., Pₙ are signal values in the lookback window (P₁ being the oldest)
- V₁, V₂, ..., Vₙ are the volume values in the lookback window (V₁ being the oldest)
- w₁, w₂, ..., wₙ are the weights assigned to each signal (w₁ being the smallest weight)
- n is the number of periods (window size)

### Linear Weighting Scheme

In the standard implementation of VWMA, weights are assigned in a linear progression:

| Price Point | Volume | Weight |
|------------|--------|--------|
| Most recent (Pₙ) | Vₙ | n |
| Second most recent (Pₙ₋₁) | Vₙ₋₁ | n-1 |
| Third most recent (Pₙ₋₂) | Vₙ₋₂ | n-2 |
| ... | ... | ... |
| Oldest (P₁) | V₁ | 1 |

### Denominator Formula

The sum of volume-weighted weights for a period n is calculated as:

Sum of (volume * weights) = (V₁ * 1) + (V₂ * 2) + ... + (Vₙ * n)

## Initialization Properties

Similar to the SMA and WMA, the VWMA has straightforward initialization characteristics:

### Full Window Requirement

VWMA requires a minimum of p data points for a complete calculation. For a period of n, the handling of the first n-1 values can be:

1. **Partial Window Calculation**: Calculate weighted averages with available data points until the window is filled
2. **NA Values**: Return "not available" until enough data points exist

### No Convergence Issue

As a FIR filter, VWMA does not suffer from the convergence issues of IIR filters like EMA. Once the initial window is filled, VWMA immediately produces correctly weighted outputs without bias.

## Advantages and Disadvantages of SMA

## Advantages of VWMA

- **Volume Consideration**: Incorporates volume into the average, providing a more accurate representation of price action.
- **Balanced Responsiveness**: More responsive to recent signal changes than SMA, but less prone to whipsaws than EMA
- **Linear Decay**: Predictable and intuitive degradation of influence for older signals
- **No Initialization Bias**: Produces valid outputs as soon as window is filled
- **Simple Weighting Logic**: Easier to understand than exponential weighting
- **Finite Memory**: Guaranteed to "forget" old signal data after p periods

## Disadvantages of VWMA

- **Still Has Lag**: Though less than SMA, still lags behind signal action
- **Abrupt Ending**: The oldest value suddenly drops out of calculation when leaving the window
- **Step Changes**: Linear weighting creates discrete steps in influence
- **Computational Overhead**: More calculations than SMA (though less than some other averages)
- **Less Smooth**: Shows more "ripples" in response to signal changes than higher-order averages
