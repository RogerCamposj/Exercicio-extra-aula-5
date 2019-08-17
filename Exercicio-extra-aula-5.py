n = input('Cheque aqui se seu número de celular está correto ou se você tem amnézia: ')


def checagem(n):
    if n[0] == '9' and len(n) == 9:
        print('Número Válido')
    else:
        print("""
        NÚMERO INVÁLIDO,
        Número deve começar com "9" e conter 9 digitos no total.""")


if n:
    checagem(n)
