'''
Escreva um programa que leia um arquivo de texto e conte o número de linhas, 
palavras e caracteres

with open('texto_teste.txt', 'w') as file:
    file.write('teste')
    
- concluido
'''

arquivo = input('Digite o nome do arquivo tipo texto (texto_teste.txt): ')
contar = 0

#lendo oarquivo
with open(arquivo, 'r') as file:
    reader = file.read()

print(reader)

#contando
for i in reader:
    contar += 1

print(contar)
