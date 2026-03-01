# ALLIGATOR - Alligator


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. ALLIGATOR addresses this by implementing `Calculates Williams Alligator indicator using SMMA (RMA)` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Williams Alligator indicator using SMMA (RMA)`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | Series to calculate Alligator from |
| `jawPeriod` | Period for Jaw line (typically 13) |
| `jawOffset` | Forward offset for Jaw line (typically 8) |
| `teethPeriod` | Period for Teeth line (typically 8) |
| `teethOffset` | Forward offset for Teeth line (typically 5) |
| `lipsPeriod` | Period for Lips line (typically 5) |
| `lipsOffset` | Forward offset for Lips line (typically 3) |

### Returns

- Tuple [jaw, teeth, lips] values

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_source` | `input.source` | default: `hlc3`, label: "Source" |
| `i_jawPeriod` | `input.int` | default: `13`, label: "Jaw Period" |
| `i_jawOffset` | `input.int` | default: `8`, label: "Jaw Offset" |
| `i_teethPeriod` | `input.int` | default: `8`, label: "Teeth Period" |
| `i_teethOffset` | `input.int` | default: `5`, label: "Teeth Offset" |
| `i_lipsPeriod` | `input.int` | default: `5`, label: "Lips Period" |
| `i_lipsOffset` | `input.int` | default: `3`, label: "Lips Offset" |

## Runtime profile

- Declared optimization: Uses Wilder's RMA (SMMA) with exponential warmup compensator for O(1) complexity
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

- Source code: `indicators/dynamics/alligator.pine`
- Documentation file: `indicators/dynamics/alligator.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/dynamics/alligator.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/dynamics/alligator.md
