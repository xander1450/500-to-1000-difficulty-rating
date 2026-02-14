for i in range(int(input())):
    n,x = map(int, input().split())
    print(((n//6))*x if n%6==0 else ((n//6)+1)*x)
