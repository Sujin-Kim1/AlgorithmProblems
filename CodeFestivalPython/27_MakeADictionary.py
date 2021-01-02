names = input().split()
scores = list(map(int, input().split()))

result = dict(zip(names, scores))
print(result)
