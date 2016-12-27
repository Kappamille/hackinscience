#!/usr/bin/python
import sys
if len(sys.argv) != 3:
    print('usage: python3 solution.py OP1 OP2')
else:
    for neko in sys.argv[1] and sys.argv[2]:
        if neko not in "0123456789":
            print("Error, OP1 and OP2 must be positive integars")
            exit(0)
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(a + b)
