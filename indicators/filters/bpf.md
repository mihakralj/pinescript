# BPF: Bandpass Filter

[Pine Script Implementation of BPF](https://github.com/mihakralj/pinescript/blob/main/indicators/filters/bpf.pine)

## Overview and Purpose

The Bandpass Filter (BPF) is a specialized signal processing tool designed to isolate specific frequency components within a defined range. Developed by John Ehlers, a pioneer in applying signal processing techniques to financial markets, this filter addresses the challenge of extracting cyclical components from price data. By implementing a cascaded structure that combines highpass and lowpass filters, BPF effectively isolates market cycles of specific periodicities while removing both longer-term trends and shorter-term noise. This makes it particularly valuable for cycle analysis, seasonality detection, and trading strategies based on rhythm identification.

## Core Concepts

* **Frequency isolation:** Combines highpass and lowpass filtering to extract market cycles within a specific frequency band
* **Dual cutoff control:** Provides independent control over both the lower and upper cutoff periods
* **Market application:** Particularly effective for identifying and trading dominant market cycles or seasonal patterns

The core innovation of BPF is its optimized cascade architecture that maintains maximum signal integrity within the passband while achieving excellent rejection of components outside the desired frequency range. Unlike simple moving averages that can only perform lowpass filtering, BPF can isolate specific market rhythms, allowing traders to focus on cycles of particular interest while eliminating both trend and noise components.

## Common Settings and Parameters

| Parameter | Default | Function | When to Adjust |
|-----------|---------|----------|---------------|
| Lower Period | 10 | Controls the longer periodicity cutoff | Set to the maximum cycle length you want to analyze |
| Upper Period | 2 | Controls the shorter periodicity cutoff | Set to the minimum cycle length you want to analyze |
| Source | close | Price data used for calculation | Consider using hlc3 for a more balanced price representation |

**Pro Tip:** For detecting market cycles, set the Lower Period to approximately 2-3× your suspected dominant cycle length and the Upper Period to about 1/3 of the dominant cycle length to isolate the primary cycle with good precision.

## Calculation and Mathematical Foundation

**Simplified explanation:**
The bandpass filter works by first removing long-term trends using a highpass filter (which blocks low frequencies), then removing short-term noise using a lowpass filter (which blocks high frequencies). What remains are the medium-term cycles that fall between these two cutoffs.

**Technical formula:**
BP = Lowpass(Highpass(X))

Highpass coefficients:
- a1 = exp(-1.414π/lp)
- b1 = 2a1 × cos(1.414 × 180/lp)
- c1 = (1 + c2 - c3)/4
- c2 = b1
- c3 = -a1²

Lowpass coefficients:
- a2 = exp(-1.414π/up)
- b2 = 2a2 × cos(1.414 × 180/up)
- k1 = 1 - k2 - k3
- k2 = b2
- k3 = -a2²

> 🔍 **Technical Note:** The 1.414 (√2) factor in the coefficient calculations optimizes the filter response for maximally flat passband with minimal ringing, providing cleaner cycle extraction than simpler designs.

## Interpretation Details

The Bandpass Filter can be used in various trading contexts:

* **Cycle identification:** Reveals dominant market cycles by isolating specific frequency bands
* **Signal generation:** Zero-line crossings and peaks/troughs of the filtered output generate potential trade signals
* **Market regime detection:** Changes in cycle amplitude indicate shifts between trending and ranging market conditions
* **Seasonal analysis:** Isolate known seasonal patterns by setting period boundaries around the seasonal timeframe
* **Multiple bandpass analysis:** Apply several bandpass filters with different period ranges to identify multiple cycle influences

## Limitations and Considerations

* **Parameter sensitivity:** Performance highly dependent on appropriate period settings
* **Initialization period:** Requires several bars to stabilize after the start of data
* **Phase shifts:** Some phase shift (timing delay) is unavoidable in the filtered output
* **Amplitude variations:** Output amplitude varies based on the energy present in the selected frequency band
* **Complementary tools:** Best used with phase analysis tools and amplitude-based indicators for confirmation

## References

* Ehlers, J.F. "Cycle Analytics for Traders," Wiley, 2013
* Ehlers, J.F. "Rocket Science for Traders," Wiley, 2001
