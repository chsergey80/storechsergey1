print("Вы находитесь в пещере на развилке.")
print('Вы можете пойти "налево", "направо" или "прямо".')
print("Введите одно из слов в кавычках для выбора.")
answer = input()
if answer == "налево":
    print("Вы направились налево. Там на вас упал валун :(")
elif answer == "направо":
    print("Вы направились направо.")
    print("Через некоторое время вы дошли до двух дверей.")
    print('Вы выберете "левую" или "правую"?')
    answer = input()
    if answer == "левую":
        print("Вы направились налево. Там был выход. Вы выбрались :)")
    elif answer == 'правую':
        print("Вы направились направо.")
        print("Там был ноутбук с интересным сериалом.")
        print("Вы не смогли оторваться и решили остаться в пещере")
    else:
        print("Такого варианта небыло")
elif answer == "прямо":
    print("Вы направились прямо. ")
    print("Через некоторое время вы дошли до двух дверей. ")
    print('Вы выберете "левую" или "правую"?')
    answer = input()
    if answer == "левую":
        print("Вы направились налево. Здесь целая гора сладостей!!! Это я считаю лучшим финалом")
    elif answer == "правую":
        print("Вы направились направо. Там находился обучающийся програмист. Он заметил вас.")
        print("*Нажал на какую-то кнопку*.")
        print("*Всё плывёт у вас перед глазами*")
        print("*Вы отключаетесь*")
    else:
        print("Такого варианта небыло")
else:
    print("Такого варианта небыло")