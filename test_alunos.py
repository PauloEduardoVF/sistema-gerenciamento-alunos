import pytest
from alunos import calcular_media, verificar_situacao, adicionar_aluno, buscar_aluno, remover_aluno, atualizar_aluno


@pytest.fixture
def arquivo_teste():
    nome_arquivo = "alunos_teste.json"

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write("{}")

    yield nome_arquivo

    import os
    os.remove(nome_arquivo)

@pytest.mark.parametrize(
    "notas, esperado",
    [
        ([8, 9, 7, 10], 8.5),
        ([10, 10, 10, 10], 10.0),
        ([5, 6, 5, 4], 5.0),
    ]
)
def test_calcular_media(notas, esperado):
    assert calcular_media(notas) == esperado

@pytest.mark.parametrize(
    "notas, esperado",
    [
        ([8, 9, 7, 10], 'Aprovado'),
        ([10, 10, 10, 10], 'Aprovado'),
        ([5, 6, 5, 4], 'Reprovado'),
    ]
)
def test_verificar_situacao(notas, esperado):
    assert verificar_situacao(notas) == esperado


def test_adicionar_aluno(arquivo_teste):
    resultado = adicionar_aluno(
    arquivo_teste,
    "Joao",
    20,
    "Engenharia de Software",
    [8, 9, 7, 10]
    )
    assert resultado

def test_adicionar_aluno_duplicado(arquivo_teste):
    resultado_1 = adicionar_aluno(
        arquivo_teste,
        "Joao",
        20,
        "Engenharia de Software",
        [8, 9, 7, 10]
        )
    resultado_2 = adicionar_aluno(
            arquivo_teste,
            "Joao",
            20,
            "Engenharia de Software",
            [8, 9, 7, 10]
        )
    assert resultado_1
    assert not resultado_2

def test_buscar_aluno(arquivo_teste):
    adicionar_aluno(
        arquivo_teste,
        "Joao",
        20,
        "Engenharia de Software",
        [8, 9, 7, 10]
        )
    resultado = buscar_aluno(arquivo_teste, 'Joao')

    assert resultado['idade'] == 20
    assert resultado["curso"] == "Engenharia de Software"
    assert resultado["notas"] == [8, 9, 7, 10]
    assert resultado["media"] == 8.5
    assert resultado["situacao"] == 'Aprovado'

def test_busca_aluno_inexistente(arquivo_teste):
    resultado = buscar_aluno(arquivo_teste, "Joao")
    assert resultado is None

def test_remover_aluno(arquivo_teste):
    adicionar_aluno(
        arquivo_teste,
        "Joao",
        20,
        "Engenharia de Software",
        [8, 9, 7, 10],
        )
    resultado_1 = remover_aluno(arquivo_teste, 'Joao')
    resultado_2 = buscar_aluno(arquivo_teste, "Joao")

    assert resultado_1
    assert resultado_2 is None

def test_atualizar_aluno(arquivo_teste):
    adicionar_aluno(
        arquivo_teste,
        "Joao",
        20,
        "Engenharia de Software",
        [8, 9, 7, 10],
        )

    resultado_1 = atualizar_aluno(arquivo_teste,
                                "Joao",
                                21,
                                "Engenharia de AI",
                                [8, 10, 10, 10],
                                )

    resultado_2 = buscar_aluno(arquivo_teste, 'Joao')
    


    assert resultado_1
    assert resultado_2['idade'] == 21
    assert resultado_2["curso"] == "Engenharia de AI"
    assert resultado_2["notas"] == [8, 10, 10, 10]
    assert resultado_2["media"] == 9.5
    assert resultado_2["situacao"] == 'Aprovado'

def test_atualizar_aluno_inexistente(arquivo_teste):
    resultado = atualizar_aluno(arquivo_teste,
                                "Joao",
                                21,
                                "Engenharia de AI",
                                [8, 10, 10, 10],
                                )
    assert not resultado

def test_remover_aluno_inexistente(arquivo_teste):
    resultado = remover_aluno(arquivo_teste, 'Joao')

    assert not resultado
