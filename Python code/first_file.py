import math

#print((45/180) * math.pi, math.sin(45/180* math.pi))

#def print_lyrics():
#    print("I'm a lumberjack, and I'm okay.")
#    print("I sleep all night and I work all day.")

#def repeat_lyrics():
#    print_lyrics()
#    print_lyrics()

#repeat_lyrics()

#def print_twice(s):
#    print(s)
#    print(s)


#def right_justify(s):
#    length_s = len(s)
#    print(((70 - length_s)*' '),s)

def plus_minus():
    print('+',4*'-','+',4*'-','+')

def colns():
    print('|',4*' ','|',4*' ','|')

def do_twice(f):
    f()
    f()

def do_four(f,v):
    v()
    do_twice(f)
    do_twice(f)


def do_eight(j,s):
    do_four(j,s)
    do_four(j,s)

#do_eight(colns,plus_minus)

def final_grid(d,x):
    do_eight(d,x)
    do_eight(d,x)
    plus_minus2()

#do_eight(colns,plus_minus)
#plus_minus()
#def plus_minus2():
#    print('+',4*'-','+',4*'-','+',4*'-','+',4*'-','+')

#def colns2():
#    print('|',4*' ','|',4*' ','|',4*' ','|',4*' ','|')

#final_grid(colns2,plus_minus2)

import turtle
bob = turtle.Turtle()

#for j in range(100000):
#    for i in range(3):
#        bob.fd(200)
#        bob.lt(90)
#    bob.fd(400)
#    for i in range(3):
#        bob.rt(90)
#        bob.fd(200)

#turtle.mainloop()

def square(t):
    t = turtle.Turtle()
    for i in range(60):
        t.fd(100)
        t.rt(45)
    turtle.mainloop()

#square('bob')

def polygon(t,length,side):
    t = turtle.Turtle()
    for i in range(side):
        t.fd(length)
        t1 = (side-2)*180
        t.lt(180 - t1/side)
    turtle.mainloop()

#polygon('a',100,10)

def polygon2(t,length,side,angle):
    t = turtle.Turtle()
    for j in range(int(360/angle)):
        for i in range(side):
            t.fd(length)
            t1 = (side-2)*180
            t.lt(180 - t1/side)
        t.lt(angle)
    turtle.mainloop()

#polygon2('a',150,8,2)

def circle(t,r):
    import math
    circumference = 2 * math.pi * r
    n = 60
    length = circumference / n
    polygon(t,length,n)


#circle('A',200)

def arc(t,r,angle):
    t = turtle.Turtle()
    import math
    arc_len = 2 * math.pi * r * angle/360
    n = int(arc_len/3) + 1
    step_len = arc_len/n
    step_ang = angle/n

    for i in range(n):
        t.fd(step_len)
        t.lt(step_ang)
    turtle.mainloop()
#arc('A',r = 100,100)

def flower(t,r,angle,side):
    t = turtle.Turtle()
    import math
    arc_len = 2 * math.pi * r * angle/360
    n = int(arc_len/3) + 1
    step_len = arc_len/n
    step_ang = angle/n

    for z in range(side):
        for j in range(2):
            for i in range(n):
                t.fd(step_len)
                t.lt(step_ang)
            t.lt(180-angle)
        t.lt(360/side)


    turtle.mainloop()

#flower('A',r=300,angle=20,side=15)


def triangle(t,side):
    t = turtle.Turtle()
    for j in range(side):
        for i in range(3):
            t.fd(100)
            t.rt(120)
        t.rt(360/side)
    turtle.mainloop()

#triangle('bob',10)

def polygon_tri(t,length,angle,side):
    t = turtle.Turtle()
    arc_len = 2 * math.pi * length * angle/360
    for i in range(side):
        for i in range(3):
            t.fd(arc_len)
            t.lt(120)
        t.fd(arc_len)
        t1 = (side-2)*180
        t.lt(180 - t1/side)
    #t.hideturtle()
    turtle.mainloop()

#polygon_tri('A',100,90,5)

def isosceles(t, r, angle):
    """Draws an icosceles triangle.
    The turtle starts and ends at the peak, facing the middle of the base.
    t: Turtle
    r: length of the equal legs
    angle: half peak angle in degrees
    """
    y = r * math.sin(angle * math.pi / 180)

    t.rt(angle)
    t.fd(r)
    t.lt(90+angle)
    t.fd(2*y)
    t.lt(90+angle)
    t.fd(r)
    t.lt(180-angle)


def polypie(t, n, r):
    """Draws a pie divided into radial segments.
    t: Turtle
    n: number of segments
    r: length of the radial spokes
    """
    angle = 360.0 / n
    for i in range(n):
        isosceles(t, r, angle/2)
        t.lt(angle)

def draw_pie(t, n, r):
    """Draws a pie, then moves into position to the right.
    t: Turtle
    n: number of segments
    r: length of the radial spokes
    """
    polypie(t, n, r)
    t.pu()
    t.fd(r*2 + 10)
    t.pd()
    turtle.mainloop()

#A = turtle.Turtle()
#draw_pie("A",6,100)

def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod

def a(x, y):
    x = x + 1
    return x * y

def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square

x = 1
y = x + 1
#print(c(x, y+3, x+y))

def ack(m,n):
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return ack(m-1,1)
        print(num2)
    elif m > 0 and n > 0:
        return ack(m-1,ack(m,n-1))

#print(ack(3,4))

import palindrome

def is_palindrome(a):
    """ it gets a word and determines if it is palindrome or not
    """
    if len(a) <= 1:
        return True
    elif palindrome.first(a) != palindrome.last(a):
        return False
    return is_palindrome(palindrome.middle(a))

#print(is_palindrome("noon"))

def is_power(a,b):
    """It gets two numbers and determines if a is a power of b, so a is bigger
    """
    if a % b != 0:
        return False
    elif a / b == 1:
        return True
    else:
        return is_power(a/b,b)

#print(is_power(16,4))

def gcd(a,b):
    """This gets two numbers and returns the greatest
       number they both dividable to without remainder.
    """
    if b == 0:
        return a
    r = a % b
    return gcd(b,r)


print(gcd(1008,546)) #must return 3
