# Technical Analysis Wishlist

## Moving Average Indicators

| Indicator  | Name                                    | Status | Description                                                  |
|------------|----------------------------------------|--------|---------------------------------------------------------------|
| AFIRMA     | Adaptive FIR Moving Average            | ❌     | Uses finite impulse response filtering                         |
| ALMA       | Arnaud Legoux Moving Average           | ✅     | Uses Gaussian distribution for weights                         |
| DEMA       | Double Exponential Moving Average      | ✅     | Reduced lag double EMA                                         |
| DSMA       | Dynamic Simple Moving Average          | ❌     | Adapts period based on volatility                              |
| DWMA       | Dynamic Weighted Moving Average        | ✅     | Adapts to market volatility                                    |
| EMA        | Exponential Moving Average             | ✅     | Weighted average with exponential decay                        |
| EPMA       | Endpoint Moving Average                | ✅     | Basic average emphasizing recent endpoints                     |
| FRAMA      | Fractal Adaptive Moving Average        | ❌     | Uses fractal dimension for adaptation                          |
| GMA        | Gaussian Moving Average                | ❌     | Based on normal distribution                                   |
| HEMA       | Hull Exponential Moving Average        | ✅     | Hull-based smoothing using EMA instead of WMA                  |
| HMA        | Hull Moving Average                    | ✅     | Reduced lag WMA with trend emphasis                            |
| HTIT       | Hilbert Transform Instantaneous Trend  | ❌     | Based on Hilbert Transform                                     |
| HWMA       | Holt-Winters Moving Average            | ✅     | Uses Hann window function for weighting                        |
| JMA        | Jurik Moving Average                   | ✅     | Complex smoothing with minimal lag                             |
| KAMA       | Kaufman Adaptive Moving Average        | ✅     | Adapts to market noise using efficiency ratio                  |
| LTMA       | Linear Time Moving Average             | ❌     | Uses linear regression over time                               |
| MAAF       | Moving Average Adaptive Filter         | ❌     | Advanced adaptive filtering technique                          |
| MAMA       | MESA Adaptive Moving Average           | ❌     | Complex cycle analysis using MESA                              |
| MGDI       | McGinley Dynamic Indicator             | ❌     | Price momentum based dynamic average                           |
| MMA        | Modified Moving Average                | ❌     | Modified version of EMA with different weighting               |
| PWMA       | Pascal Weighted Moving Average         | ✅     | A moving average that uses Pascal's triangle coefficients      |
| QEMA       | Quadruple Exponential Moving Average   | ✅     | Simplified EMA calculation                                     |
| REMA       | Regularized Exponential Moving Average | ✅     | Optimized EMA using regularization                             |
| RMA        | wildeR Moving Average                  | ✅     | Variation of EMA with different smoothing factor               |
| SINEMA     | Sine-weighted Moving Average           | ✅     | Uses sine function for weight distribution                     |
| SMA        | Simple Moving Average                  | ✅     | Basic arithmetic mean of signal over N periods                 |
| SMMA       | Smoothed Moving Average                | ❌     | Smoothed version of simple moving average                      |
| SSF        | Ehler's Super Smoother Filter          | ❌     | Advanced noise reduction filter                                |
| SUPERTREND | Supertrend                             | ❌     | Trend following indicator based on ATR                         |
| SWMA       | Symmetric Weighted Moving Average      | ❌     | Balanced weight distribution moving average                    |
| T3         | Triple Exponential Moving Average (T3) | ❌     | Tim Tillson's improved triple EMA                              |
| TEMA       | Triple Exponential Moving Average      | ✅     | Further reduced lag triple EMA                                 |
| TRIMA      | Triangular Moving Average              | ✅     | Double-smoothed SMA with triangular weight distribution        |
| VIDYA      | Variable Index Dynamic Average         | ❌     | Volatility-based dynamic average                               |
| VWAP       | Volume Weighted Average Price          | ❌     | Price average weighted by volume                               |
| VWMA       | Volume Weighted Moving Average         | ❌     | Moving average weighted by volume                              |
| WCP        | Weighted Closing Price                 | ❌     | Price calculation with emphasis on closing price               |
| WMA        | Weighted Moving Average                | ✅     | Linear-weighted average giving more weight to recent signals   |
| ZLDEMA     | Zero-Lag Double Exponential MA         | ✅     | Advanced DEMA with lag reduction                               |
| ZLEMA      | Zero-Lag Exponential Moving Average    | ✅     | EMA with minimal lag                                           |
| ZLTEMA     | Zero-Lag Triple Exponential MA         | ✅     | Advanced TEMA with lag reduction                               |


## Numeric/Geometric Transformations

| Code | Name	|  Status | Description |
|-----------|------------------------------------------|--------|------------------------------------------------------------------|
| LINEAR       | Linear Transformation           | ❌ | Linear scaling & shifting |
| LOG          | Logarithmic Transformation      | ❌ | Natural logarithm transform for stabilizing variance |
| EXP          | Exponential Transformation      | ❌ | Exponential transform for modeling growth or decay |
| SQRT         | Square Root Transformation      | ❌ | The square root to the input data, useful for variance stabilization |
| DIFF         | Difference                      | ❌ | The absolute difference (first order) |
| CHANGE       | Percentage Change               | ❌ | Percentage change of relative changes |
| MINMAX_SCALE | Min-Max Scaling (Normalization) | ❌ | Scales data to a specific range (e.g., [0, 1] or [-1, 1]) |
| STANDARDIZE  | Standardization                 | ❌ | Z-score Normalization around zero with unit variance |
| RELU         | Rectified Linear Unit           | ❌ | ReLU activation function (max(0, x)) |
| TANH         | Hyperbolic Tangent              | ❌ | Hyperbolic tangent function, scaling output between -1 and 1 |
| SIGMOID      | Logistic Function               | ❌ | Sigmoid function, scaling output between 0 and 1 |
| SSSIGMOID    | Scaled & Shifted Logistics fn   | ❌ | Scaled and shifted sigmoid function, scaling output between -1 and 1 |
| POLYFIT      | Polynomial Fitting              | ❌ | Fits a polynomial of a specified degree to the input data |
| SLOPE        | Direction/Magnitude             | ❌ | First derivative, rate of change |
| CURVATURE    | Acceleration/Deceleration       | ❌ | Second derivative, curvature or concavity |
| JERK         | Jerk/Smoothness                 | ❌ | Third derivative, jaggedness or smoothness |
| CORRELATION  | Correlation (Pearson's)         | ❌ | Calculates the Pearson correlation coefficient between two data series |
| STDDEV       | Standard Deviation              | ❌ | Calculates the standard deviation of the input data |
| VARIANCE     | Variance                        | ❌ | Calculates the variance of the input data |
| MEDIAN       | Median                          | ❌ | Calculates the median of the input data |
| MODE         | Mode                            | ❌ | Calculates the mode of the input data |
| QUANTILE     | Quantile                        | ❌ | Calculates the specified quantile of the input data |


## Error Metrics

| Code      | Name                                     | Status | Description                                                        |
|-----------|------------------------------------------|--------|------------------------------------------------------------------|
| HUBER     | Huber Loss                                | ✅ | Robust error measurement less sensitive to outliers                |
| MAE       | Mean Absolute Error                       | ✅ | Average of absolute differences between predictions and actuals    |
| MAPD      | Mean Absolute Percentage Deviation        | ✅ | Average of absolute percentage deviations from reference value    |
| MAPE      | Mean Absolute Percentage Error            | ✅ | Average of absolute percentage differences between forecast/actual |
| MASE      | Mean Absolute Scaled Error                | ✅ | MAE scaled by the MAE of a naive forecast                         |
| MDA       | Mean Directional Accuracy                 | ✅ | Percentage of times forecast direction matches actual direction    |
| ME        | Mean Error                                | ❌ | Average of differences between predictions and actual values       |
| MPE       | Mean Percentage Error                     | ❌ | Average of percentage differences between forecasts and actuals   |
| MSE       | Mean Squared Error                        | ✅ | Average of squared differences between predictions and actuals     |
| MSLE      | Mean Squared Logarithmic Error            | ❌ | Average of squared logarithmic errors for relative measurement    |
| RAE       | Relative Absolute Error                   | ❌ | Ratio of MAE to the MAE of a naive model                         |
| RMSE      | Root Mean Squared Error                   | ❌ | Square root of the average of squared errors                      |
| RMSLE     | Root Mean Squared Logarithmic Error       | ❌ | Square root of the mean squared logarithmic error                |
| RSE       | Relative Squared Error                    | ❌ | Ratio of squared errors to squared errors of a naive model        |
| RSQUARED  | R-Squared (Coefficient of Determination)  | ❌ | Proportion of variance in dependent variable explained by model   |
| SMAPE     | Symmetric Mean Absolute Percentage Error  | ❌ | Symmetric alternative to MAPE for zero/near-zero values          |
| RMSE       | Root Mean Squared Error                  | ❌ | Square root of the average of squared errors  |
| RMSLE      | Root Mean Squared Logarithmic Error      | ❌ | Square root of the mean squared logarithmic error |
| RSE        | Relative Squared Error                   | ❌ | Ratio of squared errors to squared errors of a naive model |
| RSQUARED   | R-Squared (Coefficient of Determination) | ❌ | Proportion of variance in dependent variable explained by model |
| SMAPE      | Symmetric Mean Absolute Percentage Error | ❌ | Symmetric alternative to MAPE that handles zero/near-zero values |

## Price Channels and Bands

| Code       | Name                                  | Status | Description                                                      |
|------------|---------------------------------------|--------|------------------------------------------------------------------|
| ABBER      | Aberration                            | ❌     | Trading bands based on standard deviation                        |
| ACCBANDS   | Acceleration Bands                    | ❌     | Bands that expand/contract based on market acceleration          |
| BB         | Bollinger Bands                       | ❌     | Volatility bands placed above and below moving average           |
| BBANDS     | Bollinger Bands                       | ❌     | Volatility bands placed above and below moving average           |
| CKSP       | Chande Kroll Stop                     | ❌     | Stop-loss indicator with upper and lower bands                   |
| DC         | Donchian Channel                      | ❌     | Shows highest high and lowest low over N periods                 |
| FCB        | Fractal Chaos Bands                   | ❌     | Uses fractal dimensions to identify support/resistance           |
| ICH        | Ichimoku Cloud                        | ❌     | Japanese system for support/resistance and trends                |
| KC         | Keltner Channel                       | ❌     | Volatility-based envelope set around EMA                         |
| MAE        | Moving Average Envelope               | ❌     | Percentage bands around moving average                           |
| MAX        | Highest value over period             | ❌     | Returns highest value over specified period                      |
| MAXINDEX   | Index of highest value                | ❌     | Returns index of highest value over specified period             |
| MIN        | Lowest value over period              | ❌     | Returns lowest value over specified period                       |
| MININDEX   | Index of lowest value                 | ❌     | Returns index of lowest value over specified period              |
| MINMAX     | Lowest and highest values             | ❌     | Returns both lowest and highest values over period               |
| MINMAXINDEX| Indexes of lowest and highest values  | ❌     | Returns indexes of both lowest and highest values                |
| PCH        | Price Channel                         | ❌     | Shows high and low points over a period                          |
| PIV        | Pivot Points                          | ❌     | Calculates potential support/resistance levels                   |
| PP         | Price Pivots                          | ❌     | Identifies price pivot points                                    |
| RPP        | Rolling Pivot Points                  | ❌     | Rolling calculation of pivot points                              |
| SDC        | Standard Deviation Channel            | ❌     | Channels based on standard deviation of price                    |
| STARC      | Stoller Average Range Channel         | ❌     | Combines SMA with ATR for trading bands                          |

## Trend Indicators

| Code       | Name                                   | Status | Description                                                      |
|------------|---------------------------------------|--------|------------------------------------------------------------------|
| ADX        | Average Directional Movement Index    | ❌     | Measures trend strength                                          |
| ADXR       | Average Directional Movement Rating   | ❌    | Smoothed version of ADX                                          |
| ALLIGATOR  | Williams Alligator                    | ❌    | Three smoothed moving averages to identify trends                |
| AMAT       | Archer Moving Averages Trends         | ❌    | System using multiple moving averages to identify trends         |
| AROON      | Aroon                                 | ❌    | Measures time between highs and lows                             |
| AROONOSC   | Aroon Oscillator                      | ❌    | Difference between Aroon Up and Aroon Down                       |
| ATRS       | ATR Trailing Stop                     | ❌    | Uses ATR for trailing stop placement                             |
| CHOP       | Choppiness Index                      | ❌    | Measures market choppiness or trendiness                         |
| DX         | Directional Movement Index            | ❌    | Measures trend strength                                          |
| DMI        | Directional Movement Index            | ❌    | Compares upward and downward price movement                      |
| DPO        | Detrended Price Oscillator            | ❌    | Removes trend to identify cycles                                 |
| HT_TRENDMODE | Hilbert Transform - Trend vs Cycle Mode | ❌ | Identifies whether market is in trend or cycle mode             |
| MACD       | Moving Average Convergence Divergence | ❌     | Trend-following momentum indicator                               |
| MACDEXT    | MACD with controllable MA type        | ❌     | Customizable MACD calculation                                    |
| MACDFIX    | Moving Average Convergence/Divergence Fix 12/26 | ❌ | MACD with fixed parameters                                |
| MINUS_DI   | Minus Directional Indicator           | ❌     | Measures negative directional movement                           |
| MINUS_DM   | Minus Directional Movement            | ❌     | Negative directional movement                                    |
| PLUS_DI    | Plus Directional Indicator            | ❌     | Measures positive directional movement                           |
| PLUS_DM    | Plus Directional Movement             | ❌     | Positive directional movement                                    |
| QSTICK     | Q Stick                               | ❌     | Quantifies buying/selling pressure using open-close relationship |
| SUPER      | SuperTrend                            | ❌     | Trend-following indicator based on ATR                           |
| TTM        | TTM Trend                             | ❌     | Identifies trend direction and strength                          |
| VORTEX     | Vortex Indicator                      | ❌     | Identifies start of new trends                                   |

## Stop and Reverse Indicators

| Code       | Name                                   | Status | Description                                                      |
|------------|---------------------------------------|--------|------------------------------------------------------------------|
| ATRS       | ATR Trailing Stop                     | ❌     | Uses ATR for trailing stop placement                             |
| CE         | Chandelier Exit                       | ❌     | Trailing stop based on ATR                                       |
| CKSP       | Chande Kroll Stop                     | ❌     | Stop and reverse system developed by Chande and Kroll            |
| PSAR       | Parabolic SAR                         | ❌     | Trend following indicator for entry/exit points                  |
| SAR        | Parabolic SAR                         | ❌     | Trend following indicator for entry/exit points                  |
| SAREXT     | Parabolic SAR - Extended              | ❌     | Extended version of Parabolic SAR                                |
| SUPER      | SuperTrend                            | ❌     | Trend following indicator based on ATR                           |
| VS         | Volatility Stop                       | ❌     | Volatility-based stop-loss system                                |

## Momentum Indicators

| Code       | Name                                   | Status | Description                                                      |
|------------|---------------------------------------|--------|------------------------------------------------------------------|
| APO        | Absolute Price Oscillator             | ❌     | Absolute difference between two moving averages                  |
| BOP        | Balance of Power                      | ❌     | Measures strength of buyers vs sellers                           |
| CCI        | Commodity Channel Index               | ❌     | Measures current price relative to average price                  |
| CMO        | Chande Momentum Oscillator            | ❌     | Momentum oscillator measuring relative strength/weakness          |
| MACD       | Moving Average Convergence Divergence | ❌     | Trend-following momentum indicator                               |
| MFI        | Money Flow Index                      | ❌     | Volume-weighted RSI, measures buying/selling pressure            |
| MOM        | Momentum                              | ❌     | Measures rate of price change                                    |
| PMO        | Price Momentum Oscillator             | ❌     | Normalized momentum indicator with smoothing                     |
| PPO        | Percentage Price Oscillator           | ❌     | Shows relationship between two moving averages as percentage     |
| PRS        | Price Relative Strength               | ❌     | Compares performance of one security to another                  |
| ROC        | Rate of Change                        | ❌     | Percentage change of price over a period                         |
| ROCP       | Rate of Change Percentage             | ❌     | Rate of change expressed as percentage                           |
| ROCR       | Rate of Change Ratio                  | ❌     | Rate of change expressed as ratio                                |
| ROCR100    | Rate of Change Ratio 100 scale        | ❌     | Rate of change ratio multiplied by 100                           |
| RSI        | Relative Strength Index               | ❌     | Measures speed and change of price movements                     |
| STOCH      | Stochastic Oscillator                 | ❌     | Compares closing price to price range over time                  |
| STOCHF     | Stochastic Fast                       | ❌     | Fast stochastic calculation                                      |
| STOCHRSI   | Stochastic Relative Strength Index    | ❌     | Applies stochastic calculation to RSI values                     |
| TRIX       | Triple Exponential Average            | ❌     | 1-day Rate-of-Change of Triple Smooth EMA                       |
| TSI        | True Strength Index                   | ❌     | Double-smoothed momentum oscillator                              |
| ULTOSC     | Ultimate Oscillator                   | ❌     | Multi-timeframe weighted oscillator                              |
| WILLR      | Williams %R                           | ❌     | Measures overbought/oversold levels                              |

## Oscillators

| Code       | Name                                   | Status | Description                                                      |
|------------|---------------------------------------|--------|------------------------------------------------------------------|
| AC         | Acceleration Oscillator               | ❌     | Measures acceleration of price movement                          |
| AO         | Awesome Oscillator                    | ❌     | Measures market momentum using price midpoints                    |
| APO        | Absolute Price Oscillator             | ❌     | Absolute difference between two moving averages                  |
| AROON      | Aroon                                 | ❌     | Measures time between highs and lows                             |
| AROONOSC   | Aroon Oscillator                      | ❌     | Difference between Aroon Up and Aroon Down                       |
| BBI        | Bulls Bears Index                     | ❌     | Compares bullish and bearish market forces                       |
| BIAS       | Bias                                  | ❌     | Measures deviation of price from moving average                  |
| BOP        | Balance of Power                      | ❌     | Measures strength of buyers vs sellers                           |
| BRAR       | BRAR                                  | ❌     | Compares bullish and bearish forces                              |
| CCI        | Commodity Channel Index               | ❌     | Measures current price relative to average price                  |
| CFO        | Chande Forecast Oscillator            | ❌     | Compares price to linear regression forecast                     |
| CG         | Center of Gravity                     | ❌     | Measures cyclical components of price movement                   |
| CHOP       | Choppiness Index                      | ❌     | Measures market choppiness or trendiness                         |
| CMO        | Chande Momentum Oscillator            | ❌     | Momentum oscillator measuring relative strength/weakness          |
| COG        | Center of Gravity                     | ❌     | Measures cyclical components of price movement                   |
| COPPOCK    | Coppock Curve                         | ❌     | Long-term momentum indicator                                     |
| CRSI       | Connors RSI                           | ❌     | Enhanced RSI that incorporates multiple factors                   |
| CTI        | Correlation Trend Indicator           | ❌     | Uses correlation to identify trends                              |
| DOSC       | Derivative Oscillator                 | ❌     | Derivative of an oscillator                                      |
| EFI        | Elder Force Index                     | ❌     | Measures force behind price movement                             |
| ER         | Efficiency Ratio                      | ❌     | Measures market efficiency                                       |
| ERI        | Elder Ray Index                       | ❌     | Measures bull and bear power                                     |
| FISHER     | Fisher Transform                      | ❌     | Converts price to normal distribution                            |
| FOSC       | Forecast Oscillator                   | ❌     | Compares price to linear regression forecast                     |
| INERTIA    | Inertia                               | ❌     | Measures resistance to price movement                            |
| KDJ        | KDJ Indicator                         | ❌     | Modified stochastic indicator                                    |
| KRI        | Kairi Relative Index                  | ❌     | Measures deviation from moving average                           |
| KST        | KST Oscillator                        | ❌     | Long-term momentum oscillator                                    |
| MACD       | Moving Average Convergence Divergence | ❌     | Trend-following momentum indicator                               |
| MFI        | Money Flow Index                      | ❌     | Volume-weighted RSI, measures buying/selling pressure            |
| MOM        | Momentum                              | ❌     | Measures rate of price change                                    |
| PGO        | Pretty Good Oscillator                | ❌     | Measures price strength                                          |
| PPO        | Percentage Price Oscillator           | ❌     | Shows relationship between two moving averages as percentage     |
| PSL        | Psychological Line                    | ❌     | Measures market sentiment                                        |
| PVO        | Percentage Volume Oscillator          | ❌     | Shows volume trend using percentage                              |
| QQE        | Quantitative Qualitative Estimation   | ❌     | Advanced RSI-based indicator                                     |
| ROC        | Rate of Change                        | ❌     | Measures percentage change in price                              |
| RSI        | Relative Strength Index               | ❌     | Measures speed and change of price movements                     |
| RSX        | Relative Strength Xtra                | ❌     | Enhanced RSI calculation                                         |
| RVI        | Relative Vigor Index                  | ❌     | Compares closing price to opening price                          |
| RVGI       | Relative Vigor Index                  | ❌     | Enhanced measurement of price vigor                              |
| SLOPE      | Slope                                 | ❌     | Measures rate of change of linear regression                     |
| SMI        | Stochastic Momentum Index             | ❌     | Improved stochastic oscillator                                   |
| SQUEEZE    | Squeeze                               | ❌     | Identifies market compression and expansion                      |
| STOCH      | Stochastic Oscillator                 | ❌     | Compares closing price to price range over time                  |
| STOCHF     | Stochastic Fast                       | ❌     | Fast stochastic calculation                                      |
| STOCHRSI   | Stochastic RSI                        | ❌     | Applies stochastic calculation to RSI values                     |
| TD_SEQ     | TD Sequential                         | ❌     | Tom DeMark's sequential indicator                               |
| TRIX       | Triple Exponential Average            | ❌     | Triple-smoothed momentum oscillator                             |
| TSI        | True Strength Index                   | ❌     | Double-smoothed momentum oscillator                              |
| ULTOSC     | Ultimate Oscillator                   | ❌     | Multi-timeframe weighted oscillator                              |
| WILLR      | Williams %R                           | ❌     | Measures overbought/oversold levels                              |

## Cycle Indicators

| Code       | Name                                   | Status | Description                                                      |
|------------|---------------------------------------|--------|------------------------------------------------------------------|
| DSS        | Double Smoothed Stochastic                 | ❌     | Double-smoothed stochastic oscillator                           |
| EBSW       | Even Better Sinewave                       | ❌     | Advanced cycle finding tool                                      |
| HT_DCPERIOD | Hilbert Transform - Dominant Cycle Period | ❌ | Identifies the dominant cycle period                        |
| HT_DCPHASE | Hilbert Transform - Dominant Cycle Phase   | ❌  | Identifies the phase of the dominant cycle                    |
| HT_PHASOR  | Hilbert Transform - Phasor Components      | ❌     | Returns phasor components of the Hilbert Transform               |
| HT_SINE    | Hilbert Transform - SineWave               | ❌     | Returns sine wave components of the Hilbert Transform            |
| HT_TRENDLINE | Hilbert Transform - Instantaneous Trendline | ❌ | Identifies the instantaneous trendline                   |
| MESA       | MESA Sine Wave                             | ❌     | Cycle-finding tool derived from MESA                            |
| SINE       | Sine Wave                                  | ❌     | Uses sine curve to predict cyclical movements                    |

## Volume Indicators

| Code       | Name                                   | Status | Description                                                      |
|------------|---------------------------------------|--------|------------------------------------------------------------------|
| AD         | Accumulation/Distribution Line         | ❌     | Volume indicator measuring supply and demand                      |
| ACCDIST    | Accumulation/Distribution              | ❌     | TradingView implementation of accumulation/distribution          |
| ADL        | Chaikin Accumulation Distribution Line | ❌     | Volume indicator measuring supply and demand                      |
| ADOSC      | Chaikin A/D Oscillator                 | ❌     | Measures momentum of AD line                                     |
| AOBV       | Archer On-Balance Volume               | ❌     | Modified OBV calculation                                         |
| CMF        | Chaikin Money Flow                     | ❌     | Volume-weighted measure of money flow                            |
| EFI        | Elder's Force Index                    | ❌     | Measures force behind price movement                             |
| EOM        | Ease of Movement                       | ❌     | Relates price change to volume                                   |
| KVO        | Klinger Volume Oscillator              | ❌     | Volume oscillator based on trend and volume                      |
| MFI        | Money Flow Index                       | ❌     | Volume-weighted RSI, measures buying/selling pressure            |
| NVI        | Negative Volume Index                  | ❌     | Focuses on days with volume decrease                             |
| OBV        | On-Balance Volume                      | ❌     | Relates price changes to volume                                  |
| PVI        | Positive Volume Index                  | ❌     | Focuses on days with volume increase                             |
| PVOL       | Price-Volume                           | ❌     | Combines price and volume data                                   |
| PVO        | Percentage Volume Oscillator           | ❌     | Measures volume trend using moving averages                      |
| PVR        | Price Volume Rank                      | ❌     | Ranks price and volume movements                                 |
| PVT        | Price Volume Trend                     | ❌     | Relates price change to volume                                   |
| TVI        | Trade Volume Index                     | ❌     | Tracks intraday accumulation/distribution of volume              |
| VF         | Volume Force                           | ❌     | Measures strength of volume                                      |
| VP         | Volume Profile                         | ❌     | Shows trading volume at specific price levels                    |
| VWAD       | Volume Weighted Accumulation/Distribution | ❌  | Combines volume weighting with accumulation/distribution     |
| VWAP       | Volume Weighted Average Price         | ❌     | Average price weighted by volume                                 |
| VWMA       | Volume Weighted Moving Average        | ❌     | Moving average weighted by volume                                |
| WAD        | Williams Accumulation/Distribution    | ❌     | Williams' implementation of accumulation/distribution            |

## Volatility Indicators

| Code       | Name                                   | Status | Description                                                      |
|------------|---------------------------------------|--------|------------------------------------------------------------------|
| ABBER      | Aberration                            | ❌     | Trading bands based on standard deviation                        |
| ACCBANDS   | Acceleration Bands                    | ❌     | Bands that expand/contract based on market acceleration          |
| ADR        | Average Daily Range                   | ❌     | Measures average price range over a period                       |
| AP         | Andrew's Pitchfork                    | ❌     | Trend channel tool using three points                            |
| ATR        | Average True Range                    | ❌     | Measures market volatility                                       |
| ATRP       | Average True Range Percent            | ❌     | ATR as percentage of price                                       |
| BBWP       | Bollinger Band Width Percentile       | ❌     | Measures current BB width relative to history                    |
| BBW        | Bollinger Band Width                  | ❌     | Measures difference between upper and lower Bollinger Bands      |
| CCV        | Close-to-Close Volatility             | ❌     | Volatility based on closing prices                               |
| CV         | Conditional Volatility                | ❌     | ARCH/GARCH model for volatility forecasting                      |
| CVI        | Chaikin's Volatility                  | ❌     | Measures rate of change of trading range                         |
| EWMA       | Exponential Weighted Moving Average Volatility | ❌ | Weighted estimation of variance                         |
| GKV        | Garman-Klass Volatility               | ❌     | Estimates volatility using OHLC prices                          |
| HLV        | High-Low Volatility                   | ❌     | Volatility based on high-low range                              |
| HV         | Historical Volatility                 | ❌     | Standard deviation of price changes                              |
| JVOLTY     | Jurik Volatility                      | ❌     | Jurik's implementation of volatility                             |
| MASSI      | Mass Index                            | ❌     | Identifies reversals based on range narrowing                    |
| NATR       | Normalized Average True Range         | ❌     | ATR normalized by price                                          |
| PDIST      | Price Distance                        | ❌     | Measures price deviation from reference point                    |
| PV         | Parkinson Volatility                  | ❌     | Volatility estimate using high-low range                         |
| RSV        | Rogers-Satchell Volatility            | ❌     | Volatility estimate for non-zero mean returns                    |
| RV         | Realized Volatility                   | ❌     | Measures observed volatility over a period                       |
| RVI        | Relative Volatility Index             | ❌     | RSI applied to volatility                                        |
| STDDEV     | Standard Deviation                    | ❌     | Measures dispersion of price from its average                    |
| SV         | Stochastic Volatility                 | ❌     | Models volatility as stochastic process                          |
| TRANGE     | True Range                            | ❌     | Base calculation for ATR, measures price range                   |
| TR         | True Range                            | ❌     | Base calculation for ATR, measures price range                   |
| UI         | Ulcer Index                           | ❌     | Measures downside risk                                           |
| VAR        | Variance                              | ❌     | Measures dispersion around mean                                  |
| VC         | Volatility Cone                       | ❌     | Shows volatility distribution across timeframes                  |
| VOV        | Volatility of Volatility              | ❌     | Measures volatility of volatility measures                       |
| VR         | Volatility Ratio                      | ❌     | Compares different volatility measures                           |
| YZV        | Yang-Zhang Volatility                 | ❌     | Volatility estimator addressing overnight jumps                  |
