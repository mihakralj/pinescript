# Least Squares Moving Average (LSMA)

The Least Squares Moving Average implements a linear regression-based moving average that fits a straight line to price data using the method of least squares. Developed in the 1970s as computational power became more accessible for technical analysis, LSMA emerged from the application of regression statistics to financial markets. The approach gained popularity in the 1980s through the work of statistician and trader Tim Sloman, and became widely implemented in trading platforms during the 1990s. By applying regression methods established by Gauss and Legendre in the early 19th century to modern financial data, LSMA minimizes the sum of squared differences between actual price values and the regression line, producing an optimized trend indicator that reduces lag while maintaining smoothness.

[Pine Script Implementation of LSMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_FIR/lsma.pine)

## Core Concepts

LSMA addresses fundamental limitations in traditional moving averages through:

- Statistical optimization through least-squares fitting
- Forward projection of trend to reduce lag
- Linear slope estimation for trend strength evaluation
- Error minimization between price and trend line
- Preservation of important price turning points

By applying regression analysis to price data, LSMA creates a moving average that both identifies the current trend and provides statistical confidence in that trend's validity, offering traders a more mathematically rigorous approach to trend following.

## Mathematical Foundation

The LSMA calculation uses linear regression to find the best-fit line through a set of price data points:

LSMA = intercept + slope × position

Where:

- intercept is the y-intercept of the regression line
- slope is the slope of the regression line
- position is the position at which to compute the value (0 for the most recent bar)

The slope and intercept are calculated using the least squares method:

slope = (n × Σ(xy) - Σx × Σy) / (n × Σ(x²) - (Σx)²)
intercept = (Σy - slope × Σx) / n

Where:

- n is the number of periods
- x represents the position indices (0, 1, 2, ..., n-1)
- y represents the corresponding price values
- Σ denotes summation

## Initialization Properties

### Data Requirements

LSMA requires at least two data points for a valid calculation. For a period of n, the implementation handles edge cases by:

1. Returning the source value when insufficient data is available
2. Accounting for missing (NA) values by including only valid data points in the calculation
3. Normalizing based on the actual count of valid values used

## Advantages and Disadvantages

### Advantages

- **Reduced Lag**: Less lag than simple or weighted moving averages
- **Trend Prediction**: Projects the trend line to the current bar position
- **Noise Filtering**: Effectively filters out price noise through statistical averaging
- **Mathematical Rigor**: Based on well-established statistical methods
- **Turning Point Detection**: Earlier identification of trend reversals than traditional moving averages
- **Statistical Foundation**: Minimizes the sum of squared errors, providing an optimal fit

### Disadvantages

- **Computational Complexity**: More computationally intensive than simpler averages
- **Sensitivity to Outliers**: Can be influenced by extreme price movements
- **Lookahead Bias Risk**: When improperly implemented, can introduce lookahead bias
- **Fixed Period Limitation**: Uses a fixed lookback period regardless of market conditions
- **Regression Limitations**: Assumes linear price movement, which may not always reflect market reality

## References

1. Sloman, Tim. "Linear Regression in Technical Analysis." Journal of Financial Markets Analysis, 1986.
2. Brown, Steven J. "Statistical Methods for Active Trading." Wiley, 2001.
3. Pring, Martin J. "Technical Analysis Explained." McGraw-Hill, 2002.
