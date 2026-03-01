# README - Readme

## Architectural problem

Technical analysis on live charts has two failure modes: inconsistent warm-up behavior and unpredictable runtime cost. This repository documents Pine implementations with a streaming-first lens so those failure modes stay visible, testable, and controllable.

## Architectural stance

Every indicator page is written for technical evaluation, not marketing. Design choices are presented with trade-offs, source-level evidence, and concrete verification steps.

## Welcome, chart wizards

This repository is a large collection of technical indicators assembled with mathematical care, operational caution, and the calm optimism of someone debugging Pine at 2 a.m.  
Use it copy-paste if needed, but the real value is understanding bar-zero behavior, warm-up effects, and runtime constraints before they surprise you in live charts.

## Features (with mild sarcasm, still useful)

- **Mathematically grounded implementations**: aligned with canonical definitions, not folklore copied from a forum thread with three rocket emojis.
- **Deterministic initialization**: explicit warm-up behavior instead of ceremonial `na` handling and crossed fingers.
- **Runtime awareness**: notes call out where Pine limitations can turn elegant ideas into expensive chart decorations.
- **Source-first documentation**: docs are expected to match code, so your future self can verify claims without archaeology.
- **Practical engineering bias**: if a method is fast, stable, and explainable, it wins over clever but fragile tricks.

## Repository facts

- Pine source files: **416**
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

## Practical usage (the part where charts meet reality)

1. Open `indicators/` and select the family you actually need (or the one your backtest said looked magical yesterday).
2. Open the linked `.pine` source from the docs page.
3. Use the full script in TradingView, or extract only the function block into your own script.
4. Run on short and long histories to inspect warm-up behavior and stability.
5. If results look too perfect, assume you found either a bug or a future Nobel Prize; statistically, it is the first one.

## Contributing expectations

Contributions should preserve mathematical correctness, deterministic initialization behavior, and runtime efficiency.  
Include concise rationale for algorithmic changes and keep documentation aligned with source.  
If a patch is clever but unverifiable, it is just performance art and will be treated accordingly.

## License

MIT License.
