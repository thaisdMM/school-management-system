from library.files import project_file
from library.students import students
from library.subjects import subjects
import os


def absolute_path(file_path):
    # Caminho absoluto da pasta onde este arquivo está localizado
    # os.path.dirname usado mais de uma vez para chegar a raiz do projeto e o caminho absoluto ficar correto,
    # > senão iria apontar para essa pasta, sendo que na verdade quero que os arquivos sejam salvos em outra pasta
    PASTA_BASE = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )
    # Se file_path já for um caminho absoluto, retorna ele mesmo
    if os.path.isabs(file_path):
        return file_path
    else:
        # Caso contrário, junta o caminho da pasta base com file_path
        # para formar o caminho absoluto completo até o arquivo
        CAMINHO_ARQUIVO = os.path.join(PASTA_BASE, file_path)
        return CAMINHO_ARQUIVO


def absolute_folder_path():
    folder_name = project_file.folder_name()
    folder_absolute_path = absolute_path(folder_name)
    return folder_absolute_path


def absolute_file_path(file_name):
    folder_path = absolute_folder_path()
    file_path = os.path.join(folder_path, file_name)
    return file_path


def students_absolute_path():
    file_name = students.students_file_name()
    student_path = absolute_file_path(file_name)
    return student_path


def subjects_absolute_path():
    file_name = subjects.subjects_file_name()
    subjects_path = absolute_file_path(file_name)
    return subjects_path
