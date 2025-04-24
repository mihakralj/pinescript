# MESA Cycle Identifier

The MESA (Maximum Entropy Spectral Analysis) Cycle Identifier is based on John Ehlers' work on cycle analysis in financial markets. It extracts the dominant cycle and its phase from price data using the MESA algorithm and identifies potential cycle turning points.

## Calculation

The MESA algorithm employs a combination of signal processing techniques:

1. **Super Smoother Filter**: Initial price smoothing using a low-lag filter
2. **Hilbert Transform**: Generates the analytic signal (in-phase and quadrature components)
3. **Instantaneous Phase**: Calculated from the in-phase and quadrature components
4. **Dominant Cycle**: Extracted from the phase progression rate

The algorithm adjusts adaptively based on the detected cycle's stability:
- Faster adaptation when cycles are clear and consistent (using `fastLimit`)
- Slower adaptation when cycles are less defined (using `slowLimit`)

## Implementation

```pinescript
mesa(series float source, float fastLimit=0.5, float slowLimit=0.05) =>
    // Implementation details...
    [period, phase, mama_val, fama_val]
```

## Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| Source | close | Price source for cycle detection |
| Fast Limit | 0.5 | Maximum adaptation rate (0.01-0.99) |
| Slow Limit | 0.05 | Minimum adaptation rate (0.001-0.5) |
| Show Moving Averages | true | Display MAMA and FAMA moving averages |
| Show Cycle Markers | true | Display cycle high/low markers |
| Show Dominant Period | true | Display the dominant cycle period |

## Outputs

1. **Dominant Cycle Period**: The detected cycle length in bars
2. **MAMA (MESA Adaptive Moving Average)**: Fast adaptive moving average that follows price closely during trending periods
3. **FAMA (Following Adaptive Moving Average)**: Slower moving average that follows MAMA
4. **Cycle Markers**: Triangles indicating potential cycle highs (red) and lows (green)

## Interpretation

- **Cycle Period**: Lower values indicate faster market cycles, higher values indicate slower cycles
- **Cycle Markers**: Potential reversal points based on phase analysis
- **Moving Averages**: 
  - MAMA crossing FAMA can signal trend changes
  - When they converge, market is trending strongly
  - When they diverge, market is in transition

## Common Settings

- For intraday trading: fastLimit = 0.5, slowLimit = 0.05
- For daily charts: fastLimit = 0.3, slowLimit = 0.03
- For less noise (fewer signals): Increase slowLimit
- For faster response (more signals): Increase fastLimit

## Notes

- The algorithm performs best when there's a clear cyclical component in the price action
- Performance may degrade during strong trends or highly random market conditions
- The phase detection system needs several bars to initialize properly
