from library.files import path
from library.files import project_file
from library.interface import project_interfaces
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
    dados_disciplinas = project_file.ler_arquivo(subjects_path)
    if dados_disciplinas is None:
        print(
            "Não foi possível carregar os dados das disciplinas. O arquivo não existe ou contém dados inválidos."
        )
    elif len(dados_disciplinas) <= 0:
        print("Ainda não existem disciplinas cadastradas.")
    else:
        print("LISTA DE DISCIPLINAS:")
        for disciplina in dados_disciplinas:
            for key, value in disciplina.items():
                print(f"{key:<5} = {value:>10}", end="  ")
            print()


def associacao_disciplinas_alunos(lista_alunos, lista_disciplinas):
    for aluno in lista_alunos:
        for disciplina in lista_disciplinas:
            if any(
                codigo_existente["codigo"] == disciplina["codigo"]
                for codigo_existente in aluno["disciplina"]
            ):
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


def existem_notas_cadastradas(lista):
    notas_cadastradas = False
    for aluno in lista:
        for disciplina in aluno["disciplina"]:
            if disciplina["notas"]:
                notas_cadastradas = True
                break
        if notas_cadastradas:
            break
    return notas_cadastradas


def cadastro_notas(aluno, codigo_disciplina, nota1, nota2):
    for valor in aluno["disciplina"]:
        if valor["codigo"] == codigo_disciplina:
            valor["notas"] = [nota1, nota2]
            print(
                f"As notas: {valor['notas']} foram cadastras com sucesso para o aluno(a) {aluno['nome']}  em {valor['nome']}"
            )
            valor["media"] = sum(valor["notas"]) / len(valor["notas"])
            situacao_aluno(aluno)
    print("=-" * 50)
    return


def situacao_aluno(aluno):
    for valor in aluno["disciplina"]:
        if len(valor["notas"]) <= 0:
            situacao = "INDEFINIDA"
        else:
            if valor["media"] >= 7:
                situacao = "APROVADO"
            elif valor["media"] >= 5:
                situacao = "RECUPERAÇÃO"
            else:
                situacao = "REPROVADO"
        valor["situacao"] = situacao
    return


def exibir_situacao_aluno(aluno):
    for valor in aluno["disciplina"]:
        print(f"A situação de {aluno['nome']} é: ")
        print(f"{valor['nome']} = {valor['situacao']}")
        print()
    print("-" * 50)
    return


def buscar_disciplina(lista_disciplina, codigo):
    for disciplina in lista_disciplina:
        if disciplina["codigo"] == codigo:
            return disciplina
    return None


def mudar_notas(aluno, disciplina_codigo, nova_nota1, nova_nota2):
    for nota in aluno["disciplina"]:
        if nota["codigo"] == disciplina_codigo:
            nota["notas"] = [nova_nota1, nova_nota2]
            nota["media"] = sum(nota["notas"]) / len(nota["notas"])
            situacao_aluno(aluno)
            return True
    return False
