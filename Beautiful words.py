num = int(input())
num1 = num // 100
num2 = num // 10 % 10
num3 = num % 10
if num1 >= num2:
    if num2 >= num3:
        if (num1 + num3) / 2 == num2:
            print('Вы ввели красивое число')
        else:
            print('Жаль, вы ввели обычное число')
    else:
        if num1 >= num3:
            if (num1 + num2) / 2 == num3:
                print('Вы ввели красивое число')
            else:
                print('Жаль, вы ввели обычное число')
        else:
            if (num3 + num2) / 2 == num1:
                print('Вы ввели красивое число')
            else:
                print('Жаль, вы ввели обычное число')
else:
    if num2 <= num3:
        if (num1 + num3) / 2 == num2:
            print('Вы ввели красивое число')
        else:
            print('Жаль, вы ввели обычное число')
    else:
        if num1 >= num3:
            if (num3 + num2) / 2 == num1:
                print('Вы ввели красивое число')
            else:
                print('Жаль, вы ввели обычное число')
        else:
            if (num1 + num2) / 2 == num3:
                print('Вы ввели красивое число')
            else:
                print('Жаль, вы ввели обычное число')