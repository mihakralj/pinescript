# Error Metrics

| Code      | Name                                     | Status | Description                                                        |
|-----------|------------------------------------------|--------|------------------------------------------------------------------|
| [DIRTY](/indicators/errors/dirty.md)     | Dirty Data Injection                     | ✅     | Injects NA values at regular intervals for testing                |
| [HUBER](/indicators/errors/huber.md)     | Huber Loss                               | ✅     | Robust error measurement less sensitive to outliers                |
| [MAE](/indicators/errors/mae.md)       | Mean Absolute Error                      | ✅     | Average of absolute differences between predictions and actuals    |
| [MAPD](/indicators/errors/mapd.md)      | Mean Absolute Percentage Deviation       | ✅     | Average of absolute percentage deviations from reference value    |
| [MAPE](/indicators/errors/mape.md)      | Mean Absolute Percentage Error           | ✅     | Average of absolute percentage differences between forecast/actual |
| [MASE](/indicators/errors/mase.md)      | Mean Absolute Scaled Error               | ✅     | MAE scaled by the MAE of a naive forecast                         |
| [MDA](/indicators/errors/mda.md)       | Mean Directional Accuracy                | ✅     | Percentage of times forecast direction matches actual direction    |
| [ME](/indicators/errors/me.md)        | Mean Error                               | ✅     | Average of differences between predictions and actual values       |
| [MPE](/indicators/errors/mpe.md)       | Mean Percentage Error                    | ✅     | Average of percentage differences between forecasts and actuals   |
| [MSE](/indicators/errors/mse.md)       | Mean Squared Error                       | ✅     | Average of squared differences between predictions and actuals     |
| [MSLE](/indicators/errors/msle.md)      | Mean Squared Logarithmic Error           | ✅     | Average of squared logarithmic errors for relative measurement    |
| [RAE](/indicators/errors/rae.md)       | Relative Absolute Error                  | ✅     | Ratio of MAE to the MAE of a naive model                         |
| [RMSE](/indicators/errors/rmse.md)      | Root Mean Squared Error                  | ✅     | Square root of the average of squared errors                      |
| [RMSLE](/indicators/errors/rmsle.md)     | Root Mean Squared Logarithmic Error      | ✅     | Square root of the mean squared logarithmic error                |
| [RSE](/indicators/errors/rse.md)       | Relative Squared Error                   | ✅     | Ratio of squared errors to squared errors of a naive model        |
| [RSQUARED](/indicators/errors/rsquared.md)  | R-Squared (Coefficient of Determination) | ✅     | Proportion of variance in dependent variable explained by model   |
| [SMAPE](/indicators/errors/smape.md)     | Symmetric Mean Absolute Percentage Error | ✅     | Symmetric alternative to MAPE for zero/near-zero values          |
