#!/usr/bin/python
def love_meet(bob, alice):
    return(set(alice) & set(bob))


def affair_meet(bob, alice, silvester):
    return((set(alice) & set(silvester)) - set(bob))
