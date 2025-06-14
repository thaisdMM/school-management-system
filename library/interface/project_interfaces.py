def leiaInt(msg):
    while True:
        try:
            valor_digitado = input(msg)
            valor_convertido = int(valor_digitado)
        except (ValueError, TypeError):
            print(
                f"\033[0;31mErro! '{valor_digitado}' Por favor digite um número inteiro válido!\033[m"
            )
            continue
        except KeyboardInterrupt:
            print(f"\33[0;31mUsuário preferiu não digitar esse número.\033[m")
            return 0
        else:
            return valor_convertido


def linha(tamanho=50):
    return "-" * tamanho


def titulo(msg):
    tamanho = len(msg) + 4
    print("*" * tamanho)
    print(f"  {msg}")
    print("*" * tamanho)
    return


def menu(lista):
    titulo("MENU DE SISTEMA DE ALUNOS E DISCIPLINAS")
    contador = 1
    for item in lista:
        print(f"\033[33m{contador:2}\033[m - \033[34m{item}\033[m")
        contador += 1
    print(linha())
    while True:
        opcao = leiaInt(
            "\033[32mBem vindo ao programa. Em que podemos ajudar? Digite a opção: \033[m"
        )
        if opcao > 0 and opcao <= len(lista):
            break
        else:
            print(
                f"\033[31mERRO! Opção '{opcao}' inexistente no menu. Escolha de acordo com o menu.\033[m"
            )
    return opcao


def continuar():
    resposta = None
    while resposta == None:
        try:
            continuar = input("Deseja continuar? [S/N] ").strip().upper()[0]
            if continuar not in "NS":
                print("Resposta inválida. Responda S para continuar ou N para parar.")
                resposta = None
            if continuar == "N":
                resposta = False
            if continuar == "S":
                resposta = True
        except (ValueError, TypeError, IndexError, KeyboardInterrupt):
            print("Resposta inválida. Responda S para continuar ou N para parar.")
            resposta = None
    return resposta
