hello_1 = str.lower(input("Привет! Хочешь пообщаться? ;)"))
start_1 = "Как дела?"
hello_2 = 'Привет'
no_1 = "Ну если не хочешь общаться, то и не надо"
glup_1 = "Это ты глупый"
dur_1 = "Я не плохой, я маленькая программа"
que_1 = "У меня все отлично!"
obs_1 = "У меня тоже все хорошо! А что новенького в мире? \n"
netr_1 = "Не грусти, все будет хорошо"
while True:
    if 'прив' in hello_1 or 'здрав' in hello_1:
        print(hello_2)
        hello_1 = input(start_1)
    if "хочу" in hello_1 or "да" in hello_1:
        hello_1 = input(start_1)
    if "хор" in hello_1 or "норм" in hello_1 or "отл" in hello_1:
        hello_1 = input(obs_1)
    else:
        if "плох" in hello_1:
             hello_1 = input(netr_1)
        if "не" in hello_1:
             print(no_1)
        if "глуп" in hello_1:
            hello_1 = input(glup_1)
        if "дур" in hello_1:
            print(dur_1)
            hello_1 = input("А ты лучше на себя посмотри :(,.")