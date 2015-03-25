lista = open('entrada.txt','r+', encoding='utf-8')
L = []

for i in lista.readlines():
    s = i.lower().strip()
    if s == '':
        None
    else:
        L.append(s)
lista.close()


print(L)