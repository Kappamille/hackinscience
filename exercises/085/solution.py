#!/usr/bin/python
def sort_a_list(l):
    return(sorted(l, reverse=True))

def sort_by_mark(my_class):
    from operator import itemgetter
    bla = itemgetter(0)
    return(sorted(my_class, key = bla, reverse=True))
	
def sort_by_mark(my_class):
    from operator import itemgetter
    bla = itemgetter(1)
    return(sorted(my_class, key = bla))
