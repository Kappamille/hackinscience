#!/usr/bin/python
import sys
if len(sys.argv) == 1:
	print("Bonjour, bel inconnu !")
elif len(sys.argv) == 2:
	print("Bonjour, " + str(sys.argv[1]) + " !")
else:
	s = sys.argv[1] + ", "
	for i in sys.argv[1:-2]:
		s += i +  ", "
	print("Bonjour, " + str(s) + str(sys.argv[-2]) + " et " + str(sys.argv[-1]) + " !")