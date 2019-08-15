def binaryS(n,arr,k):
     s,e=0,len(arr)-1
     count=0
     l,f,m=n,0,0
     while(s<=e):
 	m=int((s+e)/2)
 	if arr[m]==k:
 		for i in range(m,n):
 		  if arr[i]==k:
 		     count=count+1
 		     l=i
 		  else:
		     break
	        for j in range(m,-1,-1):
 		  if arr[i]==k:
 		     count=count+1
 		     f=j
 		  else:
		     break
		print(f,"",l,"",count-1)
		break
	elif k>arr[m]:
         s=m+1
	elif k<arr[m]:
         e=m-1
	else:
                print("-1-10")
		 
n=int(input())
arr=list(map(int,input().split()))
k=int(input())
binaryS(n,arr,k)
