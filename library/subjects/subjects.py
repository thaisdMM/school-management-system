from library.files import path
from library.files import project_file
from library.interface import project_interfaces
from library.students import students
import os


def subjects_file_name():
    return "cadastro_disciplinas.json"


def coleta_dados_disciplinas():
    subjects_path = path.subjects_absolute_path()
    if not project_file.verificar_arquivo_existe(subjects_path):
        project_file.criar_subscrever_arquivo(subjects_path)
    dados_disciplinas = project_file.ler_arquivo(subjects_path)
    if dados_disciplinas is None:
        dados_disciplinas = []
    return dados_disciplinas


def verificar_nome_disciplina_existe(nome_disciplina, lista_disciplinas):
    if any(
        disciplina_existente["nome"] == nome_disciplina
        for disciplina_existente in lista_disciplinas
    ):
        return True
    return False


def verifica_codigo_disciplina_existe(codigo_disciplina, lista_disciplinas):
    if any(
        codigo_existente["codigo"] == codigo_disciplina
        for codigo_existente in lista_disciplinas
    ):
        return True
    return False


def cadastro_disciplinas():
    subjects_path = path.subjects_absolute_path()
    dados_disciplinas = coleta_dados_disciplinas()
    while True:
        while True:
            nome_disciplina = input("Nome da disciplina: ").strip().title()
            verifica_nome_disciplina = verificar_nome_disciplina_existe(
                nome_disciplina, dados_disciplinas
            )
            if verifica_nome_disciplina:
                print(
                    f"A disciplina {nome_disciplina} já está cadastrada. Por favor digite outro nome de disciplina."
                )
            else:
                break
        while True:
            codigo_disciplina = abs(
                project_interfaces.leia_int(f"Código da disciplina {nome_disciplina}: ")
            )
            verifica_disciplina = verifica_codigo_disciplina_existe(
                codigo_disciplina, dados_disciplinas
            )
            if verifica_disciplina:
                print(
                    f"O código {codigo_disciplina} já está cadastrado em outra disciplina. Por favor digite outro codigo para {nome_disciplina}"
                )
            else:
                break
        disciplina = {"nome": nome_disciplina, "codigo": codigo_disciplina}
        dados_disciplinas.append(disciplina.copy())
        print(
            f"Disciplina: {nome_disciplina}, código: {codigo_disciplina}  cadastrada com sucesso!"
        )
        # associacao_disciplinas_alunos(lista_alunos, [disciplina])
        resposta = project_interfaces.continuar()
        if not resposta:
            project_file.criar_subscrever_arquivo(subjects_path, dados_disciplinas)
            print(f"Arquivo de disciplinas atualizado.")
            break


def mostrar_disciplinas():
    subjects_path = path.subjects_absolute_path()
    conteudo_arquivo_disciplinas = project_file.ler_arquivo(subjects_path)
    if conteudo_arquivo_disciplinas is None:
        print(
            "Não foi possível carregar os dados das disciplinas. O arquivo não existe ou contém dados inválidos."
        )
    # vale pra listas vazias
    elif not conteudo_arquivo_disciplinas:
        print("Ainda não existem disciplinas cadastradas.")
    else:
        print("LISTA DE DISCIPLINAS:")
        for disciplina in conteudo_arquivo_disciplinas:
            for key, value in disciplina.items():
                print(f"{key:<5} = {value:>10} |", end="  ")
            print()


def associacao_disciplinas_alunos():
    students_path = path.students_absolute_path()
    dados_alunos = students.coleta_dados_alunos()
    dados_disciplinas = coleta_dados_disciplinas()
    if not dados_alunos:
        print(
            "Ainda não existem alunos cadastrados. Para associar aluno à disciplinas é necessário cadastrar alunos."
        )
    if not dados_disciplinas:
        print(
            "Ainda não existem disciplinas cadastradas. Para associar aluno à disciplinas é necessário cadastrar disciplinas."
        )
    else:
        modificou_dados = False
        for aluno in dados_alunos:
            for disciplina in dados_disciplinas:
                existe_disciplina = students.buscar_disciplina_do_aluno(
                    disciplina, aluno
                )
                if existe_disciplina:
                    continue
                else:
                    print(
                        f"Quer assossiar ao {aluno['nome']} a disciplina {disciplina['nome']}"
                    )
                    resposta = project_interfaces.continuar()
                    if not resposta:
                        continue
                    else:
                        aluno["disciplina"].append(
                            {
                                "nome": disciplina["nome"],
                                "codigo": disciplina["codigo"],
                                "notas": [],
                                "media": 0.0,
                                "situacao": "INDEFINIDA",
                            }
                        )
                        modificou_dados = True
        # print(dados_alunos)
        if modificou_dados:
            project_file.criar_subscrever_arquivo(students_path, dados_alunos)
        else:
            print(
                "Nenhuma nova disciplina foi adicionada a nenhum aluno ou todos os alunos já possuem as diciplinas existentes cadastradas."
            )


def disciplina_associada_a_algum_aluno(lista_alunos):
    disciplina_existe = False
    for aluno in lista_alunos:
        for disciplina in aluno["disciplina"]:
            if disciplina["codigo"]:
                disciplina_existe = True
                break
        if disciplina_existe:
            break
    return disciplina_existe


def obter_codigo_disciplina_existente_com_loop(conteudo_disciplinas):
    while True:
        codigo_disciplina = project_interfaces.leia_int(
            "Digite o código da disciplina que deseja cadastrar as notas: "
        )
        disciplina_existe = verifica_codigo_disciplina_existe(
            codigo_disciplina, conteudo_disciplinas
        )
        if disciplina_existe:
            return codigo_disciplina
        else:
            print(
                "Código de disciplina inexistente. Por favor digite o código correto."
            )


def buscar_disciplina(lista_disciplina, codigo):
    for disciplina in lista_disciplina:
        if disciplina["codigo"] == codigo:
            return disciplina
    return None
