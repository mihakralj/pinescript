# Exponential Moving Average (EMA)

The Exponential Moving Average (EMA) is a widely used technical indicator that applies more weight to recent prices. Unlike the Simple Moving Average (SMA), which assigns equal weights to all prices within the lookback period, the EMA gives greater importance to more recent data points, making it more responsive to new information.

[Pine Script Implementation of EMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends/ema.pine)

## Mathematical Foundation

### Basic Formula

The EMA calculation utilizes a smoothing factor (α), which determines how much weight is given to the most recent price. The standard formula is:

EMA₍ₙ₎ = (Price₍ₙ₎ × α) + (EMA₍ₙ₋₁₎ × (1 - α))

Where:
- EMA₍ₙ₎ is the current EMA value
- Price₍ₙ₎ is the current price
- EMA₍ₙ₋₁₎ is the previous EMA value
- α is the smoothing factor

### Optimized Formula

The formula can be rearranged to use fewer arithmetic operations:

EMA₍ₙ₎ = α × (Price₍ₙ₎ - EMA₍ₙ₋₁₎) + EMA₍ₙ₋₁₎

This form requires only three operations instead of four and is mathematically equivalent.

### Smoothing Factor

The smoothing factor α is typically calculated as:

α = 2 / (period + 1)

Where 'period' is the chosen lookback period for the EMA.

## IIR Filter Nature

The EMA is an Infinite Impulse Response (IIR) filter, meaning its current value theoretically depends on all past inputs extending to infinity. A converged EMA requires approximately:

- EMA(5): 13 initialization points to reach 95% accuracy of true IIR
- EMA(20): 55 points to reach 95% accuracy of true IIR
- EMA(50): 138 points to reach 95% accuracy of true IIR

Initialization compensation methods addresses this warm-up issues with IIR nature of EMA.

## Initialization Methods

When calculating an EMA, its infinite nature represents fundamental challenge to warm-up: the formula always requires significant lead of previous EMA values - but what to do when we don't have enough past values? Several approaches exist, each with its trade-offs:

### 1. Zero Initialization (EMA₍₀₎ = 0)

Assumes all previous values before first value were zero. This leads to significant underestimation of early EMA values and requires a long warm-up period to converge to true IIR values.

### 2. First-Value Initialization (EMA₍₀₎ = Price₍₀₎)

Assumes all previous values before first value were equal to the first price. This creates an overestimation bias, especially when the first value isn't a true representative of the prior trend. Will need equally long warm-up period to converge to true IIR line.

### 3. SMA Initialization

Uses a simple moving average for the first 'period' set of values, then abrptly switches to EMA calculation. SMA calculation helps shortening the convergence warm-up period to true IIR line and is very common and even described in many TA reference material. This approach creates un-smoothness and discontinuity when transitioning from Finite Impulse Response SMA to Infinite Impulse Response EMA. For strategies that depend on smotthness of slope, this discontinuity FIR-IIR will generate false signals and is a terrible trade-off for faster IIR convergence.

### 4. Compensated Initialization (this Implementation)

This implementation (which is implemented in this pine script implementation) uses a mathematical compensation technique to correct the initialization bias inherent in an EMA IIR calculation, therefore returning valid early values as close to true IIR output, providing fastest convergence and no abrupt changes between different calculations (FIR-IIR)

## Compensation Method Explained

### The Mathematical Rationale

The compensator method explicitly accounts for the early bias of over- or underestimation of true IIR by:

1. Tracking how much of current EMA value comes from implicit history where we don't have historical data
2. Removing this inherited influence through a compensation factor
3. Gradually decaying this compensating adjustment as more actual data enters the calculation, until compensation is small enough to ignore.

### The Compensation Formula

The corrected EMA is calculated as:

EMA₍corrected₎ = EMA₍raw₎ / (1 - compensation)

Where:
- EMA₍raw₎ is the standard EMA calculation starting from zero
- Compensation starts at 1.0 and decays by multiplying by (1-α) on each bar

This approach yields EMA values as close to true IIR from the very first bar without discontinuities or long warm-up periods. The compensation factor accounts for the "missing history" that would have influenced a true IIR EMA calculation if we had infinite history data.

## Period vs. Alpha Explained

While period is commonly used to specify smoothness of FIR filters (period measures the size of FIR window), EMA is not a FIR and is using a parameter used by IIR algorithms, comonly referred as the smoothing factor (α).

Since FIR period (FIR windows size) is always an integer, converting FIR period into IIR α creates unwanted gaps between possible α values:

| Period | Alpha (α) | gap  |
|--------|-----------|------|
| 1      | 1.00      | 0.33 |
| 2      | 0.67      | 0.17 |
| 3      | 0.50      | 0.17 |
| 5      | 0.33      | 0.15 |
| 10     | 0.18      |      |

For fine-tuned strategies with IIR filters, use α directly instead of deriving it from discrete period meant for FIR filters only.

## Advantages and Disadvantages of EMA

### Advantages

- **Mathematical Accuracy**: Provides theoretically correct EMA values from the first bar
- **No Warm-up Period**: Delivers usable values immediately without waiting for initialization
- **Smooth Transition**: Avoids discontinuities that occur with other initialization methods that switch from FIR to IIR algorithm
- **No Bias**: Neither overestimates nor underestimates early values, unlike other approaches
- **Consistency**: Maintains the expected behavior of an EMA throughout the entire dataset

### Disadvantages

- **Lag**: While more responsive than SMA, EMA still lags behind price action, especially with larger periods
- **Parameter Sensitivity**: Small changes in α can lead to significant differences in signals and performance
- **False Signals**: In ranging or choppy markets, increased sensitivity can generate more false signals than SMA
- **Overfitting Risk**: The flexibility of α parameter can lead to overfitting during strategy optimization
- **Recursive Dependency**: Each EMA value depends on the previous one, so calculation errors compound
