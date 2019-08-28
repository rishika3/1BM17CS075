def bubble(a):
    print("bubble sort \n")
    c=0
    for i in range(len(a)):
        for j in range(len(a)-1-i):
            c=c+1
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    print(a)
    print(c)

def mergeS(l):
    c=0
    if len(l)>1:
        m=len(l)//2
        l1=l[:m]
        l2=l[m:]
        mergeS(l1)
        mergeS(l2)
        i,j,k=0,0,0
        while i<len(l1)and j<len(l2):
            c=c+1
            if l1[i]<l2[j]:
                l[k]=l1[i]
                i=i+1
            else:
                l[k]=l2[j]
                j=j+1
            k=k+1
        while i<len(l1):
            l[k]=l1[i]
            i=i+1
            k=k+1
        while j<len(l2):
            l[k]=l2[j]
            j=j+1
            k=k+1
def selection(a):
    c=0
    print("selection \n")
    for i in range(len(a)):
        min=i
        for j in range(i+1,len(a)):
            c=c+1
            if a[j]<a[min]:
                min=j
        a[i],a[min]=a[min],a[i]
    print(a)
    print(c)
a=list(map(int,input().split()))
bubble(a)
mergeS(a)
print(len(a)-1)
selection(a)
        
