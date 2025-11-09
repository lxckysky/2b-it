textSplit = list(map(str, input().split(" ")))

highest = 0
word = ""
for i in range(len(textSplit)):
    if len(textSplit[i]) > highest:
        highest = len(textSplit[i])
        word = textSplit[i]
print(word)

