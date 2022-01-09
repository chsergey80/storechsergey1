quest_1 = 'салат оливье'
quest_2 = 'крабовый салат'
quest_3 = 'зимний салат'
quest_4 = 'Шпиц'
quest_5 = 'Сиба-ину'
quest_6 = 'Терьер'
quest_7 = 'Чихуахуа'

print('Какой салат вы предпочитаете на Новый год?')

question_1 = input()

if question_1 == quest_1:
    print('Я тоже обожаю этот салат.')
elif question_1 == quest_2:
    print('Знайте, что в крабовых палочках не содержится крабовое мясо.')
elif question_1 == quest_3:
    print('Хороший у вас вкус!')

if question_1 == quest_1 or question_1 == quest_2 or question_1 == quest_3:

    print('Какая порода собак вам нравится?')

    question_2 = input()

    if question_2 == quest_4:
        print('У людей, которые предпочитают Шпица развит отдел мозга, отвечающий за любовь.')
    elif question_2 == quest_5:
        print('Вы любите мемы!.')
    elif question_2 == quest_6:
        print('Безусловно, любители Терьеров - это настоящие лидеры.')
    elif question_2 == quest_7:
        print('Вы любите поворчать со своей собакой.')
    else:
        print('ERROR')
else:
    print('ERROR')