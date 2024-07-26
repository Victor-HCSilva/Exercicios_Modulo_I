
'''
DELEÇÃO - CHAT-GPT

Passo a Passo:
Importação de bibliotecas:

python
Copiar código
import pandas as pd
Importa a biblioteca pandas, que será usada para manipulação de dados em DataFrames.

Definição da função:

python
Copiar código
def acessar(nome='', matricula='0', mudanca='', tipo='', arquivo='registro de aluno fap 2024.csv', email=''):
A função acessar recebe os seguintes parâmetros:

nome: o nome do aluno.
matricula: a matrícula do aluno.
mudanca: o novo valor para o campo que será alterado.
tipo: o tipo de alteração que será feita.
arquivo: o nome do arquivo CSV onde os dados estão armazenados.
email: o email do aluno (usado para confirmar algumas alterações).
Carregar os dados no DataFrame:

python
Copiar código
df = pd.read_csv(arquivo)
Carrega os dados do arquivo CSV em um DataFrame df.

Transformar nome e matrícula para o formato desejado:

python
Copiar código
nome = nome.lower().strip()
matricula = str(matricula).strip()
Converte o nome para minúsculas e remove espaços em branco. Converte a matrícula para
string e remove espaços em branco.

Iterar sobre as linhas do DataFrame:

python
Copiar código
for i, row in df.iterrows():
Itera sobre as linhas do DataFrame usando iterrows(), que retorna o índice i e a linha row como
uma série de pandas.

Verificar e realizar a alteração:

python
Copiar código
if row['nome'].lower().strip() == nome and str(row['matricula']).strip() == matricula:
    if tipo == '1':
        df.at[i, 'nome'] = mudanca
        print('\nMudança tipo 1 realizada')
    elif tipo == '2':
        df.at[i, 'matricula'] = mudanca
        print('Mudança realizada')
    elif tipo == '3':
        df.at[i, 'curso'] = mudanca
        print('Mudança realizada')
    elif tipo == '4':
        df.at[i, 'telefone'] = mudanca
        print('Mudança realizada')
    elif tipo == '5':
        df.at[i, 'email'] = mudanca
        print('\nMudança de email realizada!')
    elif tipo == '6':
        df = df.drop(i).reset_index(drop=True)  # Excluir a linha e resetar o índice
        print('Deleção realizada...')

Compara o nome e a matrícula da linha atual com os valores fornecidos. Se corresponder,
 realiza a alteração ou deleção com base no valor de tipo:

Tipo '1': altera o nome.
Tipo '2': altera a matrícula.
Tipo '3': altera o curso.
Tipo '4': altera o telefone.
Tipo '5': altera o email.
Tipo '6': exclui a linha e reseta o índice.
Salvar o DataFrame atualizado de volta no arquivo CSV:

python
Copiar código
df.to_csv(arquivo, index=False, encoding='utf-8')
print('Arquivo atualizado.')
Salva o DataFrame atualizado de volta no arquivo CSV, removendo o índice original e usando a codificação UTF-8.

Essa função permite que você altere ou exclua registros de alunos de acordo com os critérios fornecidos,
garantindo que o arquivo CSV seja atualizado corretamente.


'''

import csv
import pandas as pd

def salvar(alunos, arquivo='registro de aluno fap 2024.csv'):
    with open(arquivo, 'a', encoding='utf8', newline='') as arquivo:
        writer = csv.writer(arquivo)
        for aluno in alunos:
            writer.writerow((aluno['nome'], str(aluno['matricula']), aluno['curso'], aluno['telefone'], aluno['email']))
    print('Cadastrado(a).')

def acessar(nome='', matricula='0', mudanca='', tipo='', arquivo='registro de aluno fap 2024.csv', email=''):
    # Carregar os dados no DataFrame
    df = pd.read_csv(arquivo)

    # Transformar nome e matrícula para o formato desejado
    nome = nome.lower().strip()
    matricula = str(matricula).strip()

    # Iterar sobre as linhas do DataFrame para encontrar a linha desejada
    for i, row in df.iterrows():
        if row['nome'].lower().strip() == nome and str(row['matricula']).strip() == matricula:
            if tipo == '1':
                df.at[i, 'nome'] = mudanca
                print('\nMudança tipo 1 realizada')
            elif tipo == '2':
                df.at[i, 'matricula'] = mudanca
                print('Mudança realizada')
            elif tipo == '3':
                df.at[i, 'curso'] = mudanca
                print('Mudança realizada')
            elif tipo == '4':
                df.at[i, 'telefone'] = mudanca
                print('Mudança realizada')
            elif tipo == '5':
                df.at[i, 'email'] = mudanca
                print('\nMudança de email realizada!')
            elif tipo == '6':
                df = df.drop(i).reset_index(drop=True)  # Excluir a linha e resetar o índice
                print('Deleção realizada...')

    # Salvar o DataFrame atualizado de volta no arquivo CSV
    df.to_csv(arquivo, index=False, encoding='utf-8')
    print('Arquivo atualizado.')

# Função auxiliar para exibir informações do aluno
def aluno_info(nome='teste da silva', matricula='20230044'):
    with open('registro de aluno fap 2024.csv', mode='r', encoding='utf8') as file:
        reader = csv.reader(file)
        rows = list(reader)
    for row in rows:
        if row[0].strip().lower() == nome.lower() and row[1] == str(matricula):
            print(f'\n\nDados gerais de {nome.title()}:')
            print('------------------------------------------')
            print('Nome:', row[0])
            print('Matrícula:', row[1])
            print('Curso:', row[2])
            print('Telefone:', row[3])
            print('Email:', row[4])
            print('------------------------------------------')

# Funções para exibir opções do menu
def informacao():
    print('\n---------------------------------------------')
    print('OPÇÕES-MENU')
    print('---------------------------------------------')
    print('[1] Para ver dados do(a) aluno(a)')
    print('[2] Para cadastrar um novo(a) aluno(a)')
    print('[3] Para deletar/alterar perfil do(a) aluno(a)')
    print('[0] Para sair')
    print('---------------------------------------------')

def informacao2():
    print('\n---------------------------------------------')
    print('ALTERAR/DELETAR:')
    print('---------------------------------------------')
    print('[1] para alterar o nome do aluno: ')
    print('[2] para alterar matricula')
    print('[3] para alterar curso')
    print('[4] para alterar telefone')
    print('[5] para alterar email')
    print('[6] Para deletar todos os dados de um aluno(a): ')
    print('[0] para voltar ao menu principal')
    print('---------------------------------------------')

def informacao3():
    print('\n------------------------------------------')
    print('BUSCAR DADOS:')
    print('---------------------------------------------')
    print('[0] para ir ao menu principal: ')
    print('[1] para ver informações gerais')

cadastrar = True
alunos = []

while cadastrar:
    informacao()
    escolha = input('Digite:')

    if escolha == '1':
        while True:
            informacao3()
            escolher = input('[2] para ver dados do(a) aluno(a) em específico: ')
            arquivo = 'registro de aluno fap 2024.csv'
            df = pd.read_csv(arquivo)

            if escolher == '1':
                print('\nTabela: Alunos - Matrícula - Email:')
                with open(arquivo, mode='r', encoding='utf8') as file:
                    reader = csv.reader(file)
                    rows = list(reader)
                for row in rows:
                    print('', row[0], '   -   ', row[1], '  -  ', row[4])

            elif escolher == '2':
                nome_pesquisa = input('Insira o nome do aluno(a): ')
                matricula_pesquisa = int(input('Insira a matrícula: '))
                aluno_info(nome=nome_pesquisa, matricula=str(matricula_pesquisa))

            elif escolher == '0':
                break
            else:
                print(f'Opção inválida! Você digitou: {escolher}')

    elif escolha == '2':
        print('\n------------------------------------------------------')
        print('CADASTRAR NOVO ALUNO')
        print('------------------------------------------------------')
        aluno_nome = input('Insira o nome: ').title()
        aluno_matricula = int(input('Insira o número de matrícula: '))
        aluno_curso = input('Curso do aluno(a): ').title().rstrip()
        aluno_telefone = input('Insira o número de telefone: ')
        aluno_email = input('Email do aluno(a): ')

        aluno = {
            'nome': aluno_nome,
            'matricula': aluno_matricula,
            'curso': aluno_curso,
            'telefone': aluno_telefone,
            'email': aluno_email,
        }

        alunos.append(aluno)
        salvar(alunos)
        alunos.remove(aluno)

        while True:
            mais_cadastro = input('\nDeseja cadastrar outro aluno ou realizar outra operação (s/n)?').lower().rstrip()
            if mais_cadastro == 's':
                break
            elif mais_cadastro == 'n':
                cadastrar = False
                break
            else:
                print('\nPor favor, digite "n" se não quiser cadastrar outro aluno(a)\nou "s" se quiser cadastrar.')

    elif escolha == '3':
        while True:
            informacao2()
            opcao = input('Digite: ')

            if opcao == '1':
                nome = input('\nInsira o nome a ser alterado: ')
                matricula = int(input('Insira o número de matrícula: '))
                novo_nome = input('Insira o novo nome: ')
                acessar(nome=nome, mudanca=novo_nome, tipo=opcao, matricula=matricula)

            elif opcao == '2':
                nome = input('Insira o nome do aluno(a): ')
                email_confirmar = input('Insira o email do aluno(a), por favor: ')
                mudanca = int(input('Insira a nova matrícula: '))
                acessar(nome=nome, mudanca=mudanca, tipo=opcao, email=email_confirmar)

            elif opcao == '3':
                nome = input('\nInsira o nome do aluno(a): ')
                matricula = input('\nInsira o número de matrícula: ')
                curso = input('Insira o novo curso: ')
                acessar(mudanca=curso, tipo=opcao, nome=nome, matricula=str(matricula))

            elif opcao == '4':
                nome = input('\nInsira o nome do(a) aluno(a): ')
                matricula = input('Insira o número de matrícula: ')
                numero = input('Insira o novo número: ')
                acessar(nome=nome, matricula=str(matricula), mudanca=numero, tipo=opcao)

            elif opcao == '5':
                nome = input('\nInsira o nome do(a) aluno(a): ')
                matricula = input('Insira o número de matrícula: ')
                email = input('Insira o novo email: ')
                acessar(nome=nome, matricula=str(matricula), mudanca=email, tipo=opcao)

            elif opcao == '6':
                nome = input('Insira o nome do(a) aluno(a) para apagar os dados: ')
                matricula = input('Insira o número de matrícula do(a) aluno(a): ')
                acessar(mudanca='', nome=nome, matricula=str(matricula), tipo=opcao)

            elif opcao == '0':
                break
            else:
                print(f'Opção inválida! Você digitou {opcao}')

    elif escolha == '0':
        cadastrar = False
    else:
        print(f'Opção inválida! Você digitou "{escolha}"')

try:
    pass
except:
    print('Nada cadastrado!')

finally:
    print('\nTudo ok!')
