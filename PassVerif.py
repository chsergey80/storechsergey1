a = input()
if len(a) < 8:
    print("Короткий!")
elif '123' in a:
    print('Простой!')
else:
    s = input()
    if a != s:
        print('Различаются.')
    else:
        print('OK')