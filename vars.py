"""
Módulo de busca por períodos de agenda para hotelaria
@autor Rodrigo M Silva
@versão 28/08/2017
-
"""
# import pdb
import sys
from exitstatus import ExitStatus
from time import sleep, time, strftime


CONST_NOME = "231231"


class Verificador:

    def log(self):

        print(strftime("%H:%M:%S"))

    # @Verificador
    def testeAAAA(self):

        # pdb.set_trace()
        Verificador.log(self)

        nome = "TESTE COM AAA - "
        print(nome)

        nome = 1521

        sleep(0.5)

        nome = "processou aqui em"
        print(nome)

        Verificador.log(self)


if __name__ == '__main__':

    try:
        V = Verificador()
        # log(self)

        # for i in range(1, 100):
        #     print('i: ', i)

        V.log()
        print('calculando valores {0}'.format(14**2))

        T0 = time()

        V.log()
        print(T0)

        sleep(5.5)

        T1 = time()

        V.log()
        print(T1)

        V.log()
        print('total time: ', T1 - T0)

    except ValueError:
        print("ERROR:", ValueError)
        sys.exit(ExitStatus.failure)

    print('ExitStatus.success', repr(ExitStatus.success))
    sys.exit(ExitStatus.success)
