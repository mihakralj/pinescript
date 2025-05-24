# WAD: Williams Accumulation/Distribution

[Pine Script Implementation of WAD](https://github.com/mihakralj/pinescript/blob/main/indicators/volume/wad.pine)

## Overview and Purpose

The Williams Accumulation/Distribution (WAD) is a technical indicator developed by Larry Williams that measures the cumulative buying and selling pressure in a security. Unlike the traditional Accumulation/Distribution Line (ADL) which uses the relationship between close and the high-low range, WAD compares the current close to the previous close and uses true range calculations to determine the degree of accumulation or distribution. This approach makes WAD particularly sensitive to gap openings and provides a different perspective on money flow that emphasizes price momentum rather than intraday position.

## Core Concepts

* **Close-to-close comparison:** Uses the relationship between current and previous closes to determine market direction
* **True range integration:** Incorporates true range calculations to account for gaps and limit moves
* **Momentum emphasis:** More sensitive to price momentum and gap movements than traditional A/D indicators
* **Volume weighting:** Multiplies price movement by volume to reflect the intensity of buying/selling pressure

WAD's unique calculation method makes it particularly valuable for markets that experience frequent gaps or limit moves, as it accounts for these price discontinuities in a way that traditional A/D indicators cannot.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| High | high | High price series | Typically uses built-in high values |
| Low | low | Low price series | Typically uses built-in low values |
| Close | close | Close price series | Typically uses built-in close values |
| Open | open | Open price series | Used for true range calculation |
| Volume | volume | Volume series | Typically uses built-in volume data |

**Pro Tip:** WAD requires no parameter adjustments as it's a cumulative indicator. However, it's particularly effective when combined with price charts that clearly show gaps, as WAD will capture the accumulation/distribution occurring across these price discontinuities.

## Calculation and Mathematical Foundation

**Simplified explanation:**
WAD calculates a Price Multiplier (PM) based on whether the current close is higher, lower, or equal to the previous close. When the close is higher, PM equals the close minus the true range low. When lower, PM equals the close minus the true range high. This value is then multiplied by volume and added to the cumulative total.

**Technical formula:**
```
True Range High = MAX(High, Previous Close)
True Range Low = MIN(Low, Previous Close)

If Close > Previous Close:
    PM = Close - True Range Low
Else If Close < Previous Close:
    PM = Close - True Range High
Else:
    PM = 0

A/D Value = PM × Volume
WAD = Cumulative sum of A/D Values
```

**Step-by-step calculation:**
```
1. Calculate True Range High: MAX(current high, previous close)
2. Calculate True Range Low: MIN(current low, previous close)
3. Determine Price Multiplier based on close direction:
   - Up close: Close - True Range Low
   - Down close: Close - True Range High
   - Unchanged: 0
4. Multiply PM by volume: A/D Value = PM × Volume
5. Add to cumulative WAD: WAD += A/D Value
```

> 🔍 **Technical Note:** WAD's use of true range calculations makes it superior to traditional A/D indicators in markets with gaps or limit moves. The true range ensures that the full price movement is captured, even when it extends beyond the current period's high-low range. This makes WAD particularly valuable for futures markets and stocks that frequently gap.

## Interpretation Details

WAD provides insights into cumulative buying and selling pressure:

* **Trend confirmation:** Rising WAD confirms accumulation and upward price momentum; falling WAD confirms distribution and downward momentum
* **Gap analysis:** WAD effectively captures accumulation/distribution that occurs across price gaps
* **Divergence signals:** WAD diverging from price can provide early warning of potential trend changes
* **Volume-confirmed moves:** Large WAD movements indicate strong volume backing behind price changes
* **Support/resistance testing:** WAD behavior during support/resistance tests reveals the conviction behind price movements
* **Momentum shifts:** Changes in WAD direction often precede changes in price momentum

## Limitations and Considerations

* **Cumulative nature:** As a cumulative indicator, WAD may trend in one direction for extended periods regardless of current conditions
* **Volume dependency:** Requires reliable volume data; less effective in markets with poor volume reporting
* **No absolute levels:** WAD values are relative; focus should be on direction and divergences rather than absolute levels
* **Gap sensitivity:** While useful for gap analysis, unusual gap activity can temporarily distort the indicator
* **Market structure:** More effective in liquid markets where volume accurately represents trading interest
* **Lag factor:** Being cumulative, WAD may lag in identifying very short-term reversals
* **Complementary analysis:** Best used alongside price action analysis, momentum indicators, and other volume tools

## References

* Williams, Larry R. "The Secret of Selecting Stocks for Immediate and Substantial Gains." Windsor Books, 1972.
* Williams, Larry R. "How I Made One Million Dollars Last Year Trading Commodities." Conceptual Management, 1973.
* Pring, Martin J. "Technical Analysis Explained." McGraw-Hill, 2002.
