# CFB - Cfb


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. CFB addresses this by implementing `Calculates CFB auxiliary value for a single depth` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates CFB auxiliary value for a single depth`
- `Calculates Composite Fractal Behavior across multiple depths`
- `Jurik Moving Average for additional smoothing`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | Price series to analyze |
| `depth` | Lookback period for fractal pattern analysis |
| `maxSize` | Maximum buffer size (must be >= depth) |
| `source` | Price series to analyze |
| `maxDepth` | Maximum depth level (1-10) |
| `length` | Smoothing period for CFB values |
| `source` | Series to smooth |
| `period` | Smoothing period |
| `phase` | Phase adjustment (-100 to 100) |
| `power` | Power parameter for responsiveness |

### Returns

- Ratio representing fractal behavior at specified depth

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_source` | `input.source` | default: `hlcc4`, label: "Source" |
| `i_depth` | `input.int` | default: `10`, label: "CFB Depth" |
| `i_length` | `input.int` | default: `8`, label: "Smooth Length" |
| `i_jma_period` | `input.int` | default: `5`, label: "JMA Period" |
| `i_jma_phase` | `input.int` | default: `0`, label: "JMA Phase" |

## Runtime profile

- Declared optimization: O(n) complexity required for fractal pattern calculation across depth range
- Streaming model: single-pass update on each new bar.
- Warm-up behavior: outputs can be unstable until enough samples satisfy `length`.
- Memory model: state is kept in Pine series context rather than external buffers.

## Trade-offs

Streaming logic keeps incremental cost stable, but initialization and edge-case handling become first-class concerns. That is a deliberate choice: predictable execution beats opaque recalculation spikes in live charts.

## Verification checklist

1. Open the script in TradingView and confirm it compiles under Pine Script v6.
2. Validate warm-up behavior on sparse data and short histories.
3. Compare output against a trusted reference implementation for the same parameters.
4. Confirm parameter bounds reject invalid values without silent fallback.

## References

- Source code: `indicators/momentum/cfb.pine`
- Documentation file: `indicators/momentum/cfb.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/momentum/cfb.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/momentum/cfb.md
