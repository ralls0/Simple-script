import utils
import json


def handleCryptoComFile(fileList: list):
    headerFile = fileList[0]
    fileList.remove(headerFile)
    cryptocomCoins = getCryptoComTransaction(fileList, headerFile)
    print("#### Crypro.com ####", json.dumps(cryptocomCoins, indent=2),
          json.dumps(utils.getAmmount(cryptocomCoins), indent=2),
          json.dumps(utils.getCoinAmmount(cryptocomCoins), indent=2))


def getCryptoComTransaction(fileList: list, headerFile: list):
    transactions = {}
    transactionTypeListNum = 0
    dateTimeListNum = 0
    usdValueListNum = 0
    coinTypeListNum = 0
    coinAmmountListNum = 0
    coinTypeEListNum = 0
    ammEListNum = 0

    for n, e in enumerate(headerFile):
        if e == 'Transaction Kind':
            transactionTypeListNum = n
        if e == 'Timestamp (UTC)':
            dateTimeListNum = n
        if e == 'To Currency':
            coinTypeEListNum = n
        if e == 'To Amount':
            ammEListNum = n
        if e == 'Native Amount (in USD)':
            usdValueListNum = n
        if e == 'Currency':
            coinTypeListNum = n
        if e == 'Amount':
            coinAmmountListNum = n

    for row in fileList:
        # Trasformo la data nel formato gg/mm/aaaa
        dateRow = utils.getDate(row[dateTimeListNum], 'cryptocom')

        transactions[dateRow] = transactions.get(
            dateRow, {})

        if row[transactionTypeListNum] == 'referral_card_cashback' or row[transactionTypeListNum] == 'reimbursement' or row[transactionTypeListNum] == 'crypto_earn_interest_paid' or row[transactionTypeListNum] == 'crypto_deposit':
            transactions[dateRow]['ammount'] = transactions[dateRow].get(
                'ammount', 0.0) + float(row[usdValueListNum])
            transactions[dateRow][row[coinTypeListNum]] = transactions[dateRow].get(
                row[coinTypeListNum], 0.0) + float(row[coinAmmountListNum])

        if row[transactionTypeListNum] == 'crypto_withdrawal' or row[transactionTypeListNum] == 'card_top_up' or row[transactionTypeListNum] == 'crypto_payment':
            transactions[dateRow]['ammount'] = transactions[dateRow].get(
                'ammount', 0.0) - float(row[usdValueListNum])
            transactions[dateRow][row[coinTypeListNum]] = transactions[dateRow].get(
                row[coinTypeListNum], 0.0) + float(row[coinAmmountListNum])

        if row[transactionTypeListNum] == 'crypto_exchange':
            transactions[dateRow][row[coinTypeListNum]] = transactions[dateRow].get(
                row[coinTypeListNum], 0.0) + float(row[coinAmmountListNum])
            transactions[dateRow][row[coinTypeEListNum]] = transactions[dateRow].get(
                row[coinTypeEListNum], 0.0) + float(row[ammEListNum])

        if row[transactionTypeListNum] == 'crypto_purchase':
            transactions[dateRow]['transfer'] = transactions[dateRow].get(
                'transfer', 0.0) + float(row[usdValueListNum])
            transactions[dateRow]['ammount'] = transactions[dateRow].get(
                'ammount', 0.0) + float(row[usdValueListNum])
            transactions[dateRow][row[coinTypeListNum]] = transactions[dateRow].get(
                row[coinTypeListNum], 0.0) + float(row[coinAmmountListNum])

    return transactions
