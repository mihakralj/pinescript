# Pascal Weighted Moving Average (PWMA)

The Pascal Weighted Moving Average (PWMA) is a type of finite impulse response (FIR) filter that uses coefficients from Pascal's triangle as weights. This approach creates a natural bell-shaped distribution of weights with highest emphasis on the middle of the lookback period, providing effective smoothing while maintaining responsiveness to price changes.

[Pine Script Implementation of PWMA](https://github.com/mihakralj/pinescript/blob/main/indicators/trends/pwma.pine)

## Historical Context and Purpose

The PWMA leverages Pascal's triangle, a triangular array of binomial coefficients first studied by Blaise Pascal in the 17th century. While Pascal's triangle has been used in various mathematical applications for centuries, its application to financial time series analysis offers a natural weighting scheme that:

1. Emphasizes the middle portion of the data window
2. Creates a symmetrical bell-shaped distribution of weights
3. Provides better statistical properties than linear weighting

## Mathematical Foundation

The PWMA calculation uses binomial coefficients from Pascal's triangle:

PWMA = ∑(Price₍ᵢ₎ × C(n-1,i)) / ∑(C(n-1,i))

Where:
- Price₍ᵢ₎ is the price at position i in the lookback window
- C(n-1,i) is the binomial coefficient "n-1 choose i"
- n is the period length

### Binomial Coefficient Calculation

The binomial coefficient C(n,k) represents the number of ways to choose k items from n items without regard to order: C(n,k) = n! / (k! × (n-k)!)

For computational stability and precision, the implementation:

1. Uses a stable recurrence relation: C(n,k) = C(n,k-1) × (n-k+1) / k
2. Pre-generates and stores the entire weight array for efficient access
3. Dynamically adjusts the calculation window based on available bars

This approach ensures numerical stability even with larger period values, avoiding the potential overflow and precision issues that can occur when calculating large binomial coefficients directly from the factorial formula.

## FIR Filter Characteristics

PWMA is a Finite Impulse Response (FIR) filter, meaning it uses only the current and past inputs without feedback. Its behavior can be analyzed in both frequency and time domains:

### Transfer Properties (Frequency Domain)

The frequency domain characteristics of PWMA include:
1. **Roll-off Rate**: Approximately -6dB per octave, similar to triangular windows
2. **Frequency Response**:
   - Smooth attenuation curve
   - Superior side-lobe suppression compared to WMA
3. **Phase Response**: Linear phase response (constant group delay)
4. **Gain**: Normalized by sum of coefficients to maintain signal amplitude

### Response Properties (Time Domain)

The time domain characteristics demonstrate:
1. **Impulse Response**:
   - Finite memory extent (exactly equal to period)
   - Bell-shaped response profile
   - Zero phase distortion

2. **Step Response**:
   - Smooth transition
   - Minimal ringing artifacts
   - Natural rise time

3. **Smoothing Properties**:
   - Effective noise reduction
   - Preservation of underlying trend
   - Balanced lag characteristics

## Advantages and Disadvantages

### Advantages

- **Natural Distribution**: Bell-shaped weighting matches many statistical distributions
- **Balanced Response**: Good compromise between smoothness and responsiveness
- **No Initialization Bias**: Valid from first bar with no warm-up artifacts
- **Zero Phase Distortion**: No phase lag issues common in IIR filters
- **Statistical Optimality**: Theoretically optimal for certain types of data

### Disadvantages

- **Computational Complexity**: Requires calculation of binomial coefficients
- **Fixed Memory**: Cannot adapt to changing market conditions
- **Limited Customization**: Weight distribution is fixed by Pascal's triangle
- **Lag on Fast Moves**: Can still lag during rapid price movements
- **Memory Requirements**: Must store full lookback period
