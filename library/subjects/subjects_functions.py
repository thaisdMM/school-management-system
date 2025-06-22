from library.files import path
from library.files import project_file
from library.interface import project_interfaces
from library.students import students_functions
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
    dados_alunos = students_functions.coleta_dados_alunos()
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
                existe_disciplina = students_functions.buscar_disciplina_do_aluno(
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


# Função mais genérica que a função abaixo, ver se ela terá utilidade no futuro ou apagar
def verifica_conteudo_arquivo(file_path):
    conteudo = project_file.ler_arquivo(file_path)
    if conteudo is None:
        print(
            "Não foi possível carregar os dados dos alunos e/ou disciplinas. O arquivo não existe ou contém dados inválidos."
        )
        return None
    if not conteudo:
        print(
            "Ainda não existem disciplinas e/ou alunos cadastradas. Primeiro cadastre disciplina e/ou aluno."
        )
        return None
    else:
        return conteudo


def verifica_conteudo_arquivos_alunos_disciplinas():
    students_path = path.students_absolute_path()
    subjects_path = path.subjects_absolute_path()
    conteudo_arquivo_alunos = project_file.ler_arquivo(students_path)
    conteudo_arquivo_disciplinas = project_file.ler_arquivo(subjects_path)
    if conteudo_arquivo_alunos is None or conteudo_arquivo_disciplinas is None:
        print(
            "Não foi possível carregar os dados dos alunos e/ou disciplinas. O arquivo não existe ou contém dados inválidos."
        )
        return None, None
    if not conteudo_arquivo_disciplinas or not conteudo_arquivo_alunos:
        print(
            "Ainda não existem disciplinas e/ou alunos cadastradas. Primeiro cadastre disciplina e/ou aluno."
        )
        return None, None
    disciplina_associada_alunos = disciplina_associada_a_algum_aluno(
        conteudo_arquivo_alunos
    )
    if not disciplina_associada_alunos:
        print(
            "As diciplinas ainda não foram associadas aos alunos. Por favor, primeiro associa as diciplinas que os alunos estão cursando."
        )
        return None, None
    else:
        return conteudo_arquivo_alunos, conteudo_arquivo_disciplinas


def coleta_notas():
    nota1 = project_interfaces.leia_float("NOTA 1= ")
    nota2 = project_interfaces.leia_float("NOTA 2= ")
    notas = valida_notas(nota1, nota2)
    if notas:
        return nota1, nota2
    else:
        return None


# return True or False
def valida_notas(nota1, nota2):
    return 0 <= nota1 <= 10 and 0 <= nota2 <= 10


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


def cadastro_notas_aluno():
    students_path = path.students_absolute_path()
    conteudo_alunos, conteudo_disciplinas = (
        verifica_conteudo_arquivos_alunos_disciplinas()
    )
    if conteudo_alunos is None or conteudo_disciplinas is None:
        return
    else:
        codigo_disciplina = obter_codigo_disciplina_existente_com_loop(
            conteudo_disciplinas
        )
        if codigo_disciplina:
            modificou_dados = False
            for aluno in conteudo_alunos:
                sair_cadastro = False
                for disciplina in aluno["disciplina"]:
                    if disciplina["codigo"] == codigo_disciplina:
                        if disciplina["notas"]:
                            continue
                        else:
                            # salvar_dados = False
                            print(
                                f"Quer cadastrar notas do aluno {aluno['nome']} para a disciplina {disciplina['nome']}"
                            )
                            resposta = project_interfaces.continuar()
                            if not resposta:
                                continue
                            else:
                                while True:
                                    try:
                                        notas = coleta_notas()
                                    except KeyboardInterrupt:
                                        salvar_dados = None
                                        if not modificou_dados:
                                            sair_cadastro = True
                                            print(
                                                "Finalizando o progama sem salvar dados"
                                            )
                                            salvar_dados = False
                                            break
                                        else:

                                            escolha = (
                                                input(
                                                    "Voce escolheu sair do cadastro de notas, quer salvar os dados digitados? Digite S para salvar "
                                                )
                                                .strip()
                                                .upper()[0]
                                            )
                                            if escolha == "S":
                                                salvar_dados = True
                                                # project_file.criar_subscrever_arquivo(
                                                #     students_path, conteudo_alunos
                                                # )
                                                sair_cadastro = True
                                                break
                                            else:
                                                salvar_dados = False
                                                sair_cadastro = True
                                                break

                                    else:
                                        if notas is None:
                                            print(
                                                "Notas inválidas. A nota tem que ser entre 0 e até 10."
                                            )
                                        elif notas:
                                            nota1, nota2 = notas
                                            disciplina["notas"] = [nota1, nota2]
                                            print(
                                                f"As notas: {disciplina['notas']} foram cadastras com sucesso para o aluno(a) {aluno['nome']}  em {disciplina['nome']}"
                                            )
                                            modificou_dados = True
                                            break
                    if sair_cadastro:
                        break
                if sair_cadastro:
                    break
        if sair_cadastro:
            if salvar_dados:
                project_file.criar_subscrever_arquivo(students_path, conteudo_alunos)
                print("Dados de cadastro de notas salvos até o momento.")
            else:
                print("Não foram adicionadas novas notas a nenhum aluno.")

        else:
            if modificou_dados:
                project_file.criar_subscrever_arquivo(students_path, conteudo_alunos)
                print("Notas salvas no arquivo de cadastro de alunos.")
            else:
                print("Não foram adicionadas novas notas a nenhum aluno.")


def existe_alguma_nota_cadastrada(arquivo_alunos):
    notas_cadastradas = False
    for aluno in arquivo_alunos:
        for disciplina in aluno["disciplina"]:
            if disciplina["notas"]:
                notas_cadastradas = True
                break
        if notas_cadastradas:
            break
    return notas_cadastradas


def media_notas(disciplina):
    media = sum(disciplina["notas"]) / len(disciplina["notas"])
    return media


def situacao_aluno(media):
    if not media:
        return "INDEFINIDA"
    elif media >= 7:
        return "APROVADO"
    elif media >= 5:
        return "RECUPERAÇÃO"
    else:
        return "REPROVADO"


# Nesse código genérico a gente passa como a chave do dicionário como está no dicionário ex: "media", "notas"
# A função como é passada como argumento, não leva parenteses e nem os parametros dentro dela
def atualizar_valor_das_disciplinas_aluno(
    lista_alunos, chave_alvo_atualizacao, funcao_calculo_atualizacao
):
    modificou_conteudo = False
    for aluno in lista_alunos:
        for disciplina in aluno["disciplina"]:
            if len(disciplina["notas"]) <= 0:
                continue
            valor_atual = disciplina.get(chave_alvo_atualizacao)
            valor_calculado = funcao_calculo_atualizacao(disciplina)
            if valor_atual != valor_calculado:
                disciplina[chave_alvo_atualizacao] = valor_calculado
                modificou_conteudo = True
    return modificou_conteudo


def definir_media_situação_aluno():
    file_path = path.students_absolute_path()
    conteudo_alunos = verifica_conteudo_arquivo(file_path)
    modificou_arquivo = False
    nota_media_alunos = atualizar_valor_das_disciplinas_aluno(
        conteudo_alunos, "media", media_notas
    )
    if nota_media_alunos:
        modificou_arquivo = True
    # aqui no caso da lambda ela é a função, disciplina(dicinário nesse codigo) é o parâmetro e o
    # retorno : é o valor que será atribuído à chave indicada.
    # Para essa disciplina, calcule a média atual e me diga a situação.
    atualizar_situacao_aluno = atualizar_valor_das_disciplinas_aluno(
        conteudo_alunos,
        "situacao",
        lambda disciplina: situacao_aluno(disciplina["media"]),
    )
    if atualizar_situacao_aluno:
        modificou_arquivo = True
    if modificou_arquivo:
        project_file.criar_subscrever_arquivo(file_path, conteudo_alunos)
        return True
    else:
        return False


def verificar_dados_arquivos():
    conteudo_alunos, conteudo_disciplina = (
        verifica_conteudo_arquivos_alunos_disciplinas()
    )
    if conteudo_alunos is None or conteudo_disciplina is None:
        return None
    else:
        algum_aluno_com_nota = existe_alguma_nota_cadastrada(conteudo_alunos)
        if not algum_aluno_com_nota:
            print(
                "Ainda não existe nenhuma nota cadastrada a nenhum dos alunos. Por favor cadastre notas primeiro."
            )
            return None
        else:
            return conteudo_alunos, conteudo_disciplina


def modificar_dados_media_situacao():
    conteudo = verificar_dados_arquivos()
    if conteudo is None:
        return None
    else:
        definir_media_situação_aluno()
    file_path = path.students_absolute_path()
    conteudo = project_file.ler_arquivo(file_path)
    return conteudo


def exibir_situacao_aluno():
    conteudo_alunos = modificar_dados_media_situacao()
    if conteudo_alunos is None:
        return None
    else:
        aluno_sem_disciplina = False
        for aluno in conteudo_alunos:
            if not aluno["disciplina"]:
                aluno_sem_disciplina = True
                continue
            for disciplina in aluno["disciplina"]:
                print(f"A situação de {aluno['nome']} é: ")
                print(f"{disciplina['nome']} = {disciplina['situacao']}")
                print()

        if aluno_sem_disciplina:
            print(
                "Existem alunos(as) que ainda não possuem disciplina(s) e nem nota(s) vinculadas."
            )


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
