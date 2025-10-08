# Unimplemented Indicators TODO

This document lists all indicators that are planned but not yet implemented in PineScript, organized by category.

## Summary
- **Total Unimplemented**: 30 indicators
- **Cycles**: 7 indicators
- **Dynamics**: 12 indicators
- **Reversals**: 10 indicators
- **Volatility**: 1 indicator

---

## Cycles (7 indicators)

| Code | Name | Key Characteristics |
|------|------|---------------------|
| EACP | Ehlers Autocorrelation Periodogram | Ehlers indicator using autocorrelation to estimate the dominant cycle period |
| HOMOD | Homodyne Discriminator | Ehlers indicator designed to measure the instantaneous frequency of market cycles |
| HT_DCPERIOD | Hilbert Transform - Dominant Cycle Period | Uses Hilbert Transform to measure the dominant cycle period in price data |
| HT_DCPHASE | Hilbert Transform - Dominant Cycle Phase | Uses Hilbert Transform to measure the phase of the dominant cycle |
| HT_PHASOR | Hilbert Transform - Phasor Components | Provides the complex phasor components (real and imaginary) from the Hilbert Transform |
| HT_SINE | Hilbert Transform - SineWave | Generates sine and lead-sine wave plots based on the dominant cycle identified by Hilbert Transform |

---

## Dynamics (12 indicators)

| Code | Name | Key Characteristics |
|------|------|---------------------|
| ALLIGATOR | Williams Alligator | Uses three smoothed moving averages (Jaw, Teeth, Lips) to identify trends and trading ranges |
| AMAT | Archer MAs Trends | Trend identification system based on multiple moving averages |
| AROONOSC | Aroon Oscillator | Subtracts Aroon Down from Aroon Up, measures trend strength |
| CHOP | Choppiness Index | Measures market sidewaysness or trendiness, higher values indicate choppiness |
| DPO | Detrended Price Oscillator | Removes longer-term trends from price to identify shorter-term cycles |
| HT_TRENDMODE | Hilbert Transform - Trend vs Cycle Mode | Uses Hilbert Transform to determine if the market is in a trending or cycling phase |
| MACD | MA Convergence Divergence | Shows relationship between two EMAs, identifies momentum and trend direction |
| MACDEXT | MACD with controllable MA type | Flexible MACD allowing different moving average types for calculation |
| QSTICK | Q Stick | Measures buying/selling pressure by comparing the open and close prices over time |
| SUPER | SuperTrend | Trend-following indicator based on ATR, plotting stop levels above/below price |
| TTM | TTM Trend | Trend indicator often used with TTM Squeeze, based on moving averages |
| VORTEX | Vortex Indicator | Identifies start of new trends and confirms current trends using +VI and -VI lines |

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

---

## Volatility (1 indicator)

| Code | Name | Key Characteristics |
|------|------|---------------------|
| MASSI | Mass Index | Predicts trend reversals by analyzing the narrowing and widening of price ranges |

---

## Implementation Notes

### Fully Implemented Categories
The following categories have all indicators implemented:
- **Channels** (20 indicators) - ✅ Complete
- **Errors** (15 indicators) - ✅ Complete
- **Filters** (17 indicators) - ✅ Complete
- **Momentum** (17 indicators) - ✅ Complete
- **Numerics** (15 indicators) - ✅ Complete
- **Oscillators** (11 indicators) - ✅ Complete
- **Statistics** (25 indicators) - ✅ Complete
- **Trends (FIR)** (18 indicators) - ✅ Complete
- **Trends (IIR)** (21 indicators) - ✅ Complete
- **Volume** (25 indicators) - ✅ Complete

### Priority Implementation Suggestions

#### High Priority (Common Trading Indicators)
1. **MACD** - One of the most widely used momentum indicators
2. **PSAR** (Parabolic SAR) - Popular trailing stop and trend indicator
3. **SUPER** (SuperTrend) - Modern trend-following indicator gaining popularity
4. **ALLIGATOR** - Well-known Bill Williams indicator

#### Medium Priority (Technical Analysis Tools)
1. **HT_DCPERIOD**, **HT_DCPHASE**, **HT_SINE** - Hilbert Transform suite
2. **VORTEX** - Effective trend confirmation tool
3. **PIV/PP** - Essential pivot point calculations
4. **CHOP** - Useful for identifying ranging markets
5. **AROONOSC** - Complement to existing Aroon indicator

#### Lower Priority (Specialized Indicators)
1. **EACP**, **HOMOD** - Advanced Ehlers cycle indicators
2. **AMAT**, **TTM** - Proprietary indicator systems
3. **CKSP**, **CE**, **VS** - Alternative stop-loss methods
4. **MASSI** - Specialized reversal predictor

---

*Last Updated: 2025-10-08*
