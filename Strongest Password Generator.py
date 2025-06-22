import random
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_-$#@!%^&*()+=}][{:;"'?/>.<,~`'""
for i in range(25):
    random_letter = random.choice(letters)
    print(random_letter, end="")