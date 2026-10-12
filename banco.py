import sqlite3
from alunos import calcular_media, verificar_situacao

def conectar_banco(nome_banco: str = "alunos.db") -> sqlite3.Connection:
    conexao = sqlite3.connect(nome_banco)
    conexao.execute("PRAGMA foreign_keys = ON")
    return conexao

def criar_tabelas(nome_banco: str = "alunos.db") -> None:
    conexao = conectar_banco(nome_banco)
    cursor = conexao.cursor()

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            curso TEXT NOT NULL
            )
        """)

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS notas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            aluno_id INTEGER NOT NULL,
            nota REAL NOT NULL,
            FOREIGN KEY (aluno_id) REFERENCES alunos(id)
            )
        """)

    conexao.commit()
    conexao.close()

def adicionar_aluno_sql(
        nome: str,
        idade: int,
        curso: str,
        nome_banco: str = "alunos.db"
) -> int:
    conexao = conectar_banco(nome_banco)
    cursor = conexao.cursor()

    cursor.execute(
        """ 
        INSERT INTO alunos (nome, idade, curso)
        VALUES (?, ?, ?)""",
        (nome, idade, curso)
    )

    conexao.commit()

    aluno_id = cursor.lastrowid

    conexao.close()

    return aluno_id

def adicionar_nota_sql(
        aluno_id: int,
        nota: float,
        nome_banco: str = "alunos.db"
) -> int:
    
    conexao = conectar_banco(nome_banco)
    cursor = conexao.cursor()

    cursor.execute(
        """
        INSERT INTO notas (aluno_id, nota )
        VALUES (?, ?) """,
        (aluno_id,nota)
    )

    conexao.commit()

    nota_id = cursor.lastrowid

    conexao.close()

    return nota_id

def listar_alunos_com_notas_sql() -> list[tuple]:
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT alunos.nome, notas.nota
        FROM alunos
        INNER JOIN notas
        ON alunos.id = notas.aluno_id
    """)

    resultado = cursor.fetchall()
    conexao.close()

    return resultado

def buscar_aluno_sql(nome: str, nome_banco: str = "alunos.db") -> tuple | None:

    conexao = conectar_banco(nome_banco)
    cursor = conexao.cursor()

    cursor.execute(
        """
        SELECT id, nome, idade, curso
        FROM alunos
        WHERE nome = ?
        """,
        (nome,)
    )

    aluno = cursor.fetchone ()
    conexao.close()

    return aluno

def buscar_notas_sql(aluno_id: int) -> list[float]:
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute(
        """
        SELECT nota
        FROM notas
        WHERE aluno_id = ?
        """,
        (aluno_id,)
    )

    resultado = cursor.fetchall()
    conexao.close()

    return [nota[0] for nota in resultado]

def buscar_aluno_completo_sql(nome: str) -> dict | None:
    aluno = buscar_aluno_sql(nome)

    if aluno is None:
        return None

    aluno_id, aluno_nome, idade, curso = aluno
    notas = buscar_notas_sql(aluno_id)

    if notas:
        media = calcular_media(notas)
        situacao = verificar_situacao(notas)
    else:
        media = 0.0
        situacao = "Sem notas"

    resultado = {
        "id": aluno_id,
        "nome": aluno_nome,
        "idade": idade,
        "curso": curso,
        "notas": notas,
        "media": media,
        "situacao": situacao
    }

    return resultado

def atualizar_aluno_sql(aluno_id: int, idade: int, curso: str, 
                        nome_banco: str = "alunos.db") -> bool:

    conexao = conectar_banco(nome_banco)
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE alunos
        SET idade = ?, curso = ?
        WHERE id = ?
    """, (idade, curso, aluno_id))

    conexao.commit()
    status = cursor.rowcount > 0

    conexao.close()
    
    return status

def remover_aluno_sql(aluno_id: int, nome_banco: str = "alunos.db") -> bool:

    conexao = conectar_banco(nome_banco)
    cursor = conexao.cursor()

    cursor.execute("""
        DELETE FROM alunos
        WHERE id = ?
        """, 
        (aluno_id,)
    )

    conexao.commit()
    status = cursor.rowcount > 0

    conexao.close()

    return status


    

    

if __name__ == "__main__":
    criar_tabelas()