def sum_of_each_digit_loop_ver(s):
    total = 0
    for i in s:
        total += int(i)
    return total


def sum_of_each_digit_recursion_ver(s):
    if len(s) == 1:
        return s
    return int(sum_of_each_digit_recursion_ver(s[1:])) + int(s[0])


def sum_of_each_digit_recursion_int_ver(n):
    if n == 0:
        return n
    return sum_of_each_digit_recursion_int_ver(n // 10) + n % 10


if __name__ == '__main__':
    x = input()
    print(sum_of_each_digit_loop_ver(x))
    print(sum_of_each_digit_recursion_ver(x))
    print(sum_of_each_digit_recursion_int_ver(int(x)))
