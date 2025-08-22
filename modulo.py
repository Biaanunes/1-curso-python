import os
restaurantes = []

def exibir_nome_programa():
    print('''
      ⟆Ꭿᑲ𝖮ᖇ ᕮⲭᕈᖇ∈⟆⟆\n\n''')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print ('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair')

def finalizar():
     os.system('clear')
     #para limpar no mac
     # no windows é 'cls'
     print('''
          Encerrando...
          ''')
     
def opcao_invalida():
    print('\n Opção invalida\n')
    input('Digite alguma tecla para voltar ao menu principal')
    main()

def escolher_opcao():
    opcao_escolhida = input('Escolha uma opção: ')
    opcao_escolhida = int(opcao_escolhida)


    if opcao_escolhida == 1:
        print('''
            Cadastrar restaurante
            ''')
    elif opcao_escolhida == 2:
        print('''
            Listar restaurante
            ''')
    elif opcao_escolhida == 3:
        print('''
            Ativar restaurante
            ''')
    elif opcao_escolhida == 4:
        finalizar()
    else:
        opcao_invalida()

def main():
    os.system('clear')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

def cadastrar():
    os.sytem('clear')
    print('cadastro de novos restaurates')
    nome_do_restaurante = input('Digite o nome do restaurante de dejesa cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    input('Digite uma tecla para coltar ao menu principal')
    main()

if __name__ == '__main__':
    main()
