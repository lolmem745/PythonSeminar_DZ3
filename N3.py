def decimalGet(anylist):
    templist = []
    for i in range(0, len(anylist)):
        templist.append(round(anylist[i] % 1, 10))
    templist = [x for x in templist if x != 0]
    return templist


def findDecimalDiff(anylist):
    res = max(anylist) - min(anylist)
    return res


list = [1.1, 1.2, 3.1, 5, 10.01, 1.93, 2.4]


reslist = decimalGet(list)
result = findDecimalDiff(reslist)
print(result)
