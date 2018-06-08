# Trading Rules

SMA100(RSI20) cross> 50 = sell $IEI + buy $VTI
SMA200(RSI20) cross< 50 = sell $VTI + buy $IEI

This simple momentum algorithm uses a 100-day SMA of the 20-day RSI for $VTI to trigger buy signals and a 200-day SMA of the 20-day RSI to trigger sell signals. When a sell signal is triggered, the algorithm rotates out of $VTI and into $IEI until a new buy signal is generated, at which point it will rotate out of $IEI and back into $VTI. I consider this a semi-passive strategy that combines long-term buy-and-hold with a tactical overlay to potentially avoid major market corrections.

The concept behind this strategy is as follows:

1) Mathematically speaking, an RSI reading above 50 indicates positive trailing momentum and a reading below 50 indicates negative trailing momentum. Most momentum traders like to buy when the RSI is "oversold" at 30 and sell when the RSI is "overbought" at 70. This, however, is inappropriate (and downright dangerous) because it is a mean-reversion trade technique, not a momentum technique. To better apply the RSI for a momentum strategy, it is better to use 50 as the buy/sell trigger.

2) The RSI by itself is too "noisy," meaning it crosses above and below 50 too often, generating many false trade signals in the process. In order to remedy this problem, you can smooth out the RSI using an SMA or EMA. A smoothed RSI is less noisy but it does tend to lag more.

3) Using a faster smoothed RSI to buy can capture positive momentum earlier and using a slower smoothed RSI to sell can avoid under-performance caused by minor corrections.
