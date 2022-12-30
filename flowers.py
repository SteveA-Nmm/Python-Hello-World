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
from polygon import arc

def petal(t,r,angle):
    """Draws a petal using two arcs.
    t: Turtle
    r: radius of the arcs
    angle: degrees that subtends the arcs
    """
    for i in range(2):
        arc(t,r,angle)
        t.lt(180-angle)

def flower(t,n,r,angle):
    """Draws a flower with n petals.
    t: Turtle
    n: number of petals
    r: radius of arcs
    angle: degrees tht sub the arcs
    """
    for i in range (n):
        petal(t,r,angle)
        t.lt(360.0/n)

def move(t,length):
    """Move turtle without leaving a trail
    exit with pen down
    """
    t.pu()
    t.fd(length)
    t.pd()


bob = turtle.Turtle()
#alice = turtle.Turtle()

move(bob,-200)
#flower(bob,7,120.0,60.0)

move(bob,200)
flower(bob,10,80.0,80.0)

move(bob,200)
flower(bob,20,140.0,20.0)


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
    """ does this docstring work to 
    do good or to do bad
    """
    for i in range(4):
        t.fd(100)
        t.rt(90)
   
def polyline(t, n, sl, sa, length, angle):
    for i in range(n):
        t.fd(sl*length)
        t.rt(sa*angle)
        
def polygon(t, n, length, s):
    angle = 360.0 / n
    polyline(t, n, s, length, angle)
    
def arc(t, r, sl, sa, angle):
    arch_length = 2 * math.pi * r * angle / 360
    n = int(arch_length / 3) + 1
    print (n)
    step_length = arch_length / n
    step_angle = float(angle) / n 
    polyline(t, n, sl, sa, step_length, step_angle)
    
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
  
#arc(alice,50,-1,100)


turtle.mainloop()
#circle(bob, 30,)
# cd users\sapplen\Documents\GitHub\Python-Hello-World
 
