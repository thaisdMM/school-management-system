def cadastro_disciplinas(lista_disciplinas, nome_disciplina, codigo_disciplina):
    disciplina = {"nome": nome_disciplina, "codigo": codigo_disciplina}
    lista_disciplinas.append(disciplina.copy())
    associacao_disciplinas_alunos(lista_alunos, [disciplina])
    print(
        f"Disciplina: {nome_disciplina} cadastrada com sucesso com o código {codigo_disciplina}"
    )
    print("=-" * 50)
    return


def mostrar_disciplinas(lista_disciplinas):
    print("LISTA DE DISCIPLINAS:")
    print()
    if len(lista_disciplinas) <= 0:
        print("Ainda não existem disciplinas cadastradas.")
    else:
        for disciplina in lista_disciplinas:
            for key, value in disciplina.items():
                print(f"{key:<5} = {value}", end="  ")
            print()
    print("=-" * 50)


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
