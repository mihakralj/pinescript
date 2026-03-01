# ACCBANDS - Accbands


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. ACCBANDS addresses this by implementing `Calculates Acceleration Bands using SMAs of high, low, close prices` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Acceleration Bands using SMAs of high, low, close prices`

### Parameters

| Parameter | Purpose |
|---|---|
| `high` | Series of high prices |
| `low` | Series of low prices |
| `close` | Series of close prices |
| `period` | Lookback period for the moving average |
| `factor` | Multiplier for band width calculation |

### Returns

- tuple with [middle, upper, lower] band values

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_period` | `input.int` | default: `20`, label: "Period" |
| `i_factor` | `input.float` | default: `2.0`, label: "Factor" |

## Runtime profile

- Declared optimization: Uses circular buffers with O(1) complexity per bar
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

- Source code: `indicators/channels/accbands.pine`
- Documentation file: `indicators/channels/accbands.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/channels/accbands.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/channels/accbands.md
