from curves.curves import FieldParams, CurveParams, CurvePoint, Curve
from Crypto.Util.number import isPrime, getRandomRange
from math import log2
from time import time


class EllipticCurveFactorization:
    def __init__(self, n, m):
        self.n = n
        self.m = m

    @staticmethod
    def get_primes(m):
        primes = []

        for i in range(m):
            if isPrime(i):
                primes.append(i)

        return primes

    def factorization(self):
        # Get base
        D = self.get_primes(self.m)

        time_start = time()
        while True:
            # Get random point
            Q = CurvePoint(getRandomRange(1, self.n - 1), getRandomRange(1, self.n - 1))
            # Get random elliptic curve
            a = getRandomRange(1, self.n - 1)
            b = (Q.y**2 - Q.x**3 - a * Q.x) % self.n

            curve = Curve(FieldParams(self.n, 0), CurveParams(a, b))

            print("Q: ")
            print(f"\tx: {Q.x}")
            print(f"\ty: {Q.y}")

            print("Curve: ")
            print(f"\ta: {curve.curve_params.a}")
            print(f"\tb: {curve.curve_params.b}")
            print("\n")

            Q_i = Q
            cnt = 0
            try:
                for prime in D:
                    a_i = int(0.5 * (log2(self.n) / log2(prime)))

                    for j in range(a_i):
                        Q_i = curve.multiply_point(prime, Q_i)

                    cnt += 1

            except Exception as exc:
                _, div = exc.args
                time_stop = time()

                print(f"Time: {time_stop - time_start} seconds")

                return div, cnt
