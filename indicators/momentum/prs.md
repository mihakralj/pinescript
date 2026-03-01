# PRS - Prs


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. PRS addresses this by implementing `Calculates Price Relative Strength comparing two assets` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Price Relative Strength comparing two assets`

### Parameters

| Parameter | Purpose |
|---|---|
| `base` | Base asset price series |
| `comp` | Compare asset price series |
| `smooth_len` | Smoothing period for ratio |

### Returns

- Tuple containing raw ratio and smoothed ratio

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_base` | `input.source` | default: `close`, label: "Base Asset" |
| `i_comp` | `input.symbol` | default: `"SPY"`, label: "SPY" |
| `i_smooth` | `input.int` | default: `1`, label: "Smoothing Length" |
| `i_norm` | `input.bool` | default: `false`, label: "Normalize to 100" |
| `i_log` | `input.bool` | default: `false`, label: "Logarithmic Scale" |

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

- Source code: `indicators/momentum/prs.pine`
- Documentation file: `indicators/momentum/prs.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/momentum/prs.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/momentum/prs.md
