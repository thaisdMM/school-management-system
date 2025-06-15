from library.files import path
from library.files import project_file
from library.students import students_functions


# caminho2 = "files_created/cadastro_alunos_matricula.json"

# arquivo = path.absolute_path(caminho2)
# print(arquivo)
# conteudo = project_file.ler_arquivo(arquivo)
# print(conteudo)

# caminho2 = "files_created/cadastro_alunos_matricula.json"
# arquivo = path.absolute_path(caminho2)
# new_file = project_file.criar_subscrever_arquivo(arquivo)

# print(new_file)
# conteudo = project_file.ler_arquivo(new_file)
# print(conteudo)

arquivo_estudantes = students_functions.students_file_name()
print(arquivo_estudantes)
caminho_absoluto_arquivo = path.absolute_file_path(arquivo_estudantes)
print(caminho_absoluto_arquivo)
print(project_file.verificar_arquivo_existe(caminho_absoluto_arquivo))
print(project_file.verificar_pasta_existe())

dados_alunos = students_functions.coleta_dados_alunos()
print(dados_alunos)
