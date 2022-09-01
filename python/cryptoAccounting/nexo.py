import utils
import json

def handleNexoFile(fileList: list):
    headerFile = fileList[0]
    fileList.remove(headerFile)
    nexoCoins = getNexoTransaction(fileList, headerFile)
    print("#### Nexo ####", json.dumps(nexoCoins, indent=2),
          json.dumps(utils.getAmmount(nexoCoins), indent=2),
          json.dumps(utils.getCoinAmmount(nexoCoins), indent=2))

def getNexoTransaction(fileList: list, headerFile: list):
    transactions = {}
    transactionTypeListNum = 0
    dateTimeListNum = 0
    usdValueListNum = 0
    coinTypeListNum = 0
    coinAmmountListNum = 0

    for n, e in enumerate(headerFile):
        if e == 'Type':
            transactionTypeListNum = n
        if e == 'Date / Time':
            dateTimeListNum = n
        if e == 'USD Equivalent':
            usdValueListNum = n
        if e == 'Output Currency':
            coinTypeListNum = n
        if e == 'Output Amount':
            coinAmmountListNum = n

    for row in fileList:
        # Trasformo la data nel formato gg/mm/aaaa
        dateRow = utils.getDate(row[dateTimeListNum], 'nexo')

        transactions[dateRow] = transactions.get(
            dateRow, {})

        if row[transactionTypeListNum] == 'DepositToExchange':
            transactions[dateRow]['transfer'] = transactions[dateRow].get(
                'transfer', 0.0) + float(row[usdValueListNum])
            transactions[dateRow]['ammount'] = transactions[dateRow].get(
                'ammount', 0.0) + float(row[usdValueListNum])
            transactions[dateRow][row[coinTypeListNum]] = transactions[dateRow].get(
                row[coinTypeListNum], 0.0) + float(row[coinAmmountListNum])

        if row[transactionTypeListNum] == 'Interest' or row[transactionTypeListNum] == 'FixedTermInterest':
            transactions[dateRow]['ammount'] = transactions[dateRow].get(
                'ammount', 0.0) + float(row[usdValueListNum])
            transactions[dateRow][row[coinTypeListNum]] = transactions[dateRow].get(
                row[coinTypeListNum], 0.0) + float(row[coinAmmountListNum])
    return transactions