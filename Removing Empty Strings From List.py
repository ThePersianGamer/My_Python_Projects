list = ["apple", "", "banana", "", "grape"]
for i in range (len(list) - 1, -1, -1):
    if list[i] == "":
        list.remove("")
print(list)