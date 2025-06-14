from library.subjects import subjects_functions
from library.files import project_file
from library.interface import project_interfaces
from library.files import path
import json
import os


## fazer uma função para coletar dados de alunos em um arquivo
def coleta_dados_alunos():
    file_name = "files_created/cadastro_alunos.json"
    file_path = path.absolute_path(file_name)

    if not project_file.verificar_arquivo_existe(file_path):
        project_file.criar_subscrever_arquivo(file_path)
    dados_aluno = project_file.ler_arquivo(file_path)
    return dados_aluno


## fazer outra funçao para apenas cadastrar alunos - chama a coleta, depois cadastra os demais no looping
def cadastro_alunos(nome_aluno, matricula_aluno, file_path):
    file_path = "cadastro_alunos_matricula.json"

    if not project_file.verificar_arquivo_existe(file_path):
        project_file.criar_arquivo(file_path)
    else:
        dados_aluno = project_file.ler_arquivo(file_path)
    # looping de cadastro
    project_interfaces.continuar()
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
