poem = input("Введите стихотворение: ").split()
def rythm(str):
    count_vowel = []
    for word in str:
        count = 0
        for i in word:
            if i in "аеёиоуыэюяАЕЁИОУЫЭЮЯ": 
                count += 1
        count_vowel.append(count)
    return len(count_vowel) == count_vowel.count(count_vowel[0])
if rythm(poem):
    print("Парам пам-па")
else:
    print("Пам парам")