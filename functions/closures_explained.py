#!/usr/bin/python3

"""
A function defined inside another function is called a nested function. 
Nested functions can access variables of the enclosing scope.

In Python, these non-local variables are read only by default and 
must be declared explicitly as non-local (using nonlocal keyword) in order to modify them.
"""

def print_msg1(msg):
    # This is the outer enclosing function
    def printer(): # This is the nested function
        print(msg)
    printer()

# We execute the function
print_msg1("Hello") #Nested function printer() can access non-local variable 'msg' of enclosing function.


def print_msg2(msg): # this is enclosing outer function
    def printer():
        print(msg)
    return printer # instead of running printer(), print_msg2() returns printer
    
another = print_msg2("Greetings")

another()

"""
The print_msg2() function, called with the string "Hello", and the return value is assiged to "another"
When another() is called, the value of "msg" ('Greetings') was still remembered even though print_msg2() had finished.
"""

del print_msg2
# Note, print_msg2, which is what another was assigned , is now deleted
another() # but another() still works. This is referred to as a closure

"""
A closure function, (in this case 'another()' ) 
holds the state of the function, even when the function is no more

A closure, unlike a plain function, allows for access to the
variables in the state they were, via the closure function's copies of the
variable values or references, even though the function is invoked outside 
the scope of these variables.

# A closure has the following 3 characteristics:
1. Enclosing function contains a nested function
2. Nested function refers to a variable defined in the enclosing function
3. Enclosing function returns the nested function

Closures avoid the use of global variables and thus provide an alternative way of data hiding.
Closures are ideal when only a single method is required as opposed to setting up a class,
which can accommodate several methods and attrbutes, since a closure with a single nested 
function is slightly more efficient than setting up a class.

Cloures can be used as callback functions.

Callbacks are often used in situations where an action is asynchronous. 
If you need to call a function, and immediately continue working, you can't sit
there wait for its return value to let you know what happened, so you provide a callback.
When the function is done completely its asynchronous work it will then invoke your callback
with some predetermined arguments (usually some you supply, and some about the status and
result of the asynchronous action you requested).
"""

