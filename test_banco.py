import sqlite3
import pytest
from banco import criar_tabelas, conectar_banco, adicionar_aluno_sql, adicionar_nota_sql

def test_criar_tabelas(tmp_path):
    banco_test = tmp_path / "teste.db"
    criar_tabelas(str(banco_test))

    conexao = conectar_banco(str(banco_test))
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type = 'table'
    """)

    tabelas = cursor.fetchall()
    conexao.close()

    nomes_tabelas = [tabela[0] for tabela in tabelas]

    assert "alunos" in nomes_tabelas
    assert "notas" in nomes_tabelas

def test_adicionar_aluno_sql(tmp_path):
    banco_teste = tmp_path / "test.db"
    criar_tabelas(str(banco_teste))

    aluno_id = adicionar_aluno_sql(
        "Maria",
        22,
        "Ciência da Computação",
        str(banco_teste)
    )

    conexao = conectar_banco(str(banco_teste))
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, nome, idade, curso
        FROM alunos
        WHERE id = ?
    """, (aluno_id,))

    aluno = cursor.fetchone()

    conexao.close()

    assert aluno is not None
    assert aluno[1] == "Maria"
    assert aluno[2] == 22
    assert aluno[3] == "Ciência da Computação"

def test_adicionar_nota_sql(tmp_path):
    banco_teste = tmp_path/ "test.db"
    criar_tabelas(str(banco_teste))

    aluno_id = adicionar_aluno_sql(
        "João",
        20,
        "Engenharia de Software",
        str(banco_teste)
    )

    nota_id = adicionar_nota_sql(
        aluno_id,
        8.5,
        str(banco_teste)
    )

    conexao = conectar_banco(str(banco_teste))
    cursor = conexao.cursor()

    cursor.execute('''
        SELECT id, aluno_id, nota
        FROM  notas
        WHERE id = ?
    ''', (nota_id,))

    nota = cursor.fetchone()

    conexao.close()

    assert nota is not None
    assert nota[0] == nota_id
    assert nota[1] == aluno_id
    assert nota[2] == 8.5

def test_adicionar_nota_para_aluno_inexistente(tmp_path):
    banco_teste = tmp_path/"test.db"
    criar_tabelas(str(banco_teste))

    with pytest.raises(sqlite3.IntegrityError):
        adicionar_nota_sql(
            999,
            8.5,
            str(banco_teste)
        )