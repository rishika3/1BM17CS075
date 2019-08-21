a=[]
a=list(map(int,input().split()))
k=int(input())
for i in range(k):
    for j in range(len(a)-1-i):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
print(a[-k:])                             
