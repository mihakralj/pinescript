# PIVOTWOOD - Pivotwood


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. PIVOTWOOD addresses this by implementing `Calculates Woodie's pivot points with weighted closing price` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Woodie's pivot points with weighted closing price`

### Parameters

| Parameter | Purpose |
|---|---|
| `tf` | Timeframe for pivot calculation ("D", "W", "M") |

### Returns

- Tuple [pp, r1, r2, r3, s1, s2, s3] with pivot levels

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_timeframe` | `input.timeframe` | default: `"D"`, label: "D" |
| `i_show_pp` | `input.bool` | default: `true`, label: "Show Pivot Point" |
| `i_show_r1` | `input.bool` | default: `true`, label: "Show R1" |
| `i_show_r2` | `input.bool` | default: `true`, label: "Show R2" |
| `i_show_r3` | `input.bool` | default: `true`, label: "Show R3" |
| `i_show_s1` | `input.bool` | default: `true`, label: "Show S1" |
| `i_show_s2` | `input.bool` | default: `true`, label: "Show S2" |
| `i_show_s3` | `input.bool` | default: `true`, label: "Show S3" |
| `i_color_pp` | `input.color` | default: `color.yellow`, label: "PP Color" |
| `i_color_r` | `input.color` | default: `color.red`, label: "Resistance Color" |
| `i_color_s` | `input.color` | default: `color.green`, label: "Support Color" |

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

- Source code: `indicators/reversals/pivotwood.pine`
- Documentation file: `indicators/reversals/pivotwood.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/reversals/pivotwood.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/reversals/pivotwood.md
