"""
GENRATORS AND COROUTINE WORKS ON FUCTION RUNNING FOR SOME TIME 
LIKE ITERATING ON SOME THING OR USING A LOOP 
Calling a generator function creates an generator object. 
 However, it does not start running function
 holds one value at a time and saved memory and time
"""


def demo(n):
    print("counting")
    while n < 10:
        yield n
        n += 1


print(demo(5))
##output:: <generator object demo at 0x7f0906fcce40>

d = demo(5)
next(d)
##output :: counting   dosnt print the yield value have to use print to print value of yield

"""
GENRATOR PRODUCE DATA WHERE AS COROUTINE CONSUMES DATA AND PRODUCE DATA
"""


def demo1():
    print("coroutine")
    try:
        while True:  # without loop it raise STOPITERATION exception
            x = yield
            print(x)
    except GeneratorExit:
        print("Done")


d1 = demo1()
next(d1)
d1.send(5)
d1.close()
##output :: coroutine
##          5
##          Done
