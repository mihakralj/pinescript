# MFI - Mfi


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. MFI addresses this by implementing `Calculates Money Flow Index, a volume-weighted RSI that measures buying/selling pressure` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Calculates Money Flow Index, a volume-weighted RSI that measures buying/selling pressure`

### Parameters

| Parameter | Purpose |
|---|---|
| `len` | Period for MFI calculation |
| `src_high` | High price series |
| `src_low` | Low price series |
| `src_close` | Close price series |
| `src_vol` | Volume series |

### Returns

- float The MFI value (0-100)

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `len` | `input.int` | default: `14`, label: "MFI Period" |

## Runtime profile

- Declared optimization: Uses circular buffers for O(1) performance with proper NA handling
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

- Source code: `indicators/volume/mfi.pine`
- Documentation file: `indicators/volume/mfi.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/volume/mfi.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/volume/mfi.md
