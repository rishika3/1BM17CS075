def search(lis,a):
    print(lis)
    if a in lis:
        return True
    else:
        return False
lis=[]
while True:
    a=int(input('enter the element'))
    if a!=-1:
        lis.append(a)
    else:
        break
b=input('enter number to be found')
print(search(lis,a)
