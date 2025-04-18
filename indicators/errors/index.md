# Error Metrics

| Code      | Name                                     | Status | Description                                                        |
|-----------|------------------------------------------|--------|------------------------------------------------------------------|
| HUBER     | Huber Loss                               | ✅     | Robust error measurement less sensitive to outliers                |
| MAE       | Mean Absolute Error                      | ✅     | Average of absolute differences between predictions and actuals    |
| MAPD      | Mean Absolute Percentage Deviation       | ✅     | Average of absolute percentage deviations from reference value    |
| MAPE      | Mean Absolute Percentage Error           | ✅     | Average of absolute percentage differences between forecast/actual |
| MASE      | Mean Absolute Scaled Error               | ✅     | MAE scaled by the MAE of a naive forecast                         |
| MDA       | Mean Directional Accuracy                | ✅     | Percentage of times forecast direction matches actual direction    |
| ME        | Mean Error                               | ✅     | Average of differences between predictions and actual values       |
| MPE       | Mean Percentage Error                    | ✅     | Average of percentage differences between forecasts and actuals   |
| MSE       | Mean Squared Error                       | ✅     | Average of squared differences between predictions and actuals     |
| MSLE      | Mean Squared Logarithmic Error           | ✅     | Average of squared logarithmic errors for relative measurement    |
| RAE       | Relative Absolute Error                  | ✅     | Ratio of MAE to the MAE of a naive model                         |
| RMSE      | Root Mean Squared Error                  | ✅     | Square root of the average of squared errors                      |
| RMSLE     | Root Mean Squared Logarithmic Error      | ✅     | Square root of the mean squared logarithmic error                |
| RSE       | Relative Squared Error                   | ✅     | Ratio of squared errors to squared errors of a naive model        |
| RSQUARED  | R-Squared (Coefficient of Determination) | ✅     | Proportion of variance in dependent variable explained by model   |
| SMAPE     | Symmetric Mean Absolute Percentage Error | ✅     | Symmetric alternative to MAPE for zero/near-zero values          |
