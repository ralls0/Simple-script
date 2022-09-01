import os
import sys
import utils
import binance
import celsius
import nexo
import coinbase
import cryptocom
import uphold

CELSIUSFILE = os.getenv('CELSIUS_FILE')
BINANCEFILE = os.getenv('BINANCE_FILE')
NEXOFILE = os.getenv('NEXO_FILE')
COINBASEFILE = os.getenv('COINBASE_FILE')
CRYPTOCOMFILE = os.getenv('CRYPTOCOM_FILE')
UPHOLDFILE = os.getenv('UPHOLD_FILE')

if __name__ == "__main__":
    fileList = {}
    fileList['celsius'] = utils.openFile(CELSIUSFILE)
    fileList['binance'] = utils.openFile(BINANCEFILE)
    fileList['nexo'] = utils.openFile(NEXOFILE)
    fileList['coinbase'] = utils.openFile(COINBASEFILE)
    fileList['cryptocom'] = utils.openFile(CRYPTOCOMFILE)
    fileList['uphold'] = utils.openFile(UPHOLDFILE)
    celsius.handleCelsiusFile(fileList['celsius'])
    binance.handleBinanceFile(fileList['binance'])
    nexo.handleNexoFile(fileList['nexo'])
    coinbase.handleCoinbaseFile(fileList['coinbase'])
    cryptocom.handleCryptoComFile(fileList['cryptocom'])
    uphold.handleUpholdFile(fileList['uphold'])
