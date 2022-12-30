#!python

# -*- coding: utf-8 -*-

"""
Created on Mon Jan 25 08:35:03 2021

@author: sapplen
"""

import turtle
bob = turtle.Turtle()
#print(bob)
bob.pd()

def do_2(f):
    f()
    f()
    
def do_4(f):
    do_2(f)
    do_2(f)
    
def ccw():
    bob.fd(100)
    bob.lt(90)
    bob.fd(100)
    
do_4(ccw)

bob.fd(200)
for i in range(4):
    ccw()
    
bob.bk(400)
for i in range(4):
    ccw()

bob.bk(100)
bob.rt(90)
bob.fd(100)

do_4(ccw)
turtle.mainloop()

