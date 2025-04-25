# Bilateral Filter

The Bilateral Filter is an edge-preserving smoothing filter. It replaces the intensity of each bar with a weighted average of intensity values from nearby bars. Crucially, the weight depends not only on Euclidean distance of bars (spatial domain) but also on the radiometric differences (range domain, e.g., intensity difference). This preserves sharp edges by systematically limiting the averaging process across large intensity variations.

[Pine Script Implementation of Bilateral Filter](https://github.com/mihakralj/pinescript/blob/main/indicators/filters/bilateral.pine)

## Mathematical Foundation

The Bilateral Filter output for a value at position `p` is calculated as:

BF[p] = (1 / Wp) × Σ_{q ∈ S} G_s(||p - q||) × G_r(|I[p] - I[q]|) × I[q]

Where:

- `I[p]` is the input value at position `p`.
- `S` is the spatial neighborhood of `p` (defined by `length`).
- `G_s` is the spatial Gaussian kernel: `exp(-||p - q||² / (2 × σ_s²))`
- `G_r` is the range Gaussian kernel: `exp(-|I[p] - I[q]|² / (2 × σ_r²))`
- `σ_s` is the spatial standard deviation (controls spatial influence).
- `σ_r` is the range standard deviation (controls intensity influence).
- `Wp` is the normalization factor: `Σ_{q ∈ S} G_s(||p - q||) × G_r(|I[p] - I[q]|)`

## Implementation Details

1. **Parameterization**:
    - `length`: Defines the size of the spatial neighborhood (number of past bars).
    - `sigma_s_ratio`: Controls the spatial standard deviation (`σ_s = length × sigma_s_ratio`). A smaller ratio gives more weight to closer bars.
    - `sigma_r_mult`: Controls the range standard deviation (`σ_r = stdev(src, length) × sigma_r_mult`). A smaller multiplier makes the filter more sensitive to intensity differences, thus preserving edges better.

2. **Weight Calculation**:
    - Iterates through the `length` bars preceding the current bar.
    - Calculates spatial weight based on distance (bar index difference).
    - Calculates range weight based on the difference between the current bar's value and the neighbor's value.
    - Combines spatial and range weights multiplicatively.

3. **Normalization**:
    - Sums all calculated weights (`Wp`).
    - Sums the product of each neighbor's value and its combined weight.
    - Divides the weighted sum of values by the sum of weights to get the filtered output.

## Advantages and Disadvantages

### Advantages

- **Edge Preservation**: Excellent at smoothing while keeping significant changes (edges) sharp.
- **Noise Reduction**: Effectively reduces noise in flat regions.
- **Parameter Control**: Offers separate control over spatial and range smoothing.
- **Non-linear**: Adapts smoothing based on local value differences.

### Disadvantages

- **Computational Cost**: More intensive than simple linear filters (like SMA or EMA) due to the loop and per-neighbor calculations.
- **Parameter Tuning**: Finding optimal `sigma_s` and `sigma_r` can be data-dependent and require experimentation.
- **Potential Artifacts**: Can sometimes introduce minor gradient reversal artifacts near edges.
- **Lag**: While edge-preserving, it still introduces some lag compared to the raw signal.
