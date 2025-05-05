# SGF: Savitzky-Golay Filter

[Pine Script Implementation of SGF](https://github.com/mihakralj/pinescript/blob/main/indicators/filters/sgf.pine)

## Overview and Purpose

The Savitzky-Golay Filter (SGF) is a digital filter that performs local polynomial regression on a series of values to determine the smoothed value for each point. Developed by Abraham Savitzky and Marcel Golay in 1964, it is particularly effective at preserving higher moments of the data while reducing noise. This implementation provides a practical adaptation for financial time series, offering superior preservation of peaks, valleys, and other important market structures that might be distorted by simpler moving averages.

## Core Concepts

* **Local polynomial fitting:** Fits a polynomial of specified order to a sliding window of data points
* **Moment preservation:** Maintains higher statistical moments (peaks, valleys, inflection points)
* **Optimized coefficients:** Uses pre-computed coefficients for common polynomial orders
* **Adaptive weighting:** Weight distribution varies based on polynomial order and window size
* **Market application:** Particularly effective for preserving significant price movements while filtering noise

The core innovation of the Savitzky-Golay filter is its ability to smooth data while preserving important features that are often flattened by other filtering methods. This makes it especially valuable for technical analysis where maintaining the shape of price patterns is crucial.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Window Size | 11 | Number of points used in local fitting (must be odd) | Increase for smoother output, decrease for better feature preservation |
| Polynomial Order | 2 | Order of fitting polynomial (2 or 4) | Use 2 for general smoothing, 4 for better peak preservation |
| Source | close | Price data used for calculation | Consider using hlc3 for more stable fitting |

**Pro Tip:** A window size of 11 with polynomial order 2 provides a good balance between smoothing and feature preservation. For sharper peaks and valleys, use order 4 with a smaller window size.

## Calculation and Mathematical Foundation

**Simplified explanation:**
The filter fits a polynomial of specified order to a moving window of price data. The smoothed value at each point is computed from this local fit, effectively removing noise while preserving the underlying shape of the data.

**Technical formula:**
For a window of size N and polynomial order M, the filtered value is:

y[n] = Σ(c_i × x[n+i])

Where:
- c_i are the pre-computed filter coefficients
- x[n+i] are the input values in the window
- Coefficients depend on window size N and polynomial order M

> 🔍 **Technical Note:** The implementation uses optimized coefficient calculations for orders 2 and 4, which cover most practical applications while maintaining computational efficiency.

## Interpretation Details

The Savitzky-Golay filter can be used in various trading strategies:

* **Pattern recognition:** Preserves chart patterns while removing noise
* **Peak detection:** Maintains amplitude and width of significant peaks
* **Trend analysis:** Smooths price movement without distorting important transitions
* **Divergence trading:** Better preservation of local maxima and minima
* **Volatility analysis:** Accurate representation of price movement dynamics

## Limitations and Considerations

* **Computational complexity:** More intensive than simple moving averages
* **Edge effects:** First and last few points may show end effects
* **Parameter sensitivity:** Performance depends on appropriate window size and order selection
* **Data requirements:** Needs sufficient points for polynomial fitting
* **Complementary tools:** Best used with volume analysis and momentum indicators

## References

* Savitzky, A., Golay, M.J.E. "Smoothing and Differentiation of Data by Simplified Least Squares Procedures," Analytical Chemistry, 1964
* Press, W.H. et al. "Numerical Recipes: The Art of Scientific Computing," Chapter 14
* Schafer, R.W. "What Is a Savitzky-Golay Filter?" IEEE Signal Processing Magazine, 2011
