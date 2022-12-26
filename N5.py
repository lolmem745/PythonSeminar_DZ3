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


def numInput(message):
    is_ok = True
    while is_ok:
        try:
            number = int(input(f"{message}"))
            is_ok = False
        except ValueError:
            print("Чето не то написал. Давай ещё раз.")
    return number


list = []
number = numInput("Введите число: ")

for i in range(-number, number + 1):
    list.append(fibonacchi(i))
print(list)
