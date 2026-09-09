# 📚 Sistema de Gerenciamento de Alunos

Projeto desenvolvido em Python para praticar fundamentos de desenvolvimento de software, organização de código, persistência de dados e testes automatizados.

## 📝 Sobre o projeto

O sistema permite realizar o gerenciamento de alunos por meio de operações CRUD:

- Cadastro de alunos
- Busca de alunos
- Atualização de dados
- Remoção de alunos
- Cálculo da média das notas
- Verificação da situação do aluno

Os dados são armazenados em um arquivo JSON.

## 🛠️ Tecnologias utilizadas

- Python
- JSON
- Git
- GitHub
- pytest

## 📌 Conceitos praticados

- Funções
- Módulos
- Estruturas de dados
- Listas e dicionários
- Tratamento de exceções
- Type hints
- Persistência de dados em JSON
- Operações CRUD
- Testes automatizados
- Fixtures com pytest
- Parametrização de testes

## ✨ Funcionalidades

### Cadastrar aluno
Permite cadastrar um novo aluno com:

- Nome
- Idade
- Curso
- Notas

O sistema impede o cadastro duplicado de um aluno com o mesmo nome.

### Buscar aluno
Permite buscar um aluno cadastrado e exibir:

- Idade
- Curso
- Notas
- Média
- Situação

### Atualizar aluno
Permite alterar os dados de um aluno já cadastrado.

### Remover aluno
Permite remover um aluno do sistema.

### Calcular média
O sistema calcula automaticamente a média das notas do aluno.

### Verificar situação
Com base na média, o sistema informa se o aluno está:

- Aprovado
- Reprovado

## 🧪 Testes automatizados

O projeto utiliza `pytest` para testar as principais funcionalidades do sistema.

Entre os cenários testados estão:

- Cálculo de média
- Verificação da situação
- Cadastro de aluno
- Cadastro duplicado
- Busca de aluno
- Busca de aluno inexistente
- Atualização de aluno
- Atualização de aluno inexistente
- Remoção de aluno
- Remoção de aluno inexistente

Atualmente, o projeto possui:

```text
14 passed
