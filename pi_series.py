#!/usr/bin/env python

# The infinite series: 1 - 1/3 + 1/5 - 1/7 ... converges to π/4 
# write a generator function which progressively makes better and better approximations of π

from math import pi
    
def pi_generator(stop = 0.001):
    """ generate series 4*(1 - 1/3 + 1/5 - 1/7 ...), according to the Leibniz formula for π.
    """
    a = 0.0
    sign = 1.0
    i = 1
    while abs(pi-a*4.0) > stop:       
        a += sign/i 
        yield a*4.0
        i += 2
        sign *= -1.0
        


def accel(g):
      """a generator that accelerate convergence by return:
        Sn = Sn+1 − (Sn+1 − Sn)^2/(Sn−1 − 2*Sn + Sn+1)"""
    s0 = g.next() #Sn-1
    s1 = g.next() #Sn
    s2 = g.next() #Sn+1
    while True:
        yield s2 - (s2 - s1)**2/(s0 - 2.0*s1 + s2)
        s0, s1, s2 = s1, s2, g.next()
        
        
def f(g, n):
    for i in range(n):
        yield g.next()
        
