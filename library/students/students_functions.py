from library.subjects import subjects_functions
from library.files import project_file
from library.interface import project_interfaces
from library.files import path
import json
import os


def students_file_name():
    return "cadastro_alunos.json"


# será que preciso passar um parâmetro nessa função? acho que não, pq quando eu chamar ela no main o usuario teria que passar algo que já está definido
def coleta_dados_alunos():
    file_path = path.students_absolute_path()
    if not project_file.verificar_arquivo_existe(file_path):
        project_file.criar_subscrever_arquivo(file_path)
    dados_alunos = project_file.ler_arquivo(file_path)
    return dados_alunos


def verifica_matricula_existente(matricula: int, lista_alunos) -> bool:

    # fazer uma validação se não for número. usar a função leiaInt no codigo principal
    # dados_alunos = coleta_dados_alunos()

    # será que coloca um while true nessa função, para só parar quando for false any

    # any() com lista vazia: seguro, retorna False, não quebra o código - nao precisa tratar esse caso
    if any(
        matricula_existente["matricula"] == matricula
        for matricula_existente in lista_alunos
    ):
        return True
    return False


def buscar_aluno(lista_alunos, matricula):
    for aluno in lista_alunos:
        if aluno["matricula"] == matricula:
            return aluno
    return None


def cadastro_alunos():
    file_path = path.students_absolute_path()
    dados_alunos = coleta_dados_alunos()
    # looping de cadastro
    while (
        True
    ):  # tem que ter looping no main pq senao ele atualiza o menu toda iteração

        nome_aluno = input("Nome do aluno: ").strip().title()
        # except NameError:
        #     print("O nome não pode ser vazio!")

        while True:
            matricula_aluno = project_interfaces.leiaInt(
                f"Matrícula do aluno {nome_aluno} "
            )
            matricula = verifica_matricula_existente(matricula_aluno, dados_alunos)
            if not matricula:
                aluno = {
                    "nome": nome_aluno,
                    "matricula": matricula_aluno,
                    "disciplina": [],
                }
                break
            print(
                f"Matrícula {matricula_aluno} já cadastrada em outro aluno. Digite outra matrícula para o aluno {nome_aluno}"
            )
        dados_alunos.append(aluno.copy())
        print(
            f"Aluno: {aluno['nome']}, matricula: {aluno['matricula']} cadastrado com sucesso!"
        )
        decisao = project_interfaces.continuar()
        # quando o loopoing finalizar - salvar os dados no arquivo:
        if not decisao:
            project_file.criar_subscrever_arquivo(file_path, dados_alunos)
            break

    # criar outra função para essa associaçao?
    # associacao_disciplinas_alunos(lista_alunos, lista_disciplinas)
    # print(
    #     f"{nome_aluno}: foi cadastrado(a) com sucesso com a matrícula {matricula_aluno}!"
    # )
    # print("=-" * 50)


def mostrar_alunos(lista_alunos):
    print("LISTA DE ALUNOS:")
    print()
    if len(lista_alunos) <= 0:
        print("Ainda não existem alunos cadastrados.")
    else:
        for aluno in lista_alunos:
            print(f"{aluno['nome']:<5} = matrícula {aluno['matricula']}", end="")
            print()
            print("-" * 60)
    print("=-" * 50)


def exibir_dados_alunos(lista_alunos, matricula):
    aluno = buscar_aluno(lista_alunos, matricula)
    if aluno == None:
        print(
            "Não há aluno com a matrícula pesquisada. Verifique a matrícula do aluno que quer exibir os dados."
        )
    else:
        for key, value in aluno.items():
            print(f"{key:<10} = {value}")
    print("=-" * 50)


def excluir_aluno(lista, aluno):
    if aluno is None:
        return False
    else:
        lista.remove(aluno)
        return True
