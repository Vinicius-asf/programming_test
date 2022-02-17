def findMultiples (n:int):
    multiples = []
    for i in range(n):
        if(i%3 == 0 and i%5==0):
            multiples.append(i)
    return multiples