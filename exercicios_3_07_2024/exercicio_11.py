'''
Implemente um programa que conte o número de ocorrências de cada palavra 
em uma frase, ignorando maiúsculas/minúsculas e pontuação. 

frase = input('Insira a palavra: ').split()
contar = 1

i = 0

for palavra1 in frase:

    for palavra2 in frase:
        if palavra1 == palavra2:
            print(f'Palavras iguais achadas 1 e 2: {palavra1},{palavra2}')
            contar += 1

    i+=1

print(frase)
print(contar)
'''

'''
14 - Desenvolva uma função que receba uma string e a comprima, substituindo 
sequências de caracteres repetidos por um número seguido do caractere (por 
exemplo, "aaabbbcccc" se tornaria "3a3b4c"). 

- concluido
'''


def contar_letras(palavra):
    i = 1
    contar = 1
    letras = []
    contar_lista = []

    #primeira letra
    for p in palavra:

        #segunda letrao range vai sempre um a menos na contagem 
        for p2 in range(1, len(palavra)): 
            
            #se forem iguais
            if p == palavra[i] and p not in letras: 

            #so vaí contar se letra não estiver#na lista de letras    
                if p !=" ":#eliminabdo espaços vazios
                    contar += 1

            #percorrendo a palavra (palavra[i])
            i += 1

        if p not in letras:
            letras.append(p)#capturando a letra
            if contar > 1:#so vai captura se existirem letras repetidas
                letras.append(contar)

        contar = 0
        #comecando de novo, zerando o i
        i = 1

    #transformando a lista em string
    letras = [str(p) for p in letras]
    #transformando a lista em string
    letras = ''.join(letras)

    print(letras) 
    


palavra = input('Insira a palavra: ').lower()
letras = contar_letras(palavra)