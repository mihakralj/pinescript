# DECO - Deco


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. DECO addresses this by implementing `Calculates Decycler Oscillator using dual 2-pole Butterworth high-pass filters` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Decycler Oscillator using dual 2-pole Butterworth high-pass filters`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | Source series to calculate DECO from |
| `short_period` | Short cycle cutoff period for high-pass filter |
| `long_period` | Long cycle cutoff period for high-pass filter |

### Returns

- DECO value (HP(longPeriod) - HP(shortPeriod))

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_short_period` | `input.int` | default: `30`, label: "Short Period" |
| `i_long_period` | `input.int` | default: `60`, label: "Long Period" |
| `i_source` | `input.source` | default: `close`, label: "Source" |

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

- Source code: `indicators/oscillators/deco.pine`
- Documentation file: `indicators/oscillators/deco.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/oscillators/deco.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/oscillators/deco.md
