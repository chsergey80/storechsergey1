kx = int(input())
ky = int(input())
mx = 0
my = 0
np = 0
col = 0
num = 0
s = 0
while kx != mx or ky != my:
    a = input()
    if a == 'направо' or a == 'разворот' or a == 'налево':
        if a == 'направо':
            np = (np + 1) % 4
        if a == 'разворот':
            np = (np + 2) % 4
        if a == 'налево':
            np = (np + 3) % 4
    if a == 'вперёд':
        b = int(input())
        if np == 0:
            my = my + b
        if np == 1:
            mx = mx + b
        if np == 2:
            my = my - b
        if np == 3:
            mx = mx - b
    col = col + 1
print(col)
if np == 0:
    s = 'север'
if np == 1:
    s = 'восток'
if np == 2:
    s = 'юг'
if np == 3:
    s = 'запад'
print(s)