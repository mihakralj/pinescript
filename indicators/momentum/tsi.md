# TSI - Tsi


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. TSI addresses this by implementing `Calculates the True Strength Index and its signal line.` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates the True Strength Index and its signal line.`

### Parameters

| Parameter | Purpose |
|---|---|
| `src` | series float The source series. |
| `longLen` | simple int The lookback period for the first EMA smoothing (typically 25). |
| `shortLen` | simple int The lookback period for the second EMA smoothing (typically 13). |
| `signalLen` | simple int The lookback period for the signal line EMA (typically 13). |

### Returns

- tuple [float, float] A tuple containing the TSI value and its signal line.

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_source` | `input.source` | default: `close`, label: "Source" |
| `i_longLen` | `input.int` | default: `25`, label: "Long Length" |
| `i_shortLen` | `input.int` | default: `13`, label: "Short Length" |
| `i_signalLen` | `input.int` | default: `13`, label: "Signal Length" |

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

- Source code: `indicators/momentum/tsi.pine`
- Documentation file: `indicators/momentum/tsi.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/momentum/tsi.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/momentum/tsi.md
