from library.files import path
import os
import json


def verificar_arquivo_existe(file_path):
    return os.path.exists(file_path)  # retorna True or False


def verificar_pasta_existe():
    folder_path = path.absolute_folder_path()
    return os.path.isdir(folder_path)  # retorna True or False


def criar_pasta():
    folder_path = path.absolute_folder_path()
    try:
        if not verificar_pasta_existe():
            os.makedirs(folder_path, exist_ok=True)
            return True  # a pasta foi criada
        else:
            return True  # a pasta já existe
    except OSError:
        print("Houve problema(OSError) e a a pasta não pode ser criada.")
        return False
    except Exception:
        print("Houve uma exceção geral e a a pasta não pode ser criada.")
        return False


def criar_subscrever_arquivo(file_path, data=None):
    if data is None:
        data = []
    if not verificar_pasta_existe():
        criar_pasta()
    try:
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
            return True
    except FileNotFoundError:
        print("Arquivo não encontrado")
        return False
    except PermissionError:
        print("Você não tem permissão para criar esse arquivo.")
        return False
    except Exception:
        print("ERRO GERAL na criação/subscrição do arquivo.")
        return False


def append_arquivo(file_path, data):
    try:
        with open(file_path, "a") as append_file:
            json.dump(data, append_file, indent=4)
            return True
    except PermissionError:
        print("Você não tem permissão para criar esse arquivo.")
        return False
    except Exception:
        print("ERRO GERAL no append do arquivo.")
        return False


def ler_arquivo(file_path):
    try:
        with open(file_path, "r") as read_file:
            content = json.load(read_file)
            return content
    except FileNotFoundError:
        print("Arquivo não encontrado")
        return None
    except PermissionError:
        print("Você não tem permissão para criar esse arquivo.")
        return None
    except Exception:
        print("ERRO GERAL na leitura do arquivo.")
        return None
