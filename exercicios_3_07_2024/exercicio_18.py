'''
18. Desenvolva um programa que mescle dados de dois arquivos CSV diferentes em 
um terceiro arquivo.
- Em progresso
'''
import csv

arquivo1 = 'arquivo1.csv'
arquivo2 = 'arquivo2.csv'
arquivo3 = 'arquivo3.csv'

with open(arquivo1, 'r', encoding='utf8', newline='') as file:  
    reader = csv.reader(file)
    reader = list(reader)
    reader1 = [s for s in reader]
    print(reader)

with open(arquivo2, 'r', encoding='utf8', newline='') as file:  
    reader = csv.reader(file)
    reader = list(reader)
    reader2 = [s for s in reader]
    print(reader)

with open(arquivo3, 'a', encoding='utf8', newline='') as file:  
    writer = csv.writer(file)
    writer.writerow((reader1, reader2, ''))
    

import pandas as pd

df = pd.read_csv(arquivo3)

print(df)





