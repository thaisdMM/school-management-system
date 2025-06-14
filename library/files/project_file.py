import os
import json


def verificar_arquivo_existe(file_path):
    return os.path.exists(file_path)  # retorna True or False


# def criar_arquivo(file_path):
#     data = []
#     try:
#         with open(file_path, "x") as file:
#             pass
#     except FileExistsError:
#         print(f"O arquivo já existe")
#     except PermissionError:
#         print(f"Você não tem permissão para criar esse arquivo.")


def criar_subscrever_arquivo(file_paht, data=None):
    if data is None:
        data = []
    try:
        with open(file_paht, "w") as file:
            json.dump(data, file, indent=4)
            return True
    except FileNotFoundError:
        print("Arquivo não encontrado")
        return False
    except PermissionError:
        print("Você não tem permissão para criar esse arquivo.")
        return False


def append_arquivo(file_path, data):
    try:
        with open(file_path, "a") as append_file:
            json.dump(data, append_file, indent=4)
            return True
    except PermissionError:
        print("Você não tem permissão para criar esse arquivo.")
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


# def verificar_arquivo_existe(file_path):
#     try:
#         with open(file_path, 'x') as file:
#             print(f"O arquivo foi criado em {file_path}")
#     except FileExistsError:
#         print(f"O arquivo já existe.")
#     except PermissionError:
#         print(f"Você não tem acesso para criar esse arquivo.")
