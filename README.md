# QuanTAlib: Technical Indicators Library in Pine Script® v6

![Pine Script v6.0](https://img.shields.io/badge/Pine%20Script-v6.0-blue?style=flat&logo=tradingview&logoColor=white)
![Indicators Done](https://img.shields.io/badge/indicators-103%2F258-orange)

*A begrudgingly assembled heap of technical indicators, duct-taped together for a scripting language so limited, it makes Excel macros look like advanced AI — because apparently, suffering builds character. And also RSI curves.*

## Welcome, young chart wizards

So you've decided to get rich using the arcane arts of Pine Script, huh? Good for you. This repository contains a patchwork quilt of lovingly hand-stitched technical indicators, each written with mathematical precision, begrudging care, and a healthy disdain for PineScript's idea of "features."

Don't worry if you're new to this – odds are high you are. And yes, some of this will look like algebra had a baby with Excel. But stick around. You might just learn something useful. Like how to tell a real trading signal from the emotional damage of a 2am pump-and-dump. Or at least how *not* to blow up your crypto account in Tradingview following some *can't fail* strategy off some Tiktok video.

## What's in the box? (Besides existential dread)

For more information about indicator types and characteristics, see:

- [Trends - Finite Impulse Response](./indicators/trends_FIR/_index.md)
- [Trends - Infinite Impulse Response](./indicators/trends_IIR/_index.md)
- [Oscillators](./indicators/oscillators/_index.md)
- [Momentum Indicators](./indicators/momentum/_index.md)
- [Volatility Indicators](./indicators/volatility/_index.md)
- [Volume Indicators](./indicators/volume/_index.md)
- [Trend Dynamics](./indicators/dynamics/_index.md)
- [Cycles Indicators](./indicators/cycles/_index.md)
- [Price Channels and Bands](./indicators/channels/_index.md)
- [Stop and Reverse Indicators](./indicators/reversals/_index.md)
- [Signal Filters](./indicators/filters/_index.md)
- [Numerics & Statistical Transformations](./indicators/numerics/_index.md)
- [Error Metrics](./indicators/errors/_index.md)

You can also explore [The Complete Master List of All Indicators](./indicators/_index.md) (Warning: Side effects may include widened eyes, sudden trading epiphanies, and the irrational confidence of someone who just discovered MACD for the first time. No refunds.)

## Features (for those who read those)

- **Mathematically Accurate**: These aren't your average forum-copy-paste indicators. No weird hacks, no half-baked logic, and no Reddit-sourced Fibonacci "enhancements" that only work during Mercury retrograde. You're welcome.
- **Optimized Code**: Because every calculation cycle counts when your backtest goes from +2000% to -73% in live trading.
- **Proper Initialization**: No hand-waving with 'na' values or voodoo warm-up tricks. These scripts do it the right way, from bar one.
- **Error Compensation**: FIR, IIR, LOL – if it can be made more accurate, I made it so. If not, I added enough math to make it look accurate until it isn’t. Because numbers matter. Especially when they're wrong.
- **Reasonable Documentation**: When I felt like it, I wrote stuff down. If you're confused, it's either in the docs or your future.
- **MIT Licensed**: Use it, abuse it, fork it, launch a coin named after it. Just don't DM asking for custom work. This is not Fiverr.

## So... how do you use this?

1. Navigate to the `indicators/` folder. Find your poison – sorry, your *indicator*.
2. If you have no idea what you're doing, copy the whole script. If you *think* you do, steal the function block and use it in your masterwork.
3. Paste it into TradingView's editor. If you don't know where that is, you may not be ready. Go back. Train more. Or join a Discord server and pretend you're testing a strategy. Same thing.
4. Apply it to your chart. Watch it do math better than your last three indicators combined. That includes many built-in indicators in PineScript library
5. Shower the dev with Github stars and fame. Not because I care, but because validation keeps me from writing Python again.

## Contributing (if you dare)

I crafted this library during late-night sessions where PineScript and I developed a love-hate relationship. (It's mostly hate. PineScript started it.) My therapist says it’s “growth.” I say it’s syntax errors.

If you're brave enough to contribute, please ensure your PR is cleaner than my coffee mug, more efficient than my sleep schedule, and mathematically sound enough to make your calculus professor weep with joy.

I'll settle for "doesn't crash TradingView" and "actually does what it claims to do." Extra karma if your indicator doesn't give false signals during sideways markets—that's the holy grail we're all pretending exists.

Please don't ask me to make an "indicator that never fails to predict the future." I already made one: it's called "not trading." Patent pending. Also backtested on my dreams.

## License

MIT. Do what you want. Seriously. Start a shady token. Build your own cult. Just don't blame me when the backtest lied to you.
