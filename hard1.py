usr = "".join(input().lower().split())
pan = True
for i in range(len(usr) // 2):
    if usr[i] != usr[len(usr) - 1 - i]:
        pan = False
        break
print(pan)