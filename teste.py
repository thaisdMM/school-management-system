from library.files import path
from library.files import project_file


caminho2 = "files_created/cadastro_alunos_matricula.json"

arquivo = path.absolute_path(caminho2)
print(arquivo)
conteudo = project_file.ler_arquivo(arquivo)
print(conteudo)


# caminho2 = "files_created/cadastro_alunos_matricula.json"
# arquivo = path.absolute_path(caminho2)
# new_file = project_file.criar_subscrever_arquivo(arquivo)

# print(new_file)
# conteudo = project_file.ler_arquivo(new_file)
# print(conteudo)
