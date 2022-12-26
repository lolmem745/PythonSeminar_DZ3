list = [1, 2, 3, 4, 5, 6, 7, 8]
reslist = []
for i in range(0, int(len(list) / 2)):
    reslist.append(list[i] * list[len(list) - i - 1])   # Перемножение элементов с двух концов
if int(len(list) % 2) != 0:
    reslist.append(list[int(len(list) / 2)] * list[int(len(list) / 2)]) # Если элементов нечетное количество, то возводим в квадрат элемент в середине
print(reslist)
