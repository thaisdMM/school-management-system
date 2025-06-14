from library.interface import project_interfaces
from library.students import students_functions
from library.files import project_file
from time import sleep
import os
import json

lista_alunos = []




while True:
    resposta = project_interfaces.menu(
        [
            "Cadastrar alunos.",
            "Exibir alunos cadastrados.",
            "Cadastrar disciplinas.",
            "Exibir disciplinas cadastradas.",
            "Cadastrar notas por disciplina.",
            "Exibir situação de todos os alunos.",
            "Exibir a situação de um aluno específico.",
            "Excluir aluno.",
            "Trocar notas do aluno.",
            "Fim do programa.",
        ]
    )
    # queria ver se é possivel usar o tamanho da lista depois para definir o fim da resposta
    if resposta == 1:
        arquivo = "cadastro_alunos_matricula.json"
        print(students_functions.coleta_dados_alunos(arquivo))
        # project_interfaces.titulo(f"{resposta}- Cadastrar alunos.")
        # file_path = "cadastro_alunos_matricula.json"

        # if not project_file.verificar_arquivo_existe(file_path):
        #     project_file.criar_arquivo(file_path)

        # nome_aluno = input("Nome do aluno: ").strip().title()
        # while True:
        #     matricula_aluno = project_interfaces.leiaInt(
        #         f"Matrícula do aluno {nome_aluno}: "
        #     )
        #     if any(
        #         matricula_existente["matricula"] == matricula_aluno
        #         for matricula_existente in lista_alunos
        #     ):
        #         print(
        #             f"Matrícula {matricula_aluno} já cadastrada em outro aluno. Por favor, digite outro número de matrícula."
        #         )
        #         print(project_interfaces.linha())
        #     else:
        #         break
        # print(project_interfaces.linha())
        # aluno = students_functions.cadastro_alunos(nome_aluno, matricula_aluno)
        # project_file.append_arquivo(file_path, aluno)
        # print(f"Aluno cadastrado com sucesso")
        # # dados = students_functions.cadastro_alunos(nome_aluno, matricula_aluno)
        # project_file.subscrever_arquivo(file_path, dados)
        # print(f"Arquivo de alunos criado com sucesso em {file_path}")

    elif resposta == 2:
        project_interfaces.titulo(f"{resposta}- Exibir alunos cadastrados:")
    elif resposta == 3:
        project_interfaces.titulo(f"{resposta}- Cadastrar disciplinas.")
    elif resposta == 4:
        project_interfaces.titulo(f"{resposta}- Exibir disciplinas cadastradas:")
    elif resposta == 5:
        project_interfaces.titulo(f"{resposta}- Cadastrar notas por disciplina.")
    elif resposta == 6:
        project_interfaces.titulo(f"{resposta}- Exibir situação de todos os alunos.")
    elif resposta == 7:
        project_interfaces.titulo(
            f"{resposta}- Exibir a situação de um aluno específico."
        )
    elif resposta == 8:
        project_interfaces.titulo(f"{resposta}- Excluir aluno.")
    elif resposta == 9:
        project_interfaces.titulo(f"{resposta}- Trocar notas do aluno.")

    elif resposta == 10:
        project_interfaces.titulo(f"{resposta}- Fim do programa.")
        sleep(1)
        print("Volte sempre.")
        break

    sleep(1)
print(lista_alunos)
