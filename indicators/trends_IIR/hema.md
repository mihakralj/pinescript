# HEMA - Hema


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. HEMA addresses this by implementing `Calculates HEMA (Hull Exponential Moving Average) combining multiple EMA calculations` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates HEMA (Hull Exponential Moving Average) combining multiple EMA calculations`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | Series to calculate HEMA from |
| `period` | Lookback period for calculation |

### Returns

- HEMA value that combines fast and slow EMAs with logarithmic weighting

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_period` | `input.int` | default: `10`, label: "Period" |
| `i_source` | `input.source` | default: `close`, label: "Source" |

## Runtime profile

- Declared optimization: Uses three-stage exponential warmup compensators for O(1) complexity
- Streaming model: single-pass update on each new bar.
- Warm-up behavior: outputs can be unstable until enough samples satisfy `period`.
- Memory model: state is kept in Pine series context rather than external buffers.

## Trade-offs

Streaming logic keeps incremental cost stable, but initialization and edge-case handling become first-class concerns. That is a deliberate choice: predictable execution beats opaque recalculation spikes in live charts.

## Verification checklist

1. Open the script in TradingView and confirm it compiles under Pine Script v6.
2. Validate warm-up behavior on sparse data and short histories.
3. Compare output against a trusted reference implementation for the same parameters.
4. Confirm parameter bounds reject invalid values without silent fallback.

## References

- Source code: `indicators/trends_IIR/hema.pine`
- Documentation file: `indicators/trends_IIR/hema.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/trends_IIR/hema.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/trends_IIR/hema.md
