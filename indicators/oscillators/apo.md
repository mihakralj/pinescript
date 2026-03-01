# APO - Apo


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. APO addresses this by implementing `Calculates Absolute Price Oscillator (APO) as difference between fast and slow EMAs` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Absolute Price Oscillator (APO) as difference between fast and slow EMAs`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | Series to calculate APO from |
| `fastLength` | Period for fast EMA |
| `slowLength` | Period for slow EMA |

### Returns

- APO value (fast EMA - slow EMA)

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_source` | `input.source` | default: `close`, label: "Source" |
| `i_fastLength` | `input.int` | default: `12`, label: "Fast Length" |
| `i_slowLength` | `input.int` | default: `26`, label: "Slow Length" |

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

- Source code: `indicators/oscillators/apo.pine`
- Documentation file: `indicators/oscillators/apo.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/oscillators/apo.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/oscillators/apo.md
