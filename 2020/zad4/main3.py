def minnum(tab):
    m = tab[0]
    for i in tab:
        if i < m:
            m = i
    return m

k = []
with open("pary.txt", "r") as f:
    for x in range(1, 100):
        k += f.read().split("\n")

for i in range(0, 100):
    k[i] = k[i].split(" ")
tab1 = []
tab2 = []

for i in k:
    
    try:
        if int(i[0]) == len(i[1]):
            tab1 += i[0]
            tab2 += i[1].split(", ")
        else: 
            pass
    except IndexError:
        pass

print(str(minnum(tab1)) + " " + sorted(tab2)[0])


