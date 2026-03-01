# DYMOI - Dymoi


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. DYMOI addresses this by implementing `Calculates StdDev over a circular buffer of given period` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates StdDev over a circular buffer of given period`
- `Calculates Wilder's RMA RSI with warmup compensation and adaptive alpha`
- `Calculates Dynamic Momentum Index`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | Price series |
| `period` | Window size |
| `source` | Close price series |
| `dynPeriod` | Dynamic period (integer, already clamped) |
| `source` | Close price series |
| `basePeriod` | Base RSI period (default 14) |
| `shortPeriod` | Short StdDev window (default 5) |
| `longPeriod` | Long StdDev window (default 10) |
| `minPeriod` | Minimum dynamic period (default 3) |
| `maxPeriod` | Maximum dynamic period (default 30) |

### Returns

- Population standard deviation of the window

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_basePeriod` | `input.int` | default: `14`, label: "Base RSI Period" |
| `i_shortPeriod` | `input.int` | default: `5`, label: "Short StdDev Period" |
| `i_longPeriod` | `input.int` | default: `10`, label: "Long StdDev Period" |
| `i_minPeriod` | `input.int` | default: `3`, label: "Min Period" |
| `i_maxPeriod` | `input.int` | default: `30`, label: "Max Period" |
| `i_source` | `input.source` | default: `close`, label: "Source" |

## Runtime profile

- Declared optimization: Uses circular buffers for O(1) StdDev; adaptive Wilder RMA for RSI
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

- Source code: `indicators/oscillators/dymoi.pine`
- Documentation file: `indicators/oscillators/dymoi.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/oscillators/dymoi.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/oscillators/dymoi.md
