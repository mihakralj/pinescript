# Regularized Exponential Moving Average (REMA)

The Regularized Exponential Moving Average (REMA) is a modified exponential moving average that includes a regularization term to reduce noise and improve trend following. By balancing standard EMA calculation with a regularization component, REMA provides smoother output while maintaining responsiveness to significant price movements.

[Pine Script Implementation of REMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends/rema.pine)

## Mathematical Foundation

The REMA calculation combines exponential smoothing with a regularization term:

R(t) = λ(E(t) - G(t)) + G(t)

where:
- E(t) = α(P(t) - R(t-1)) + R(t-1)   [EMA component]
- G(t) = R(t-1) + ΔR(t-1)            [Regularization component]
- ΔR(t-1) = R(t-1) - R(t-2)          [Rate of change]
- λ ∈ [0,1]                          [Regularization parameter]
- α = 2/(n+1)                        [Smoothing factor for period n]

### Lambda Parameter

The lambda (λ) parameter controls the balance between the EMA component and the regularization component:

- λ = 1: REMA behaves close to a standard EMA
- λ = 0: REMA uses only the regularization component
- 0 < λ < 1: REMA balances between EMA and regularization

Typical values for λ range from 0.3 to 0.7, with 0.5 being a common default that provides a balanced trade-off between smoothness and responsiveness.

### Regularization Component

The regularization term predicts the next value based on recent movement:

G(t) = R(t-1) + (R(t-1) - R(t-2))

This component:
1. Reduces noise by incorporating momentum
2. Helps maintain the trend direction
3. Adapts to the recent movement pattern

## Initialization

REMA uses a simple but effective initialization approach:

1. First bar: Both REMA and previous REMA are set to the source value
2. Subsequent bars: Previous REMA is updated before calculating new value
3. No warm-up period required: Valid from first bar

## Advantages and Disadvantages

### Advantages

- **Effective Noise Reduction**: The regularization term helps filter out market noise
- **Momentum Integration**: Considers recent price momentum in calculations
- **Quick Stabilization**: Valid from first bar with no warm-up period
- **Customizable Smoothing**: Lambda parameter allows fine-tuning the balance
- **Simple Implementation**: More straightforward than other adaptive MAs

### Disadvantages

- **Parameter Sensitivity**: Requires proper tuning of lambda parameter
- **Potential Oversmoothing**: Can oversmooth at low lambda values
- **Momentum Bias**: May continue trend too long in reversals
- **Less Traditional**: Not as widely used as classic moving averages
