# -*- coding: utf-8 -*-
#!python
"""
Created on Wed Feb 17 08:58:31 2021

@author: sapplen
squares and circles
"""



# circle.py

import math
import turtle

bob = turtle.Turtle()
alice = turtle.Turtle()

"""
#print(bob)
#turtle.mainloop()

# interface design
#def circle(t,r):
#    circumference = 2* math.pi * r
#    n = int(circumference / 3) + 1
#    length = circumference / n 
#    polygon(t, n, length)
"""
def square(t):
"""Docstring for my function named square
and it is a very simple docstring
"""
    for i in range(4):
        t.fd(100)
        t.lt(90)
    
def polyline(t, n, s, length, angle):
    for i in range(n):
        t.fd(s*length)
        t.lt( s*angle)
        
def polygon(t, n, length, s):
    angle = 360.0 / n
    polyline(t, n, s, length, angle)
    
def arc(t, r, s, angle):
    arch_length = 2 * math.pi * r * angle / 360
    n = int(arch_length / 3) + 1
    print (n)
    step_length = arch_length / n
    step_angle = float(angle) / n 
    polyline(t, n, s, step_length, step_angle)
    
def circle (t, r, s):
    arc(t, r, 360)
    
def halfcircle (t,r,s):
    arc(t,r,s,180)
    
"""    
def circle(t,r):
        circumference = 2 * math.pi * r
        n = 50
        length = circumference / n
        polygon(t,n,length)
"""        
  
halfcircle(alice,50, -1)

halfcircle(bob,75,-1)
square(alice)
polygon(bob,4,75,1)
 	
halfcircle(alice,50, 1)
halfcircle(bob,75,1)

turtle.mainloop()
#circle(bob, 30,)
# cd users\sapplen\Documents\GitHub\Python-Hello-World
 