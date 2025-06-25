from library.files import project_file
from library.files import path
from library.grades import grades
from library.subjects import subjects


# Função mais genérica que a função abaixo:
# pode ficar melhor se receber uma msg como parametro, pq ai eu posso personalizar a msg de print e usar ela em outros lugares
def verifica_conteudo_arquivo_msg_generica(file_path, msg1, msg2):
    conteudo = project_file.ler_arquivo(file_path)
    if conteudo is None:
        print(msg1)
        return None
    if not conteudo:
        print(msg2)
        return None
    else:
        return conteudo


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


def verificar_integridade_arquivos_alunos_disciplinas():
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
    disciplina_associada_alunos = subjects.disciplina_associada_a_algum_aluno(
        conteudo_arquivo_alunos
    )
    if not disciplina_associada_alunos:
        print(
            "As diciplinas ainda não foram associadas aos alunos. Por favor, primeiro associa as diciplinas que os alunos estão cursando."
        )
        return None, None
    else:
        return conteudo_arquivo_alunos, conteudo_arquivo_disciplinas


def verificar_integridade_dados_para_operacoes_com_notas():
    conteudo_alunos, conteudo_disciplina = (
        verificar_integridade_arquivos_alunos_disciplinas()
    )
    if conteudo_alunos is None or conteudo_disciplina is None:
        return None
    else:
        algum_aluno_com_nota = grades.existe_alguma_nota_cadastrada(conteudo_alunos)
        if not algum_aluno_com_nota:
            print(
                "Ainda não existe nenhuma nota cadastrada a nenhum dos alunos. Por favor cadastre notas primeiro."
            )
            return None
        else:
            return conteudo_alunos, conteudo_disciplina


def verifica_integridade_arquivo_alunos():
    file_path = path.students_absolute_path()
    msg1 = "Não foi possível carregar os dados dos alunos. O arquivo não existe ou contém dados inválidos."
    msg2 = "Ainda não existem alunos cadastrados no arquivo de alunos."
    conteudo = verifica_conteudo_arquivo_msg_generica(file_path, msg1, msg2)
    return conteudo
