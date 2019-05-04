# *-* coding: utf-8 *-*
import sys
import math


def seive_of_erastothenes(n):
    if n < 2:
        return []

    tmp = [True] * (n-2)
    flags = [False, False] + tmp

    prime = 2
    while prime < math.sqrt(n):
        cross_off(flags, prime)
        prime = get_next_prime(prime, flags)

    return flags


def cross_off(flags, prime):
    for i in range(prime*prime, len(flags), prime):
        flags[i] = False


def get_next_prime(current_prime, flags):
    next_prime = current_prime + 1
    while next_prime < len(flags) and not flags[next_prime]:
        next_prime += 1
    return next_prime


def primes(n):
    sifted_range = seive_of_erastothenes(n)
    return (i for i, v in enumerate(sifted_range) if v)


if __name__ == '__main__':
    for i in primes(int(sys.argv[1])):
        print(i)
