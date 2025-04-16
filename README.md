# PineScript Technical Indicators Library

![Pine Script v6.0](https://img.shields.io/badge/Pine%20Script-v6.0-blue?style=flat&logo=tradingview&logoColor=white)

*A begrudgingly assembled pile of technical indicators, duct-taped together for a scripting language so limited, it makes Excel macros look like advanced AI. Written in PineScript — because apparently, suffering builds character.*

## Welcome, young chart wizards

So you've decided to get rich using the arcane arts of Pine Script, huh? Good for you. This repository contains a patchwork quilt of lovingly hand-stitched technical indicators, each written with mathematical precision, begrudging care, and a healthy disdain for PineScript's idea of "features."

Don't worry if you're new to this – odds are high you are. And yes, some of this will look like algebra had a baby with Excel. But stick around. You might just learn something useful. Or at least how *not* to blow up your crypto account in Tradingview with some *can't fail* strategy off some Tiktok video.

## Features (for those who read those)

- **Mathematically Accurate**: These aren't your average forum-copy-paste indicators. They're implemented as intended by people who know their FIRs from their IIRs. You're welcome.
- **Optimized Code**: Because every millisecond counts when your backtest goes from +2000% to -73% in live trading.
- **Proper Initialization**: No hand-waving with 'na' values or voodoo warm-up tricks. These scripts do it the right way, from bar one.
- **Error Compensation**: FIR, IIR, LOL – if it can be made more accurate, I made it so. Because numbers matter. Especially when they're wrong.
- **Reasonable Documentation**: When I felt like it, I wrote stuff down. If you're confused, it's either in the docs or your future.
- **MIT Licensed**: Use it, abuse it, fork it, launch a coin named after it. Just don't DM asking for custom work. This is not Fiverr.

## So... how do you use this?

1. Navigate to the `indicators/` folder. Find your poison – sorry, your *indicator*.
2. If you have no idea what you're doing, copy the whole script. If you *think* you do, steal the function block and use it in your masterwork.
3. Paste it into TradingView's editor. If you don't know where that is, you may not be ready. Go back. Train more.
4. Apply it to your chart. Watch it do math better than your last three indicators combined. That includes many built-in indicators in PineScript library
5. Shower the dev with Github stars and fame. Not because I care, but because validation keeps me from writing Python again.

## What's in the box? (Besides existential dread)

### Averages & Trends

| Indicator | Description | Implementation | Documentation |
|-----------|-------------|----------------|----------------|
| **SMA** | Simple MA - the indicator equivalent of using a calculator to add 2+2 | [sma.pine](indicators/trends/sma.pine) | [Docs](docs/trends/sma.md) |
| **EMA** | Exponential MA – for those who like recursion and regret | [ema.pine](indicators/trends/ema.pine) | [Docs](docs/trends/ema.md) |
| **DEMA** | Double Exponential MA – for traders who think "if one recursion is good, two must be better" | [dema.pine](indicators/trends/dema.pine) | [Docs](docs/trends/dema.md) |
| **TEMA** | Triple Exponential MA – when you're so afraid of lag you'll accept mathematical hallucinations instead | [tema.pine](indicators/trends/tema.pine) | [Docs](docs/trends/tema.md) |
| **QEMA** | Quadruple Exponential MA – congratulations, we've mathematically engineered a seizure detector | [qema.pine](indicators/trends/qema.pine) | [Docs](docs/trends/qema.md) |
| **WMA** | Weighted MA – treating recent candles like the favorite children they are | [wma.pine](indicators/trends/wma.pine) | [Docs](docs/trends/wma.md) |
| **DWMA** | Double Weighted MA – twice the math for roughly the same result, because reasons | [dwma.pine](indicators/trends/dwma.pine) | [Docs](docs/trends/dwma.md) |
| **ZLEMA** | Zero Lag Exponential MA – a unicorn | [zlema.pine](indicators/trends/zlema.pine) | [Docs](docs/trends/zlema.md) |
| **ZLDEMA** | Zero Lag Double Exponential MA – a unicorn with wings | [zldema.pine](indicators/trends/zldema.pine) | [Docs](docs/trends/zldema.md) |
| **ZLTEMA** | Triple Zero Lag Exponential MA – a unicorn with wings, a sword, and a caffeine addiction | [zltema.pine](indicators/trends/zltema.pine) | [Docs](docs/trends/zltema.md) |
| **RMA** | Wilder's MA – moves so slowly it makes government bureaucracy look efficient | [rma.pine](indicators/trends/rma.pine) | [Docs](docs/trends/rma.md) |
| **HMA** | Hull MA – the sports car of moving averages: flashy, fast, and prone to crashes | [hma.pine](indicators/trends/hma.pine) | [Docs](docs/trends/hma.md) |
| **HWMA** | Holt-Winters MA – treating market cycles like seasons, then acting surprised when winter comes in July | [hwma.pine](indicators/trends/hwma.pine) | [Docs](docs/trends/hwma.md) |
| **HEMA** | Hull Exponential MA – when HMA and EMA have a mathematically gifted IIR child | [hema.pine](indicators/trends/hema.pine) | [Docs](docs/trends/hema.md) |
| **JMA** | Jurik MA – an algorithm so complex even its creator probably questions why the hell | [jma.pine](indicators/trends/jma.pine) | [Docs](docs/trends/jma.md) |
| **EPMA** | Endpoint MA – linear regression's lazy cousin who showed up just for the trend line | [epma.pine](indicators/trends/epma.pine) | [Docs](docs/trends/epma.md) |
| **SINEMA** | Sine-weighted MA – an indicator that rides waves of data like a mathematical surfer | [sinema.pine](indicators/trends/sinema.pine) | [Docs](docs/trends/sinema.md) |
| **TRIMA** | Triangular MA –  because nothing says "I understand math" like averaging an average | [trima.pine](indicators/trends/trima.pine) | [Docs](docs/trends/trima.md) |
| **PWMA** | Pascal Weighted MA – using 17th century math to lose money with 21st century efficiency | [pwma.pine](indicators/trends/pwma.pine) | [Docs](docs/trends/pwma.md) |
| **REMA** | Regularized Exponential MA –  an EMA that went to therapy and learned to stop overreacting | [rema.pine](indicators/trends/rema.pine) | [Docs](docs/trends/rema.md) |
| **ALMA** | Arnaud Legoux MA – a Gaussian distribution curve decided to trade stocks while wearing a beret and smoking Gauloises | [alma.pine](indicators/trends/alma.pine) | [Docs](docs/trends/alma.md) |
| **KAMA** | Kaufman's Adaptive MA – the chameleon of moving averages that changes its personality more than your ex | [kama.pine](indicators/trends/kama.pine) | [Docs](docs/trends/kama.md) |

### Errors

| Error | Description | Implementation | Documentation |
|-----------|-------------|----------------|----------------|
| **HUBER** | Huber Loss - the diplomatic negotiator that cares deeply about small errors but refuses to completely melt down over outliers | [huber.pine](indicators/errors/huber.pine) | [Docs](docs/errors/huber.md) |
| **MAE** | Mean Absolute Error - treats all trading mistakes equally, just like I treat my children (at least that's what I tell them) | [mae.pine](indicators/errors/mae.pine) | [Docs](docs/errors/mae.md) |
| **MSE** | Mean Squared Error - for when big mistakes haunt exponentially more than small ones | [mse.pine](indicators/errors/mse.pine) | [Docs](docs/errors/mse.md) |
| **MAPD** | Mean Absolute Percentage Deviation - because expressing failure as a percentage somehow makes it feel more scientific | [mapd.pine](indicators/errors/mapd.pine) | [Docs](docs/errors/mapd.md) |
| **MAPE** | Mean Absolute Percentage Error - perfect for quantifying disappointment in neat little percentage points | [mape.pine](indicators/errors/mape.pine) | [Docs](docs/errors/mape.md) |
| **MASE** | Mean Absolute Scaled Error - compares current disasters to previous ones and calls it "progress" | [mase.pine](indicators/errors/mase.pine) | [Docs](docs/errors/mase.md) |
| **MPE** | Mean Percentage Error - allows positive and negative errors to cancel out, like profits and losses, but brokers still charges fees for both | [mpe.pine](indicators/errors/mpe.pine) | [Docs](docs/errors/mpe.md)

## Documentation

For detailed information about indicator types and characteristics, see:

- [Indicators Classification](docs/classification.md)
- [Wishlist](docs/wishlist.md)

## Contributing (if you dare)

I wrote this stuff while cursing PineScript's quirks and limitations. If you want to contribute, be warned: your PR better be clean, efficient, and mathematically legit. Bonus points if it comes with no bugs and solves world hunger.

Please don't ask me to make an "indicator that never fails to predict the future." I already made one: it's called "not trading."

## License

MIT. Do what you want. Seriously. Start a shady token. Build your own cult. Just don't blame me when the backtest lied to you.
