# JMA - Jma


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. JMA addresses this by implementing `Calculates JMA using adaptive techniques to adjust to market volatility` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates JMA using adaptive techniques to adjust to market volatility`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | Series to calculate JMA from |
| `period` | Number of bars used in the calculation |
| `phase` | Phase shift (-100 to 100). Negative values reduce lag but may cause overshoot |
| `power` | Smoothing factor (0.1-1.0). Lower values create smoother curves |

### Returns

- JMA value with adaptive smoothing and reduced lag

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_period` | `input.int` | default: `10`, label: "Period" |
| `i_phase` | `input.int` | default: `0`, label: "Phase" |
| `i_power` | `input.float` | default: `0.45`, label: "Power" |
| `i_source` | `input.source` | default: `close`, label: "Source" |

## Runtime profile

- Declared optimization: Uses adaptive volatility adjustment and phase control for O(1) complexity per bar
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

- Source code: `indicators/trends_IIR/jma.pine`
- Documentation file: `indicators/trends_IIR/jma.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/trends_IIR/jma.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/trends_IIR/jma.md
