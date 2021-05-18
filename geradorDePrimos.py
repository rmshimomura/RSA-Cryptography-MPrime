import time

def escreverPrimosNoTxt():
    
    tempoGeracaoDePrimos = open("tempoPrimos.txt", "a")
    timestart = time.time()
    current = 3
    n = 10000
    arquivo = open("primos.txt", "w")

    while(n > 0):
    
        for i in range(2, current):
    
            if(current % i == 0):
    
                break
    
        else:
    
            arquivo.write(f"{str(current)}\n")
            n -= 1
    
        current += 1

    arquivo.close()
    timeend = time.time()
    tempoGeracaoDePrimos.write(f"{round(timeend - timestart, 3)} segundos usados na geracao de 10.000 primos\n")
    tempoGeracaoDePrimos.close()

if __name__ == '__main__':
    
    escreverPrimosNoTxt()