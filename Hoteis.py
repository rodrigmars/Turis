# -*- coding: utf-8 -*-
""" - """
import json

class Hoteis:
    """ - """
    nome = ""
    gerais = ""
    servicos = []
    hoteis = []

    def __init__(self):

        Hoteis.nome = "rodrigo"
        Hoteis.gerais = "testeaaaaaaaaaaaaaaa"
        Hoteis.servicos = [
            "Recepção 24h",
            "Traslado com Custo Adicional",
            "Estacionamento Gratis",
            "Deposito de Bagagem Gratis",
            "Lavanderia com Custo Adicional",
            "Caixa Eletronico",
            "Sala de Reunioes"]

    def soma_valor(self):
        """ - """
        Hoteis.hoteis = {
            'nome': Hoteis.nome,
            'gerais': Hoteis.gerais,
            'servicos': Hoteis.servicos}

        # print("Hoteis.hoteis:= {}".format(Hoteis.hoteis))
        for key, value in Hoteis.hoteis.items():

            if key == 'servicos':
                for item in value:
                    print("Hoteis.hoteis.servicos:=", item)

            else:
                print("Hoteis.hoteis:= {0} - {1}".format(key, value))

        # print("json", json.dumps(Hoteis.hoteis).encode('utf-8'))

        return " "

    def funcname(self):
        """ - """
        print("funcname")

        return "-"

    def funcname2(self):
        """ - """
        print("funcname")

        return "-"
