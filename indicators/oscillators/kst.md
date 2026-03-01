# KST - Kst


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. KST addresses this by implementing `SMA helper via circular buffer with running sum, O(1) per bar` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `SMA helper via circular buffer with running sum, O(1) per bar`
- `KST Oscillator: weighted sum of 4 smoothed ROC values + signal line`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | Input series |
| `period` | SMA period |
| `buf` | Circular buffer array (pre-allocated) |
| `head_idx` | Head index (passed by reference via array) |
| `sum_val` | Running sum (passed by reference via array) |
| `cnt` | Count of valid values (passed by reference via array) |
| `source` | Series to analyze |
| `r1` | ROC period 1 (shortest) |
| `r2` | ROC period 2 |
| `r3` | ROC period 3 |
| `r4` | ROC period 4 (longest) |
| `s1` | SMA smoothing for ROC1 |
| `s2` | SMA smoothing for ROC2 |
| `s3` | SMA smoothing for ROC3 |
| `s4` | SMA smoothing for ROC4 |
| `sigPeriod` | Signal line SMA period |

### Returns

- SMA value

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_source` | `input.source` | default: `close`, label: "Source" |
| `i_r1` | `input.int` | default: `10`, label: "ROC Period 1" |
| `i_r2` | `input.int` | default: `15`, label: "ROC Period 2" |
| `i_r3` | `input.int` | default: `20`, label: "ROC Period 3" |
| `i_r4` | `input.int` | default: `30`, label: "ROC Period 4" |
| `i_s1` | `input.int` | default: `10`, label: "SMA Smooth 1" |
| `i_s2` | `input.int` | default: `10`, label: "SMA Smooth 2" |
| `i_s3` | `input.int` | default: `10`, label: "SMA Smooth 3" |
| `i_s4` | `input.int` | default: `15`, label: "SMA Smooth 4" |
| `i_sig` | `input.int` | default: `9`, label: "Signal Period" |

## Runtime profile

- Declared optimization: not explicitly annotated in source comments.
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

- Source code: `indicators/oscillators/kst.pine`
- Documentation file: `indicators/oscillators/kst.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/oscillators/kst.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/oscillators/kst.md
