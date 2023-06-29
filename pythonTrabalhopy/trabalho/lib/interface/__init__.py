def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um número inteiro VÁLIDO.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuario preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def linha(tam=120):
    return '-' * tam


def cabecalho(txt):
    print (linha())
    print(txt.center(120))
    print(linha())


def Menu(lista):
    cabecalho('\033[35mMENU TOCADISCO\033[m')
    c = 1
    for item in lista:
        print(f'\033[35m{c}\033[m - \033[36m {item} \033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc

def submenu(lista):

    c = 1
    for item in lista:
        print(f'\033[35m{c}\033[m - \033[36m {item} \033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mOpção: \033[m')
    return opc

def submenu_playlist(lista):

    c = 1
    for item in lista:
        print(f'\033[35m{c}\033[m - \033[36m {item} \033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mOpção: \033[m')
    return opc














