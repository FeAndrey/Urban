import random

def get_num():  # число первой вставки
    numbers = list(range(3, 21))
    number = random.choice(numbers)
    return number

def get_passcode(n):
    pass_dict = {3: 12, 4: 13, 5: 1423, 6: 121524, 7: 162534, 8: 13172635, 9: 1218273645, 10: 141923283746,
                11: 11029384756, 12: 12131511124210394857, 13: 112211310495867, 14: 1611325212343114105968,
                15: 1214114232133124115106978, 16: 1317115262143531341251161079, 17: 11621531441351261171089,
                18: 12151811724272163631545414513612711810, 19: 118217316415514613712811910,
                20: 13141911923282183731746416515614713812911}
    passcode = pass_dict.get(n)
    return passcode

n = get_num()
print('Первое поле:', n)

pair1 = list(range(1, n))
pair2 = list(range(1, n))
pairs = []
result = ''

for i in pair1:
    for j in pair2:
        pn1 = i  # pair1[i]
        pn2 = j  # pair2[j]
        if pn1 >= pn2:
            continue
        else:
            kratno = n % (pn1 + pn2)
            if kratno == 0:
                pairs.append([pn1, pn2])
                result = result + str(pn1) + str(pn2)

print('Пары чисел', pairs)
print('Вротрое поле', result)
if int(result) == get_passcode(n):
    print('Путь свободен!')