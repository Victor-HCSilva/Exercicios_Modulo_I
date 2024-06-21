# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 14:52:29 2024

@author: victor
"""

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
    escala_para_converter = input('Qual escala inicial da temperatura k/c/f ')
    escolha_escala = input('Qual escala quer para a conversão k/c/f ')
    temperatura = float(input('Qual a temperatura ? '))

      # Conversões para Fahrenheit
    if escolha_escala.lower().rstrip() == 'f' and escala_para_converter.lower().rstrip() == 'c':
        print(f'{mensagem} {fahrenheit_para_celsius(temperatura):.2f}°{escolha_escala.upper()}')
    elif escolha_escala.lower().rstrip() == 'f' and escala_para_converter.lower().rstrip() == 'f':
        print(f'{mensagem} {fahrenheit_para_fahrenheit(temperatura):.2f}°{escolha_escala.upper()}')
    elif escolha_escala.lower().rstrip() == 'f' and escala_para_converter.lower().rstrip() == 'k':
        print(f'{mensagem} {fahrenheit_para_kelvin(temperatura):.2f}°{escolha_escala.upper()}')

      # Conversões para Celsius
    elif escolha_escala.lower().rstrip() == 'c' and escala_para_converter.lower().rstrip() == 'c':
        print(f'{mensagem} {celsius_para_celsius(temperatura):.2f}°{escolha_escala.upper()}')
    elif escolha_escala.lower().rstrip() == 'c' and escala_para_converter.lower().rstrip() == 'f':
        print(f'{mensagem} {celsius_para_fahrenheit(temperatura):.2f}°{escolha_escala.upper()}')
    elif escolha_escala.lower().rstrip() == 'c' and escala_para_converter.lower().rstrip() == 'k':
        print(f'{mensagem} {celsius_para_kelvin(temperatura):.2f}°{escolha_escala.upper()}')

      # Conversões para Kelvin
    elif escolha_escala.lower().rstrip() == 'k' and escala_para_converter.lower().rstrip() == 'f':
        print(f'{mensagem} {kelvin_para_fahrenheit(temperatura):.2f}°{escolha_escala.upper()}')
    elif escolha_escala.lower().rstrip() == 'k' and escala_para_converter.lower().rstrip() == 'k':
        print(f'{mensagem} {kelvin_para_kelvin(temperatura):.2f}°{escolha_escala.upper()}')
    elif escolha_escala.lower().rstrip() == 'k' and escala_para_converter.lower().rstrip() == 'c':
        print(f'{mensagem} {kelvin_para_celsius(temperatura):.2f}°{escolha_escala.upper()}')
    else:
        print('Escolha uma opção válida!')
        print('Digite k, c, ou f')

  except Exception as erro:
    print(f'Você digitou algo errado: {erro}')

  # Converter outra temperatura?
  mais_uma_conversao = input('Quer converter outra temperatura (s/n)? ')

  if mais_uma_conversao.lower() == 's':
      pass
  else:
      print('\nOk, fim do programa!')
      converter = False
      
