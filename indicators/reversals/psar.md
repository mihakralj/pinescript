# PSAR - Psar


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. PSAR addresses this by implementing `Calculates Parabolic Stop And Reverse (SAR)` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Parabolic Stop And Reverse (SAR)`

### Parameters

| Parameter | Purpose |
|---|---|
| `af_start` | Initial acceleration factor (Wilder's original: 0.02) |
| `af_increment` | Acceleration factor increment per new extreme (Wilder's original: 0.02) |
| `af_max` | Maximum acceleration factor (Wilder's original: 0.20) |

### Returns

- SAR value (stop level for current trend)

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_af_start` | `input.float` | default: `0.02`, label: "Start AF" |
| `i_af_increment` | `input.float` | default: `0.02`, label: "AF Increment" |
| `i_af_max` | `input.float` | default: `0.20`, label: "Max AF" |

## Runtime profile

- Declared optimization: Minimal state variables, O(1) per bar
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

- Source code: `indicators/reversals/psar.pine`
- Documentation file: `indicators/reversals/psar.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/reversals/psar.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/reversals/psar.md
