# MEDIAN: Median Filter

[Pine Script Implementation of MEDIAN](https://github.com/mihakralj/pinescript/blob/main/indicators/filters/median.pine)

## Overview and Purpose

The Median Filter is a non-linear digital filter that replaces each value with the median of neighboring values. Unlike linear filters that can blur edges, the median filter is particularly effective at removing impulse noise (spikes and outliers) while preserving important edge transitions in the data. This implementation provides a robust approach for financial time series, offering superior noise reduction for price data that contains sudden spikes or outliers while maintaining significant price level transitions.

## Core Concepts

* **Non-linear filtering:** Uses order statistics rather than weighted averages
* **Edge preservation:** Maintains sharp transitions in price levels
* **Outlier removal:** Effectively eliminates spikes and anomalous values
* **Robust statistics:** Less sensitive to extreme values than mean-based filters
* **Market application:** Particularly effective for cleaning price data with sudden spikes

The core innovation of the median filter is its ability to remove noise while preserving edges, making it especially valuable for technical analysis where maintaining significant price transitions is crucial.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Length | 5 | Window size for median calculation (must be odd) | Increase for stronger noise reduction, decrease for better detail preservation |
| Source | close | Price data used for calculation | Consider using hlc3 for more stable filtering |

**Pro Tip:** A length of 5 provides a good balance between noise reduction and signal preservation. For removing longer anomalies, increase the length, but be aware this may delay edge detection.

## Calculation and Mathematical Foundation

**Simplified explanation:**
The filter sorts values within a sliding window and selects the middle (median) value. This approach naturally eliminates outliers while preserving step changes in the data.

**Technical formula:**
For a window of size N centered at point i:

y[i] = median(x[i-(N-1)/2], ..., x[i], ..., x[i+(N-1)/2])

Where:
- x[i] are the input values in the window
- N is the window size (must be odd)
- median() selects the middle value after sorting

> 🔍 **Technical Note:** The implementation handles edge cases and missing values by considering only valid data points within the window, ensuring robust operation even with incomplete data.

## Interpretation Details

The median filter can be used in various trading strategies:

* **Spike removal:** Eliminates false signals from price spikes
* **True range analysis:** Provides cleaner price levels for support/resistance
* **Gap handling:** Maintains legitimate gaps while removing noise
* **Pattern recognition:** Improves reliability of chart pattern identification
* **Volatility analysis:** Removes outliers for better volatility measurement

## Limitations and Considerations

* **Computational complexity:** Requires sorting operations
* **Window size tradeoff:** Larger windows remove more noise but may delay edge detection
* **Non-linear behavior:** Cannot be analyzed with linear system theory
* **Detail preservation:** May remove small but legitimate price movements
* **Complementary tools:** Best used with trend and momentum indicators

## References

* Tukey, J.W. "Exploratory Data Analysis," Chapter 7: Smoothing
* Arce, G.R. "Nonlinear Signal Processing: A Statistical Approach," Chapter 3
* Nodes, T.A., Gallagher, N.C. "Median Filters: Some Modifications and Their Properties," IEEE Transactions on Acoustics, Speech, and Signal Processing
