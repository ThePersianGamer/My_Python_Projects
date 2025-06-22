word = input("Enter a word: ")
vowels = ["a", "e", "i", "o", "u"]
for i in word:
    for v in vowels:
        if i == v:
            print(v)
