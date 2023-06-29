from trabalho.lib.interface import *
from trabalho.lib.arquivo import *
from time import sleep
import csv
from musica import reproducao


arq = 'ficheiros_csv\Autores.csv'
arq1 = 'ficheiros_csv\Albuns.csv'


if not arquivoExiste(arq1):
    criarArquivo(arq1)

#Listar Menu
while True:
    resposta = Menu(['Autores',
                     'Registar Novos Autores',
                     'Excluir','Albuns',
                     'Registar Albuns',
                     'Lucro dos Direitos Editoriais ',
                     'Pesquisa',
                     'Playlist',
                     'Sair do Sistema'])
    #autores
    if resposta == 1:
        usuariLogin()
        lerArquivo1(arq)

    #registar novos autores
    elif resposta == 2:
        cabecalho('Registar Novos Autores')

        nome = str(input('Nome do Autor:'))
        nacionalidade = str(input('Nacionalidade:'))
        albuns = str(input('Albuns :'))
        direitos = str(input('Direitos Autorais % :'))
        registar(arq, nome, nacionalidade, albuns, direitos)

    #excluir autores + albuns
    elif resposta == 3:
            cabecalho('Excluir Autores e Albuns')
            #definir uma lista
            linhas = list()
            linhas2 = list()

            pesquisa = input('\033[34mQual Autor que pretende Excluir?:\033[m ')

            #atribui uma variavel para abrir o ficheiro
            #remove autores
            with open('ficheiros_csv\Autores.csv', 'r') as ler_ficheiro:

                ler = csv.reader(ler_ficheiro)

                for linha in ler:

                    linhas.append(linha)

                    for procurar in linha:

                        if procurar == pesquisa:
                            linhas.remove(linha)

            with open('ficheiros_csv\Autores.csv', 'w') as escreve_ficheiro:

                escrever = csv.writer(escreve_ficheiro)

                escrever.writerows(linhas)

            #remove albuns
                # atribui uma variavel para abrir o ficheiro
                with open('ficheiros_csv\Albuns.csv', 'r') as ler_ficheiro:

                    ler = csv.reader(ler_ficheiro)

                    for linha1 in ler:

                        linhas2.append(linha1)

                        for procurar in linha1:

                            if procurar == pesquisa:
                                linhas2.remove(linha1)

                print('Acabou de remover o Autor assim como os seus albuns')

                with open('ficheiros_csv\Albuns.csv', 'w') as escreve_ficheiro:

                    escrever = csv.writer(escreve_ficheiro)

                    escrever.writerows(linhas2)

    #Albuns -
    elif resposta == 4:
        lerArquivo(arq1)

    #Registar Albuns
    
    elif resposta == 5:
        cabecalho('Registar Albuns ')

        nome = str(input('Nome do Autor:'))
        genero = str(input('Genero Musical: '))
        data = str(input('Data de Lançamento:'))
        venda = str(input('Unidades Vendidas:'))
        preco = input('Preço:€' )
        musica = str(input('Musica a Adicionar: '))
        registar1(arq1, nome, genero, data, venda, preco, musica)

    #Lucro Direitos Editoriais por fazer
    elif resposta == 6:
        cabecalho('Lucro dos Direitos Editoriais')
        usuariLogin()
        direitos_autorais()

    elif resposta == 7:
        cabecalho('Pesquisar ')
        while True:
            opcao = submenu(['Musicas', 'Autores','Sair do SubMenu'])
            if opcao==1:
                p_musicas()
            elif opcao==2:
                p_autores()
            elif opcao==3:
                cabecalho('\033[43mSaindo do Submenu ...\033[m')
                break
            else:
                print('\033[31mERRO! Digite uma opção valida:\033[m')
                sleep(3)



    elif resposta == 8:
        cabecalho('Playlist ')
        while True:
            opcao = submenu_playlist(['Reproduzir','Sair do SubMenu'])
            if opcao==1:
                reproducao()
            elif opcao==3:
                cabecalho('\033[43mSaindo do Submenu ...\033[m')
                break
            else:
                print('\033[31mERRO! Digite uma opção valida:\033[m')
                sleep(3)


    elif resposta == 9:
        cabecalho('\033[43mSaindo do Sistema ... Até Logo...\033[m')
        break
    else:
        print('\033[31mERRO! Digite uma opção valida:\033[m')
        sleep(3)










