#%time
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 20:08:16 2024

@author: victo
"""
#Consertar a conversão do tamanho (21/08/23)
def volume_cubo(lado):
    cubo = lado * lado * lado
    volume = cubo 
    return volume

def volume_deposito(altura, largura, base):
    volume = altura * largura * base  # volume do depósito em metros cúbicos
    return volume

opcoes_de_bolas = {
    1: 'Bola de basquete adulto',
    2: 'Bola de futebol oficial',
    3: 'Bola de basquete infantil',
    4: 'Bola de Vôlei',
    5: 'Bola de Handball',
    6: 'Bola de Futebol de Salão',
    7: 'Outro tipo'
}

iniciar = True

while iniciar:
    try:
        altura = float(input('Qual a altura do seu depósito (em m)? '))
        base = float(input('Qual a base do seu depósito (em m)? '))
        largura = float(input('Qual a largura do seu depósito (em m)? '))
    
        tipo_bola = True
        
        while tipo_bola:
            print('\n\n\n\n\nModelos disponíveis:\n')
            
            for i in range(1, 8):
                print(f'{i} - {opcoes_de_bolas[i]}')
    
            escolha = int(input('Escolha o número correspondente à bola desejada.\n'))
            
            if escolha == 1:
                print(f'\n\n\n\n\n\nOk, você escolheu a opção "{opcoes_de_bolas[1]}".')
                lado = 24
            elif escolha == 2:
                print(f'\n\n\n\n\n\nOk, você escolheu a opção "{opcoes_de_bolas[2]}".')
                lado = 22
            elif escolha == 3:
                print(f'\n\n\n\n\n\nOk, você escolheu a opção "{opcoes_de_bolas[3]}".')
                lado = 22
            elif escolha == 4:
                print(f'\n\n\n\n\n\nOk, você escolheu a opção "{opcoes_de_bolas[4]}".')
                lado = 21
            elif escolha == 5:
                print(f'\n\n\n\n\n\nOk, você escolheu a opção "{opcoes_de_bolas[5]}".')
                lado = 19
            elif escolha == 6:
                print(f'\n\n\n\n\n\nOk, você escolheu a opção "{opcoes_de_bolas[6]}".')
                lado = 20
            elif escolha == 7:
                print(f'\n\n\n\n\n\nOk, você escolheu a opção "{opcoes_de_bolas[7]}".')
                lado = float(input('Qual o diâmetro da esfera (em m)? '))
            else:
                print("Opção inválida. Por favor, escolha um número de 1 a 7.")
                continue
            
            tipo_bola = False
    
        quantidade_bolas = 0
        deposito = volume_deposito(altura=altura, largura=largura, base=base)
        bolas = volume_cubo(lado)/100
    
        print(f'\n\n\n\nEspaço cúbico disponível: {deposito:.2f} m³')
        print(f'Volume cúbico da esfera: {bolas:.2f} cm³')
        
        while deposito >= bolas:
            quantidade_bolas += 1
            deposito -= bolas
    
        print(f'\n\n\n\nAproximadamente cabem {quantidade_bolas} bola(s) no seu depósito.')
        
        iniciar = False  # Encerrar o loop principal após a primeira execução
        
    except Exception as erro:
        
        erro_de_digitacao = True
        
        while erro_de_digitacao:
            print(f'Dado inválido: {erro} \n\n')
            novamente = input('Deseja inserir dados novamente (s/n)?')
            
            if novamente.lower() == 's':
                erro_de_digitacao = False
            elif novamente.lower() == 'n':
                iniciar = False
                erro_de_digitacao = False
            else:
                continue#mudança
        
        
