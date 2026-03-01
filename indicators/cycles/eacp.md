# EACP - Eacp


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. EACP addresses this by implementing `Autocorrelation periodogram dominant cycle estimator` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Autocorrelation periodogram dominant cycle estimator`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | Price input series |
| `minPeriod` | Minimum period to evaluate |
| `maxPeriod` | Maximum period to evaluate |
| `avgLength` | Averaging length for Pearson correlation (0 uses lag length) |
| `enhance` | Apply cubic emphasis to highlight dominant peaks |

### Returns

- Smoothed dominant cycle estimate

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_source` | `input.source` | default: `close`, label: "Source" |
| `i_minPeriod` | `input.int` | default: `8`, label: "Min Period" |
| `i_maxPeriod` | `input.int` | default: `48`, label: "Max Period" |
| `i_avgLength` | `input.int` | default: `3`, label: "Autocorrelation Length" |
| `i_enhance` | `input.bool` | default: `true`, label: "Enhance Resolution" |

## Runtime profile

- Declared optimization: Removed buffer complexity, uses native PineScript historical operator for O(n) correlation
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

- Source code: `indicators/cycles/eacp.pine`
- Documentation file: `indicators/cycles/eacp.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/cycles/eacp.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/cycles/eacp.md
