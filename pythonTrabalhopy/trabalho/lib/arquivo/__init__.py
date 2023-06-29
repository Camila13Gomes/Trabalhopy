from trabalho.lib.interface import *
import csv
from time import sleep
import re
import os


def arquivoExiste(nome):
    try:
        a= open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('\033[31mErro ao criar o arquivo\033[m')
    else:
        print(f'\033[34mArquivo criado {nome} criado\033[m')


def lerArquivo1(nome):
    try:
        csvfile = open(nome, 'r')
    except:
        print('\033[31mErro ao ler o arquivo!\033[m')
    else:
        cabecalho('Autores')
        csv_ler = csv.DictReader(csvfile)
        for linha in csv_ler:
            print('\033[35mArtista:\033[m',linha['artista'])
            print('\033[35mNacionalidade:\033[m', linha['nacionalidade'])
            print('\033[35mAlbuns:\033[m', linha['albuns'])
            print('\033[35mDireitos Editoriais:%\033[m', linha['direitos'])
            print('')
    finally:
        csvfile.close()


def lerArquivo(nome):
    try:
        csvfile = open(nome, 'r')
    except:
        print('\033[31mErro ao ler o arquivo!\033[m')
    else:
        cabecalho('Albuns')
        csv_ler = csv.DictReader(csvfile)
        for linha in csv_ler:
            print('\033[35mNome:\033[m', linha['nome'])
            print('\033[35mGénero Musical:\033[m', linha['genero'])
            print('\033[35mData de Lançamento:\033[m',linha['data_lancamento'])
            print('\033[35mUnidades Vendidas:\033[m',linha['unidades'])
            print('\033[35mPreço:\033[m', linha['preco'])
            print('\033[35mMusica:\033[m',linha['musica'])
            print('')
    finally:
        csvfile.close()


def registar(arq, nome, nacionalidade, albuns, direitos):
    try:
        a = open(arq, 'at')
    except:
        print('\033[31mErro na Abertura do arquivo!\033[m ')
    else:
        try:
            a.write(f'{nome},{nacionalidade},{albuns},{direitos}\n')
        except:
            print('\033[31mErro ao Registar\033[m')
        else:
            print(f'\033[34mNovo Registo {nome} Realizado\033[m')
        a.close()


def registar1(arq1, nome, genero, data, venda, preco, musica):
    try:
        a = open(arq1, 'at')
    except:
        print('\033[31mErro na Abertura do arquivo!\033[m ')
    else:
        try:
             a.write(f'{nome},{genero},{data},{venda},{preco},{musica}\n')
        except:
            print('\033[31mErro ao Registar\033[m')
        else:
            print(f'\033[35mNovo Registo {nome} Realizado\033[m')
        a.close()

#funcao login
def usuariLogin():
    try:

        #utilizador + password
        usuario = 'admin'
        senha = '123'
        while True:
            seu_usuario = input('Usuario: ')
            sua_senha = input('Senha: ')
            if usuario == seu_usuario and senha == sua_senha:
                print(' \033[32m SEJA BEM VINDO !!! \033[m ')
                break
            else:
                print('\033[31m Utilizador ou Password INCORRETA!\033[m \n Tente novamente! ')
    except:
        print('')


def direitos_autorais():
    try:
        csvfile_autores = open('ficheiros_csv\Autores.csv', 'r')


    except:
        print('\033[31mErro ao ler o arquivo!\033[m')
    else:

            soma_unit_prec=0
            csv_ler_autores = csv.DictReader(csvfile_autores)
            for linha in csv_ler_autores:
                percentagem = linha['direitos']
                csvfile = open('ficheiros_csv\Albuns.csv', 'r')
                csv_ler = csv.DictReader(csvfile)
                for linhas in csv_ler:
                    if linha['artista'] == linhas['nome']:
                        multi = float(linhas['unidades'])*float(linhas['preco'])
                        soma_unit_prec = soma_unit_prec + multi

                print('\033[31mTodos Direitos Editoriais: \033[m',)
                print('\033[35mArtista:\033[m', linha['artista'])
                print('\033[35mDireitos Editoriais: \033[m',int(soma_unit_prec)/int(linha['direitos']),'€')
                print('')
            csvfile_autores.close()



    finally:
        csvfile.close()




#Pesquisar Musicas
def p_musicas():
    try:
        pes = input("Artista: ").title()
        csvfile = open('ficheiros_csv\Musicas.csv', 'r')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho('Pesquisar')
        csv_ler = csv.DictReader(csvfile)
        for linha in csv_ler:
            if linha['artista']== pes:
                sleep(0.5)
                print('\033[35mArtista:\033[m', linha['artista'])
                print('\033[35mGénero Musical:\033[m', linha['genero'])
                print('\033[35mData de Lançamento:\033[m', linha['data_lancamento'])
                print('\033[35mUnidades Vendidas:\033[m', linha['unidades_vendidas'])
                print('\033[35mPreço:\033[m', linha['preco'],'€')
                print('\033[35mMusica:\033[m', linha['musica'])
                print('')
    finally:
        csvfile.close()



def p_autores():
    try:
        pes = input("Autor: ").title()
        csvfile = open('ficheiros_csv\Autores.csv', 'r')
    except:
        print('\033[31mErro ao ler o arquivo!\033[m')
    else:
        cabecalho('Pesquisar')
        csv_ler = csv.DictReader(csvfile)
        for linha in csv_ler:
            if linha['artista']== pes:
                sleep(0.5)
                print('\033[35mArtista:\033[m', linha['artista'])
                print('\033[35mNacionalidade:\033[m', linha['nacionalidade'])
                print('\033[35mAlbuns:\033[m', linha['albuns'])
                print('\033[35mDireitos Editoriais:\033[m', linha['direitos'])
                print('')
    finally:
        csvfile.close()

















