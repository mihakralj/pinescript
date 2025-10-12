# Reversals and Pattern Recognition

## Implemented Indicators

| Code | Name | Key Characteristics |
| ------------ | --------------------------------------- | --------------------------------------------------------------------------------------- |
| [PIVOT](/indicators/reversals/pivot.md) | Pivot Points (Classic) | Standard floor trader pivots with 7 levels (PP, R1-R3, S1-S3) |
| [PIVOTCAM](/indicators/reversals/pivotcam.md) | Camarilla Pivot Points | Mean-reversion pivots with 9 levels; R3/S3 are key reversal zones |
| [PIVOTDEM](/indicators/reversals/pivotdem.md) | DeMark Pivot Points | Minimalist trend-following pivots with only 3 levels and conditional logic |
| [PIVOTEXT](/indicators/reversals/pivotext.md) | Extended Traditional Pivots | Extended pivots with 11 levels (R1-R5, S1-S5) for volatile markets |
| [PIVOTFIB](/indicators/reversals/pivotfib.md) | Fibonacci Pivot Points | Fibonacci-ratio based pivots; Golden Ratio (61.8%) at R2/S2 |
| [PIVOTWOOD](/indicators/reversals/pivotwood.md) | Woodie's Pivot Points | Weighted close pivots (2× close weight) for intraday trading |
| [PSAR](/indicators/reversals/psar.md) | Parabolic Stop And Reverse | Trailing stop indicator that accelerates with trend; provides entry/exit signals via SAR dots |

## Planned Indicators

| Code | Name | Key Characteristics | Notes |
| ------------ | --------------------------------------- | --------------------------------------------------------------------------------------- | ----- |
| SWINGS | Swing High/Low Detection | Identifies significant price reversals and swing points | TODO |
| FRACTALS | Williams Fractals | Five-bar pattern for identifying potential reversal points | TODO |

### Candlestick Patterns (TA-Lib has 60+)

| Code | Name | Key Characteristics | Notes |
| ------------ | --------------------------------------- | --------------------------------------------------------------------------------------- | ----- |
| CDL_DOJI | Doji Patterns | Indecision patterns with equal open/close | TODO |
| CDL_HAMMER | Hammer & Inverted Hammer | Bullish reversal with long lower shadow | TODO |
| CDL_ENGULFING | Engulfing Pattern | Body completely engulfs prior candle | TODO |
| CDL_HARAMI | Harami Pattern | Small candle within prior candle's body | TODO |
| CDL_STAR | Morning/Evening Star | Three-candle reversal patterns | TODO |
| CDL_MARUBOZU | Marubozu | No shadows, strong directional candle | TODO |
| CDL_SPINNING | Spinning Top | Small body with upper/lower shadows | TODO |
| CDL_3BLACKCROWS | Three Black Crows | Three consecutive bearish candles | TODO |
| CDL_3WHITESOLDIERS | Three White Soldiers | Three consecutive bullish candles | TODO |
| CDL_ABANDONED | Abandoned Baby | Gap pattern with doji in middle | TODO |
| CDL_ADVANCEBLOCK | Advance Block | Three white candles with weakening momentum | TODO |

### Chart Patterns

| Code | Name | Key Characteristics | Notes |
| ------------ | --------------------------------------- | --------------------------------------------------------------------------------------- | ----- |
| HEAD_SHOULDERS | Head and Shoulders | Major reversal pattern with three peaks | TODO |
| DOUBLE_TOP | Double Top/Bottom | Two peaks/troughs at similar levels | TODO |
| TRIANGLE | Triangle Patterns | Converging trendlines (ascending, descending, symmetrical) | TODO |
| FLAG | Flag Patterns | Continuation patterns with parallel channels | TODO |
| WEDGE | Wedge Patterns | Converging lines (rising/falling wedge) | TODO |

**Note:** The Reversals category focuses on identifying potential trend changes and reversal patterns. This is the newest category in the collection, starting with the foundational Parabolic SAR indicator.
