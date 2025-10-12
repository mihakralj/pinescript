# Trend Dynamics

## Implemented Indicators

| Code | Name | Key Characteristics |
| ------------ | --------------------------------------- | --------------------------------------------------------------------------------------- |
| [ADX](/indicators/dynamics/adx.md) | Average Directional Movement Index | Measures trend strength, regardless of direction (uses +DI and -DI) |
| [ADXR](/indicators/dynamics/adxr.md) | Average Directional Movement Rating | Smoothed version of ADX, often used in conjunction with ADX for signals |
| [ALLIGATOR](/indicators/dynamics/alligator.md) | Williams Alligator | Uses three smoothed moving averages (Jaw, Teeth, Lips) to identify trends and trading ranges |
| [AROON](/indicators/dynamics/aroon.md) | Aroon | Identifies trend direction and strength by measuring time since price recorded new highs/lows |
| [DMX](/indicators/dynamics/dmx.md) | Jurik Directional Movement Index | Smoothed Bipolar Directional Movement Index (DMI) |
| [DX](/indicators/dynamics/dx.md) | Directional Movement Index | Measures directional strength; unsmoothed component of ADX (100 * abs(+DI - -DI) / (+DI + -DI)) |
| [IMI](/indicators/dynamics/imi.md) | Intraday Momentum Index | RSI-like indicator using intraday ranges (open vs close); identifies overbought/oversold conditions |

## Planned Indicators

| Code | Name | Key Characteristics | Notes |
| ------------ | --------------------------------------- | --------------------------------------------------------------------------------------- | ----- |
| AMAT | Archer MAs Trends | Trend identification system based on multiple moving averages | TODO |
| AROONOSC | Aroon Oscillator | Subtracts Aroon Down from Aroon Up, measures trend strength | TODO |
| CHOP | Choppiness Index | Measures market sidewaysness or trendiness, higher values indicate choppiness | TODO |
| DPO | Detrended Price Oscillator | Removes longer-term trends from price to identify shorter-term cycles | TODO |
| HT_TRENDMODE | Hilbert Transform - Trend vs Cycle Mode | Uses Hilbert Transform to determine if the market is in a trending or cycling phase | TODO |
| QSTICK | Q Stick | Measures buying/selling pressure by comparing the open and close prices over time | TODO |
| SUPER | SuperTrend | Trend-following indicator based on ATR, plotting stop levels above/below price | TODO |
| TTM | TTM Trend | Trend indicator often used with TTM Squeeze, based on moving averages | TODO |
| VORTEX | Vortex Indicator | Identifies start of new trends and confirms current trends using +VI and -VI lines | TODO |

**Note:** MACD and MACDEXT are implemented in the [Momentum](/indicators/momentum/_index.md) category.
