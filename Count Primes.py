# Determine how many prime numbers there are before the input number

print("Please enter the input number.")

input_number = int(input())

prime_count = 0


def countPrimes(input_number, prime_count):
    for number in range(1, input_number - 1):
        current_number = input_number - number
        #        isPrime(current_number, prime_count)

        if isPrime(current_number, prime_count) == True:
            prime_count += 1
        else:
            continue

    return prime_count


def isPrime(current_number, prime_count):
    for division_number in range(2, current_number):
        if current_number % division_number == 0:
            return False
    return True


countPrimes(input_number, prime_count)