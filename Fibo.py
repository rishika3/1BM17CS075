>>> a=0
>>> b=1
>>> n=int(input("enter a number"))
enter a number15
>>> fib=[a,b]
>>> while b<n:
	a,b=b,a+b
	fib.append(b)

	
>>> print(fib)
[0, 1, 1, 2, 3, 5, 8, 13, 21]
