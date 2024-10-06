#!/bin/python
def a():
    print('a() status')
    b()
    d()
def b():
    print('b() status')
    c()
    print('b() restart')
def c():
    print('c() status')
    print('c() restart')
def d():
    print('d() status')
    print('d() restart')
a()