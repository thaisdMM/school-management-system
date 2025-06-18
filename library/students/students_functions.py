from library.subjects import subjects_functions
from library.files import project_file
from library.interface import project_interfaces
from library.files import path
import json
import os


def students_file_name():
    return "cadastro_alunos.json"


def coleta_dados_alunos():
    file_path = path.students_absolute_path()
    if not project_file.verificar_arquivo_existe(file_path):
        project_file.criar_subscrever_arquivo(file_path)
    dados_alunos = project_file.ler_arquivo(file_path)
    if dados_alunos is None:
        dados_alunos = []
    return dados_alunos


def verifica_matricula_existente(matricula: int, lista_alunos) -> bool:
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
    while True:
        nome_aluno = input("Nome do aluno: ").strip().title()
        while True:
            matricula_aluno = abs(
                project_interfaces.leia_int(f"Matrícula do aluno {nome_aluno} ")
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
        print("-" * 60)
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


def mostrar_alunos():
    file_path = path.students_absolute_path()
    dados_arquivo = project_file.ler_arquivo(file_path)
    if dados_arquivo is None:
        print(
            "Não foi possível carregar os dados dos alunos. O arquivo não existe ou contém dados inválidos."
        )
    elif len(dados_arquivo) <= 0:
        print("Ainda não existem alunos cadastrados no arquivo de alunos.")
    else:
        print("LISTA DE ALUNOS:")
        for aluno in dados_arquivo:
            print(f"{aluno['nome']:<30}| matrícula: {aluno['matricula']:>10}", end="")
            print()
            print("-" * 60)


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
