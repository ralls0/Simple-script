import utils
import json


def handleCoinbaseFile(fileList: list):
    headerFile = fileList[0]
    fileList.remove(headerFile)
    coinbaseCoins = getCoinbaseTransaction(fileList, headerFile)
    print("#### Coinbase ####", json.dumps(coinbaseCoins, indent=2),
          json.dumps(utils.getAmmount(coinbaseCoins), indent=2),
          json.dumps(utils.getCoinAmmount(coinbaseCoins), indent=2))

def getCoinbaseTransaction(fileList: list, headerFile: list):
    transactions = {}
    transactionTypeListNum = 0
    dateTimeListNum = 0
    usdValueListNum = 0
    coinTypeListNum = 0
    coinAmmountListNum = 0
    notesListNum = 0

    for n, e in enumerate(headerFile):
        if e == 'Transaction Type':
            transactionTypeListNum = n
        if e == 'Timestamp':
            dateTimeListNum = n
        if e == 'Total (inclusive of fees)':
            usdValueListNum = n
        if e == 'Asset':
            coinTypeListNum = n
        if e == 'Quantity Transacted':
            coinAmmountListNum = n
        if e == 'Notes':
            notesListNum = n

    for row in fileList:
        # Trasformo la data nel formato gg/mm/aaaa
        dateRow = utils.getDate(row[dateTimeListNum], 'coinbase')

        transactions[dateRow] = transactions.get(
            dateRow, {})

        if row[transactionTypeListNum] == 'Receive':
            # transactions[dateRow]['transfer'] = transactions[dateRow].get(
            #     'transfer', 0.0) + float(row[usdValueListNum])
            # transactions[dateRow]['ammount'] = transactions[dateRow].get(
            #     'ammount', 0.0) + float(row[usdValueListNum])
            transactions[dateRow][row[coinTypeListNum]] = transactions[dateRow].get(
                row[coinTypeListNum], 0.0) + float(row[coinAmmountListNum])

        if row[transactionTypeListNum] == 'Send':
            # transactions[dateRow]['ammount'] = transactions[dateRow].get(
            #     'ammount', 0.0) - float(row[usdValueListNum])
            transactions[dateRow][row[coinTypeListNum]] = transactions[dateRow].get(
                row[coinTypeListNum], 0.0) - float(row[coinAmmountListNum])

        if row[transactionTypeListNum] == 'Sell':
            transactions[dateRow][row[coinTypeListNum]] = transactions[dateRow].get(
                row[coinTypeListNum], 0.0) - float(row[coinAmmountListNum])
            transactions[dateRow]['USD'] = transactions[dateRow].get(
                'USD', 0.0) + float(row[usdValueListNum])

        if row[transactionTypeListNum] == 'Buy':
            transactions[dateRow][row[coinTypeListNum]] = transactions[dateRow].get(
                row[coinTypeListNum], 0.0) + float(row[coinAmmountListNum])
            transactions[dateRow]['USD'] = transactions[dateRow].get(
                'USD', 0.0) - float(row[usdValueListNum])

        if row[transactionTypeListNum] == 'Coinbase Earn':
            # transactions[dateRow]['ammount'] = transactions[dateRow].get(
            #     'ammount', 0.0) + float(row[usdValueListNum])
            transactions[dateRow][row[coinTypeListNum]] = transactions[dateRow].get(
                row[coinTypeListNum], 0.0) + float(row[coinAmmountListNum])

        if row[transactionTypeListNum] == 'Convert':
            transactions[dateRow][row[coinTypeListNum]] = transactions[dateRow].get(
                row[coinTypeListNum], 0.0) - float(row[coinAmmountListNum])
            notes = (row[notesListNum].split(' to ')[1]).split(' ')
            transactions[dateRow][notes[1]] = transactions[dateRow].get(
                notes[1], 0.0) - float(notes[0])

    return transactions