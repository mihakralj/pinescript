# Quadruple Exponential Moving Average (QEMA)

The Quadruple Exponential Moving Average implements an advanced four-stage cascade architecture delivering superior lag reduction and robust noise suppression through progressive smoothing optimization. QEMA's sophisticated four-stage filtering process provides exceptional trend identification accuracy with minimal phase delay, while achieving faster trend detection during rapid market transitions through optimized coefficient distribution.

[Pine Script Implementation of QEMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_IIR/qema.pine)

## Mathematical Foundation

QEMA = 4 × EMA₁ - 6 × EMA₂ + 4 × EMA₃ - EMA₄

Where:

- EMA₁ is the first exponential moving average of the source signal
- EMA₂ is the second exponential moving average
- EMA₃ is the third exponential moving average
- EMA₄ is the fourth exponential moving average

### Detailed Breakdown

1. Calculate first EMA:
   EMA₁ = EMA(source, α₁)

2. Calculate second EMA:
   EMA₂ = EMA(EMA₁, α₂)

3. Calculate third EMA:
   EMA₃ = EMA(EMA₂, α₃)

4. Calculate fourth EMA:
   EMA₄ = EMA(EMA₃, α₄)

5. Apply QEMA formula:
   QEMA = 4 × EMA₁ - 6 × EMA₂ + 4 × EMA₃ - EMA₄

The coefficients (4, -6, 4, -1) are selected to effectively eliminate the inherent lag while maintaining a smooth output.

### Smoothing Factor

QEMA uses a progressive smoothing factor system:

- Base α₁ is calculated as 2 / (period + 1)
- Each subsequent alpha increases by a ratio:
  α₂ = α₁ × r
  α₃ = α₂ × r
  α₄ = α₃ × r
- where r is derived from α₁: r = (1/α₁)^(1/3)
- r represents the maximum possible ratio that still maintains numerical stability

This progressive adjustment ensures balance between responsiveness and smoothness across all four EMA stages while preserving numerical stability throughout the calculation process.

## Initialization and Compensation

This implementation uses advanced initialization strategies to ensure numerical stability:

1. All EMA stages are initialized with the first valid source value rather than using progressive initialization
2. The implementation calculates each EMA independently using its corresponding alpha value
3. The mathematical formula applies precise coefficient weighting (4, -6, 4, -1) for optimal lag compensation
4. The ratio-controlled alpha progression ensures each filter stage maintains proper response characteristics
5. First-bar validity is achieved through synchronized initialization of all filter stages

This comprehensive approach eliminates warm-up artifacts and provides mathematically consistent results from the very first calculation bar.

### Alpha vs Period

As with other IIR moving averages, QEMA can be fine-tuned using α directly instead of period:

- Provides more precise control over smoothing
- Avoids the discrete steps inherent in period-based calculations
- Allows for more sophisticated optimization in trading strategies

## Advantages and Disadvantages

### Advantages

- **Fourth-Order Lag Reduction**: The quadruple EMA architecture provides superior lag reduction compared to all lower-order EMA variants (EMA, DEMA, TEMA)
- **Optimized Coefficient Distribution**: The precise 4, -6, 4, -1 coefficient selection balances maximum lag reduction with minimal signal distortion
- **Adaptive Progressive Smoothing**: The ratio-based alpha progression creates an adaptive filter cascade that responds differently to various frequency components
- **Numerical Stability Control**: The mathematically derived ratio parameter ensures stability while maximizing responsiveness
- **Early Signal Generation**: Provides the earliest possible indication of trend changes among all EMA-derived indicators

### Disadvantages

- **Maximum Overshooting Potential**: The aggressive fourth-order lag reduction creates the most pronounced overshooting during sharp reversals of any EMA variant
- **Highest Computational Complexity**: Requires four separate EMA calculations plus coefficient application, making it the most resource-intensive EMA variant
- **Sensitive Ratio Parameter**: The derived ratio value is critical - even small deviations can cause instability or reduce effectiveness
- **Error Propagation**: Each EMA stage compounds any calculation errors from previous stages, potentially amplifying numerical imprecisions
- **Excessive Responsiveness**: In highly volatile markets, the extreme responsiveness can generate excessive false signals compared to lower-order alternatives
