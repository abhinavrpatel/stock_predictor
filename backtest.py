import numpy as np
import math
import talib

# Run requires Quantopian 2

rsi = ta.RSI(timeperiod=20)

from collections import deque

def initialize(context):
    context.stock1 = symbol('VTI') #equity asset
    context.stock2 = symbol('IEI') #bond asset
    context.values1 = deque(maxlen=100)
    context.values2 = deque(maxlen=200)
    context.prevCommand = "Sell"
    set_benchmark(symbol('SPY'))
    schedule_function(func = strategy, date_rule = date_rules.every_day(), time_rule = time_rules.market_open(minutes=30))    
    
def handle_data(context, data):
    pass
    
def strategy(context, data):
    equity = context.stock1
    bond = context.stock2
    rsi_data = rsi(data)    
    rsi_osc = rsi_data[equity]
    context.values1.append(rsi_osc)
    context.values2.append(rsi_osc)
    rsi_sma1 = sum(context.values1)/100
    rsi_sma2 = sum(context.values2)/200
 
    if(rsi_sma1 >= 50 and context.prevCommand == "Sell"):
        context.prevCommand = "Buy"
        order_target(bond, 0.00)
        order_target_percent(equity, 1.00)
        
    elif(rsi_sma1 < rsi_sma2 < 50 and context.prevCommand == "Buy"):
        context.prevCommand = "Sell"
        order_target(equity, 0.00)  
        order_target_percent(bond, 1.00)
        
    record (RSI = rsi_osc)  
    record (Fast_RSI_SMA = rsi_sma1)
    record (Slow_RSI_SMA = rsi_sma2)
    record (Trigger = 50)
    
