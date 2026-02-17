index = 0
t = int(input())
index += 1

for i in range(t):
    x, y = map(int, input().split())
    index += 2
    print(4 * x + y)
