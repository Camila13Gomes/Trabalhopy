import os
from tkinter import*

import pygame
from PIL import Image, ImageTk
from pygame import *

cor0 = "#f0f3f5"  # Preta
cor1 = "#feffff"  # branca
cor2 = "#3fb5a3"  # verde
cor3 = "#2e2d2c"  # Negro
cor4 = "#403d3d"  # letra
cor5 = "#4a88e8"  # Azul

def reproducao():
        #Janela Principal
        janela = Tk()
        janela.title("Playlist")
        # Largura x comprimento
        janela.geometry('645x350')
        janela.configure(background=cor1)
        janela.resizable(width=False, height=False)
        # Frame Esquerda = Frame da Imagem
        frame_esquerda = Frame(janela, width=200, height=200, bg=cor3)
        frame_esquerda.grid(row=0, column=0, pady=1, padx=1, sticky=NSEW)

        # Frame Direita = Frame da Lista de Músicas
        frame_direita = Frame(janela, width=500, height=500, bg=cor3)
        frame_direita.grid(row=0, column=1, pady=1, padx=1, sticky=NSEW)

        frame_baixo = Frame(janela, width=300, height=500, bg=cor3)
        frame_baixo.grid(row=1, column=0, columnspan=3, pady=1, padx=0, sticky=NSEW)

        img_1 = Image.open('icon1.png')
        #COMPRIMENTO X ALTURA
        img_1 = img_1.resize((185,230))
        img_1 = ImageTk.PhotoImage(img_1)
        #ATRIBUI FRAME_ESQUERDA A LABEL E DENTRO DESSA LABEL ENCONTRA SE A IMAGEM DA MENINA ATRIBUINDO AS PROPRIEDADES COMO ALTURA/COMPRIMENTO/ESPAÇAMENTO DA LABEL
        l_logo = Label(frame_esquerda, height=300, image=img_1, compound=CENTER, padx=1, anchor='nw', font=('ivy 16 bold'),
                       bg=cor3, fg=cor3)

        #PONTO INICIAL DA IMAGEM(MENINA) DO PONTO X(ESQUERDA) E PONTO INICIAL Y
        l_logo.place(x=5, y=5)


        # criando funçoes-----


        def play_musica():
            rodando = listbox.get(ACTIVE)
            l_rodando['text'] = rodando
            pygame.mixer.music.load(rodando)
            pygame.mixer.music.play()


        def pausa_musica():
            pygame.mixer.music.pause()


        def continuar_musica():
            pygame.mixer.music.unpause()


        def parar_musica():
            mixer.music.stop()


        def proxima_musica():
            tocando = l_rodando['text']
            index = musicas.index(tocando)
            novo_index = index + 1
            tocando = musicas[novo_index]
            mixer.music.load(tocando)
            mixer.music.play()

            listbox.delete(0, END)

            mostrar()

            listbox.select_set(novo_index)
            listbox.config(selectmode=SINGLE)
            l_rodando['text'] = tocando


        def anterior_musica():
            tocando = l_rodando['text']
            index = musicas.index(tocando)
            novo_index = index - 1
            tocando = musicas[novo_index]
            mixer.music.load(tocando)
            mixer.music.play()

            listbox.delete(0, END)

            mostrar()

            listbox.select_set(novo_index)
            listbox.config(selectmode=SINGLE)
            l_rodando['text'] = tocando


        # frame_direita
        #definir tamanho listbox | modo de seleçao neste caso selecao unica | fonte usada |cor background e cor fonte
        listbox = Listbox(frame_direita, width=60, height=15, selectmode=SINGLE, font=('arial 9 bold'), bg=cor3, fg=cor1)
        # listbox vai inicializar com 0 linhas e 0 colunas
        listbox.grid(row=0, column=0)
        #Adicionar Scrool na Listbox e ajusta
        s = Scrollbar(frame_direita)
        s.grid(row=0, column=1, sticky=NSEW)
        listbox.config(yscrollcommand=s.set)
        s.config(command=listbox.yview)

        # fraime baixo

        #label com um comprimento de 90 texto justificado ao lado esquerdo e posicionado no canto superior esquerdo
        l_rodando = Label(frame_baixo, text='Selecione a Musica que pretende Ouvir: ', width=90, justify=LEFT, anchor='nw',
                          font=('ivy 10'), bg=cor1, fg=cor4)
        #Label x= 0 para ficar chegada totalmente ao lado esquerdo, Y tem margem de 1.
        l_rodando.place(x=0, y=1)

        img_2 = Image.open('img1.png')
        img_2 = img_2.resize((30, 30))
        img_2 = ImageTk.PhotoImage(img_2)
        #Botao é inserido dentro da frame.
        b_anterior = Button(frame_baixo, command=anterior_musica, width=40, height=40, image=img_2, font=('ivy 10 bold'),
                            relief=RAISED, overrelief=RIDGE, bg=cor3, fg=cor1)
        # posicao dos botoes - X incia no ponto 222 e soma se sempre + 46
        b_anterior.place(x=222, y=35)

        img_3 = Image.open('img2.png')
        img_3 = img_3.resize((30, 30))
        img_3 = ImageTk.PhotoImage(img_3)
        b_play = Button(frame_baixo, command=play_musica, width=40, height=40, image=img_3, font=('ivy 10 bold'), relief=RAISED,
                        overrelief=RIDGE, bg=cor3, fg=cor1)

        b_play.place(x=268, y=35)

        img_4 = Image.open('img3.png')
        img_4 = img_4.resize((30, 30))
        img_4 = ImageTk.PhotoImage(img_4)
        b_proxima = Button(frame_baixo, command=proxima_musica, width=40, height=40, image=img_4, font=('ivy 10 bold'),
                           relief=RAISED, overrelief=RIDGE,
                           bg=cor3, fg=cor1)
        b_proxima.place(x=314, y=35)

        img_5 = Image.open('img4.png')
        img_5 = img_5.resize((30, 30))
        img_5 = ImageTk.PhotoImage(img_5)
        b_pausar = Button(frame_baixo, command=pausa_musica, width=40, height=40, image=img_5, font=('ivy 10 bold'),
                          relief=RAISED, overrelief=RIDGE, bg=cor3, fg=cor1)
        b_pausar.place(x=360, y=35)

        img_6 = Image.open('img5.png')
        img_6 = img_6.resize((30, 30))
        img_6 = ImageTk.PhotoImage(img_6)
        b_continuar = Button(frame_baixo, command=continuar_musica, width=40, height=40, image=img_6, font=('ivy 10 bold'),
                             relief=RAISED, overrelief=RIDGE, bg=cor3, fg=cor1)
        b_continuar.place(x=406, y=35)

        img_7 = Image.open('img6.png')
        img_7 = img_7.resize((30, 30))
        img_7 = ImageTk.PhotoImage(img_7)
        b_stop = Button(frame_baixo, command=parar_musica, width=40, height=40, image=img_7, font=('ivy 10 bold'),
                        relief=RAISED, overrelief=RIDGE, bg=cor3, fg=cor1)
        b_stop.place(x=452, y=35)

        os.chdir(r'Musicas')
        musicas = os.listdir()


        def mostrar():
            for i in musicas:
                listbox.insert(END, i)
        mostrar()

        # inicializando o mixer
        pygame.mixer.init()
        janela.mainloop()

