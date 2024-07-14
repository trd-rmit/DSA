words = { letter: 0 for letter in input()}
no_words = int(input())
for _ in range(no_words):
    word = input()
    for letter in word:
        if letter not in words:
            print("No")
            break
    else:
        print("Yes")
