
## Channels (2 indicators)

| Code | Name | Key Characteristics |
|------|------|---------------------|
| MIDPOINT | Midpoint over period | Average of highest and lowest values over period: (MAX(high,n) + MIN(low,n))/2 |
| MIDPRICE | Midpoint Price | Average of high and low for single period: (high + low)/2 |

---

## Cycles (6 indicators)

| Code | Name | Key Characteristics |
|------|------|---------------------|
| EACP | Ehlers Autocorrelation Periodogram | Ehlers indicator using autocorrelation to estimate the dominant cycle period |
| HOMOD | Homodyne Discriminator | Ehlers indicator designed to measure the instantaneous frequency of market cycles |
| HT_DCPERIOD | Hilbert Transform - Dominant Cycle Period | Uses Hilbert Transform to measure the dominant cycle period in price data |
| HT_DCPHASE | Hilbert Transform - Dominant Cycle Phase | Uses Hilbert Transform to measure the phase of the dominant cycle |
| HT_PHASOR | Hilbert Transform - Phasor Components | Provides the complex phasor components (real and imaginary) from the Hilbert Transform |
| HT_SINE | Hilbert Transform - SineWave | Generates sine and lead-sine wave plots based on the dominant cycle identified by Hilbert Transform |

---

## Momentum (8 indicators)

| Code | Name | Key Characteristics |
|------|------|---------------------|
| AROONOSC | Aroon Oscillator | Subtracts Aroon Down from Aroon Up, measures trend strength |
| CHOP | Choppiness Index | Measures market sidewaysness or trendiness, higher values indicate choppiness |
| DPO | Detrended Price Oscillator | Removes longer-term trends from price to identify shorter-term cycles |
| HT_TRENDMODE | Hilbert Transform - Trend vs Cycle Mode | Uses Hilbert Transform to determine if the market is in a trending or cycling phase |
| MACDEXT | MACD with controllable MA type | Flexible MACD allowing different moving average types for calculation |
| QSTICK | Q Stick | Measures buying/selling pressure by comparing the open and close prices over time |
| VORTEX | Vortex Indicator | Identifies start of new trends and confirms current trends using +VI and -VI lines |

---

## Numerics (3 indicators)

| Code | Name | Key Characteristics |
|------|------|---------------------|
| AVGPRICE | Average Price | Simple OHLC average: (open + high + low + close)/4 |
| CEIL | Ceiling | Round up to nearest integer |
| FLOOR | Floor | Round down to nearest integer |

---

## Oscillators (1 indicator)

| Code | Name | Key Characteristics |
|------|------|---------------------|
| FISHER | Fisher Transform | Transforms prices to Gaussian normal distribution for clearer turning points |

---

## Statistics (3 indicators)

| Code | Name | Key Characteristics |
|------|------|---------------------|
| LINEARREG_ANGLE | Linear Regression Angle | Angle of linear regression line in degrees |
| LINEARREG_INTERCEPT | Linear Regression Intercept | Y-intercept value of linear regression line |
| LINEARREG_SLOPE | Linear Regression Slope | Slope coefficient of linear regression line |

---

## Volatility (1 indicator)

| Code | Name | Key Characteristics |
|------|------|---------------------|
| TRANGE | True Range | Single-period true range: max(H-L, abs(H-C_prev), abs(L-C_prev)) |

---

## Reversals (10 indicators)

| Code | Name | Key Characteristics |
|------|------|---------------------|
| ATRS | ATR Trailing Stop | Trailing stop loss level calculated using Average True Range |
| CE | Chandelier Exit | Trailing stop loss based on ATR, placed below highs (long) or above lows (short) |
| CKSP | Chande Kroll Stop | Stop-loss system using ATR to define stop levels for long and short positions |
| PIV | Pivot Points | Calculates potential support/resistance levels based on previous period's high, low, close |
| PP | Price Pivots | Similar to Pivot Points, identifies key price levels for potential reversals |
| PSAR | Parabolic SAR | Time/price based trailing stop system that follows trends and reverses on stop hits |
| RPP | Rolling Pivot Points | Pivot points calculated using a moving window, adapting to recent price action |
| SAREXT | Parabolic SAR - Extended | Extended version of Parabolic SAR with additional parameters for customization |
| SUPER | SuperTrend | Trend-following indicator based on ATR, plotting stop levels above/below price |
| VS | Volatility Stop | Trailing stop loss based on volatility, often using ATR or standard deviation |
