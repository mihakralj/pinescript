# HARMEAN - Harmean


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. HARMEAN addresses this by implementing `Calculates the Harmonic Mean of a series over a lookback period.` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates the Harmonic Mean of a series over a lookback period.`

### Parameters

| Parameter | Purpose |
|---|---|
| `src` | series float Input data series (must contain positive values). |
| `len` | simple int Lookback period (must be > 0). |

### Returns

- series float The Harmonic Mean, or na if data is not suitable (e.g., non-positive values, insufficient data).

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_source` | `input.source` | default: `close`, label: "Source (must be positive values)" |
| `i_length` | `input.int` | default: `14`, label: "Lookback Period" |

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

- Source code: `indicators/statistics/harmean.pine`
- Documentation file: `indicators/statistics/harmean.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/statistics/harmean.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/statistics/harmean.md
