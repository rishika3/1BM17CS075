def squareroot(n):
 f,l=0,n
 if n<0:
  return "imaginary..!"
 while(f<=l):
  mid=int((f+l)/2)
  if mid*mid==n:
     ans=mid
     break
  elif mid*mid<n:
     f=mid+1
     ans=mid
  elif mid*mid>n:
     l=mid-1
 return ans
x=input("squareroot of:")
print (squareroot(x))

