# LINEARTRANS - Lineartrans


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. LINEARTRANS addresses this by implementing `Applies a linear transformation (y = a*(x - sma) + sma + b) relative to the source's SMA, calculated internally.` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Applies a linear transformation (y = a*(x - sma) + sma + b) relative to the source's SMA, calculated internally.`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | series float The input series to transform. |
| `period` | simple int The lookback period for the internal SMA calculation. |
| `a` | float The scaling factor (slope). |
| `b` | float The offset (intercept). |

### Returns

- series float The linearly transformed series relative to its internally calculated SMA.

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_smaPeriod` | `input.int` | default: `200`, label: "SMA Period" |
| `i_a` | `input.float` | default: `2.0`, label: "Scale (a)" |
| `i_b` | `input.float` | default: `20.0`, label: "Offset (b)" |

## Runtime profile

- Declared optimization: for performance and dirty data
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

- Source code: `indicators/numerics/lineartrans.pine`
- Documentation file: `indicators/numerics/lineartrans.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/numerics/lineartrans.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/numerics/lineartrans.md
