import os

def exibir_nome_app():
    print('''
    █ █▀▀ █░░ ▄▀█ █░█ █▀█ █▀█
    █ █▀░ █▄▄ █▀█ ▀▄▀ █▄█ █▀▄
        ''')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    # os.system('cls') Comando para o Windows
    os.system('clear')
    print('Fechando o App\n')

def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))

    match opcao_escolhida:
        case 1:
            print('Cadastrar restaurante')
        case 2:
            print('Listar restaurantes')
        case 3:
            print('Ativar restaurante')
        case 4:
            finalizar_app()
        case _:
            print('Opção inválida')

    # if opcao_escolhida == 1: 
    #     print('Cadastrar restaurante')
    # elif opcao_escolhida == 2:
    #     print('Listar restaurantes')
    # elif opcao_escolhida == 3:
    #     print('Ativar restaurantes')
    # elif opcao_escolhida == 4:
    #     finalizar_app()
    # else:
    #     print('Opção inválida')

def main():
    exibir_nome_app()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()