# ATRBANDS - Atrbands


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. ATRBANDS addresses this by implementing `Calculates ATR Bands using ATR for width` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates ATR Bands using ATR for width`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | Source series for the center line |
| `length` | Period for ATR and MA calculations |
| `multiplier` | ATR multiplier for band width |

### Returns

- tuple with [middle, upper, lower] band values

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_source` | `input.source` | default: `close`, label: "Source" |
| `i_length` | `input.int` | default: `20`, label: "Length" |
| `i_mult` | `input.float` | default: `2.0`, label: "ATR Multiplier" |

## Runtime profile

- Declared optimization: Uses RMA with warmup compensator, O(1) complexity per bar
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

- Source code: `indicators/channels/atrbands.pine`
- Documentation file: `indicators/channels/atrbands.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/channels/atrbands.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/channels/atrbands.md
