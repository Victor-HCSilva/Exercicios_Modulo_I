# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 22:04:45 2024

@author: victor
"""

1#jogo

from random import randint

iniciar = True

tentativas = 0
dificuldade = {'Fácil': 1,'Médio': 2,'Difícil': 3}

while iniciar:

    print('\nFácil: 1;\nMédio: 2;\nDifícil: 3.')
    print('\nEscolha a dificuldade digitando 1,2 ou 3')
    escolher_dificuldade = input('')

    if escolher_dificuldade.rstrip() == '1':    #Escolhendo a dificuldade: facil, médio ou difcil
        limite = 10
        break
    elif escolher_dificuldade.rstrip() == '2':
        limite = 50
        break
    elif escolher_dificuldade.rstrip() == '3':
        limite = 100
        break
    else:
        print('inválido')

numero_sorteado = randint(1, limite)

while iniciar:

  try:
    numero_do_jogador = int(input(f'Você deve digitar um numero inteiro de 1 a {limite},\nSe o numero for igual ao numero sorteado você ganha!'))

    if numero_do_jogador == numero_sorteado:#Se o jogador acertar o numero
      break
    elif numero_do_jogador == 1234:#Obtenção da resposta
      print(f'Resposta: {numero_sorteado}')
      break
    elif numero_do_jogador > numero_sorteado:#Pequena ajuda para o jogador
        print(f'\nO numero é menor que {numero_do_jogador}.')
    elif numero_do_jogador < numero_sorteado:
        print(f'\nO numero é maior {numero_do_jogador}.')
    else:
        pass

    denovo = input('\nVocê não acertou! Deseja tentar novamente click (s/n)?')

    if denovo == 'n':#Se errar e não quiser jogar novamente
        print('\nVocê perdeu.')
        break
    else:
        pass

    tentativas += 1


  except Exception as erro:
    print(f'Ops, digitou algo inválido: {erro}')

    tentativas += 1

if tentativas > 0:
    print(f'Parabéns você acertou o numero sorteado ({numero_sorteado})! Errou apenas {tentativas} vez(es).')
else:
    print('\n\nUal! que sorte acertou de primeira!')



