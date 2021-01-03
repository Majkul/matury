k = []
h = ""
tab = []
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
            if int(x) is isinstance(x, str):
                #print(x)
                pass
            else:
                pass
        except ValueError:
            out.append(x)

for i in out:
    a = ""
    znak = ""
    liczba = 1
    k = 2
    for x in range(0, len(i) - 1):
        a = i[x]
        if a == i[x + 1]:
            znak = str(a)
            liczba = k
            k += 1
            try:
                if i[x + 1] == i[x + 2]:
                    pass
                else:
                    break
            except IndexError:
                pass
        else:
            pass
    if liczba == 1:
        with open("ouput.txt", "a") as f:
            f.writelines("brak" + "\n")
    else: 
        with open("ouput.txt", "a") as f:
            
            f.writelines(str(znak * liczba) + " ")
            f.writelines(str(liczba) + "\n")
