'''
parte-2
1. Crie uma função que receba uma string e retorne uma nova string com todas as 
vogais removidas. 
- CONCLUIDO
'''

palavra = input('Insira a palavra: ').lower()
palavra_sem_vogal = []

i = 0

for p in palavra:
    if p not in 'aeiou':
        palavra_sem_vogal.append(p)
    
palavra_sem_vogal = ''.join(palavra_sem_vogal)
print(f'Palavra de entrada: {palavra}')
print(f'Palavra sem vogais: {palavra_sem_vogal}')