'''
9. Desenvolva um programa que leia um arquivo CSV e imprima seu conteúdo 
formatado na tela. 
- CONCLUIDO
'''

import csv
import pandas as pd

#Arquivo de exemplo
with open('exemplo.csv', 'w', encoding='utf8', newline='') as arquivo:  
    writer = csv.writer(arquivo)
    writer.writerow(('coluna1', 'coluna2', 'coluna3'))
    writer.writerow((1,'um','UM'))
    writer.writerow((2,'dois','DOIS'))

#Com o múdulo csv
with open('exemplo.csv', mode='r', encoding='utf8') as file :
    reader = csv.reader(file)
    reader = list(reader)
    print(reader)


coluna1 = [c[0] for c in reader]
coluna2 = [c[1] for c in reader]
coluna3 = [c[2] for c in reader]
coluna1 = coluna1[0]

print('coluna 1:',coluna1,'\n')
print('coluna 2:',coluna2,'\n')
print('coluna 3:',coluna3,'\n')

#Com o módulo pandas

arquivo = 'exemplo.csv'

df = pd.read_csv(arquivo)

print(df)
