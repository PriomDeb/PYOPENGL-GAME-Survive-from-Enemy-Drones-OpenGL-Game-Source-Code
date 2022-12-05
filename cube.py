from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math


from line import MidpointLine

line = MidpointLine()


def CUBE(value=100, x=0, y=0):
    for i in range(value):
        line.midpoint(0 + x, i + y, value + x, i + y)


























