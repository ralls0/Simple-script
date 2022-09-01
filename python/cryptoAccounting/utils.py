import os
import sys
import csv
import re
import json
import datetime

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

MON = {'Jan': 1,
       'Feb': 2,
       'Mar': 3,
       'Apr': 4,
       'May': 5,
       'Jun': 6,
       'Jul': 7,
       'Aug': 8,
       'Sep': 9,
       'Oct': 10,
       'Nov': 11,
       'Dec': 12
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

    if platform == 'binance' or platform == 'nexo' or platform == 'cryptocom':
        dateRow = (dateString.split(" "))[0].split('-')
        result = f"{dateRow[2]}/{dateRow[1]}/{dateRow[0]}"

    if platform == 'coinbase':
        dateRow = (dateString.split("T"))[0].split('-')
        result = f"{dateRow[2]}/{dateRow[1]}/{dateRow[0]}"

    if platform == 'uphold':
        dateRow = dateString.split(" ")
        result = f"{dateRow[2]}/{MON[dateRow[1]]}/{dateRow[3]}"

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
