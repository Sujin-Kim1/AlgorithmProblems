"""
골드바흐의 추측(Goldbach's conjecture)은 오래전부터 알려진 정수론의 미해결 문제로, 2보다 큰 모든 짝수는 두 개의 소수(Prime number)의 합으로 표시할 수 있다는 것이다. 이때 하나의 소수를 두 번 사용하는 것은 허용한다. - 위키백과

위 설명에서 2보다 큰 모든 짝수를 두 소수의 합으로 나타낸 것을 골드바흐 파티션이라고 합니다.

예)
100 == 47 + 53
56 == 19 + 37

**2보다 큰 짝수 n이 주어졌을 때, 골드바흐 파티션을 출력하는 코드를** 작성하세요.

* 해당 문제의 출력 형식은 자유롭습니다. 가능하시다면 골드바흐 파티션 모두를 출력하거나, 그 차가 작은 것을 출력하거나 그 차가 큰 것 모두 출력해보세요.
"""

import time


def get_prime_numbers(n):
    prime_numbers = [i for i in range(2, n)]
    for i in prime_numbers:
        if is_prime(i):
            for j in prime_numbers:
                if j != i and j % i == 0:
                    prime_numbers.remove(j)

    return prime_numbers


def is_prime(n):
    for i in range(2, int(n ** 0.5)):
        if n % i == 0:
            return False
    return True


def goldbach_conjecture(n):
    prime_numbers = get_prime_numbers(n)
    print(prime_numbers)

    goldbach_li = []
    for i in range(len(prime_numbers)):
        for j in range(i, len(prime_numbers)):
            if prime_numbers[i] * 2 > n:
                break
            if prime_numbers[i] + prime_numbers[j] == n:
                goldbach_li.append((prime_numbers[i], prime_numbers[j]))

    return print(goldbach_li)


"""
====== other solution ======
"""


def cal():
    n = 10000 * 2
    primes = []
    a = [False, False] + [True] * (n - 1)

    for i in range(2, n + 1):
        if a[i]:
            primes.append(i)
            for j in range(2 * i, n + 1, i):
                a[j] = False
    return primes


def answer(n):
    a = cal()

    # goldbach's partition
    l = [(i, n - i) for i in range(n // 2 + 1) if i in a and n - i in a]
    return print(l)


if __name__ == '__main__':
    n = int(input())

    t = time.time()
    goldbach_conjecture(n)
    print(time.time() - t)

    t = time.time()
    answer(n)
    print(time.time() - t)
