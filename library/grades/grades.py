from library.interface import project_interfaces
from library.files import path
from library.files import data_validation
from library.subjects import subjects
from library.files import project_file
from library.students import students


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


def cadastro_notas_aluno():
    students_path = path.students_absolute_path()
    conteudo_alunos, conteudo_disciplinas = (
        data_validation.verificar_integridade_arquivos_alunos_disciplinas()
    )
    if conteudo_alunos is None or conteudo_disciplinas is None:
        return
    else:
        codigo_disciplina = subjects.obter_codigo_disciplina_existente_com_loop(
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


def existe_alguma_nota_cadastrada(lista_alunos):
    notas_cadastradas = False
    for aluno in lista_alunos:
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
    conteudo_alunos = data_validation.verifica_conteudo_arquivo(file_path)
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


def modificar_dados_media_situacao():
    conteudo = data_validation.verificar_integridade_dados_para_operacoes_com_notas()
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


def buscar_notas_por_disciplina(aluno: dict, disciplina_codigo: int):
    for disciplina in aluno["disciplina"]:
        if disciplina["codigo"] == disciplina_codigo:
            return disciplina
        else:
            continue
    return False


def controlar_mudanca_notas_aluno():
    file_path = path.students_absolute_path()
    conteudo_arquivos = (
        data_validation.verificar_integridade_dados_para_operacoes_com_notas()
    )
    sair_cadastro = None
    if conteudo_arquivos is None:
        return None
    # if conteudo_arquivos is not None:
    else:
        lista_alunos, lista_disciplinas = conteudo_arquivos
        modificou_dados = None
        while True:
            ficar_loop = project_interfaces.continuar()
            if not ficar_loop:
                break
            else:
                aluno_buscado = students.verifica_dados_aluno_específico(lista_alunos)

                if not aluno_buscado:
                    continue
                elif not aluno_buscado["disciplina"]:
                    print(
                        f"O aluno {aluno_buscado['nome']} não possui nenhuma disciplina cadastrada."
                    )
                    print(
                        f"Ainda quer mudar as notas de algum(a) aluno(a) ou deseja sair do cadastro de notas?"
                    )
                    continue
                else:
                    print(f"Aluno(a): {aluno_buscado['nome']}")
                    codigo_disciplina = (
                        subjects.obter_codigo_disciplina_existente_com_loop(
                            lista_disciplinas
                        )
                    )
                    if codigo_disciplina:

                        disciplina_existe = buscar_notas_por_disciplina(
                            aluno_buscado, codigo_disciplina
                        )
                        if not disciplina_existe:
                            print(
                                f"A disciplina existe, mas não está vinculada ao aluno {aluno_buscado['nome']}."
                            )
                            print(
                                f"Ainda quer mudar as notas de algum(a) aluno(a) ou deseja sair do cadastro de notas?"
                            )
                            continue

                        else:
                            print(
                                f"Disciplina: {disciplina_existe['nome']}, notas atuais: {disciplina_existe['notas']}. Deseja mudar as notas dessa disciplina?"
                            )

                        resposta = project_interfaces.continuar()
                        if not resposta:
                            break
                        else:
                            while True:
                                try:
                                    novas_notas = coleta_notas()
                                except KeyboardInterrupt:
                                    salvar_dados = None
                                    if not modificou_dados:
                                        sair_cadastro = True
                                        print("Finalizando o progama sem salvar dados")
                                        salvar_dados = False
                                        break
                                    else:
                                        escolha = (
                                            input(
                                                "Voce escolheu sair da alteração de notas, quer salvar os dados digitados? Digite S para salvar "
                                            )
                                            .strip()
                                            .upper()[0]
                                        )
                                        if escolha == "S":
                                            salvar_dados = True
                                            sair_cadastro = True
                                            break
                                        else:
                                            salvar_dados = False
                                            sair_cadastro = True
                                            break

                                else:
                                    if novas_notas is None:
                                        print(
                                            "Notas inválidas. A nota tem que ser entre 0 e até 10."
                                        )
                                    elif novas_notas:
                                        nova_nota1, nova_nota2 = novas_notas
                                        disciplina_existe["notas"] = [
                                            nova_nota1,
                                            nova_nota2,
                                        ]
                                        print(
                                            f"As novas notas: {disciplina_existe['notas']} foram cadastras com sucesso para o aluno(a) {aluno_buscado['nome']}  em {disciplina_existe['nome']}"
                                        )
                                        modificou_dados = True
                                        break

    if sair_cadastro:
        if salvar_dados:
            project_file.criar_subscrever_arquivo(file_path, lista_alunos)
            print("Dados de cadastro de novas notas salvos até o momento.")
        else:
            print("Não foram adicionadas novas notas a nenhum aluno.")

    else:
        if modificou_dados:
            project_file.criar_subscrever_arquivo(file_path, lista_alunos)
            print("Notas salvas no arquivo de cadastro de alunos.")
        else:
            print("Não foram adicionadas novas notas a nenhum aluno.")
