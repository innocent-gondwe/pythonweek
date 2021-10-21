""" Functions that compute areas of shapes """

def square(a):
    """ This calculates area of a square """
    print("Area of the square is", a*a)


from math import pi
def circle(r):
    """ This calculates area of a circle """
    print("Area of the circle is", pi*r*r)


def triangle(b,h):
    """ This calculates area of a triangle """
    print("Area of a triangle is", (1/2)*b*h)
    

def trapezium(a,b,h):
    """ This calculates area of a trapezium """
    print("Area of a trapezium is", (1/2)*(a+b)*h)
    

def rectangle(l,w):
    """ This calculates area of a rectangle """
    print("Area of a rectangle is", l*w)