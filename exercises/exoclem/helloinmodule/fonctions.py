#!/usr/bin/python
def dire_bonjour():
	import sys
	if len(sys.argv) == 1:
		return(1)
	elif len(sys.argv) == 2:
		return(2)

def texte_bonjour():
	import sys 
	if dire_bonjour() == 1 :
		return("Bonjour, bel inconnu !")
	elif dire_bonjour() == 2 :
		return("Bonjour, " + str(sys.argv[1]) + " !")
	else:
		s = sys.argv[1] + ", "
		for i in sys.argv[2:-2]:
			s += i +  ", "
		return("Bonjour, " + str(s) + str(sys.argv[-2]) + " et " + str(sys.argv[-1]) + " !")
		
if __name__ == "__main__" :
	print(texte_bonjour())