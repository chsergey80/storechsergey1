stolen = int(input())
while stolen > 0:
    take = int(input())
    if 1 <= take <= 3 and take <= stolen:
        stolen -= take
    print(stolen)