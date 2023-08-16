
# 1. Дано предложение. Удалить все повторяющиеся слова.
#      Например: Today is nice day, today is fine day.
# 1.1 Удаляем из предложения зяпятые и точку в конце предложения,
#     переводим всю строку в нижний регистр.

sentence = input('Enter sentence: ')
sent1 = ''
for index in range(len(sentence)):
    if sentence[index] == ',' or sentence[index] == '.':
        continue
    sent1 += sentence[index]

sent11 = sent1.lower()
print(sent11)

# 1.2 Удаляем повторяющиеся слова.
sent = sent11.split(' ')
sent2 = []

for item in sent:
    if sent.count(item) == 1:
       sent2.append(item)

print(' '.join(sent2))
