# AGC - Agc


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. AGC addresses this by implementing `Ehlers Automatic Gain Control — amplitude normalization via exponential peak tracking` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Ehlers Automatic Gain Control — amplitude normalization via exponential peak tracking`
- `Roofing filter — 2-pole HPF → Super Smoother bandpass for detrending raw price`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | Series to normalize (must oscillate around zero — use a filter output, not raw price) |
| `decay` | Peak decay factor per bar (controls adaptation speed; 0.991 ≈ 110-bar half-life) |
| `source` | Raw price series |
| `hpLength` | Highpass cutoff period (removes trend below this period) |
| `ssLength` | Super Smoother cutoff period (removes noise above this period) |

### Returns

- Amplitude-normalized signal in [-1, +1] range

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_source` | `input.source` | default: `close`, label: "Source" |

## Runtime profile

- Declared optimization: O(1) per bar — single division + comparison, zero lookback
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

- Source code: `indicators/filters/agc.pine`
- Documentation file: `indicators/filters/agc.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/filters/agc.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/filters/agc.md
