def fibonacchi(num):
    if num >= 0:
        if num == 0:
            return 0
        if num == 1:
            return 1
        else:
            return fibonacchi(num - 1) + fibonacchi(num - 2)
    else:
        return fibonacchi(num + 2) - fibonacchi(num + 1)


list = []
number = 8

for i in range(-number, number + 1):
    list.append(fibonacchi(i))
print(list)
