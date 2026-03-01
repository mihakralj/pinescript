# SINE - Sine


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. SINE addresses this by implementing `Calculates Ehlers’ original Sine Wave using a two‑pole High‑Pass, a Super‑Smoother,` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Ehlers’ original Sine Wave using a two‑pole High‑Pass, a Super‑Smoother,`

### Parameters

| Parameter | Purpose |
|---|---|
| `src` | Series to calculate the Sine Wave from |
| `hpLength` | High‑Pass filter length (detrending period) |
| `ssfLength` | Super‑Smoother filter length (cycle smoothing period) |

### Returns

- single normalized sine‑wave value in [‑1 … +1]

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_source` | `input.source` | default: `close`, label: "Source" |
| `i_hpLength` | `input.int` | default: `40`, label: "High‑Pass Filter Length" |
| `i_ssfLength` | `input.int` | default: `10`, label: "Super‑Smoother Filter Length" |

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

- Source code: `indicators/cycles/sine.pine`
- Documentation file: `indicators/cycles/sine.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/cycles/sine.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/cycles/sine.md
