n = int(input())
while n > 0:
    n1 = n % 4
    if n1 == 0:
        n1 = 2
    n -= n1
    print(n1, n)
    if n == 0:
        print('ИИ выиграл!')
    else:
        n1 = int(input())
        while not (1 <= n1 <= 3 and n1 <= n):
            print('Некорректный ход:', n1)
            n1 = int(input())
        n -= n1
        print(n1, n)
        if n == 0:
            print('Вы выиграли!')