#!/usr/bin/env python3
import colorama
from colorama import Fore, Style
import blockcypher
from moneywagon import AddressBalance

from forex_python.bitcoin import BtcConverter

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
    #btcaddr = input("Enter an Address:\t")

    #print(str(balance(btcaddr) * eur) + "€")


    fakeBTCamount = 0.0097779
    inve_dirt = fakeBTCamount * eur
    print(str(round(inve_dirt, 2)) + "€")
    inve = 300
    rel = inve_dirt / inve
    if rel > 1:
        #print("You're winning")
        winrate = (rel / 100) * 100
        print(Fore.GREEN + "WIN: " + str(winrate) + "%")
    else:
        #print("Sorry to lose")
        winrate = (rel / 100) * 100
        print(Fore.RED + "LOSE: " + str(winrate) + "%")


if __name__ == '__main__':
    #inve = int(input("Enter invest:\t"))

    #amou = int(input("Calculate actual wallet amount:\t"))

    b = BtcConverter()  # force_decimal=True to get Decimal rates
    b.get_latest_price('EUR')
    #print("1 BTC = " + str(b.get_latest_price('EUR')) + "€")
    bitcoineuroprice = b.get_latest_price('EUR')

    main(bitcoineuroprice)
