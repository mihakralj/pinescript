# PVD - Pvd


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. PVD addresses this by implementing `Calculates Price Volume Divergence` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Price Volume Divergence`

### Parameters

| Parameter | Purpose |
|---|---|
| `price_period` | Lookback period for price momentum |
| `volume_period` | Lookback period for volume momentum |
| `smoothing_period` | Period for smoothing divergence signals |
| `c` | Close price series |
| `vol` | Volume series |

### Returns

- Smoothed divergence value

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `price_period` | `input.int` | default: `14`, label: "Price Period" |
| `volume_period` | `input.int` | default: `14`, label: "Volume Period" |
| `divergence_threshold` | `input.float` | default: `50.0`, label: "Divergence Threshold" |
| `smoothing_period` | `input.int` | default: `3`, label: "Smoothing Period" |

## Runtime profile

- Declared optimization: for performance and dirty data
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

- Source code: `indicators/volume/pvd.pine`
- Documentation file: `indicators/volume/pvd.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/volume/pvd.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/volume/pvd.md
