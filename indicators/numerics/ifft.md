# IFFT - Ifft


## Architectural problem

Real-time chart analysis needs deterministic updates per bar and explicit handling of warm-up periods. IFFT addresses this by implementing `Spectral filter via forward DFT + frequency zeroing + inverse DFT` with parameterized inputs and direct state progression.

## Design decision

This implementation favors streaming execution over batch recomputation. The trade-off is more attention to state initialization, but latency stays predictable when charts scale.

## API surface

### Functions

- `Spectral filter via forward DFT + frequency zeroing + inverse DFT`

### Parameters

| Parameter | Purpose |
|---|---|
| `source` | Series to filter |
| `windowSize` | DFT window size (power of 2: 32, 64, 128) |
| `numHarmonics` | Number of lowest-frequency harmonics to keep (1..windowSize/2) |

### Returns

- reconstructed (filtered) value at the current bar

## Input configuration

| Input variable | Type | Configuration |
|---|---|---|
| `i_source` | `input.source` | default: `close`, label: "Source" |
| `i_window` | `input.int` | default: `64`, label: "Window Size" |
| `i_harmonics` | `input.int` | default: `5`, label: "Harmonics" |

## Runtime profile

- Declared optimization: Forward O(N*H) + inverse O(H); H = numHarmonics
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

- Source code: `indicators/numerics/ifft.pine`
- Documentation file: `indicators/numerics/ifft.md`
- GitHub source view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/numerics/ifft.pine
- GitHub documentation view: https://github.com/mihakralj/QuanTAlib/blob/main/indicators/numerics/ifft.md
