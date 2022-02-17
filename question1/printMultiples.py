from tkinter.tix import INTEGER

from attr import mutable


from findMultiples import findMultiples

def printMultiples (n:int):
    multiples = findMultiples(n)
    print(' '.join(str(i) for i in multiples))
