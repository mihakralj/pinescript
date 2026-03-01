# EFI - Efi


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. EFI addresses this by implementing `Calculates Elder's Force Index (EFI), measuring buying and selling pressure through price change and volume` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Elder's Force Index (EFI), measuring buying and selling pressure through price change and volume`

### Parameters

| Parameter | Purpose |
|---|---|
| `len` | Lookback period for EMA smoothing (default: 13) |
| `src` | Source price for calculation (default: built-in close) |
| `src_vol` | The volume (default: built-in volume) |

### Returns

- float The smoothed Force Index value

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_length` | `input.int` | default: `13`, label: "Length" |

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

- Source code: `indicators/volume/efi.pine`
- Documentation file: `indicators/volume/efi.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/volume/efi.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/volume/efi.md
