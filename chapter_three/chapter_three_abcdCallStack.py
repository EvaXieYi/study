#!/bin/python
import inspect,traceback
def a():
    print('a() status')
    global wo
    wo=1

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
    infd=inspect.stack()
    for fram_info in infd:
        print(f"文件名: {fram_info.filename}")
        print(f"行号: {fram_info.lineno}")
        print(f"函数名: {fram_info.function}")
        print(f"代码上下文: {fram_info.code_context}")
        print("--------------")
a()
print(wo)
'''
import inspect

def outer_function():
    inner_function()
 
def inner_function():
    # 获取当前调用栈
     
    stack = inspect.stack()
    print(inspect.stack())
    # 获取栈顶函数的名字
    top_frame = stack[0]
    function_name = top_frame[3]

    print(f"当前正在执行的函数是: {function_name}")
 
# 调用outer_function，它会调用inner_function


outer_function()'''