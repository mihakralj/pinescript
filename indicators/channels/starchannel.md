# STARCHANNEL - Starchannel


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. STARCHANNEL addresses this by implementing `Calculates Stoller Average Range Channel using ATR for width and SMA for center` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Stoller Average Range Channel using ATR for width and SMA for center`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | Source series for the center line |
| `length` | Period for ATR and SMA calculations |
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

- Declared optimization: Uses circular buffer for SMA and ATR with compensator, O(1) complexity
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

- Source code: `indicators/channels/starchannel.pine`
- Documentation file: `indicators/channels/starchannel.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/channels/starchannel.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/channels/starchannel.md
