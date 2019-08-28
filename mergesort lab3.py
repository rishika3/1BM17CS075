def mergeS(l):
    if len(l)>1:
        m=len(l)//2
        l1=l[:m]
        l2=l[m:]
        mergeS(l1)
        mergeS(l2)
        i,j,k=0,0,0
        while i<len(l1)and j<len(l2):
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
l=list(map(int,input().split()))
mergeS(l)
print(l)
        
