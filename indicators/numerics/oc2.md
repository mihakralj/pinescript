# OC2: Open-Close Midpoint

[Pine Script Implementation of OC2](https://github.com/mihakralj/pinescript/blob/main/indicators/numerics/oc2.pine)

## Naming Convention

**OC2** is known as **Midpoint** or **Open-Close Midpoint** in technical analysis. This measure focuses on the opening and closing prices:

- **OC2**: Programming/library notation (Open-Close average of 2)
- **Midpoint**: Common name emphasizing the middle point between open and close
- **Open-Close Average**: Descriptive name showing the calculation
- **Settlement Midpoint**: Alternative emphasizing start and end points

## Overview and Purpose

The OC2 indicator calculates the midpoint between the opening and closing prices for each bar. This price transformation provides a balanced view of the bar's directional movement by averaging where the period started and where it finished. Unlike HL2 which focuses on the trading range extremes, OC2 emphasizes the actual directional progress made during each period, filtering out intrabar volatility while maintaining sensitivity to the net price change.

This measure is particularly useful for analyzing price momentum and directional bias without the noise of intrabar price fluctuations. By averaging the open and close, OC2 creates a smoothed price series that represents the bar's directional thrust while reducing the impact of opening or closing spikes.

## Core Concepts

* **Directional midpoint:** Represents the average of where price started and ended, focusing on net movement
* **Volatility filtering:** Removes intrabar range extremes, smoothing price action
* **Momentum representation:** Emphasizes the directional component of price movement
* **Opening-closing balance:** Provides equal weight to session start and finish prices

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Open | open | Opening price data | Typically not adjusted, uses standard open price |
| Close | close | Closing price data | Typically not adjusted, uses standard close price |

**Pro Tip:** OC2 is effective for reducing noise in choppy markets where intrabar wicks are large but net movement is minimal. Use OC2 as a source for trend-following indicators when you want to focus on directional progress rather than range extremes.

## Calculation and Mathematical Foundation

**Simplified explanation:**
OC2 calculates the arithmetic mean of the opening and closing prices, representing the midpoint of the bar's directional movement.

**Technical formula:**

```
OC2 = (Open + Close) / 2
```

Where:
- Open is the price at the start of the period
- Close is the price at the end of the period

> 🔍 **Technical Note:** This calculation has O(1) complexity with minimal computational overhead. The formula requires no historical data and can be computed in real-time as each bar develops.

## Interpretation Details

OC2 provides several analytical perspectives:

* **Directional focus:** Emphasizes net price movement while filtering intrabar extremes
* **Momentum smoothing:** Creates a naturally smoothed representation of price momentum
* **Gap analysis:** Clearly shows gaps between periods through discontinuities in the OC2 line
* **Trend clarity:** Removes range noise to reveal underlying directional trends
* **Session balance:** Shows the average price between session open and close

## Limitations and Considerations

* **Ignores intrabar action:** Does not capture the full range of price movement within each bar
* **Time-weighted bias:** Assumes equal importance of open and close regardless of when most trading occurred
* **Volume independence:** Does not account for volume distribution during the session
* **Gap sensitivity:** Can show abrupt changes when gaps occur between bars
* **No range information:** Loses information about intrabar volatility and trading range

## References

* Kaufman, P. J. (2013). Trading Systems and Methods. John Wiley & Sons.
* Murphy, J. J. (1999). Technical Analysis of the Financial Markets. New York Institute of Finance.
* Elder, A. (1993). Trading for a Living. John Wiley & Sons.
