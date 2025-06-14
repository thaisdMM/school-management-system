
# PROGRAMA PRINCIPAL:
lista_alunos = []
lista_disciplinas = []
linha1 = "-" * 70

while True:
    print(
        """
    MENU PROGRAMA DE ALUNOS E DISCIPLINAS

    1- Cadastrar alunos.
    2- Exibir alunos cadastrados.
    3- Cadastrar disciplinas.
    4- Exibir disciplinas cadastradas.
    5- Cadastrar notas por disciplina.
    6- Exibir situação de todos os alunos.
    7- Exibir a situação de um aluno específico.
    8- Excluir aluno.
    9- Trocar notas do aluno.
    10- Fim do programa.
    """
    )
    while True:
        resposta = input(
            "Bem vindo ao programa. Em que podemos ajudar? Digite a opção: "
        ).strip()
        if not resposta.isnumeric():
            print("Resposta inválida! Digite de acordo com o menu.")
        else:
            resposta = int(resposta)
            if 0 < resposta <= 10:
                break
            else:
                print("Resposta inválida! Escolha de acordo com o menu.")
        print(linha1)

    if resposta == 1:
        titulo("1- Cadastrar alunos.")
        nome_aluno = input("Nome do aluno: ").strip().title()
        while True:
            matricula_aluno = int(input(f"Matrícula do aluno {nome_aluno}: "))
            # fazer uma validação se não for número.
            if any(
                matricula_existente["matricula"] == matricula_aluno
                for matricula_existente in lista_alunos
            ):
                print(
                    f"Matrícula {matricula_aluno} já cadastrada em outro aluno. Por favor, digite outro número de matrícula."
                )
                print(linha1)
            else:
                break
        print(linha1)
        cadastro_alunos(lista_alunos, nome_aluno, matricula_aluno)

    if resposta == 2:
        titulo("2- Exibir alunos cadastrados:")
        mostrar_alunos(lista_alunos)

    if resposta == 3:
        titulo("2- Cadastrar disciplinas.")
        while True:
            nome_disciplina = input("Nome da disciplina: ").strip().title()
            if any(
                disciplina_existente["nome"] == nome_disciplina
                for disciplina_existente in lista_disciplinas
            ):
                print(
                    f"A disciplina {nome_disciplina} já está cadastrada. Por favor digite outra disciplina."
                )
                print(linha1)
            else:
                break
        while True:
            # quero limitar o codigo a apenas 3 digitos
            # quero importar depois a função leiaInt() que eu fiz, para aceitar só valores numéricos
            codigo_disciplina = int(input(f"Código da disciplina {nome_disciplina}: "))
            pesquisar_disciplina = buscar_disciplina(
                lista_disciplinas, codigo_disciplina
            )
            if pesquisar_disciplina:
                print(
                    f"O código {codigo_disciplina} já está cadastrada em outra disciplina. Por favor digite outro código."
                )
                print(linha1)

            else:
                break
        cadastro_disciplinas(lista_disciplinas, nome_disciplina, codigo_disciplina)

    if resposta == 4:
        titulo("4- Exibir disciplinas cadastradas:")
        mostrar_disciplinas(lista_disciplinas)

    if resposta == 5:
        titulo("5- Cadastrar notas por disciplina:")
        mostrar_alunos(lista_alunos)
        mostrar_disciplinas(lista_disciplinas)
        if len(lista_disciplinas) <= 0 or len(lista_alunos) <= 0:
            print(
                "Ainda não existem disciplinas e/ou alunos cadastradas. Primeiro cadastre disciplina e/ou aluno."
            )
        else:
            while True:
                codigo_disciplina = int(
                    input(
                        "Digite o código da disciplina que deseja cadastrar as notas: "
                    )
                )
                disciplina_existe = buscar_disciplina(
                    lista_disciplinas, codigo_disciplina
                )
                if disciplina_existe:
                    break
                else:
                    print(
                        "Código de disciplina inexistente. Por favor digite o código correto."
                    )
            for aluno in lista_alunos:
                for disciplina in aluno["disciplina"]:
                    if disciplina["codigo"] == codigo_disciplina:
                        if len(disciplina["notas"]) > 0:
                            continue
                        else:

                            print(
                                f"Notas de {aluno['nome']} na disciplina {disciplina['nome']}:"
                            )
                            nota1 = float(input("1ª nota: "))
                            nota2 = float(input("2ª nota: "))
                            print(linha1)
                            cadastro_notas(aluno, codigo_disciplina, nota1, nota2)
                            print(linha1)

    if resposta == 6:
        titulo("6- Exibir situação de todos os alunos:")
        if len(lista_alunos) <= 0 or len(lista_disciplinas) <= 0:
            print(
                "Ainda não existem disciplinas e/ou alunos cadastradas. Primeiro cadastre disciplina e/ou aluno e notas."
            )
        else:
            # notas_cadastradas = False
            # for aluno in lista_alunos:
            #     for disciplina in aluno["disciplina"]:
            #         if disciplina["situacao"] != "INDEFINIDA":
            #             notas_cadastradas = True
            #             break
            #     if notas_cadastradas:
            #         break

            notas_existem = existem_notas_cadastradas(lista_alunos)

            if notas_existem:
                for aluno in lista_alunos:
                    exibir_situacao_aluno(aluno)
            if not notas_existem:
                print(
                    "Todos os alunos não possuem notas ainda. Cadastre as notas dos alunos."
                )

    if resposta == 7:
        titulo("7- Exibir a dados de um aluno específico:")
        mostrar_alunos(lista_alunos)
        matricula_pesquisada = int(
            input("Digite a matrícula do aluno que deseja ver os dados: ")
        )
        exibir_dados_alunos(lista_alunos, matricula_pesquisada)

    if resposta == 8:
        titulo("Excluir aluno:")
        if len(lista_alunos) <= 0:
            print(
                "Lista de alunos vazia. Para excluir algum aluno é necessário que haja alunos cadastrados na lista primeiro."
            )
        else:
            mostrar_alunos(lista_alunos)
            matricula_pesquisada = int(
                input("Digite a matrícula do aluno que deseja excluir os dados: ")
            )
            aluno_buscado = buscar_aluno(lista_alunos, matricula_pesquisada)
            if aluno_buscado is None:
                print(
                    f"Não há aluno com a matrícula = {matricula_pesquisada}. Verifique a matrícula do aluno para efetuar a exclusão."
                )
            else:
                while True:
                    usuario = (
                        input(
                            f"Você irá excluir da lista de alunos o aluno {aluno_buscado['nome']}, matricula {aluno_buscado['matricula']}. Digite S para excluir ou N para não excluir e sair. "
                        )
                        .strip()
                        .upper()[0]
                    )
                    if usuario == "N":
                        print("Não foi feita a exclusão.")
                        break
                    if usuario == "S":
                        exclusao_aluno = excluir_aluno(lista_alunos, aluno_buscado)
                        if exclusao_aluno:
                            print(f"Aluno removido com sucesso.")
                        else:
                            print("Aluno não existe ou não pode ser removido.")
                        break
                    else:
                        print("Resposta inválida. Digite S ou N.")
                    print(linha1)
        print("=-" * 50)

    if resposta == 9:
        titulo("9- Trocar notas do aluno.")
        if len(lista_disciplinas) <= 0 or len(lista_alunos) <= 0:
            print(
                "Ainda não existem disciplinas e/ou alunos cadastradas. Primeiro cadastre disciplina e/ou aluno."
            )
        else:
            notas = existem_notas_cadastradas(lista_alunos)
            if not notas:
                print(
                    "Todos os alunos não possuem notas ainda. Cadastre as notas dos alunos antes de fazer alguma mudança nas notas."
                )
            else:
                mostrar_alunos(lista_alunos)
                matricula_pesquisada = int(
                    input("Digite a matrícula do aluno que deseja trocar as notas: ")
                )
                aluno_existe = buscar_aluno(lista_alunos, matricula_pesquisada)
                if aluno_existe is None:
                    print(
                        f"Não há aluno com a matrícula = {matricula_pesquisada}. Verifique a matrícula do aluno para efetuar a troca de notas."
                    )
                else:
                    mostrar_disciplinas(lista_disciplinas)
                    codigo_existe = int(
                        input(
                            "Qual o código da disciplina que deseja alterar as notas? "
                        )
                    )
                    disciplina_existe = buscar_disciplina(
                        lista_disciplinas, codigo_existe
                    )
                    if not disciplina_existe:
                        print(
                            "Código de disciplina inexistente. Por favor digite o código correto."
                        )
                    else:
                        # fazer uma função para quando a disciplina escolhida não tiver notas
                        print(f"{aluno_existe['nome']}")
                        nova_nota1 = float(
                            input(f"{disciplina_existe['nome']} nova nota 1: ")
                        )
                        nova_nota2 = float(
                            input(f"{disciplina_existe['nome']} nova nota 2: ")
                        )
                        mudar_notas(aluno_existe, codigo_existe, nova_nota1, nova_nota2)
                        print(linha1)

    if resposta == 10:
        print("Volte sempre.")
        print(linha1)
        break

print("\nPrograma finalizado!")
