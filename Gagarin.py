expectan = 0
min_expectan = 190
max_expectan = 150
a = input()
while a != '!':
    a = int(a)
    if a >= 150 and a <= 190:
        expectan += 1
        if a < min_expectan:
            min_expectan = a
        if a > max_expectan:
            max_expectan = a
    a = input()

print(expectan)
print(min_expectan, max_expectan)