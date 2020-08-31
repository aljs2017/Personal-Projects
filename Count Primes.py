# Determine how many prime numbers there are before the input number

print("Please enter the input number.")

input_number = int(input())

prime_count = 1

def countPrimes(input_number, prime_count):
    for number in range(1, input_number):
        current_number = input_number - number
        isPrime(current_number)

        if isPrime == True:
            prime_count += 1
        else:
            continue


def isPrime(current_number):
    for division_number in range(2, current_number):
        if division_number % current_number == 0:
            return False
    return True





