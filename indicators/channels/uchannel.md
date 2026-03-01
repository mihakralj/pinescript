# UCHANNEL - Uchannel


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. UCHANNEL addresses this by implementing `Calculates Ultimate Channel` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Ultimate Channel`

### Parameters

| Parameter | Purpose |
|---|---|
| `src` | Source series for the centerline (typically close) |
| `high_src` | Source series for high prices |
| `low_src` | Source series for low prices |
| `strLength` | Lookback period for smoothing the True Range |
| `length` | Lookback period for smoothing the centerline |
| `numSTRs` | Multiplier for the Smoothed True Range to define channel width |

### Returns

- tuple [upperChannel, middleChannel, lowerChannel]

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_source` | `input.source` | default: `close`, label: "Source for Centerline" |
| `i_high` | `input.source` | default: `high`, label: "Source for High" |
| `i_low` | `input.source` | default: `low`, label: "Source for Low" |
| `i_strLength` | `input.int` | default: `20`, label: "STR Length" |
| `i_length` | `input.int` | default: `20`, label: "Centerline Length" |
| `i_numSTRs` | `input.float` | default: `1.0`, label: "STR Multiplier" |

## Runtime profile

- Declared optimization: not explicitly annotated in source comments.
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

- Source code: `indicators/channels/uchannel.pine`
- Documentation file: `indicators/channels/uchannel.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/channels/uchannel.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/channels/uchannel.md
