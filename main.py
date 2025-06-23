from library.interface import project_interfaces
from library.students import students
from library.files import project_file
from library.subjects import subjects
from library.grades import grades
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
            "Vincular disciplina aos alunos.",
            "Cadastrar notas por disciplina.",
            "Exibir situação de todos os alunos.",
            "Exibir a situação de um aluno específico.",
            "Excluir aluno.",
            "Trocar notas do aluno.",
            "Fim do programa.",
        ]
    )

    if resposta == 1:
        project_interfaces.titulo(f"{resposta}- Cadastrar alunos.")
        students.cadastro_alunos()

    elif resposta == 2:
        project_interfaces.titulo(f"{resposta}- Exibir alunos cadastrados:")
        students.mostrar_alunos()

    elif resposta == 3:
        project_interfaces.titulo(f"{resposta}- Cadastrar disciplinas.")
        subjects.cadastro_disciplinas()

    elif resposta == 4:
        project_interfaces.titulo(f"{resposta}- Exibir disciplinas cadastradas:")
        subjects.mostrar_disciplinas()

    elif resposta == 5:
        project_interfaces.titulo(f"{resposta}- Vincular disciplina aos alunos.")
        subjects.associacao_disciplinas_alunos()

    elif resposta == 6:
        project_interfaces.titulo(f"{resposta}- Cadastrar notas por disciplina.")
        exibir_disciplinas = subjects.mostrar_disciplinas()
        if not exibir_disciplinas:
            continue
        else:
            grades.cadastro_notas_aluno()

    elif resposta == 7:
        project_interfaces.titulo(f"{resposta}- Exibir situação de todos os alunos.")
        grades.exibir_situacao_aluno()
    elif resposta == 8:
        project_interfaces.titulo(
            f"{resposta}- Exibir a situação de um aluno específico."
        )
    elif resposta == 9:
        project_interfaces.titulo(f"{resposta}- Excluir aluno.")
    elif resposta == 10:
        project_interfaces.titulo(f"{resposta}- Trocar notas do aluno.")

    elif resposta == 11:
        project_interfaces.titulo(f"{resposta}- Fim do programa.")
        sleep(1)
        print("Volte sempre.")
        break

    sleep(1)
