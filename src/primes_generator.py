import time

def write_primes():
    
    prime_generation_time = open("primes_time.txt", "a")
    time_start = time.time()
    current = 3
    n = 10000
    file_for_store_primes = open("primes.txt", "w")

    while(n > 0):
    
        for i in range(2, current):
    
            if(current % i == 0):
    
                break
    
        else:
    
            file_for_store_primes.write(f"{str(current)}\n")
            n -= 1
    
        current += 1

    file_for_store_primes.close()
    time_end = time.time()
    prime_generation_time.write(f"{round(time_end - time_start, 3)} seconds used to generate 10.000 primes\n")
    prime_generation_time.close()

if __name__ == '__main__':
    
    write_primes()