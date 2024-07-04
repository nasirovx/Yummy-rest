b = ','.join(input()).split(",")
s = 0

for i in b:
    s += int(i)


print(" + ".join(b),'=',s)