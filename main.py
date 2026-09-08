from arquivos import ler_arquivo
from alunos import buscar_aluno, remover_aluno, adicionar_aluno


def main():
    while True:
        print('\n----------- MENU --------------\n')
        print('\t1 - Adicionar aluno\n'
            '\t2 - Buscar aluno\n'
            '\t3 - Remover aluno\n'
            '\t4 - Listar alunos\n'
            '\t0 - Sair\n')
        
        try:
            opcao = int(input('=> '))
        except ValueError:
            print('Digite um numero!')
            continue

        if not 0 <= opcao <= 4:
            print('\nOpção Invalida! Digite um número 0 a 4\n')
            continue

        if opcao == 0:
            break

        if opcao == 1:
            while True:
                try:
                    nome = input('Nome: ').strip().title()
                    idade = int(input('Idade: '))
                    curso = input('Curso: ').strip().title()
                    notas = []
                    for i in range(4):
                        while True:
                            nota = float(input(f'{i+1}° Nota : '))
                            if 0 <= nota <= 10:
                                notas.append(nota)
                                break
                            print('Nota inválida! Digite um valor entre 0 e 10.')

                    adicionar_aluno('alunos_dados.json', nome, idade, curso, notas)
                    break                   
                    
                except ValueError:
                    print('\n\tValor invalido!')

        elif opcao == 2:
            nome = input('Digite um nome: ').strip().title()
            resultado = buscar_aluno('alunos_dados.json', nome)

            if resultado is None:
                print('\nNão possível localizar o aluno.')
            else:
                print(f'\nNome do Aluno: {nome}')
                print(f"Idade: {resultado['idade']}")
                print(f"Curso: {resultado['curso']}")
                print(f"Notas: {resultado['notas']}")
                print(f"Média: {resultado['media']}")
                print(f"Situação: {resultado['situacao']}")

        elif opcao == 3:
            nome = input('Digite um nome: ').strip().title()
            resultado = remover_aluno('alunos_dados.json', nome)

            if resultado:
                print('\nAluno Removido.')
            else:
                print('\nNão possível Remover o aluno.')

        elif opcao == 4:
            arquivo = ler_arquivo('alunos_dados.json')

            if arquivo is None:
                print('\n Lista indisponivel.')
                continue 

            for aluno, dados in arquivo.items():
                print(f'\nNome: {aluno}')
                print(f"  Idade: {dados['idade']}")
                print(f"  Curso: {dados['curso']}")
                print(f"  Notas: {dados['notas']}")

if __name__ == "__main__":
    main()