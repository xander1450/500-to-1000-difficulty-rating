for i in range(int(input())):
    x,y = map(int, input().split())
    total = x*y
    if total<100 :
       print(0)
    else:
        print(total//100)
