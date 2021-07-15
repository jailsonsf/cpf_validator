from typing import Tuple


def cpfValidate(cpf):
    if (allDigitsEquals(cpf) == True or has11digits(cpf) == False):
        return False
    else:
        if (validateFirstDigit(cpf)):
            return validateSecondDigit(cpf)

        else:
            return False


def allDigitsEquals(cpf):
    if len(set(cpf)) == 1:
        return True
    else:
        return False


def has11digits(cpf):
    if len(cpf) == 11:
        return True
    else:
        return False


def validateFirstDigit(cpf):
    sum_products = sum(int(a) * b for a, b in zip(cpf, range(10, 1, -1)))

    res = (sum_products * 10) % 11

    if (int(cpf[-2]) == res):
        return True
    else:
        return False


def validateSecondDigit(cpf):
    sum_products = sum(int(a) * b for a, b in zip(cpf, range(11, 1, -1)))

    res = (sum_products * 10) % 11

    if (int(cpf[-1]) == res):
        return True
    else:
        return False
