# MAMA - Mama


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. MAMA addresses this by implementing `Calculates MAMA and FAMA using Ehlers' MESA adaptive algorithm` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates MAMA and FAMA using Ehlers' MESA adaptive algorithm`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | Series to calculate MAMA from |
| `fastLimit` | Maximum rate of adaptation (0.5 typical) |
| `slowLimit` | Minimum rate of adaptation (0.05 typical) |

### Returns

- [mama, fama] array containing MAMA and FAMA values

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_source` | `input.source` | default: `close`, label: "Source" |
| `i_fastLimit` | `input.float` | default: `0.5`, label: "Fast Limit" |
| `i_slowLimit` | `input.float` | default: `0.05`, label: "Slow Limit" |

## Runtime profile

- Declared optimization: Uses Hilbert Transform phase detection for O(1) complexity per bar
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

- Source code: `indicators/trends_IIR/mama.pine`
- Documentation file: `indicators/trends_IIR/mama.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/trends_IIR/mama.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/trends_IIR/mama.md
