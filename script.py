#!/usr/bin/env python3
import colorama
from colorama import Fore, Style
import blockcypher
from moneywagon import AddressBalance
from forex_python.bitcoin import BtcConverter
import cryptocompare

import numpy as np
import pandas as pd
import yfinance as yf

def balance(addr):
    try:
        total = float(blockcypher.get_total_balance(addr))
        #print("Balance of address wallet " + addr + "is:\t" + str(total))
        return total
    except:
        total = float(AddressBalance().action("btc", addr))
        #print("Balance (€) of address wallet " + addr + " is:\t" + str(total))
        return total


def main(eur):
    inve = 300

    #btcaddr = input("Enter an Address:\t")
    #ethcaddr = "0x3Fd6800B4dD843818A011707D9176371792f7549"
    #inve_dirt = balance(btcaddr) * eur
    #inve_dirt = balance(ethcaddr)
    inve_dirt = 0.0097779 * eur

    rel = inve_dirt / inve
    if rel > 1:
        print(Fore.GREEN + "WIN: " + Fore.RESET + str(rel) + "%")
    else:
        print(Fore.RED + "LOSE: " + Fore.RESET + str(rel) + "%")

    balance_dirty = inve_dirt - inve
    if balance_dirty > 0:
        balance_dirty = "+" + str(round(balance_dirty, 2))
    elif balance_dirty == 0:
        balance_dirty = str(balance_dirty)
    else:
        balance_dirty = "-" + str(round(balance_dirty, 2))

    print("(" + str(inve) + "€) Balance is:\t" + Fore.GREEN + balance_dirty)
    current_winnings = float(balance_dirty.strip("+")) / inve

    if current_winnings > 0:
        print(Fore.GREEN + str(current_winnings))
    else:
        print(Fore.RED + str(current_winnings))


if __name__ == '__main__':
    b = BtcConverter()  # force_decimal=True to get Decimal rates
    b.get_latest_price('EUR')
    print("1 BTC = " + str(round(b.get_latest_price('EUR'), 2)) + "€")
    bitcoineur = b.get_latest_price('EUR')
    dictio1 = cryptocompare.get_price(["BTC", "ETH"], ["EUR", "USD"])
    etheur = str(list(dictio1["ETH"].items())[0]).split(",")[1].strip(")")
    print("1 ETH = " + str(etheur) + "€")
    ethbin = round(float(etheur) / float(bitcoineur), 2)


    #main(bitcoineur)

    data = yf.download(tickers="ETH-USD", period="1d", interval="15m")
    data

    import plotly.graph_objs as go
    fig = go.Figure()
    fig.add_trace(go.Candlestick(x=data.index,
                                 open=data["Open"],
                                 high=data["High"],
                                 low=data["Low"],
                                 close=data["Close"],
                                 name="ethereum market data"))

    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=15, label="15m", step="minute", stepmode="backward"),
                dict(count=45, label="45m", step="minute", stepmode="backward"),
                dict(count=1, label="HTD", step="hour", stepmode="todate"),
                dict(count=6, label="6h", step="hour", stepmode="backward"),
                dict(step="all"),
            ])
        )
    )
    #fig.show()