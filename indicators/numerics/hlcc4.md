# HLCC4: Weighted Close

[Pine Script Implementation of HLCC4](https://github.com/mihakralj/pinescript/blob/main/indicators/numerics/hlcc4.pine)

## Naming Convention

**HLCC4** is commonly known as **Weighted Close** in technical analysis. This measure emphasizes the closing price by giving it double weight:

- **HLCC4**: Programming/library notation (High-Low-Close-Close average of 4)
- **Weighted Close**: Standard terminology emphasizing the double-weighted close
- **Weighted Average Price**: Alternative name highlighting the weighting
- **Close-Weighted Price**: Descriptive name showing closing bias

## Overview and Purpose

The HLCC4 indicator, commonly known as Weighted Close, calculates a weighted average that gives double emphasis to the closing price while including the high and low. This price transformation recognizes that the closing price often carries more significance than intrabar extremes, as it represents where the market actually settled after all participants completed their trading for the period. By weighting the close at 2x versus single weights for high and low, HLCC4 creates a price series that balances range information with closing bias.

This measure is widely used in technical analysis when you want to emphasize the closing price's importance while still considering the full trading range. The double weighting of the close reflects the belief that final settlement prices are more representative of true market consensus than intrabar extremes, which may represent brief spikes or temporary imbalances.

## Core Concepts

* **Closing emphasis:** Double weight on close price recognizes its greater significance
* **Range inclusion:** Still incorporates high and low extremes for complete context
* **Settlement focus:** Emphasizes where market actually settled versus where it spiked
* **Weighted averaging:** Unequal weights reflect different importance of price components

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| High | high | High price data | Typically not adjusted, uses standard high price |
| Low | low | Low price data | Typically not adjusted, uses standard low price |
| Close | close | Closing price data (2x weight) | Typically not adjusted, uses standard close price |

**Pro Tip:** HLCC4 is ideal when you believe closing prices are more significant than intrabar extremes, common in markets where settlement prices determine key levels. The 2x weight on close provides more emphasis than HLC3 (equal weights) but less smoothing than OHLC4.

## Calculation and Mathematical Foundation

**Simplified explanation:**
HLCC4 (Weighted Close) calculates a weighted average giving double importance to the closing price compared to the high and low prices.

**Technical formula:**

```
HLCC4 = (High + Low + Close × 2) / 4
```

Which can also be expressed as:
```
HLCC4 = (High + Low + Close + Close) / 4
```

Where:
- High is the highest price reached during the period
- Low is the lowest price reached during the period
- Close is the closing price (counted twice for double weight)

> 🔍 **Technical Note:** This calculation maintains O(1) complexity and is computationally efficient. The formula provides a middle ground between equal-weighted HLC3 and fully-weighted OHLC4 approaches.

## Interpretation Details

HLCC4 provides several analytical perspectives:

* **Closing priority:** Emphasizes final settlement price as most representative value
* **Range context:** Still considers high and low for volatility information
* **Moderate smoothing:** Less averaged than OHLC4 but smoother than HLC3
* **Settlement focus:** Reflects belief that closes are more meaningful than extremes
* **Weighted balance:** Provides 50% weight to close, 25% each to high and low

## Limitations and Considerations

* **Closing assumption:** Assumes closes are twice as important as extremes, which may not always be true
* **Opening omission:** Does not consider where the period started
* **Time-weighted bias:** Does not account for actual time spent at different price levels
* **Volume independence:** Ignores volume distribution across the price range
* **Arbitrary weighting:** The 2x weight is conventional but not mathematically derived
* **Extreme inclusion:** Still captures high and low extremes that may represent brief spikes

## References

* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
* Achelis, S. B. (2000). Technical Analysis from A to Z. McGraw-Hill.
* Kaufman, P. J. (2013). Trading Systems and Methods. John Wiley & Sons.
