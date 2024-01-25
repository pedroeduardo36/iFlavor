import os

restaurantes = ['Bananas bananas, amigos a parte', 'Ma che pasta']

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

def exibir_subtitulo(texto):
    os.system('clear')
    print(texto)
    print()

def finalizar_app():
    # os.system('cls') Comando para o Windows
    exibir_subtitulo('Fechando o App')

def voltar_menu_principal():
      input('\nDigite enter para voltar ao menu principal ')
      main()


def opcao_invalida():
    print('Opção invalida\n')
    voltar_menu_principal()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')

    nome_do_restaurante = input('\nDigite o nome do restaurante que deseja cadastrar\n')
    restaurantes.append(nome_do_restaurante)
    print(f'\nO restaurante {nome_do_restaurante} foi adicionado com sucesso!\n')
    voltar_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Lista dos restaurantes')

    for restaurante in restaurantes:
        print(f'\n .{restaurante}\n')
        
    voltar_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                print('Ativar restaurante')
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('clear')
    exibir_nome_app()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()



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
