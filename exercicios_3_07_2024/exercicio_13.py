'''
 Implemente uma função que receba uma string contendo números e operações 
matemáticas básicas (+, -, *, /) e retorne o resultado da expressão. 
'''
'''

'''
'''
- MARIA EXERCICIO 1

numeros = [i for i in range(1,4321)]

numeros = [str(i) for i in numeros]

numeros = ''.join(numeros)

total = 0

for i in numeros:
    total+=1

print(total)
#result of chatgpt-16177.
'''

numeros = input('Operção: ')
operador = [i for i in numeros if i in '*/+-']
n1 = []
n2 = []
i = 0

while i < len(numeros):
    if numeros[i] in '+-*/':
        #operador.append(numeros[i])
        break
    n1.append(numeros[i])
    i += 1
   

#i += 1#para passar o index do operador na palavra

while i < len(numeros):
    n2.append(numeros[i])
    i+=1

n1 = float(''.join(n1))
n2 = float(''.join(n2))

print(operador)