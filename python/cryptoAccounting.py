import os
import sys
import csv
from tokenize import Double
from typing import List
import re

CELSIUSFILE = os.getenv('CELSIUS_FILE')
BINANCEFILE = os.getenv('BINANCE_FILE')
YEAR = int(os.getenv('YEAR_CRYPTO'))

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


def yearFilter(fileList: List):
    pass


def handleCelsiusFile(fileList: List, headerFile: List, dateCheck: str = ""):
    coins = {}
    ttn = 0
    datn = 0
    usdvn = 0
    ctn = 0

    # Cerco il cambo 'Transaction type' in che posizione si trova della lista
    for n, e in enumerate(headerFile):
        if e == 'Transaction type':
            ttn = n
        if e == 'Date and time':
            datn = n
        if e == 'USD Value':
            usdvn = n
        if e == 'Coin type':
            ctn = n

    # Per ogni riga controllo se è prima del dateCheck (ammesso che ci sia il dataCheck)
    # Se si tratta di una:
    # - Promo Code Reward
    # - Reward
    # sommiamo il valore
    # Se si tratta di una 'Transfer' sommiamo e inseriamo un inizio
    for row in fileList:
        dateRow = [re.sub('[^A-Za-z0-9]+', '', x)
                   for x in row[datn].split(" ")]
        dateRow = f"{dateRow[1]}/{MONTH[dateRow[0]]}/{dateRow[2]}"
        if dateCheck == "" or dateRow < dateCheck:
            if row[ttn] == 'Transfer':
                coins['Transfer'] = coins.get(
                    'Transfer', 0.0) + float(row[usdvn])
                coins['Ammount'] = coins.get(
                    'Ammount', 0.0) + float(row[usdvn])
            if row[ttn] == 'Reward' or row[ttn] == 'Promo Code Reward' or row[ttn] == 'Referred Award':
                coins['Ammount'] = coins.get(
                    'Ammount', 0.0) + float(row[usdvn])
            # TODO: per ogni coin il suo ammount e valore
    return coins


def handleFile(fileList: List):
    headerFile = fileList[0]
    fileList.remove(headerFile)
    celsiusCoins = handleCelsiusFile(fileList, headerFile)
    print(celsiusCoins)


if __name__ == "__main__":
    fileList = openFile(CELSIUSFILE)
    handleFile(fileList)
