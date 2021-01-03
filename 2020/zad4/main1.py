import random

k = []

def pierwsza(num):

    if num > 1:
        for i in range (2, num):
            if (num % i) == 0:
                return False
                break
        else:
            return True

    else:
        return False
    

with open("pary.txt", "r") as f:
    for x in range(1, 100):
        k += f.read().split("\n")

for i in range(0, 100):
    k[i] = k[i].split(" ")
out = []

for i in k:
    #print(i)
    for x in i:
        try:
            if int(x) % 2 == 0:
                #print(x)
                out.append(x)
            else:
                pass
        except ValueError:
            pass
x = 1
print(out)
for i in out:
    i = int(i)
    a = int(i)
    a -= 1
    y = i - x
    while pierwsza(y) is False and pierwsza(a) is False:
        if pierwsza(a) is False:
            a -= 1
            x += 1
            #print(a, x)
            y = i - x
        elif pierwsza(y) is True:
            y = i - x
            
        else:
            pass
    else:
        print(x, y)
        x = 1
