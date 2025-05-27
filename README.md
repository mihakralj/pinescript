# QuanTAlib: Technical Indicators Library for Pine Script® v6

![Pine Script v6.0](https://img.shields.io/badge/Pine%20Script-v6.0-blue?style=flat&logo=tradingview&logoColor=white)
![Indicators Done](https://img.shields.io/badge/Indicators-218%2F278-blue?style=flat)

*A begrudgingly assembled heap of technical indicators, duct-taped together for a scripting language so limited, it makes Excel macros look like advanced AI — because apparently, suffering builds character. And also RSI curves.*

## Welcome, young chart wizards

So you've decided to get rich using the arcane arts of Pine Script, huh? Good for you. This repository contains a patchwork quilt of lovingly hand-stitched technical indicators, each written with mathematical precision, half-sincere perfectionism, and a deep resentment for Pine Script’s idea of "versioning".

Don't worry if you're new to this – odds are high you are. And yes, some of this will look like algebra had a baby with Excel. But stick around. You might just learn something useful. Like how to separate actual trading logic from the fever dreams of a YouTube crypto-bro who shills "secret indicators" between affiliate links and protein shake ads. Or at least learn how to avoid blowing up your account after copying a strategy named “MoonSniper V8.3 Ultimate” posted by a dude named Kevin420 in the TradingView forums.

## What's in the box? (Besides existential dread)

- [Finite Impulse Response Trends](./indicators/trends_FIR/_index.md)
- [Infinite Impulse Response Trends](./indicators/trends_IIR/_index.md)
- [Oscillators](./indicators/oscillators/_index.md)
- [Momentum Indicators](./indicators/momentum/_index.md)
- [Volatility Indicators](./indicators/volatility/_index.md)
- [Volume Indicators](./indicators/volume/_index.md)
- [Trend Dynamics](./indicators/dynamics/_index.md)
- [Cycles Indicators](./indicators/cycles/_index.md)
- [Price Channels and Bands](./indicators/channels/_index.md)
- [Stop and Reverse Indicators](./indicators/reversals/_index.md)
- [Signal Filters](./indicators/filters/_index.md)
- [Numerics](./indicators/numerics/_index.md)
- [Statistics](./indicators/statistics/_index.md)
- [Error Metrics](./indicators/errors/_index.md)

You can also explore [The Complete Master List of All Indicators](./indicators/_index.md) (Warning: Side effects may include widened eyes, sudden trading epiphanies, and the irrational confidence of someone who just discovered MACD for the first time. No refunds.)

## Features (or: "Why This Library Doesn’t Suck")

- **Mathematically Accurate**: These aren't your average copy-pasta indicators ripped from some rando’s trading post written during a Red Bull crash. No weird hacks, no mystical constants, and absolutely zero Reddit-sourced Fibonacci “enhancements” that only work during Mercury retrograde on a leap year. If you needed magic, go back to tuning MACD with moon phases. You're welcome.
- **Optimized Code**: Every calc cycle counts when your backtest says you're the next Buffet but your live trades scream “please clap.” Wherever possible, indicators are written in O(1) instead of O(n) — which, for the uninitiated, means they run in constant time instead of chugging through each bar like a hungover intern on earnings day. If you're not sure what that means, just know that O(1) is the kind of code that slaps, not drags.
- **Proper Initialization**: No na-filled fakeouts. No warm-up rituals involving ten candles, a goat, and three lines of if bar_index > 100. Just proper initialization from bar one, like your indicators actually graduated basic training and didn’t just wander in from Pine Script kindergarten.
- **Error Compensation**: FIR, IIR, LOL – if it can be made more accurate, I made it so. If not, I added enough math to make it look accurate until it isn’t. Because numbers matter. Especially when they're wrong.
- **Reasonable Documentation**: Some parts are documented. Some aren’t. Consider it a spiritual journey. If you're confused, it's either in the docs, the code, or the stars. Besides, real traders don’t read documentation – they just tweet angrily until someone answers.
- **MIT Licensed**: Use it, abuse it, fork it, launch a tokenized DAO around it. Just don’t DM me asking for “just a quick tweak” or to review your “super secret trading strategy” in broken Pine v2. This isn’t Fiverr, and I’m not your unpaid TA sensei.

## So... how do you use this?

1. Navigate to the `indicators` folder. Find your poison – sorry, your *indicator*.
2. If you have no idea what you're doing, copy the whole script. If you *think* you do, steal the function block and use it in your masterwork.
3. Paste it into TradingView's editor. If you don't know where that is, you may not be ready. Go back. Train more. Or join a Discord server and pretend you're backtesting a strategy by using random numbers. Same thing.
4. Apply it to your chart. Watch it do math better than your last three indicators combined. That includes many built-in indicators in Pine Script library
5. Shower the dev with Github stars and fame. Not because I care, but because validation keeps me from writing Python again.

## Contributing (if you dare)

I crafted this library during late-night sessions where Pine Script and I developed a love-hate relationship. (It's mostly hate. Pine Script started it.) My therapist says it’s “growth.” I say it’s syntax errors.

If you're brave enough to contribute, please ensure your PR is mathematically sound enough to make your calculus professor weep with joy. If implementations sucks, don't worry. I'll settle for "doesn't crash TradingView" and "actually does what it claims to do." Extra karma if your indicator doesn't give false signals during sideways markets—that's the holy grail we're all pretending exists.

Please don't ask me to make an "indicator that never fails to predict the future." I already made one: it's called "not trading." Patent pending. Also backtested on my dreams.

## License

MIT. Do what you want. Seriously. Start a shady token. Build your own cult. Just don't blame me when the backtest lies to you.
