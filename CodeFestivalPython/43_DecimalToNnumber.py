"""
우리가 흔히 사용하는 숫자 1, 8, 19, 28893 등등...은 10진수 체계입니다.
이를 컴퓨터가 알아 들을 수 있는 2진수로 바꾸려고 합니다. 어떻게 해야할까요?

예를들어 13은 2^3 + 2^2 + 2^0 = 13 이기때문에 1101으로 표현합니다

사용자에게 숫자를 입력받고 이를 2진수를 바꾸고 그 값을 출력해주세요.
(bin 함수를 사용하지 않고 풀어주세요.)
"""

def decimal_to_binary(num):
    reversed_binary = ''
    while int(num / 2) > 0:
        reversed_binary += str(num % 2)
        num = int(num / 2)

    reversed_binary += '1'
    binary = reversed_binary[::-1]
    print(binary)


def binary_to_decimal(num):
    decimal = 0
    for i in range(len(num)):
        decimal += int(num[i]) * (2 ** (len(num) - i - 1))
    print(decimal)


if __name__ == '__main__':
    decimal_to_binary(int(input()))
    binary_to_decimal(input())
