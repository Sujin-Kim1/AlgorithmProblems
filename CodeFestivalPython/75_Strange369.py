"""
369 게임을 하는데 조금 이상한 규칙이 있습니다. 3이나 6, 9 일 때만 박수를 쳐야합니다. 예를 들어 13, 16과 같이 3과 6, 9 만으로 된 숫자가 아닐 경우엔 박수를 치지 않습니다.
수현이는 박수를 몇 번 쳤는지 확인하고 싶습니다. 36일 때 박수를 쳤다면 박수를 친 횟수는 5번입니다.

n을 입력하면 박수를 몇 번 쳤는지 그 숫자를 출력해주세요.

1. 3
2. 6
3. 9
4. 33
5. 36
6. 39
7. 63
8. 66
9. 69
10. 93

**입력 - 문자로 입력받습니다.**
'93'

**출력**
10
"""


"""
1.  3   : 1
2.  6   : 2
3.  9   : 3
4.  33  : (1 * 3) + 1
5.  36  : (1 * 3) + 2 
6.  39  : (1 * 3) + 3
7.  63  : (2 * 3) + 1
8.  66  : (2 * 3) + 2
9.  69  : (2 * 3) + 3
10. 93  : (3 * 3) + 1
11. 96  : (3 * 3) + 2
12. 99  : (3 * 3) + 3
13. 333 : (1 * 9) + (1 * 3) + 1
14. 336 : (1 * 9) + (1 * 3) + 2
15. 339 : (1 * 9) + (1 * 3) + 3 
"""


def strange369(s):
    count = 0
    for i in range(len(s)):
        count += (int(s[-1]) // 3) * (3 ** i)
        s = s[:-1]
    return count



if __name__ == '__main__':
    print(strange369(input()))
