# MSTOCH - Mstoch


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. MSTOCH addresses this by implementing `Calculates Ehlers MESA Stochastic` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Ehlers MESA Stochastic`

### Parameters

| Parameter | Purpose |
|---|---|
| `src` | Series to calculate MESA Stochastic from |
| `stochLength` | Lookback period for the stochastic highest/lowest calculation |
| `hpLength` | Cutoff period for the Roofing Filter highpass stage (default 48) |
| `ssLength` | Cutoff period for the Roofing Filter super smoother stage (default 10) |

### Returns

- MESA Stochastic value (0 to 1 range, smoothed)

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_stochLength` | `input.int` | default: `20`, label: "Stochastic Length" |
| `i_hpLength` | `input.int` | default: `48`, label: "HP Length" |
| `i_ssLength` | `input.int` | default: `10`, label: "SS Length" |
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

- Source code: `indicators/oscillators/mstoch.pine`
- Documentation file: `indicators/oscillators/mstoch.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/oscillators/mstoch.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/oscillators/mstoch.md
