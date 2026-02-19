a = list(map(int, input().split()))
even = 0
odd = 0
j=0
for j in range(len(a)):
    if(a[j]%2==0):
        even+=1
    else:
        odd+=1
print("NOT READY" if odd>=even else "READY FOR BATTLE" )
