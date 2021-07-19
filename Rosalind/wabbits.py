def wabbits(n, k):
    babies = 0
    adults = 1
    i = 1

    while i <= n-2:
        newbabies = adults * k
        adults += babies
        babies = newbabies
        i += 1
        
    return babies+adults


print(wabbits(5,3))
