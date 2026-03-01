# VWAPSD - Vwapsd


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. VWAPSD addresses this by implementing `Calculate VWAP with Standard Deviation Bands` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculate VWAP with Standard Deviation Bands`

### Parameters

| Parameter | Purpose |
|---|---|
| `src` | Source price series (typically hlc3) |
| `vol` | Volume series |
| `reset_condition` | Condition to reset VWAP calculation |
| `num_devs` | Number of standard deviations for bands |

### Returns

- [vwap, upper_band, lower_band]

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_source` | `input.source` | default: `hlc3`, label: "Source" |
| `i_session_type` | `input.string` | default: `"1D"`, label: "1D" |
| `i_num_devs` | `input.float` | default: `2.0`, label: "Standard Deviations" |

## Runtime profile

- Declared optimization: not explicitly annotated in source comments.
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

- Source code: `indicators/channels/vwapsd.pine`
- Documentation file: `indicators/channels/vwapsd.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/channels/vwapsd.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/channels/vwapsd.md
