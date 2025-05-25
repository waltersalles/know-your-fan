def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    for i in [9, 10]:
        soma = sum(int(cpf[j]) * ((i + 1) - j) for j in range(i))
        verificador = (soma * 10 % 11) % 10
        if verificador != int(cpf[i]):
            return False
    return True
