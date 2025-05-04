# Error Metrics

| Indicator | Name | Key Characteristics |
|-----------|------|---------------------|
| [MAE](/indicators/errors/mae.md) | Mean Absolute Error | Measures average error magnitude with equal weighting, robust to outliers |
| [RMSE](/indicators/errors/rmse.md) | Root Mean Squared Error | Emphasizes larger errors through squaring, maintains original units |
| [HUBER](/indicators/errors/huber.md) | Huber Loss | Combines MSE for small errors and MAE for large errors, balancing sensitivity and robustness |
| [MSE](/indicators/errors/mse.md) | Mean Squared Error | Heavily weights large errors, produces squared units |
| [ME](/indicators/errors/me.md) | Mean Error | Preserves error direction to reveal systematic bias |
| [MAPE](/indicators/errors/mape.md) | Mean Absolute Percentage Error | Expresses errors as percentages, enabling cross-scale comparison |
| [SMAPE](/indicators/errors/smape.md) | Symmetric Mean Absolute Percentage Error | Improves on MAPE with symmetric treatment of errors |
| [MPE](/indicators/errors/mpe.md) | Mean Percentage Error | Reveals directional bias in percentage terms |
| [MAPD](/indicators/errors/mapd.md) | Mean Absolute Percentage Difference | Treats both series equally using average as denominator |
| [MSLE](/indicators/errors/msle.md) | Mean Squared Logarithmic Error | Focuses on proportional rather than absolute errors |
| [RMSLE](/indicators/errors/rmsle.md) | Root Mean Squared Logarithmic Error | Square root of MSLE, maintains better interpretability |
| [MASE](/indicators/errors/mase.md) | Mean Absolute Scaled Error | Scales errors against naive forecast performance |
| [RAE](/indicators/errors/rae.md) | Relative Absolute Error | Normalizes absolute errors against baseline model |
| [RSE](/indicators/errors/rse.md) | Relative Squared Error | Normalizes squared errors against baseline model |
| [RSQUARED](/indicators/errors/rsquared.md) | R-Squared | Measures proportion of variance explained by the model |
| [DIRTY](/indicators/errors/dirty.md) | Dirty Data Injection | Simulates missing data to test indicator robustness |
