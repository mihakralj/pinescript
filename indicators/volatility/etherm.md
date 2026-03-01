# ETHERM - Etherm


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. ETHERM addresses this by implementing `Calculates Elder's Market Thermometer with EMA signal line` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Elder's Market Thermometer with EMA signal line`

### Parameters

| Parameter | Purpose |
|---|---|
| `period` | The EMA smoothing period for the signal line |

### Returns

- [thermometer, signal] The raw thermometer value and EMA signal line

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_period` | `input.int` | default: `22`, label: "EMA Period" |
| `i_multiplier` | `input.float` | default: `3.0`, label: "Explosive Threshold" |

## Runtime profile

- Declared optimization: Beta precomputation for EMA warmup compensation
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

- Source code: `indicators/volatility/etherm.pine`
- Documentation file: `indicators/volatility/etherm.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/volatility/etherm.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/volatility/etherm.md
