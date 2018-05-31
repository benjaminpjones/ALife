import sys

the_quick_brown_fox = {"{} jumps": "over", "the": "lazy \"dog\""}

counter = 0

def my_decorator(some_function):
    def wrapper():
        global counter
        counter += 1
        print "Function decorated!"
        return some_function() + counter
    return wrapper

@my_decorator
def f1():
    print("Hello World!")
    return 0

def f2(arg1, arg2 = 23, *argv, **kwargs):
    print "Here's a lot of arguments!"
    print "arg1:", arg1
    print "arg2:", arg2
    print "argv:", argv
    print "kwargs:", kwargs

if __name__ == '__main__':
    for i in xrange(3 * 4):
        print i**2
    a = 1
    try:
        while (True):
            a *= 2
        else:
            print "Every statement should have an else clause!"
    except OverflowError as error:
        print "Overflowed!"
    else:
        pass

    my_list = [1, 'a', f1]

    print "Does this count as functional programming?", my_list[2]()

    my_list.append("{} <-- curly braces in strings can be tricky...")

    is_this, a_tuple = '?', (5 - 4 / 69, 8 > 3)

    print True and False

    
