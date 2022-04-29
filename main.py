from elliptic_curve_factorization.elliptic_curve_factorization import EllipticCurveFactorization
from Crypto.Util.number import getPrime


def get_random_composite(size):
    while True:
        p = getPrime(size // 2)
        q = getPrime(size // 2)

        if p*q.bit_length() >= size:
            break

    return p * q, p, q


def main():
    n = int(input('Enter n or 0 for generate random:'))
    if n == 0:
        size = int(input('n size (bits):'))
        n, p, q = get_random_composite(size)
        print(f"n = {n} = {p} * {q}")
    m = int(input('m:'))

    P_1 = EllipticCurveFactorization(n, m)

    d, counter = P_1.factorization()
    print(f"Find divisor {n}: {d}")
    print(f"d length: {d.bit_length()}")
    q = n // d
    print(f"n//d: {q}")
    print(f"n//d length: {q.bit_length()}")
    print(f"numbers of iterations: {counter}")


if __name__ == '__main__':
    main()
