# Домашнее задание по теме "Генераторы"

def all_variants(text):
    for i in range(len(text)):
        for j in range(len(text)-i):
            yield text[j: j+i+1] # возврат текста по срезу

# Пример работы функции:
a = all_variants("abc")
for i in a:
    print(i)