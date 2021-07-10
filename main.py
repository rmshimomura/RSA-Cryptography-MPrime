import random
import time
import RSAMPrime


def main():

    testNumber = 0

    quantity_of_primes = int(input("How many primes the test will use? "))
    category = int(input("Which category? "))

    if category < 5 and category > 0:

        if category == 1:

            inferior_limit = 0

            upper_limit = 100

        elif category == 2:

            inferior_limit = 1000

            upper_limit = 5000

        elif category == 3:

            inferior_limit = 5001

            upper_limit = 10000

        elif category == 4:

            inferior_limit = 0

            upper_limit = 10000

    else:

        print("Invalid category, plese try again.")
        return

    results_file = open(
        "Category" + str(category) + "ResultsK" + str(quantity_of_primes) + ".txt", "w")

    final_data_results = open(
        "Category" + str(category) + "TotalTimeK" + str(quantity_of_primes) + ".txt", "w")

    primes = []

    time_average = 0

    success_percentage = 0

    file_with_primes = open("primes.txt", "r")

    general_start_time = time.time()

    for i in range(10000):

        primes.append(int(file_with_primes.readline()))

    file_with_primes.close()

    while(testNumber < 1000000):

        start_time = time.time()

        chosen_indexes = []

        chosen_primes = []

        chosen_indexes = random.sample(
            range(inferior_limit, upper_limit), quantity_of_primes)

        for i in range(quantity_of_primes):

            chosen_primes.append(primes[chosen_indexes[i]])

        chosen_primes.sort()

        reductions = []

        mis = []

        n = RSAMPrime.find_N(chosen_primes, quantity_of_primes)

        message = random.randint(0, n - 1)

        e = RSAMPrime.find_E(chosen_primes, quantity_of_primes)

        d = RSAMPrime.find_D(chosen_primes, quantity_of_primes, e)

        encryption = RSAMPrime.encrypt(message, e, n)

        RSAMPrime.modular_reduction(
            chosen_primes, reductions, d, quantity_of_primes)

        RSAMPrime.find_Mis(
            chosen_primes, reductions, mis, encryption, quantity_of_primes)

        decryption = RSAMPrime.decrypt(
            chosen_primes, mis, quantity_of_primes, n)

        end_time = time.time()

        total_time = round(end_time - start_time, 3)

        results_file.write(
            f"{chosen_primes} {total_time}s {message} {encryption} {decryption} {message == decryption}\n")

        time_average += total_time

        if(message == decryption):

            success_percentage += 1

        testNumber += 1

    general_end_time = time.time()

    final_data_results.write(
        f"Total time = {round(general_end_time - general_start_time, 3)}s\n")

    final_data_results.write(
        f"Time average = {time_average/1000000} s per execution\n")

    final_data_results.write(f"Success = {success_percentage/10000}%\n")

    results_file.close()

    final_data_results.close()


if __name__ == '__main__':
    main()
