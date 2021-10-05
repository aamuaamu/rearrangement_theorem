# L = [1, 1/2, 1/2, 1/4, 1/4, 1/4, 1/4, ...]
# last terms are of the form 1/2^power, and there are 2^power-many of them.
def binarySequence(power):
    L = []
    multiplier = 1
    for i in range(power):
        for j in range(multiplier):
            L.append(1.0/multiplier)
        multiplier*= 2

# print the first l partial sums of the series L
def printSeries(L, l):
    print("n".ljust(4) + ":" + " s_n".ljust(8) + "a_1 + ... + a_n")
    for i in range(1,min(len(L), l)+1):
        print (str(i).ljust(4) + ": " + str(format(sum(L[:i]), ".2f")).ljust(8), L[:i])

# merge the two sequences p and n in alternating way
def defaultSequence(p,n):
    merged = []
    while p and n:
        if p:
            merged.append(p.pop(0))
        if n:
            merged.append(n.pop(0))
    if p:
        merged = merged + p
    if n:
        merged = merged + n
    return merged    

# Rearrange the sequence
def targetSequence(p,n, target, l):
    merged = []
    s = 0
    while p and n and l:
        print(s)
        if s <= target:
            s += p[0]
            merged.append(p.pop(0))
        else:
            s += n[0]
            merged.append(n.pop(0))
        l -= 1 
    print(merged)
    return merged

P = []
N = []
print(P)
print(N)
P = binarySequence(5)
N = binarySequence(5)
N = [-N[i] for i in range(len(N))]
R = targetSequence(P, N, 0.33, 20)
printSeries(R, 15)
