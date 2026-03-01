# PFE - Pfe


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. PFE addresses this by implementing `Calculates Polarized Fractal Efficiency using fractal geometry` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Polarized Fractal Efficiency using fractal geometry`

### Parameters

| Parameter | Purpose |
|---|---|
| `period` | Lookback period for fractal path measurement (default: 10) |
| `smoothPeriod` | EMA smoothing period for raw PFE (default: 5) |

### Returns

- Smoothed PFE value oscillating between -100 and +100

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_period` | `input.int` | default: `10`, label: "Period" |
| `i_smooth` | `input.int` | default: `5`, label: "Smooth Period" |

## Runtime profile

- Declared optimization: O(period) per bar via circular buffer for fractal path sum; O(1) EMA smoothing
- Streaming model: single-pass update on each new bar.
- Warm-up behavior: outputs can be unstable until enough samples satisfy `period`.
- Memory model: state is kept in Pine series context rather than external buffers.

## Trade-offs

Streaming logic keeps incremental cost stable, but initialization and edge-case handling become first-class concerns. That is a deliberate choice: predictable execution beats opaque recalculation spikes in live charts.

## Verification checklist

1. Open the script in TradingView and confirm it compiles under Pine Script v6.
2. Validate warm-up behavior on sparse data and short histories.
3. Compare output against a trusted reference implementation for the same parameters.
4. Confirm parameter bounds reject invalid values without silent fallback.

## References

- Source code: `indicators/dynamics/pfe.pine`
- Documentation file: `indicators/dynamics/pfe.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/dynamics/pfe.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/dynamics/pfe.md
