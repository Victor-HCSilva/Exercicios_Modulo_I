'''
. Crie uma função que receba uma lista de números e retorne a soma de todos os 
elementos pares
- CONCLUIDO
'''

def somar_pares(lista):
    lista = lista.split()
    lista = [int(i) for i in lista ]
    lista = [i for i in lista if i %2 == 0]
    lista = sum(lista)
    print(lista)


lista = input('Lista: ')
somar_pares(lista)
    