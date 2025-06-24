from library.subjects import subjects
from library.files import project_file
from library.interface import project_interfaces
from library.files import path
from library.files import data_validation


def students_file_name():
    return "cadastro_alunos.json"


def coleta_dados_alunos():
    file_path = path.students_absolute_path()
    if not project_file.verificar_arquivo_existe(file_path):
        project_file.criar_subscrever_arquivo(file_path)
    dados_alunos = project_file.ler_arquivo(file_path)
    if dados_alunos is None:
        dados_alunos = []
    return dados_alunos


def verifica_matricula_existente(matricula: int, lista_alunos) -> bool:
    # any() com lista vazia: seguro, retorna False, não quebra o código - nao precisa tratar esse caso
    if any(
        matricula_existente["matricula"] == matricula
        for matricula_existente in lista_alunos
    ):
        return True
    return False


def cadastro_alunos():
    file_path = path.students_absolute_path()
    dados_alunos = coleta_dados_alunos()
    while True:
        nome_aluno = input("Nome do aluno: ").strip().title()
        while True:
            matricula_aluno = abs(
                project_interfaces.leia_int(f"Matrícula do aluno {nome_aluno} ")
            )
            matricula = verifica_matricula_existente(matricula_aluno, dados_alunos)
            if not matricula:
                aluno = {
                    "nome": nome_aluno,
                    "matricula": matricula_aluno,
                    "disciplina": [],
                }
                break
            print(
                f"Matrícula {matricula_aluno} já cadastrada em outro aluno. Digite outra matrícula para o aluno {nome_aluno}"
            )
        dados_alunos.append(aluno.copy())
        print(
            f"Aluno: {aluno['nome']}, matricula: {aluno['matricula']} cadastrado com sucesso!"
        )
        print("-" * 60)
        decisao = project_interfaces.continuar()
        # quando o loopoing finalizar - salvar os dados no arquivo:
        if not decisao:
            project_file.criar_subscrever_arquivo(file_path, dados_alunos)
            break


def mostrar_alunos():
    dados_arquivo = data_validation.verifica_integridade_arquivo_alunos()
    if dados_arquivo is None:
        return None
    else:
        print("LISTA DE ALUNOS:\n".center(30))
        for aluno in dados_arquivo:
            print(f"{aluno['nome']:<30}| matrícula: {aluno['matricula']:>10}", end="")
            print()
            print("-" * 60)


# retorna True no primeiro momento que encontrar e encerra ou False se não encontrar
def buscar_disciplina_do_aluno(codigo_disciplina: int, aluno: dict):
    return any(
        codigo_existente["codigo"] == codigo_disciplina["codigo"]
        for codigo_existente in aluno["disciplina"]
    )


def buscar_aluno(lista_alunos, matricula):
    for aluno in lista_alunos:
        if aluno["matricula"] == matricula:
            return aluno
    return None


def exibir_dados_aluno(aluno: dict):
    for key, value in aluno.items():
        print(f"{key:<10} = {value}")


def verifica_dados_aluno_específico(lista_alunos):
    if lista_alunos is None:
        return None
    else:
        matricula_aluno = abs(
            project_interfaces.leia_int("Digite a matrícula do aluno: ")
        )
        aluno_existe = buscar_aluno(lista_alunos, matricula_aluno)
        if aluno_existe is None:
            print(
                "Não há aluno com a matrícula pesquisada. Digite a matrícula correta do aluno."
            )
            return False
        else:
            return aluno_existe


def mostrar_dados_aluno_apos_validacao():
    lista_alunos = data_validation.verifica_integridade_arquivo_alunos()
    if lista_alunos is None:
        return
    while True:
        aluno_selecionado = verifica_dados_aluno_específico(lista_alunos)
        if aluno_selecionado:
            print(f"Dados do aluno(a): {aluno_selecionado['nome']}")
            exibir_dados_aluno(aluno_selecionado)
            print("Deseja continuar exibindo dados de algum aluno(a) especifico?")
            continuar = project_interfaces.continuar()
            if not continuar:
                break


def excluir_aluno(lista, aluno):
    if aluno is None:
        return False
    else:
        lista.remove(aluno)
        return True


# preciso tratar a melhor forma de sair da função, pois só depois de entrar na matricula correta que sai.
# > Talvez tratar o keyboardinterrupt, ou dar a opção de saida quando digitar a matricula errada...
def controlar_exclusao_aluno_apos_validacao():
    students_path = path.students_absolute_path()
    lista_alunos = data_validation.verifica_integridade_arquivo_alunos()
    if lista_alunos is None:
        return
    modificou_arquivo = False
    while True:
        if not lista_alunos:
            break
        aluno_selecionado = verifica_dados_aluno_específico(lista_alunos)
        if aluno_selecionado:
            resposta = (
                input(
                    f"Deja excluir o aluno {aluno_selecionado['nome']}? S para excluir N para não excluir: "
                )
                .strip()
                .upper()[0]
            )
            if resposta == "S":
                excluir_aluno(lista_alunos, aluno_selecionado)
                print(f"Aluno {aluno_selecionado['nome']} excluido com sucesso!")
                print(project_interfaces.linha())
                modificou_arquivo = True
                continue
            else:
                continuar = project_interfaces.continuar()
                if continuar:
                    continue
                else:
                    break
    if not modificou_arquivo:
        print("Nenhum aluno foi excluido!")
        return False
    if modificou_arquivo:
        project_file.criar_subscrever_arquivo(students_path, lista_alunos)
        print("Arquvo de alunos salvo após a exclusão de aluno.")
