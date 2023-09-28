t = str(input("Введіть речення: "))

words = t.split()

words_e = []

for word in words:
    if word.count('e') == 3:
        words_e.append(word)

print("Слова з трьома літерами 'е':")
for word in words_e:
    print(word)