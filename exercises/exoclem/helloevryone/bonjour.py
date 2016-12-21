#!/usr/bin/python
import sys
if len(sys.argv) == 1:
	print("Bonjour, bel inconnu !")
elif len(sys.argv) == 2:
	print("Bonjour, " + str(sys.argv[1]) + " !")
else:
	print("Bonjour ," + str(sys.argv[1:-1]) + " et " + str(sys.argv[-1]) + " !") 