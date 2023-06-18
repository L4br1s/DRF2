import re
from validate_docbr import CPF


def validate_cpf(cpf):
    validador = CPF()
    return validador.validate(cpf)


def validate_nome(nome):
    return nome.isalpha()


def validate_rg(rg):
    return len(rg) == 9

def LimpaString(string,caract):
    NewString = string
    for x in range(len(caract)):
        NewString = NewString.replace(caract[x], '')
    return NewString

def validate_celular(celular):
    celular = LimpaString(celular,"-)(")
    modelo = re.compile('[\d]{2}[\d]{5}[\d]{4}')
    resposta = re.findall(modelo,celular)
    return resposta
