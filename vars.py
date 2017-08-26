"""
Módulo de busca por períodos de agenda para hotelaria
@autor Rodrigo M Silva
@versão 28/08/2017
-
"""
# import pdb
import sys
# import random
import uuid
from time import sleep, time, strftime
from unittest.mock import MagicMock
from exitstatus import ExitStatus


CONST_NOME = "231231"

class Verificador:
    "-"

    def log(self, mensagem):
        "LOG DE MENSAGENS"
        print("{0}-{1}".format(strftime("%H:%M:%S"), mensagem))

    def gera_cliente(self):
        "GERA CLIENTES PARA INSERÇÃO"
        clientes = [
            {
                'id': uuid.uuid1(),
                'nome': 'Carolina Nina Mirella Pereira',
                'cpf': '246.345.088-69',
                'rg': '41.195.683-8',
                'dataNascimento': '20/11/1995',
                'email': 'carolina_nina@prsea.com.br',
                'cep': '02185-010',
                'telefone': '(11) 3866-1559',
                'celular': '(11) 98961-2230'
            },
            {
                'id': uuid.uuid1(),
                'nome': 'Milena Mariana Luana Campos',
                'cpf': '099.871.788-63',
                'rg': '17.842.152-2',
                'dataNascimento': '11/03/1995',
                'email': 'milena_mariana@trimempresas.com.br',
                'cep': '05181-015',
                'telefone': '(11) 2738-9471',
                'celular': '(11) 99986-0048'
            },
            {
                'id': uuid.uuid1(),
                'nome': 'Beatriz Jennifer Rocha',
                'cpf': '549.092.688-04',
                'rg': '25.903.068-5',
                'dataNascimento': '08/02/1991',
                'email': 'beatriz_j_rocha@mktec.com.br',
                'cep': '03020-020',
                'telefone': '(11) 2617-8122',
                'celular': '(11) 99205-7642'
            }
        ]

        return clientes

    def insere(self, clientes):
        "indexa registros para uma base mongodb"
        Verificador.log(self, str(clientes))

    # @Verificador
    def computa_valores(self):
        "-"
        # pdb.set_trace()
        Verificador.log(self, "-")

        clientes = [
            {
                'id': uuid.uuid1(),
                'nome': 'Carolina Nina Mirella Pereira',
                'cpf': '246.345.088-69',
                'rg': '41.195.683-8',
                'dataNascimento': '20/11/1995',
                'email': 'carolina_nina@prsea.com.br',
                'cep': '02185-010',
                'telefone': '(11) 3866-1559',
                'celular': '(11) 98961-2230'
            }
        ]

        Verificador.log(self, "simulo latência operando uma consulta")

        sleep(0.5)

        Verificador.log(
            self, "Retorna um total de {0} clientes".format(clientes.count()))

        Verificador.log(self, "Inicia análise computacional")


if __name__ == '__main__':

    try:
        V = Verificador()

        CLIENTES = V.gera_cliente()
        TOTAL = CLIENTES.__len__()

        V.log('Total clientes:' + str(TOTAL))

        if TOTAL > 0:
            V.insere(CLIENTES)
        else:
            V.log("Não existem dados para inserção.")
            sys.exit(ExitStatus.success)

        # for i in range(1, 100):
        #     print('i: ', i)

        # V.log("-")
        # print('calculando valores {0}'.format(14**2))

        # T0 = time()

        # V.log("-")
        # print(T0)

        # sleep(5.5)

        # T1 = time()

        # V.log("-")
        # print(T1)

        # V.log("-")
        # print('total time: ', T1 - T0)

    except ValueError:
        V.log("ERROR:" + ValueError)
        sys.exit(ExitStatus.failure)

    V.log('ExitStatus.success' + repr(ExitStatus.success))
    sys.exit(ExitStatus.success)
