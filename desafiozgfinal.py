import requests
from secret import SECRET_ID
import time


def buscar_musica():
    nome_artista = input("Insira o nome do artista:")
    nome_musica = input("Insira o nome da música:")

    params = {"apikey": SECRET_ID, "art": nome_artista, "mus": nome_musica}

    response = requests.get("https://api.vagalume.com.br/search.php", params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro {response.status_code}: {response.text}")
        return None


def extrair_musica(data):
    if data and "mus" in data:
        return data["mus"][0]


def organizar_letra(letra):
    partes = letra["text"].split("\n")
    partes_sem_repeticao = sorted(set(partes), key=lambda x: partes.index(x))
    return "\n".join(partes_sem_repeticao)


def selecionar_tempo_reproducao(musica):
    opcao = input("Deseja imprimir a letra completa da música? (s/n): ").lower()
    if opcao == "s":
        print(organizar_letra(musica))
    else:
        inicio = int(
            input(
                "Selecione o tempo em segundos que deseja iniciar a música: "
            )
        )
        fim = int(
            input(
                "Selecione o tempo em segundos que deseja finalizar a música: "
            )
        )

        if inicio == 0 and fim == 0:
            print("Reproduzindo a música completa.")
        else:
            trecho = musica["text"].split("\n")[1:-1]  # Remove linhas em branco
            trecho_selecionado = "\n".join(trecho[inicio:fim])
            print(organizar_letra({"text": trecho_selecionado}))


data = buscar_musica()
musica = extrair_musica(data)

if musica:
    selecionar_tempo_reproducao(musica)
else:
    print("Não foi possível obter a letra da música.")
