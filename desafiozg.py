import time
import lyricsgenius
import pygame
from secret import SECRET_ID


def buscar_artista():
    genius = lyricsgenius.Genius(SECRET_ID)
    nome_artista = input("Insira o nome do artista:")
    nome_musica = input("Insira o nome da música:")
    resultado = genius.search_song(nome_artista, nome_musica)

    if resultado:
        frases_filtradas = set(resultado.lyrics.splitlines())
        return list(frases_filtradas)
    else:
        print("Música não encontrada.")
        return None


def reproduzir_musica():
    letras = buscar_artista()

    if letras:
        pygame.init()
        start = int(input("Selecione o início do trecho da música (em segundos): "))
        end = int(input("Selecione o fim do trecho da música (em segundos): "))

        start_music = start * 1000
        end_music = end * 1000

        pygame.mixer.music.load("/home/jessica/Área de Trabalho/erguei.mp3")
        pygame.mixer.music.play()

        for frase in letras[1:]:
            print(frase.encode('utf-8').decode('utf-8'))

        while pygame.mixer.music.get_pos() < start_music:
            time.sleep(0.1)

        while pygame.mixer.music.get_pos() < end_music:
            time.sleep(0.1)
        pygame.mixer.music.pause()

        input("Pressione Enter para encerrar!")


reproduzir_musica()
