def reverse_string_loop_ver(s):
    result = ''
    for i in s:
        result = i + result
        # as it is: result = result + i
    return result


def reverse_string_recursion_ver(s):
    if s == '':
        return ''
    else:
        return reverse_string_recursion_ver(s[1:]) + s[0]
        # as it is: return s[0] + reverse_string_recursion_ver(s[1:])


if __name__ == '__main__':
    x = input()
    print(reverse_string_loop_ver(x))
    print(reverse_string_recursion_ver(x))
