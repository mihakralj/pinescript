# BILATERAL - Bilateral


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. BILATERAL addresses this by implementing `Calculates Bilateral Filter` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Bilateral Filter`

### Parameters

| Parameter | Purpose |
|---|---|
| `src` | Series to calculate Bilateral Filter from |
| `length` | Number of bars used in the calculation (spatial domain) |
| `sigma_s_ratio` | Ratio to determine spatial standard deviation |
| `sigma_r_mult` | Multiplier for range standard deviation |

### Returns

- Bilateral Filter value

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_length` | `input.int` | default: `20`, label: "Length" |
| `i_sigma_s_ratio` | `input.float` | default: `0.5`, label: "Spatial Sigma Ratio" |
| `i_sigma_r_mult` | `input.float` | default: `1.0`, label: "Range Sigma Multiplier" |
| `i_source` | `input.source` | default: `close`, label: "Source" |

## Runtime profile

- Declared optimization: Uses edge-preserving bilateral smoothing with O(n) complexity per bar
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

- Source code: `indicators/filters/bilateral.pine`
- Documentation file: `indicators/filters/bilateral.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/filters/bilateral.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/filters/bilateral.md
