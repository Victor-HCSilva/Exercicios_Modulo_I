# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 22:04:45 2024

@author: victor
"""
#Atualizado 25/06

from random import randint
from datetime import date

time = date.today()
iniciar = True
tentativas = 0
dificuldade = {'Fácil': 1,'Médio': 2,'Difícil': 3}
numbers_digiteds = []
print('Bém vindo ao jogo - @divinhe 0 númer0')
print('Apenas para teste, não obrigatório:')
nome = input('Qual seu nome?')

while iniciar:

    print('\nFácil: 1;\nMédio: 2;\nDifícil: 3.')
    print('\nEscolha a dificuldade (1, 2 ou 3)')
    escolher_dificuldade = input('')

    if escolher_dificuldade.rstrip() == '1':    #Escolhendo a dificuldade: facil, médio ou difcil
        limite = 10
        dificuldade_escolhida = 'Fácil'
        break
    elif escolher_dificuldade.rstrip() == '2':
        limite = 50
        dificuldade_escolhida = 'Médio'
        break
    elif escolher_dificuldade.rstrip() == '3':
        limite = 100
        dificuldade_escolhida = 'Difícil'
        break
    else:
        print(f'inválido! Você digitou "{escolher_dificuldade}"')

print(f'Muito bém você escolheu a dificuldade "{dificuldade_escolhida}"\n\n')

número_sorteado = randint(1, limite)

while iniciar:

  try:
    número_do_jogador = int(input(f'Você deve digitar um número inteiro de 1 a {limite},\nSe o número for igual ao número sorteado você ganha!\nDigite um numero!'))
    numbers_digiteds.append(número_do_jogador) # capturando numeros digitados


    if número_do_jogador == número_sorteado:#Se o jogador acertar o número
      break
    elif número_do_jogador == 1234:  #Obtenção da resposta caso o jogador desista
      print(f'Resposta: {número_sorteado}')
      break
    elif número_do_jogador > número_sorteado:  #Pequena ajuda para o jogador
        print(f'\nO número é menor que {número_do_jogador}.')
    elif número_do_jogador < número_sorteado:
        print(f'\nO número é maior que {número_do_jogador}.')
    else:
        pass

    print('\nVocê não acertou :(\n')

    tentativas += 1

  except Exception as erro:
    print(f'Ops, digitou algo inválido: {erro}')

    tentativas += 1

if tentativas > 0 and número_do_jogador != 1234:
    print(f'\n\n\n\nParabéns você acertou o número sorteado ({número_sorteado})! Errou apenas {tentativas} vez(es).')
elif número_do_jogador == 1234:
	print(f'Numero sorteado: {número_sorteado}\nTentativa/erros: {tentativas}')
else:
    print('\n\n\n\nUal! que sorte acertou de primeira! Parabéns!!!')

message0 = f'\n\n- Nome: {nome.title()};'
message1 = f'\n- Dificuldade escolhida: {dificuldade_escolhida} (de 1 a {limite});'
message2 = f'\n- Números digitados: {numbers_digiteds};'
message3 = f'\n- Número sorteado: {número_sorteado};'
message4 = f'\n- Número de erros: {tentativas};'
message5 = f'\n- Data: {time}.'

with open('dados.txt', 'a' , encoding='utf8') as dado:
	dado.write(message0)
	dado.write(message1)
	dado.write(message2)
	dado.write(message3)
	dado.write(message4)
	dado.write(message5)

