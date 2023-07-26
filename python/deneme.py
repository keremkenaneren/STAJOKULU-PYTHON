def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def find_primes(start, end):
    prime_numbers = []
    for num in range(start, end + 1):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers


start_number = 1
end_number = 100

prime_numbers_list = find_primes(start_number, end_number)
print("1'den 100'e kadar olan asal sayılar:")
print(prime_numbers_list)
