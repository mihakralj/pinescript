# KAMA - Kama


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. KAMA addresses this by implementing `Calculates KAMA using adaptive smoothing based on market volatility` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates KAMA using adaptive smoothing based on market volatility`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | Series to calculate KAMA from |
| `period` | Length of the efficiency ratio lookback period |
| `fast_alpha` | Fastest EMA constant (2/(2+1)) |
| `slow_alpha` | Slowest EMA constant (2/(30+1)) |

### Returns

- KAMA value with efficiency ratio-based adaptive smoothing

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_period` | `input.int` | default: `10`, label: "Period" |
| `i_source` | `input.source` | default: `close`, label: "Source" |
| `i_fast` | `input.int` | default: `2`, label: "Fast EMA Period" |
| `i_slow` | `input.int` | default: `30`, label: "Slow EMA Period" |

## Runtime profile

- Declared optimization: Uses efficiency ratio calculation for O(n) complexity per bar due to lookback sum
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

- Source code: `indicators/trends_IIR/kama.pine`
- Documentation file: `indicators/trends_IIR/kama.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/trends_IIR/kama.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/trends_IIR/kama.md
