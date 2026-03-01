# APCHANNEL - Apchannel


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. AP addresses this by implementing `Calculates Andrews' Pitchfork lines based on three pivot points` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Andrews' Pitchfork lines based on three pivot points`

### Parameters

| Parameter | Purpose |
|---|---|
| `p1_back` | Bars back to first pivot point (leftmost) |
| `p2_back` | Bars back to second pivot point (middle) |
| `p3_back` | Bars back to third pivot point (rightmost) |

### Returns

- tuple of [median, upper, lower] lines for current bar

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_p1_back` | `input.int` | default: `45`, label: "Point 1 (Leftmost)" |
| `i_p2_back` | `input.int` | default: `30`, label: "Point 2 (Second)" |
| `i_p3_back` | `input.int` | default: `15`, label: "Point 3 (Third)" |

## Runtime profile

- Declared optimization: Geometric projection with O(1) complexity per bar
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

- Source code: `indicators/channels/apchannel.pine`
- Documentation file: `indicators/channels/apchannel.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/channels/apchannel.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/channels/apchannel.md
