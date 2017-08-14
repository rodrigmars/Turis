# -*- coding: iso-8859-1 -*-
"""
Módulo para obter custo de hospedagem
"""
import Hoteis as H

# import math
# from math import ceil, floor
IMPOSTO = 0.15

def calcula_custohospedagem(valor=0):
    """
    Retorna calculo de viagem.
    """
    try:
        valor_as_float = float(float(valor) * IMPOSTO)

        if valor_as_float >= 25.0:
            raise ValueError('O cálculo total sob imposto é superior ao permitido', valor_as_float)

    except ValueError as error:
        print("Erro:=", error.args)
        valor_as_float = 0.0

    return valor_as_float


def main():
    """ Obtém resultado sob cálculo de imposto para custo de viagem """
    hotel = H.Hoteis()

    print("json hotel: ", hotel.soma_valor())
    #input_as_float = float(input("Informe um valor: "))
    resultado_as_float = float(calcula_custohospedagem(180))

    print('Cálculo total:= {0}'.format(resultado_as_float))

main()
