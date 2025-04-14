# PineScript Technical Indicators Library

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
| **SMA** | Simple MA (the "Hello World" of indicators) | [sma.pine](...) | [Docs](...) |
| **EMA** | Exponential MA – for those who like recursion and regret | [ema.pine](...) | [Docs](...) |
| **DEMA** | Double Exponential MA – because once wasn't enough | [dema.pine](...) | [Docs](...) |
| **TEMA** | Triple Exponential MA – we clearly have a problem | [tema.pine](...) | [Docs](...) |
| **WMA** | Weighted MA – because your candles aren't all equally special | [wma.pine](...) | [Docs](...) |
| **DWMA** | Double Weighted MA – getting ridiculous yet? | [dwma.pine](...) | [Docs](...) |
| **HMA** | Hull MA – deceptively smooth, suspiciously fast, full of FIR dark magic | [hma.pine](...) | [Docs](...) |
| **HEMA** | Hull Exponential MA – when HMA and EMA have a mathematically gifted IIR child | [hema.pine](...) | [Docs](...) |
| **JMA** | Jurik MA – a near-mythical beast forged in the fires of DSP hell | [jma.pine](...) | [Docs](...) |
| **RMA** | Wilder's MA – the special child that RSI likes | [rma.pine](...) | [Docs](...) |
| **TRIMA** | Triangular MA – because your average should be shaped like a Dorito | [trima.pine](...) | [Docs](...) |
| **PWMA** | Pascal Weighted MA – for when your weights should form a perfect bell curve | [pwma.pine](...) | [Docs](...) |
| **EPMA** | Endpoint MA – if you like linear regression but wish it did less | [epma.pine](...) | [Docs](...) |
| **REMA** | Regularized Exponential MA – when your EMA needs anger management | [rema.pine](...) | [Docs](...) |
| **ZLEMA** | Zero Lag Exponential MA – a unicorn | [zlema.pine](...) | [Docs](...) |
| **ZLDEMA** | Zero Lag Double Exponential MA – unicorn with wings | [zldema.pine](...) | [Docs](...) |
| **ZLTEMA** | Triple Zero Lag Exponential MA – unicorn with wings, a sword, and a caffeine addiction | [zltema.pine](...) | [Docs](...) |

## Indicator Classification

| Indicator | Type | Lag | Smoothness | Accuracy | Overshooting | CPU Anger |
|-----------|------|-----|------------|----------|--------------|------------|
| **RMA** | IIR | High | High | Low | Very Low | Low |
| **TRIMA** | FIR | High | Very High | Low | None | Medium |
| **SMA** | FIR | High | High | Low | None | Low |
| **EPMA** | FIR | Medium | Low | Medium | Low | High |
| **WMA** | FIR | Medium | Medium | Medium | None | Medium |
| **PWMA** | FIR | Medium | High | Medium | None | Medium |
| **DWMA** | FIR | Medium | Medium | High | Low | Medium |
| **EMA** | IIR | Medium | Medium | Medium | Low | Low |
| **REMA** | IIR | Medium | Medium-High | Medium-High | Low | Low |
| **DEMA** | IIR | Low | Medium | High | Medium | Medium |
| **TEMA** | IIR | Low | Medium | Very High | High | Medium |
| **HMA** | FIR | Low | Medium-High | High | Medium | High |
| **HEMA** | IIR | Low | High | High | Low | High |
| **ZLEMA** | IIR | Very Low | Low | Very High | Medium | Medium |
| **ZLDEMA** | IIR | Very Low | Very Low | Very High | Medium-High | Medium |
| **ZLTEMA** | IIR | Extremely Low | Very Low | Extremely High | High | High |
| **JMA** | IIR | Extremely Low | High | Very High | Low | Very High |

## Indicator Characteristics (aka: Why Your Backtest Lies)

### **Type**  
There are two kinds of indicators in this world: those that remember too much, and those that forget on purpose. You're either dealing with an obedient filter that operates strictly within its assigned window, or with one that recursively consults its own increasingly blurry past like a wizard staring into a cracked crystal ball.
  - **FIR (Finite Impulse Response)** – Uses a fixed-length memory, doesn't try to predict the future, and behaves like a well-trained dog. Great if you like indicators that mind their business and stay where you left them.
  - **IIR (Infinite Impulse Response)** – Recursive, has "infinite memory" like your ex, and can wander off unexpectedly because it "remembers something from 40 bars ago." Dangerous, unpredictable, fun at parties.

### **Lag**
Lag is that frustrating quality of an indicator that makes it technically correct, but completely useless *in the moment*. Think of it as the indicator equivalent of hindsight — great for telling you what you should've done three trades ago, but nowhere to be found when you're about to FOMO into a green candle.
  - **High Lag** – This indicator waits until the move is basically over before it acts up. But hey, at least it's accurate — sort of like calling the winner of a race two minutes after it ends. It'll draw the right shape and trend... eventually. Just not in time for it to matter unless you're trading with the reflexes of a sloth on Ambien.
  - **Low Lag** – Shows up early, full of energy, probably holding a meme coin and a hot take. These indicators try to predict what's happening *right now*, which means they're often confidently wrong. Expect a flurry of early signals and just as many early regrets — trusting one is like letting a squirrel on Adderall manage your trades.

### **Smoothness**  
The silky illusion that makes an indicator look intelligent when it's really just heavily sedated. This is the property that determines how much your plotted line behaves like a gentle meandering stream—or a drunk squirrel on a sugar high.
  - **High Smoothness** – The line glides across your chart like a figure skater. It's elegant, serene, and completely disconnected from reality. Useful when you need a trend line that won't emotionally destabilize you.
  - **Low Smoothness** – Think seismograph during a Metallica concert. Every price tick is a personal emergency. Useful if you enjoy indicators that yell "BUY!" and "SELL!" every three seconds.

### **Accuracy**  
How easily the indicator freaks out.  
  - **High Accuracy** – Reacts instantly to every tiny price twitch. Great for panic signals.  
  - **Low Accuracy** – Ignores most things. Might still be processing that dip from two weeks ago.

### **Overshooting**  
Overshooting is what happens when your indicator tries to be helpful by aggressively predicting where price *might* go—only to promptly reverse itself in shame once reality kicks in. It's like a weatherman announcing a hurricane and then telling you it's sunny an hour later.
  - **High Overshoot** – High overshoot indicators are bold liars. These indicators like to leap dramatically ahead of price, only to awkwardly walk it back a few bars later. Great for triggering premature entries, existential doubt, and that feeling that the market is gaslighting you.
  - **Low Overshoot** – These are the chill indicators. They don't overreact, don't jump to conclusions, and don't force you into false trades. They also might be too cautious to be useful in fast-moving markets, preferring instead to sip tea while the candles go full chaos mode.

### **CPU Anger**  
  How likely your indicator is to crash PineScript or cause your laptop fan to become a jet engine.  
  - **Low** – Code runs like a dream. Or at least like PineScript was meant to work.  
  - **High** – Congratulations, you've written a GPU stress test in Pine.

## Contributing (if you dare)

I wrote this stuff while cursing PineScript's quirks and limitations. If you want to contribute, be warned: your PR better be clean, efficient, and mathematically legit. Bonus points if it comes with no bugs and solves world hunger.

Please don't ask me to make an "indicator that never fails to predict the future." I already made one: it's called "not trading."

## License

MIT. Do what you want. Seriously. Start a shady token. Build your own cult. Just don't blame me when the backtest lied to you.
