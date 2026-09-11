from arquivos import ler_arquivo, salvar_arquivo
from typing import Any


def adicionar_aluno(nome_arquivo: str, nome: str, idade: int, 
                    curso: str, notas: list[float]) -> bool:
    if not validar_notas(notas):
        return False

    arquivo = ler_arquivo(nome_arquivo)

    if arquivo is None:
        arquivo = {}

    if nome in arquivo:
        return False

    arquivo[nome] = {
        "idade": idade,
        "curso": curso,
        "notas": notas
    }
    salvar_arquivo(nome_arquivo, arquivo)
    return True


def buscar_aluno(nome_arquivo: str, nome_aluno: str) -> dict[str, Any] | None:
    arquivo = ler_arquivo(nome_arquivo)

    if arquivo is None or nome_aluno not in arquivo:
        return None

    aluno = arquivo.get(nome_aluno)
    media = calcular_media(aluno["notas"])
    situacao = verificar_situacao(aluno["notas"])

    resultado = {
        "idade": aluno["idade"],
        "curso": aluno["curso"],
        "notas": aluno["notas"],
        "media": media,
        "situacao": situacao
    }

    return resultado


def remover_aluno(nome_arquivo: str, nome_aluno: str) -> bool:
    arquivo = ler_arquivo(nome_arquivo)

    if arquivo is None or nome_aluno not in arquivo:
        return False

    del arquivo[nome_aluno]
    salvar_arquivo(nome_arquivo, arquivo)

    return True

def calcular_media(notas: list[float]) -> float:
    return round(sum(notas) / len(notas), 2) 

def verificar_situacao(notas: list[float]) -> str:
    if calcular_media(notas) >= 7:
        return 'Aprovado'
    
    return 'Reprovado'

def atualizar_aluno(nome_arquivo: str, nome_aluno: str, idade: int,
                     curso: str, notas: list[float]) -> bool:
    arquivo = ler_arquivo(nome_arquivo)

    if arquivo is None or nome_aluno not in arquivo:
        return False

    if not validar_notas(notas):
        return False

    aluno = arquivo.get(nome_aluno)
    aluno['idade'] = idade
    aluno['curso'] = curso
    aluno['notas'] = notas

    salvar_arquivo(nome_arquivo, arquivo)
    return True

def validar_notas(notas: list[float]) -> bool:
    for nota in notas:
        if not 0 <= nota <= 10:
            return False
    return True