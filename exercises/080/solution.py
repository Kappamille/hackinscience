#!/usr/bin/python
from string import ascii_lowercase
lol = "bcdefghijklmnopqrstuvwxyz"
for i in ascii_lowercase:
	for lul in lol:
		if i < lul:
			print(i+lul) 
	