#!/usr/bin/python
import sys
if len(sys.argv) == 1:
	print("Bonjour, bel inconnu !")
elif len(sys.argv) == 2:
	print("Bonjour, " + str(sys.argv[1]) + " !")
else:
	a = len(sys.argv)
	b = 1
	while b <= a:
		s = str(sys.argv[b])
		b = b + 1
		print(s)