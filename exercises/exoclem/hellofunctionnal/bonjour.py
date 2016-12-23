#!/usr/bin/python
def dire_bonjour():
	import sys
	if len(sys.argv) == 1:
		print("Bonjour, bel inconnu !")
	elif len(sys.argv) == 2:
		print("Bonjour, " + str(sys.argv[1]) + " !")
	else:
		s = sys.argv[1] + ", "
		for i in sys.argv[2:-2]:
			s += i +  ", "
		print("Bonjour, " + str(s) + str(sys.argv[-2]) + " et " + str(sys.argv[-1]) + " !")
	
if __name__ == "__main__" :
	dire_bonjour()