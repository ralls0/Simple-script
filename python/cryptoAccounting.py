import os
import sys
import csv
import re
import json
import datetime

CELSIUSFILE = os.getenv('CELSIUS_FILE')
BINANCEFILE = os.getenv('BINANCE_FILE')

MONTH = {'January': 1,
         'February': 2,
         'March': 3,
         'April': 4,
         'May': 5,
         'June': 6,
         'July': 7,
         'August': 8,
         'September': 9,
         'October': 10,
         'November': 11,
         'December': 12
         }


def openFile(filePath: str):
    fileList = []
    with open(filePath, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in spamreader:
            fileList.append(row)
    return fileList


def getDate(dateString: str, platform: str):
    result = ""
    if platform == 'celsius':
        dateRow = [re.sub('[^A-Za-z0-9]+', '', x)
                   for x in dateString.split(" ")]
        result = f"{dateRow[1]}/{MONTH[dateRow[0]]}/{dateRow[2]}"
    if platform == 'binance':
        dateRow = (dateString.split(" "))[0].split('-')
        result = f"{dateRow[2]}/{dateRow[1]}/{dateRow[0]}"
    return result


def getCoinAmmount(transactions: dict, dateCheck: str = ""):
    result = {}
    transactionKeys = transactions.keys()
    for k in transactionKeys:
        if dateCheck == "" or datetime.datetime.strptime(k, "%d/%m/%Y") <= datetime.datetime.strptime(dateCheck, "%d/%m/%Y"):
            coinKeys = transactions[k].keys()
            for c in coinKeys:
                if c != 'ammount' and c != 'transfer':
                    result[c] = result.get(
                        c, 0.0) + transactions[k].get(c, 0.0)
    resultKeys = result.keys()
    delKeys = []
    for r in resultKeys:
        if result[r] < 1e-5:
            delKeys.append(r)

    for r in delKeys:
        del result[r]

    return result


def getAmmount(transactions: dict, dateCheck: str = ""):
    result = {'ammount': 0.0, 'transfer': 0.0}
    transactionKeys = transactions.keys()
    for k in transactionKeys:
        if dateCheck == "" or datetime.datetime.strptime(k, "%d/%m/%Y") <= datetime.datetime.strptime(dateCheck, "%d/%m/%Y"):
            result['ammount'] = result.get(
                'ammount', 0.0) + transactions[k].get('ammount', 0.0)
            result['transfer'] = result.get(
                'transfer', 0.0) + transactions[k].get('transfer', 0.0)

    return result


def getCelsiusTransaction(fileList: list, headerFile: list):
    transactions = {}
    transactionTypeListNum = 0
    dateTimeListNum = 0
    usdValueListNum = 0
    coinTypeListNum = 0
    coinAmmountListNum = 0

    for n, e in enumerate(headerFile):
        if e == 'Transaction type':
            transactionTypeListNum = n
        if e == 'Date and time':
            dateTimeListNum = n
        if e == 'USD Value':
            usdValueListNum = n
        if e == 'Coin type':
            coinTypeListNum = n
        if e == 'Coin amount':
            coinAmmountListNum = n

    for row in fileList:
        # Trasformo la data nel formato gg/mm/aaaa
        dateRow = getDate(row[dateTimeListNum], 'celsius')

        transactions[dateRow] = transactions.get(
            dateRow, {})

        if row[transactionTypeListNum] == 'Transfer':
            transactions[dateRow]['transfer'] = transactions[dateRow].get(
                'transfer', 0.0) + float(row[usdValueListNum])
            transactions[dateRow]['ammount'] = transactions[dateRow].get(
                'ammount', 0.0) + float(row[usdValueListNum])
            transactions[dateRow][row[coinTypeListNum]] = transactions[dateRow].get(
                row[coinTypeListNum], 0.0) + float(row[coinAmmountListNum])

        if row[transactionTypeListNum] == 'Reward' or row[transactionTypeListNum] == 'Promo Code Reward' or row[transactionTypeListNum] == 'Referred Award':
            transactions[dateRow]['ammount'] = transactions[dateRow].get(
                'ammount', 0.0) + float(row[usdValueListNum])
            transactions[dateRow][row[coinTypeListNum]] = transactions[dateRow].get(
                row[coinTypeListNum], 0.0) + float(row[coinAmmountListNum])
    return transactions


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
        dateRow = getDate(row[dateTimeListNum], 'binance')

        transactions[dateRow] = transactions.get(
            dateRow, {})

        # if row[accountListNum] != 'Savings' or row[transactionTypeListNum] == 'Savings Interest':
        # if row[transactionTypeListNum] != 'Savings Principal redemption':
        if row[accountListNum] != 'Savings':
            transactions[dateRow][row[coinTypeListNum]] = transactions[dateRow].get(
                row[coinTypeListNum], 0.0) + float(row[coinAmmountListNum])

    return transactions


def handleCelsiusFile(fileList: list):
    headerFile = fileList[0]
    fileList.remove(headerFile)
    celsiusCoins = getCelsiusTransaction(fileList, headerFile)
    print(json.dumps(celsiusCoins, indent=2),
          json.dumps(getAmmount(celsiusCoins, "5/3/2021"), indent=2))


def handleBinanceFile(fileList: list):
    headerFile = fileList[0]
    fileList.remove(headerFile)
    binanceCoins = getBinanceTransaction(fileList, headerFile)
    print(json.dumps(binanceCoins, indent=2),
          json.dumps(getCoinAmmount(binanceCoins), indent=2))


if __name__ == "__main__":
    fileList = {}
    fileList['celsius'] = openFile(CELSIUSFILE)
    fileList['binance'] = openFile(BINANCEFILE)
    # handleCelsiusFile(fileList['celsius'])
    handleBinanceFile(fileList['binance'])
