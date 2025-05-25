# TVI: Trade Volume Index

[Pine Script Implementation of TVI](https://github.com/mihakralj/pinescript/blob/main/indicators/volume/tvi.pine)

## Overview and Purpose

The Trade Volume Index (TVI) is a technical indicator that uses price and volume to determine whether a security is being accumulated (purchased) or distributed (sold). Very similar to the On Balance Volume (OBV) indicator, TVI was specifically designed to work with intraday tick data, making it more suitable for short-term analysis compared to OBV which works better with end-of-day data.

The key innovation of TVI is its use of minimum tick movements to determine market direction, filtering out insignificant price fluctuations that might give false signals. This makes TVI particularly effective at identifying the underlying buying and selling pressure in actively traded securities.

## Core Concepts

* **Tick-based direction**: Uses minimum tick size to determine meaningful price movements
* **Binary classification**: Distinguishes between accumulation (buying pressure) and distribution (selling pressure)
* **Volume weighting**: Adds volume during accumulation, subtracts during distribution
* **Direction persistence**: Maintains previous direction when price changes are within tick threshold
* **Cumulative measurement**: Running total showing net accumulation/distribution over time

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Price Field | Close | Price series for direction analysis | Use High/Low for range analysis, Open for gap analysis |
| Min. Move | 0.125 | Minimum price change to register direction | Adjust based on instrument's typical tick size |
| Volume Source | Volume | Volume data for weighting calculations | Use different volume types if available |

**Pro Tip:** Set Min. Move to your instrument's actual minimum tick size for optimal sensitivity. For stocks, this might be 0.01, for futures it varies by contract, and for forex it's typically the pip value.

## Calculation and Mathematical Foundation

**Simplified explanation:**
TVI compares each price change to a minimum movement threshold. If the change exceeds the threshold, it sets the direction (up=accumulation, down=distribution). If the change is within the threshold, it maintains the previous direction. Volume is then added or subtracted based on this direction.

**Technical formula:**
```
Price_Change = Price - Previous_Price

If Price_Change > Min_Tick then Direction = 1 (Accumulation)
If Price_Change < -Min_Tick then Direction = 0 (Distribution)  
If -Min_Tick <= Price_Change <= +Min_Tick then Direction = Previous_Direction

TVI += Volume if Direction = 1
TVI -= Volume if Direction = 0
```

Where:
- Min_Tick = Minimum meaningful price movement
- Direction = Binary state (1=Accumulation, 0=Distribution)
- Previous_Direction = Direction from the previous calculation

> 🔍 **Technical Note:** The direction persistence feature is crucial - when price changes are smaller than the minimum tick, TVI assumes the previous trend continues, avoiding noise from insignificant price movements.

## Interpretation Details

TVI provides clear signals about market sentiment:

* **Rising TVI (Accumulation Phase):**
  - Trades taking place at the asking price
  - Buyers are accumulating the security
  - Indicates underlying buying pressure
  - Bullish signal, especially when price is flat

* **Falling TVI (Distribution Phase):**
  - Trades taking place at the bid price  
  - Sellers are distributing the security
  - Indicates underlying selling pressure
  - Bearish signal, especially when price is flat

* **TVI-Price Divergences:**
  - **Bullish divergence:** Price flat/declining while TVI rising (accumulation during weakness)
  - **Bearish divergence:** Price flat/rising while TVI falling (distribution during strength)
  - **Leading indicator:** TVI often changes direction before price

## Trading Applications

**Primary Signals:**
- **Accumulation Alert:** TVI rising while prices flat → expect upward price movement
- **Distribution Alert:** TVI falling while prices flat → expect downward price movement
- **Trend Confirmation:** TVI direction confirms price trend strength
- **Early Warning:** TVI divergence signals potential price reversals

**Advanced Strategies:**
- **Breakout Confirmation:** Use TVI direction to validate price breakouts
- **Support/Resistance:** TVI levels can act as dynamic support/resistance
- **Volume Quality:** Assess whether volume supports price movements
- **Market Timing:** Enter positions when TVI aligns with desired direction

## Limitations and Considerations

* **Tick size dependency:** Requires proper Min. Move calibration for each instrument
* **Trending bias:** Cumulative nature can create long-term directional bias
* **Volume quality:** Effectiveness depends on accurate volume reporting
* **Market conditions:** Less reliable during low-volume or choppy market periods
* **Lag consideration:** Being cumulative, TVI may lag during rapid trend changes
* **False signals:** Sudden volume spikes can temporarily distort readings

## Comparison with OBV

| Aspect | TVI | OBV |
|--------|-----|-----|
| **Data Type** | Intraday tick data | End-of-day data |
| **Direction Logic** | Minimum tick threshold | Simple up/down comparison |
| **Noise Filtering** | Built-in via tick size | No filtering |
| **Best Use** | Short-term, active trading | Longer-term trend analysis |
| **Sensitivity** | Adjustable via Min. Move | Fixed sensitivity |

## References

* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
* Schwager, J. D. (1996). Technical Analysis. John Wiley & Sons.
* Elder, Alexander (1993). Trading for a Living. John Wiley & Sons.
* Pring, Martin J. (2002). Technical Analysis Explained. McGraw-Hill.
