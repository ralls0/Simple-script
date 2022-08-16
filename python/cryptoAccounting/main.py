import os
import sys
import json
import datetime
import utils
import binance
import celsius

CELSIUSFILE = os.getenv('CELSIUS_FILE')
BINANCEFILE = os.getenv('BINANCE_FILE')

if __name__ == "__main__":
    fileList = {}
    # fileList['celsius'] = utils.openFile(CELSIUSFILE)
    fileList['binance'] = utils.openFile(BINANCEFILE)
    # celsius.handleCelsiusFile(fileList['celsius'])
    binance.handleBinanceFile(fileList['binance'])
