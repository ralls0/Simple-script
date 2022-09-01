import utils
import json

def handleBinanceFile(fileList: list):
    headerFile = fileList[0]
    fileList.remove(headerFile)
    binanceCoins = getBinanceTransaction(fileList, headerFile)
    print("#### Binance ####", json.dumps(binanceCoins, indent=2),
          json.dumps(utils.getCoinAmmount(binanceCoins), indent=2))

def getBinanceTransaction(fileList: list, headerFile: list):
    transactions = {}
    transactionTypeListNum = 0
    dateTimeListNum = 0
    # usdValueListNum = 0
    coinTypeListNum = 0
    coinAmmountListNum = 0
    accountListNum = 0

    for n, e in enumerate(headerFile):
        if e == 'Operation':
            transactionTypeListNum = n
        if e == 'UTC_Time':
            dateTimeListNum = n
        # if e == 'USD Value':
        #     usdValueListNum = n
        if e == 'Coin':
            coinTypeListNum = n
        if e == 'Change':
            coinAmmountListNum = n
        if e == 'Account':
            accountListNum = n

    for row in fileList:
        # Trasformo la data nel formato gg/mm/aaaa
        dateRow = utils.getDate(row[dateTimeListNum], 'binance')

        transactions[dateRow] = transactions.get(
            dateRow, {})

        # if row[accountListNum] != 'Savings' or row[transactionTypeListNum] == 'Savings Interest':
        # if row[transactionTypeListNum] != 'Savings Principal redemption':
        if row[accountListNum] != 'Savings':
            transactions[dateRow][row[coinTypeListNum]] = transactions[dateRow].get(
                row[coinTypeListNum], 0.0) + float(row[coinAmmountListNum])

    return transactions