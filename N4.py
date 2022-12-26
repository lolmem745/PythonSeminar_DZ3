number = 342
list = []


def decimalToBinary(num):
    list = []
    while num != 0:
        list.append(str(num % 2))
        num = int(num / 2)
    return list

list = decimalToBinary(number)
list.reverse()
a = "".join(list)
print(a)
