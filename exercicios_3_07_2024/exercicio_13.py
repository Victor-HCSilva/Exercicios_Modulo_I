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

'''
Implemente uma função que receba uma string contendo números e operações 
matemáticas básicas (+, -, *, /) e retorne o resultado da expressão.
- Concluido
'''
numeros = input('Operação: ')
operador = [i for i in numeros if i in '*/+-']
operador = ''.join(operador)
n1 = []
n2 = []
i = 0

while i < len(numeros):
    if numeros[i] in '+-*/':
        print(numeros[i])
        #operador.append(numeros[i])
        break
    else:
        n1.append(numeros[i])
        i += 1
   
i += 1#para passar o index do operador na string

while i < len(numeros):
    n2.append(numeros[i])
    i+=1

try:
  n1 = float(''.join(n1))
  n2 = float(''.join(n2))
  if operador == '+':
    print(n1 + n2)
  elif operador == '-':
    print(n1 - n2)
  elif operador == '*':
    print(n1 * n2)
  elif operador == '/':
    print(n1 / n2)
except:
  print('Deve conter uma operação básica')


