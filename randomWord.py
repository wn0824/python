import random

print("영어단어 맞추기")
print("-------------------------------")

words = {
    'frog' : '개구리',
    'agent' : '요원',
    'fire' : '불',
    'range' : '범위'
    }

keys = list(words.keys())
random.shuffle(keys)

means = list(words.values())
random.shuffle(means)

counter = 0

print(keys)
print(means)

print('::choice number::')
print('1 = 의미 해석')
print('2 = 단어 번역')
print('3 = exit')

while True:
    choice = int(input('input number: '))
    if choice == 1:
        for i in keys:
            korean = words[i]
            guess = input('{} 의 뜻은?'.format(i))

            if guess == korean:
                print('정답')
                counter += 1
            else:
                print('오답')

        print('맞춘 정답 수 : {}'.format(counter))
        counter = 0
        continue
    elif choice == 2:
        for i in keys:
            korean = words[i]

            guess = input('{} 의 뜻은?'.format(korean))

            if guess == i:
                print('정답')
                counter += 1
            else:
                print('오답')

        print('맞춘 정답 수 : {}'.format(counter))
        
        counter = 0
        continue
    elif choice == 3:
        break
    else:
        print('please choice 1(word) or 2(mean) or 3(exit)')
        continue
