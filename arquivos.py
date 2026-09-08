import json


def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo:
            return json.load(arquivo)

    except FileNotFoundError:
        return None

    except json.JSONDecodeError:
        return None

def salvar_arquivo(nome_arquivo, dados):
    with open(nome_arquivo, "w") as arquivo:
        json.dump(dados, arquivo, indent=4)

    