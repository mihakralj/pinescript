# README - Readme

## Architectural problem

Technical analysis on live charts has two failure modes: inconsistent warm-up behavior and unpredictable runtime cost. This repository documents Pine implementations with a streaming-first lens so those failure modes stay visible, testable, and controllable.

## Architectural stance

Every indicator page is written for technical evaluation, not marketing. Design choices are presented with trade-offs, source-level evidence, and concrete verification steps.

## Repository facts

- Pine source files: **416**
- Markdown documentation files: **436**
- Canonical upstream project: https://github.com/mihakralj/QuanTAlib

## Indicator families

- [Channels and Bands](./indicators/channels/_index.md) — 22 documented scripts
- [Core Price Transforms](./indicators/core/_index.md) — 7 documented scripts
- [Cycles](./indicators/cycles/_index.md) — 16 documented scripts
- [Dynamics](./indicators/dynamics/_index.md) — 20 documented scripts
- [Error Metrics](./indicators/errors/_index.md) — 27 documented scripts
- [Filters](./indicators/filters/_index.md) — 40 documented scripts
- [Forecasts](./indicators/forecasts/_index.md) — 2 documented scripts
- [Momentum](./indicators/momentum/_index.md) — 19 documented scripts
- [Numerics](./indicators/numerics/_index.md) — 41 documented scripts
- [Oscillators](./indicators/oscillators/_index.md) — 47 documented scripts
- [Reversals](./indicators/reversals/_index.md) — 10 documented scripts
- [Statistics](./indicators/statistics/_index.md) — 34 documented scripts
- [Trends - FIR](./indicators/trends_FIR/_index.md) — 34 documented scripts
- [Trends - IIR](./indicators/trends_IIR/_index.md) — 36 documented scripts
- [Volatility](./indicators/volatility/_index.md) — 28 documented scripts
- [Volume](./indicators/volume/_index.md) — 27 documented scripts

## How to validate the docs

1. Pick any indicator page and open its linked `.pine` source.
2. Confirm parameters, returns, and optimization notes match source annotations.
3. Run the script in TradingView with short and long histories to inspect warm-up behavior.
4. Compare outputs with a reference implementation before production use.

## License

MIT License.
