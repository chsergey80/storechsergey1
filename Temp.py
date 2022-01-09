total = 0
print('Вводите цены; для остановки введите -1.')
price = float(input())
while price > 0:
    total = total + price  # можно заменить на аналогичную запись
    # total += price  234242342334234234234234567
    price = float(input())
print('Общая стоимость равна', total)