def get_W_list(term, words_set):
    mass = []
    letters = 'aeouiy'
    term_low = term.lower()
    for word in words_set:
        for letter in letters:
            if word.find(letter) != -1 and term_low.find(letter) != -1:
                mass.append(word)
    return mass
terms_set = set()
while True:
    term_c = input()
    if term_c == 'FINISH':
        break
    terms_set.add(term_c)
words_list = input('\nНапишите слова через пробел и запятую: ').lower().split(', ')
words_set = set(words_list)
for term in terms_set:
    term_words = get_W_list(term, words_set)
    if term_words:
        print(term + '++' + '_'.join(term_words))
        