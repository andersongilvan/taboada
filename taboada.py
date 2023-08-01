# Taboada #

def mostrar_linha():
    print('_' * 30)
    


numero = int(input('Digite um número e veja a sua taboada:_'))

for c in range(0, 11):
    soma = numero + c

    print(numero,'+',c,'=',soma)
mostrar_linha()
mostrar_linha()


for c in range(1, 11):
    sub = numero - c
  
    print(numero,'-',c,'=',sub)
mostrar_linha()
mostrar_linha()

for c in range(0, 11):
    mult = numero * c

    print(numero,'x',c,'=',mult)
mostrar_linha()
mostrar_linha()

for c in range(1, 11):
    div = numero / c

    print('{} / {} = {:.2f}'.format(numero,c,div))


mostrar_linha()
print('FIM...')
mostrar_linha()


