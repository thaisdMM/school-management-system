import os


def absolute_path(file_path):
    # Caminho absoluto da pasta onde este arquivo está localizado
    PASTA_BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    # Se file_path já for um caminho absoluto, retorna ele mesmo
    if os.path.isabs(file_path):
        return file_path
    else:
        # Caso contrário, junta o caminho da pasta base com file_path
        # para formar o caminho absoluto completo até o arquivo
        CAMINHO_ARQUIVO = os.path.join(PASTA_BASE, file_path)
        return CAMINHO_ARQUIVO

caminho2 = "files_create/cadastro_alunos_matricula.json"

absolute_path(caminho2)