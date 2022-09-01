import utils
import json


def handleUpholdFile(fileList: list):
    headerFile = fileList[0]
    fileList.remove(headerFile)
    upholdCoins = getUpholdTransaction(fileList, headerFile)
    print("#### Uphold ####", json.dumps(upholdCoins, indent=2),
          json.dumps(utils.getAmmount(upholdCoins), indent=2),
          json.dumps(utils.getCoinAmmount(upholdCoins), indent=2))


def getUpholdTransaction(fileList: list, headerFile: list):
    transactions = {}
    transactionTypeListNum = 0
    dateTimeListNum = 0
    # usdValueListNum = 0
    coinTypeListNum = 0
    coinAmmountListNum = 0
    coinTypeEListNum = 0
    ammEListNum = 0

    for n, e in enumerate(headerFile):
        if e == 'Type':
            transactionTypeListNum = n
        if e == 'Date':
            dateTimeListNum = n
        if e == 'Destination Currency':
            coinTypeEListNum = n
        if e == 'Destination Amount':
            ammEListNum = n
        if e == 'Origin Currency':
            coinTypeListNum = n
        if e == 'Origin Amount':
            coinAmmountListNum = n

    for row in fileList:
        # Trasformo la data nel formato gg/mm/aaaa
        dateRow = utils.getDate(row[dateTimeListNum], 'uphold')

        transactions[dateRow] = transactions.get(
            dateRow, {})

        if row[transactionTypeListNum] == 'in':
            transactions[dateRow][row[coinTypeListNum]] = transactions[dateRow].get(
                row[coinTypeListNum], 0.0) + float(row[coinAmmountListNum])

        if row[transactionTypeListNum] == 'out':
            transactions[dateRow][row[coinTypeListNum]] = transactions[dateRow].get(
                row[coinTypeListNum], 0.0) - float(row[coinAmmountListNum])

        if row[transactionTypeListNum] == 'transfer':
            transactions[dateRow][row[coinTypeListNum]] = transactions[dateRow].get(
                row[coinTypeListNum], 0.0) - float(row[coinAmmountListNum])
            transactions[dateRow][row[coinTypeEListNum]] = transactions[dateRow].get(
                row[coinTypeEListNum], 0.0) + float(row[ammEListNum])

    return transactions
