# Recursive Gaussian Moving Average (RGMA)

The Recursive Gaussian Moving Average (RGMA) filter provides enhanced smoothing for time series data by applying a multi-pass exponential moving average (EMA) recursively. While a true Gaussian filter is symmetric and technically an FIR (Finite Impulse Response) filter due to its fixed weights, RGMA utilizes recursive (IIR - Infinite Impulse Response) techniques to *approximate* the smoothing characteristics of a Gaussian filter. This recursive approach, often achieved by cascading simple IIR filters like EMAs, offers computational efficiency while effectively reducing noise and identifying underlying trends. The degree of smoothing is controlled by the number of recursive passes.

[Pine Script Implementation of RGMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends_IIR/rgma.pine)

## Core Concepts

RGMA utilizes a recursive application of an EMA filter:

- **Multi-Pass Smoothing**: Applies the EMA filter multiple times, controlled by the **passes** parameter. Each pass refines the smoothing.
- **Adjusted Period**: The effective smoothing period is adjusted based on the number of passes to maintain consistency.
- **Recursive Application**: The output of each EMA pass serves as the input for the subsequent pass, creating a cascaded filtering effect.

## Mathematical Foundation

The RGMA calculation approximates a Gaussian filter by applying an EMA recursively over a specified number of passes. Cascading multiple first-order IIR filters (like EMAs) in this manner tends towards a Gaussian response shape due to principles related to the central limit theorem. The process is as follows:

For each pass *i* (from 0 to **passes** - 1):

1. **Adjusted Period Calculation**:
    adjusted_period = period / sqrt(passes)

2. **Smoothing Factor (Alpha) Calculation**:
    alpha = 2.0 / (adjusted_period + 1.0)

3. **Recursive EMA Calculation**:
    - **First Pass (i=0)**: The EMA is applied to the original source data.
        filter[0] = alpha * (source - filter[0]) + filter[0]
    - **Subsequent Passes (i > 0)**: The EMA is applied to the output of the previous pass (filter[i-1]).
        filter[i] = alpha * (filter[i-1] - filter[i]) + filter[i]

Where:

- *source*: The input time series value at the current bar.
- *period*: The user-defined initial smoothing period.
- *passes*: The number of recursive passes (iterations) of the EMA.
- *adjusted_period*: The period used in the EMA calculation for each pass, adjusted by the square root of the number of passes.
- *alpha*: The smoothing factor derived from the *adjusted_period*.
- *filter[i]*: The output value of the i-th pass EMA filter. The final RGMA value is *filter[passes-1]*.

### Passes Parameter

The **passes** parameter determines how many times the EMA filter is applied recursively:

- **passes** = 1: RGMA behaves like a standard EMA with the specified **period**.
- **passes** > 1: Increases the smoothness and approximates a Gaussian filter more closely. Higher values introduce more lag but provide greater noise reduction. Common values range from 2 to 4.

### Adjusted Period

Adjusting the period by sqrt(passes) ensures that the overall smoothing effect remains comparable regardless of the number of passes, preventing excessive smoothing as passes increase.

## Initialization

RGMA requires careful initialization for its recursive nature:

1. **Filter State**: An array (filter) stores the intermediate results for each pass.
2. **First Bar**: On the first calculation bar, all elements of the filter array are initialized with the *source* value.
3. **Subsequent Bars**: The filter array values from the previous bar are used in the recursive calculations for the current bar.

## Advantages and Disadvantages

### Advantages

- **Superior Smoothing**: Provides significantly smoother output compared to a single EMA, effectively reducing noise.
- **Gaussian Approximation**: Recursively applying EMAs approximates the response of a Gaussian filter, known for its good frequency domain characteristics.
- **Adjustable Smoothness**: The **period** and **passes** parameters offer fine control over the trade-off between smoothness and lag.
- **Trend Clarity**: Helps in identifying the underlying trend by filtering out short-term fluctuations.

### Disadvantages

- **Increased Lag**: Introduces more lag than a single EMA, especially with a higher number of **passes**.
- **Computational Cost**: Requires more calculations than a simple EMA due to the multiple passes.
- **Parameter Tuning**: Requires careful selection of both **period** and **passes** to achieve the desired response.
