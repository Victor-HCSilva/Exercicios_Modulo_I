# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 22:04:45 2024

@author: victor
"""

#Atualizado 21/06

from random import randint

iniciar = True
tentativas = 0
dificuldade = {'Fácil': 1,'Médio': 2,'Difícil': 3} 

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
    número_do_jogador = int(input(f'Você deve digitar um número inteiro de 1 a {limite},\nSe o número for igual ao número sorteado você ganha!'))

    if número_do_jogador == número_sorteado:#Se o jogador acertar o número
      break
    elif número_do_jogador == 1234:  #Obtenção da resposta caso o jogador desista
      print(f'Resposta: {número_sorteado}')
      break
    elif número_do_jogador > número_sorteado:  #Pequena ajuda para o jogador
        print(f'\nO número é menor que {número_do_jogador}.')
    elif número_do_jogador < número_sorteado:
        print(f'\nO número é maior {número_do_jogador}.')
    else:
        pass

    print('\nVocê não acertou :(\n')

    tentativas += 1

  except Exception as erro:
    print(f'Ops, digitou algo inválido: {erro}')

    tentativas += 1

if tentativas > 0:
    print(f'\n\n\n\nParabéns você acertou o número sorteado ({número_sorteado})! Errou apenas {tentativas} vez(es).')
else:
    print('\n\n\n\nUal! que sorte acertou de primeira!')



