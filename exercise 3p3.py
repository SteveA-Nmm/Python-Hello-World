# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 15:47:59 2021

@author: sapplen
How to think liek a computer programar / scientest derp
based on exercise by Steve Oualline, Practical C Programming

"""

def do_2(f):
    f()
    f()
    
def do_4(f):
    do_2(f)
    do_2(f)

def print_beam():
    print('+ - - - -',end= ' ')
         
def print_post():
    print("|        ", end=' ')
    
def print_row():
    do_4(print_beam)
    print('+')
    
def print_col():
    do_2(print_post)
    print('|')
    
def print_cols():
    do_2(print_col)
    print('|')    
    
     
def print_column():
    do_4(print_post)
    print('|')   

def holywood_square():
    #do_4(print_beam)
    print_row()
    #print_row()
    #print('+')
    do_4(print_column)  
    #print_cols()

def holywood_squares():
    do_4(holywood_square)
    print_row()  #the stage floor
    
holywood_squares()
    
def four_sqr():
    do_2(print_beam)
    print('+')
    do_4(print_col)
    do_2(print_beam)
    print('+')
    do_4(print_col)
    do_2(print_beam)  
    print('+')   

def play_grnd():
    four_sqr()
    print()
    print()
    four_sqr()

play_grnd()


