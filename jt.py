#!/bin/env python
# Simple test program to run through johnson trotter 
# permutations, given a number, N, as input
import sys

def permute(n):
    N = int(n)
    print "Running permutation for N = %d" % N
    dir = [-1 for i in range(0,N)]
    p = [i for i in range(0,N)] 
    pi = [i for i in range(0,N)] 
    perm(0, p, pi, dir)
    print "    (0 1)"
   
def perm(n, p, pi, dir):
    # base case
    if n >= len(p):
        for i in range(0, len(p)):
            print "%d" % p[i],
        return
    perm(n+1, p, pi, dir)
    for i in range(0, n):
        print "    (%d %d%d)" % (pi[n], pi[n], dir[n])
        z = p[pi[n] + dir[n]]
        p[pi[n]] = z                                                      
        p[pi[n] + dir[n]] = n                                   
        pi[z] = pi[n]                                                     
        pi[n] = pi[n] + dir[n]                                            
        perm(n+1, p, pi, dir)  
    dir[n] = -dir[n]

def usage():
    print "Usage: ./jt <N>"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        n = sys.argv[1]
        if n.isdigit():
            permute(sys.argv[1])
        else:
            usage()
    else:
        usage()
 


