"""
문자열이 주어지면 대문자와 소문자를 바꿔서 출력하는 프로그램을 작성하세요.

>> 입력
AAABBBcccddd

>> 출력
aaabbbCCCDDD
"""

s = input()
change_s = ''
for sub in s:
    change_s += sub.upper() if sub.islower() else sub.lower()
print(change_s)

