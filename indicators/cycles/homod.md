# HOMOD - Homod


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. HOMOD addresses this by implementing `Quadrant-aware angle calculation using stable atan2` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Quadrant-aware angle calculation using stable atan2`
- `Measures dominant cycle period using Ehlers homodyne discriminator`

### Parameters

| Parameter | Purpose |
|---|---|
| `y` | Imaginary component |
| `x` | Real component |
| `source` | Price input series |
| `minPeriod` | Minimum dominant cycle length |
| `maxPeriod` | Maximum dominant cycle length |

### Returns

- Angle in radians from -π to π

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_source` | `input.source` | default: `hlc3`, label: "Source" |
| `i_minPeriod` | `input.float` | default: `6`, label: "Min Period" |
| `i_maxPeriod` | `input.float` | default: `50`, label: "Max Period" |

## Runtime profile

- Declared optimization: Exponential warmup compensation for dominant cycle smoothing
- Streaming model: single-pass update on each new bar.
- Warm-up behavior: outputs can be unstable until enough samples satisfy `lookback parameter`.
- Memory model: state is kept in Pine series context rather than external buffers.

## Trade-offs

Streaming logic keeps incremental cost stable, but initialization and edge-case handling become first-class concerns. That is a deliberate choice: predictable execution beats opaque recalculation spikes in live charts.

## Verification checklist

1. Open the script in TradingView and confirm it compiles under Pine Script v6.
2. Validate warm-up behavior on sparse data and short histories.
3. Compare output against a trusted reference implementation for the same parameters.
4. Confirm parameter bounds reject invalid values without silent fallback.

## References

- Source code: `indicators/cycles/homod.pine`
- Documentation file: `indicators/cycles/homod.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/cycles/homod.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/cycles/homod.md
