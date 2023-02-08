import math

def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)

#countdown(8)

def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)

#print_n('Hello',10)

#name = input("What is ur name?\n")
#print("fuck you", name)

import time
time.time()

def time_convertor(t):
    t.time()



import time

# Get current time in seconds since the epoch
current_time = time.time()

# Calculate the current time of day in hours, minutes, and seconds
seconds = int(current_time % 60)
minutes = int((current_time / 60) % 60)
hours = int((current_time / 3600) % 24)

# Calculate the number of days since the epoch
days = int(current_time / 86400)

# Print the results
#print("Current time of day:", hours, "hours,", minutes, "minutes,", seconds, "seconds")
#print("Number of days since the epoch:", days)


def check_format(a,b,c,n):
    if (a^n + b^n == c^n) and n >2:
        print('Holy smokes, Fermat was wrong!')
    else:
        print('No, that doesnt work.')

#check_format(1,1,1,2)

def is_triangle(a,b,c):
    if a>b+c or b>a+c or c>a+b:
        print("No")
    else:
        print("Yes")

#a = int(input("Give me 3 integers starting the first one:"))
#b = int(input("Now second one:"))
#c = int(input("And the last one:"))
#is_triangle(a,b,c)

def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

#recurse(-1, 0)
import turtle
def koch(t, n):
    if n < 3:
        t.fd(n)
    else:
        m = n/3
        koch(t, m)
        t.lt(60)
        koch(t, m)
        t.rt(120)
        koch(t, m)
        t.lt(60)
        koch(t, m)


#bob = turtle.Turtle()
#koch(bob,1000)


#turtle.mainloop()
#x = int(input("first integer:\n"))
#y = int(input("second integer:\n"))

def compare(x,y):
    if x < y:
        return -1
    elif x == y:
        return 0
    elif x > y:
        return 1

#d = compare(x,y)
#print("The result is",d)

#a = int(input("first integer:\n"))
#b = int(input("second integer:\n"))
def hypotenuse(a,b):
    """This gets 2 integers and calculates the third edge of a right triangle
    a:first edge
    b:second edge
    """
    return math.sqrt(a**2+b**2)

#print(hypotenuse(a,b))

def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)

#print_n(4,3)

def print_n2(s,n):
    while n != 0:
        print(s)
        n = n - 1

#print_n2(4,3)

#while True:
#	line = input('> ')
#	if line == 'done':
#		break
#print('Done!')

#a = int(input("Input an integer:\n"))
def mysqrt(a):
    """" This function calculates square root of the input number"""
    x = a/2
    epsilon = 0.0000000000000001
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            break
        x = y
    return y


def test_square_root(a,y):
    """ This function gets use of mysqrt to form a table and a sequence of square roots as values
    """
    diff = abs(math.sqrt(a) - y(a))
    print(2*" ","a",5*" ","mysqrt(a)",8*" ","math.sqrt(a)",6*" ","diff")
    print(2*" ","-",5*" ",9*"-",9*" ",12*"-",6*" ",9*"-")
    b = 1
    while b <= a:
        print(2*" ",b,5*" ",'%.9f'%y(b),7*" ",'%.9f'%math.sqrt(b),9*" ",'%.3f'%diff)
        b = b + 1

#test_square_root(a,mysqrt)

#print(eval("2+2"))

def eval_loop():
    """ This function takes input repeatedly and evaluates it using Python interpreter,
    stops when it gets "done" as input
    """
    while True:
        b = input('> ')
        if b == "done":
            print("Done!")
            break
        print(eval(b))

#eval_loop()

def factorial(a):
    """ this is a factorial function
    """
    if a == 0 or a == 1:
        return 1
    else:
        return a * factorial(a-1)

def estimate_pi():
    k = 0
    tot = 0
    factor = 2 * math.sqrt(2)/9801
    while True:
        num = (factorial(4*k) * (1103 + 26390*k))
        den = factorial(k)**4 * 396**(4*k)
        tot += num / den
        term = factor * num/den

        if abs(term)  < 1e-15:
            break
        k += 1
    return 1/ (factor * tot)

#print("estimate is:" ,estimate_pi())

print(math.sqrt(((-0.53+0.73)**2) + ((-0.86-0.4)**2) +((-0.35+0)**2) + ((-0.64+0.11)**2) + ((-1.15+0.67)**2)))
