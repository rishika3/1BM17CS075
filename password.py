>>> import string
>>> from random import randint
>>> import random
>>> str1=string.printable
>>> print(str1)
0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ 	

>>> print(len(str1))
100
>>> for i in range(6):
	print(str1[randint(0,100)],end="")

	
6 =aS
