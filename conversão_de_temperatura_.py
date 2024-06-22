# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 14:52:29 2024

@author: victor
"""
#Atualizado (21/08/23)

celsius_para_kelvin = lambda temperatura_c: temperatura_c + 273.15
celsius_para_fahrenheit = lambda temperatura_c: (temperatura_c * 9/5) + 32
celsius_para_celsius = lambda temperatura_c: temperatura_c

kelvin_para_kelvin = lambda temperatura_k: temperatura_k
kelvin_para_fahrenheit = lambda temperatura_k: (temperatura_k - 273.15) * 9/5 + 32
kelvin_para_celsius = lambda temperatura_k: temperatura_k - 273.15

fahrenheit_para_kelvin = lambda temperatura_f: (temperatura_f - 32) * 5/9 + 273.15
fahrenheit_para_fahrenheit = lambda temperatura_f: temperatura_f
fahrenheit_para_celsius = lambda temperatura_f: (temperatura_f - 32) * 5/9

mensagem = 'Temperatura:'

converter = True

while converter:
  try:
    escala_para_converter = input('Qual escala inicial da temperatura (k/c/f)? ').lower().rstrip()
    escolha_escala = input('Qual escala quer para a conversão (k/c/f)? ').lower().rstrip()
    escala_final = escolha_escala.upper()
    temperatura = float(input('Qual a temperatura ? '))

      # Conversões:
    if escala_para_converter == 'c':
        if escolha_escala == 'f':
            print(f'{mensagem} {celsius_para_fahrenheit(temperatura):.2f}°{escala_final}')
        elif escolha_escala == 'k':
            print(f'{mensagem} {celsius_para_kelvin(temperatura):.2f}°{escala_final}')
        elif escolha_escala == 'c':
            print(f'{mensagem} {celsius_para_celsius(temperatura):.2f}°{escala_final}')
        else:
            print('Escolha uma opção válida!')

    elif escala_para_converter == 'k':
        if escolha_escala == 'f':
            print(f'{mensagem} {kelvin_para_fahrenheit(temperatura):.2f}°{escala_final}')
        elif escolha_escala == 'c':
            print(f'{mensagem} {kelvin_para_celsius(temperatura):.2f}°{escala_final}')
        elif escolha_escala == 'k':
            print(f'{mensagem} {kelvin_para_kelvin(temperatura):.2f}°{escala_final}')
        else:
            print('Escolha uma opção válida!')

    elif escala_para_converter == 'f':
        if escolha_escala == 'c':
            print(f'{mensagem} {fahrenheit_para_celsius(temperatura):.2f}°{escala_final}')
        elif escolha_escala == 'k':
            print(f'{mensagem} {fahrenheit_para_kelvin(temperatura):.2f}°{escala_final}')
        elif escolha_escala == 'f':
            print(f'{mensagem} {fahrenheit_para_fahrenheit(temperatura):.2f}°{escala_final}')
        else:
            print('Escolha uma opção válida!')
    else:
        print('Escolha uma opção válida! Digite k, c, ou f.')
        print(f'Você digitou "{escala_para_converter}" e "{escolha_escala}"')

    # Converter outra temperatura?
    mais_uma_conversao = input('Quer converter outra temperatura (s/n)? ')

    if mais_uma_conversao.lower() == 's':
        pass
    else:
      print('\nOk, fim do programa!')
      converter = False
  
  except Exception as erro:
    print(f'Você digitou algo errado: {erro}')

      
