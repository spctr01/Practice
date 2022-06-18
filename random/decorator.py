""" any object which implements the special method __call__() is termed callable.
 So, in the most basic sense, a decorator is a callable that returns a callable.
"""

# takes function as argument and return a function
def demo(func):
    def inner():
        print("inner function")
        func()

    return inner


def lzz():
    print("luzz function")


r = demo(lzz)
r()
##output :: inner function
##          luzz function

# USING @ SYMBOL DECORATOR
def demo1(func):
    def inner():
        print("inner function1")
        func()

    return inner


@demo1
def lzz1():
    print("luzz function1")


lzz1()

##output :: inner function1
##          luzz function1


# CHANING DCORATORS


def function(func):
    def inner():
        print("inner function")
        func()

    return inner


def function1(func):
    def inner1():
        print("inner function1")
        func()

    return inner1


@function
@function1
def function2():
    print(" function2")


function2()
## output : inner function
##           inner function1
##           function2
