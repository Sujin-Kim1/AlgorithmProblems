# Bottom-up
def binary_loop_ver(n):
    result = ''
    while True:
        result += '0' if n % 2 == 0 else '1'
        n = n // 2
        if n == 1 or n == 0:
            result += str(n)
            print(result[::-1])
            break


# Top-down
def binary_recursion_ver(n):
    if n <= 1:
        return str(n)
    else:
        return str(binary_recursion_ver(n // 2)) + str(n % 2)


"""
binary_recursion_ver(11) -> str(binary_recursion_ver(5)) + str(1)
binary_recursion_ver(5)  -> str(binary_recursion_ver(2)  + str(1)
binary_recursion_ver(2)  -> str(binary_recursion_ver(1)  + str(0)
binary_recursion_ver(1)  -> 1

binary_recursion_ver(11) -> 1011
binary_recursion_ver(5)  -> 101
binary_recursion_ver(2)  -> 10
binary_recursion_ver(1)  -> 1
"""

if __name__ == '__main__':
    x = int(input())
    binary_loop_ver(x)
    print(binary_recursion_ver(x))
