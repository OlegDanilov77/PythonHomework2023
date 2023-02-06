scores = {1: {'A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'},
          2: {'D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У'},
          3: {'B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я'},
          4: {'F', 'H', 'V', 'W', 'Y', 'Й', 'Ы'},
          5: {'K', 'Ж', 'З', 'Х', 'Ц', 'Ч'},
          8: {'J', 'X', 'Ш', 'Э', 'Ю'},
          10: {'Q', 'Z', 'Ф', 'Щ', 'Ъ'}}
word_input = str(input("Введите слово: "))
word = word_input.upper()
result = 0
for bukva in range(len(word)):
    for n in scores.keys():
        for a in scores[n]:
            if a == word[bukva]:
                result += n
# result = result + n if a == word[bukva] for a in scores[n] for n in scores.keys() for bukva in range(len(word)):
print(result)