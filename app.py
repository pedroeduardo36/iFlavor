import os

restaurantes = [{'nome':'Amigos amigos, bananas a parte', 'categoria':'Fusion', 'ativo':True},
                {'nome':'Santé13', 'categoria':'Bistro', 'ativo':False},
                {'nome':'Ma che pasta', 'categoria':'Italiano', 'ativo':False}]

def exibir_nome_app():
    print('''
    █ █▀▀ █░░ ▄▀█ █░█ █▀█ █▀█
    █ █▀░ █▄▄ █▀█ ▀▄▀ █▄█ █▀▄
        ''')

def exibir_opcoes():
    '''Essa função é responsável por: exibir as opções no menu '''
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
    '''Essa função é responsável por: Cadastrar novos restaurantes'''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('\nDigite o nome do restaurante que deseja cadastrar\n')
    categoria = input(f'\nDigite o nome da categoria do restaurante {nome_do_restaurante}: \n')

    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}

    restaurantes.append(dados_do_restaurante)

    print(f'\nO restaurante {nome_do_restaurante} foi adicionado com sucesso!\n')
    voltar_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Lista dos restaurantes')

    print(f"{'Nome do restaurante'.ljust(33)} | {'Categoria'.ljust(30)} | Status")
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'-> {nome_restaurante.ljust(30)} | {categoria.ljust(30)} | {ativo}\n')
        
    voltar_menu_principal()

def ativando_restaurante():
    exibir_subtitulo('Alternar estado do restaurante')
    nome_restaurante = input('\nDigite o nome do restaurante que deseja alterar o estado: \n')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
            voltar_menu_principal()
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
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
                ativando_restaurante()
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
