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
    dados_aluno = project_file.ler_arquivo(file_path)
    return dados_aluno


def cadastro_alunos(nome_aluno, matricula_aluno):
    file_path = path.students_absolute_path()

    # if not project_file.verificar_arquivo_existe(file_path):
    #     project_file.criar_arquivo(file_path)
    # else:
    # dados_aluno = project_file.ler_arquivo(file_path)
    dados_aluno = coleta_dados_alunos()
    # looping de cadastro
    while True:
        decisao = project_interfaces.continuar()
        if not decisao:
            break
        else:
            # aqui tem que receber os dados e fazer um for
            # fazer uma função para verificar a questão da matricula - pegar a verificação do codigo principal com any()

# while True:
#             matricula_aluno = int(input(f"Matrícula do aluno {nome_aluno}: "))
#             # fazer uma validação se não for número.
#             if any(
#                 matricula_existente["matricula"] == matricula_aluno
#                 for matricula_existente in lista_alunos
#             ):
#                 print(
#                     f"Matrícula {matricula_aluno} já cadastrada em outro aluno. Por favor, digite outro número de matrícula."
#                 )
        


            # todo aluno que for cadastra nesse looping tem que chamar a função da matricula e depois fazer um apend na  lista de dado_aluno
            lista_alunos = []
            if dados_aluno:
                lista_alunos.append(dados_aluno[:])
            # verificar se a matricula existe:

    # se matricula não existe:
    aluno = {"nome": nome_aluno, "matricula": matricula_aluno, "disciplina": []}
    lista_alunos.append(aluno.copy())

    # quando o loopoing finalizar - salvar os dados no arquivo:
    project_file.subscrever_arquivo(file_path, lista_alunos)
    return aluno

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


def buscar_aluno(lista_alunos, matricula):
    for aluno in lista_alunos:
        if aluno["matricula"] == matricula:
            return aluno
    return None


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
