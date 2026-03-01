# BBS - Bbs


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. BBS addresses this by implementing `Calculates Bollinger Bands for squeeze detection` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Bollinger Bands for squeeze detection`
- `Calculates Average True Range for Keltner Channels`
- `Calculates Keltner Channels using SMA and ATR`
- `Detects Bollinger Band Squeeze condition`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | Series to calculate from |
| `period` | Lookback period |
| `period` | Lookback period for ATR calculation |
| `source` | Series to calculate from |
| `period` | Lookback period |
| `atr_mult` | ATR multiplier for channel width |
| `atr_val` | Pre-calculated ATR value |
| `source` | Series to analyze |
| `bb_period` | Bollinger Band period |
| `bb_mult` | Bollinger Band standard deviation multiplier |
| `kc_period` | Keltner Channel period |
| `kc_mult` | Keltner Channel ATR multiplier |

### Returns

- tuple with [middle, deviation] values

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_bb_period` | `input.int` | default: `20`, label: "Bollinger Band Period" |
| `i_bb_mult` | `input.float` | default: `2.0`, label: "BB StdDev Multiplier" |
| `i_kc_period` | `input.int` | default: `20`, label: "Keltner Channel Period" |
| `i_kc_mult` | `input.float` | default: `1.5`, label: "KC ATR Multiplier" |
| `i_source` | `input.source` | default: `close`, label: "Source" |
| `i_show_bands` | `input.bool` | default: `true`, label: "Show Bands" |
| `i_show_channels` | `input.bool` | default: `true`, label: "Show Channels" |

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

- Source code: `indicators/oscillators/bbs.pine`
- Documentation file: `indicators/oscillators/bbs.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/oscillators/bbs.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/oscillators/bbs.md
