import utils
import json

def handleCelsiusFile(fileList: list):
    headerFile = fileList[0]
    fileList.remove(headerFile)
    celsiusCoins = getCelsiusTransaction(fileList, headerFile)
    print("#### Celsius ####", json.dumps(celsiusCoins, indent=2),
          json.dumps(utils.getAmmount(celsiusCoins), indent=2),
          json.dumps(utils.getCoinAmmount(celsiusCoins), indent=2))

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
        dateRow = utils.getDate(row[dateTimeListNum], 'celsius')

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