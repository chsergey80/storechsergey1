#Вводится 4-х значное число. Нужно разделить его на отдельные цифры и с их помощью записать
#наименьшее возможное, но тоже четырехзначное число. В задаче нельзя использовать циклы, строки и списки.
#Формат ввода : Четырехзначное число.
#Формат вывода : Минимальное число, записанное теми же цифрами.

num = int(input())
num1 = num // 1000
num2 = num // 100 % 10
num3 = num % 100 // 10
num4 = num % 10
w1 = num1
w2 = num2
w3 = num3
w4 = num4
q1 = 0
q2 = 0
q3 = 0
q4 = 0
if w1 >= w2 and w1 >= w3 and w1 >= w4:
    q4 = w1
    num = int(str(w3) + str(w2) + str(w4))
    num1 = num // 100
    num2 = num // 10 % 10
    num3 = num % 10
if w2 >= w1 and w2 >= w3 and w2 >= w4:
    q4 = w2
    num = int(str(w3) + str(w1) + str(w4))
    num1 = num // 100
    num2 = num // 10 % 10
    num3 = num % 10
if w3 >= w2 and w3 >= w1 and w3 >= w4:
    q4 = w3
    num = int(str(w1) + str(w2) + str(w4))
    num1 = num // 100
    num2 = num // 10 % 10
    num3 = num % 10
if w4 >= w2 and w4 >= w3 and w4 >= w1:
    q4 = w4
    num = int(str(w3) + str(w2) + str(w1))
    num1 = num // 100
    num2 = num // 10 % 10
    num3 = num % 10
w1 = num1
w2 = num2
w3 = num3
if w1 >= w2 and w1 >= w3:
    q3 = w1
    num = int(str(w3) + str(w2))
    num1 = num // 10
    num2 = num % 10
if w2 >= w1 and w2 >= w3:
    q3 = w2
    num = int(str(w3) + str(w1))
    num1 = num // 10
    num2 = num % 10
if w3 >= w2 and w3 >= w1:
    q3 = w3
    num = int(str(w1) + str(w2))
    num1 = num // 10
    num2 = num % 10
w1 = num1
w2 = num2
if w1 >= w2:
    q1 = w2
    q2 = w1
else:
    q1 = w1
    q2 = w2
if q1 == 0:
    if q3 == 0:
        print(str(q4) + str(q2) + str(q3) + str(q1))
    elif q2 == 0:
        print(str(q3) + str(q2) + str(q1) + str(q4))
    elif q1 == 0:
        print(str(q2) + str(q1) + str(q3) + str(q4))
else:
    print(str(q1) + str(q2) + str(q3) + str(q4))
