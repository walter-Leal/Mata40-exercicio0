def conf(d, a, b, c):
    if d == 'C':
        if (a > 0) and (c > 0) and (c > (a + b)):
            return 1 
        else:
            print('Dados invalidos, tente novamente')
            return 0
    if d == 'D':
        if (a > 0) and (a < (b - c)):
            return 1 
        else:
            print('Dados invalidos, tente novamente')
            return 0
    

j = 0
while j == 0:
    ordem, tam, min, max = (input("entrada: ").split())
    tam = int(tam)
    min = int(min)
    max = int(max)

    j = conf(ordem,tam,min,max)

vetor = []
if ordem == 'C':
    for i in range(tam):
        vetor.append(min + i)

    print(vetor)

if ordem == 'D':
    for i in range(tam):
        vetor.append(min - i)

    print(vetor)
