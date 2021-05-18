import random
import time
import RSANPrime


def main():

    testNumber = 0

    nDP = int(input("Quantos primos serao usados? "))
    cat = int(input("Qual categoria? "))

    if cat < 5 and cat > 0:

        if cat == 1:

            limInf = 0

            limSup = 100

        elif cat == 2:

            limInf = 1000

            limSup = 5000

        elif cat == 3:

            limInf = 5001

            limSup = 10000

        elif cat == 4:

            limInf = 0

            limSup = 10000

    else:

        print("Categoria invalida!")
        return

    arquivoResultados = open(
        "CAT" + str(cat) + "resultadosK" + str(nDP) + ".txt", "w")

    dadosFinaisResultados = open(
        "CAT" + str(cat) + "tempoTotalK" + str(nDP) + ".txt", "w")

    primos = []

    mediaTempo = 0

    porcentagemDeSucesso = 0

    arquivoComPrimos = open("primos.txt", "r")

    tempoGeralIni = time.time()

    for i in range(10000):

        primos.append(int(arquivoComPrimos.readline()))

    arquivoComPrimos.close()


    while(testNumber < 1000000):

        comeco = time.time()

        indicesEscolhidos = []

        primEsc = []

        indicesEscolhidos = random.sample(range(limInf, limSup), nDP)

        for i in range(nDP):

            primEsc.append(primos[indicesEscolhidos[i]])

        primEsc.sort()


        reductions = []

        mis = []

        n = RSANPrime.encontrarN(primEsc, nDP)

        mens = random.randint(0, n - 1)

        e = RSANPrime.encontrarE(primEsc, nDP)

        d = RSANPrime.encontrarD(primEsc, nDP, e)

        enc = RSANPrime.encrypt(mens, e, n)


        RSANPrime.reducaoModular(primEsc, reductions, d, nDP)

        RSANPrime.encontrarMis(
            primEsc, reductions, mis, enc, nDP)

        dec = RSANPrime.decrypt(primEsc, mis, nDP, n)


        fim = time.time()

        tempoTotal = round(fim - comeco, 3)

        arquivoResultados.write(
            f"{primEsc} {tempoTotal}s {mens} {enc} {dec} {mens == dec}\n")

        mediaTempo += tempoTotal

        if(mens == dec):

            porcentagemDeSucesso += 1

        testNumber += 1


    tempoGeralFinal = time.time()

    dadosFinaisResultados.write(
        f"Tempo geral = {round(tempoGeralFinal - tempoGeralIni, 3)}s\n")

    dadosFinaisResultados.write(
        f"Media tempo = {mediaTempo/1000000} s por execucao\n")

    dadosFinaisResultados.write(f"Sucesso = {porcentagemDeSucesso/10000}%\n")

    arquivoResultados.close()

    dadosFinaisResultados.close()


if __name__ == '__main__':
    main()
