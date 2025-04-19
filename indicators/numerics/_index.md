# Numerics & Statistical Transformations

| Code         | Name                            | Status | Description |
|--------------|---------------------------------|--------|------------------------------------------------------------------|
| LINEAR       | Linear Transformation           | ❌     | Linear scaling & shifting |
| LOG          | Logarithmic Transformation      | ❌     | Natural logarithm transform for stabilizing variance |
| EXP          | Exponential Transformation      | ❌     | Exponential transform for modeling growth or decay |
| SQRT         | Square Root Transformation      | ❌     | The square root to the input data, useful for variance stabilization |
| DIFF         | Difference                      | ❌     | The absolute difference (first order) |
| CHANGE       | Percentage Change               | ❌     | Percentage change of relative changes |
| MINMAX_SCALE | Min-Max Scaling (Normalization) | ❌     | Scales data to a specific range (e.g., [0, 1] or [-1, 1]) |
| STANDARDIZE  | Standardization                 | ❌     | Z-score Normalization around zero with unit variance |
| RELU         | Rectified Linear Unit           | ❌     | ReLU activation function (max(0, x)) |
| TANH         | Hyperbolic Tangent              | ❌     | Hyperbolic tangent function, scaling output between -1 and 1 |
| SIGMOID      | Logistic Function               | ❌     | Sigmoid function, scaling output between 0 and 1 |
| SSSIGMOID    | Scaled & Shifted Logistics fn   | ❌     | Scaled and shifted sigmoid function, scaling output between -1 and 1 |
| POLYFIT      | Polynomial Fitting              | ❌     | Fits a polynomial of a specified degree to the input data |
| SLOPE        | Direction/Magnitude             | ❌     | First derivative, rate of change |
| CURVATURE    | Acceleration/Deceleration       | ❌     | Second derivative, curvature or concavity |
| JERK         | Jerk/Smoothness                 | ❌     | Third derivative, jaggedness or smoothness |
| CORRELATION  | Correlation (Pearson's)         | ❌     | Calculates the Pearson correlation coefficient between two data series |
| STDDEV       | Standard Deviation              | ❌     | Calculates the standard deviation of the input data |
| VARIANCE     | Variance                        | ❌     | Calculates the variance of the input data |
| MEDIAN       | Median                          | ❌     | Calculates the median of the input data |
| MODE         | Mode                            | ❌     | Calculates the mode of the input data |
| QUANTILE     | Quantile                        | ❌     | Calculates the specified quantile of the input data |
