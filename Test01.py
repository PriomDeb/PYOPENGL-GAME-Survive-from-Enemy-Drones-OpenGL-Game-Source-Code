# import pygame
# from pygame.locals import *
#
# from OpenGL.GL import *
# from OpenGL.GLU import *
#
# verticies = (
#     (1, -1, -1),
#     (1, 1, -1),
#     (-1, 1, -1),
#     (-1, -1, -1),
#     (1, -1, 1),
#     (1, 1, 1),
#     (-1, -1, 1),
#     (-1, 1, 1)
#     )
#
# edges = (
#     (0,1),
#     (0,3),
#     (0,4),
#     (2,1),
#     (2,3),
#     (2,7),
#     (6,3),
#     (6,4),
#     (6,7),
#     (5,1),
#     (5,4),
#     (5,7)
#     )
#
#
# def Cube():
#     glBegin(GL_LINES)
#     for edge in edges:
#         for vertex in edge:
#             glVertex3fv(verticies[vertex])
#     glEnd()
#
#
# def main():
#     pygame.init()
#     display = (800,600)
#     pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
#
#     gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
#
#     glTranslatef(0.0,0.0, -5)
#
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#
#         glRotatef(1, 3, 1, 1)
#         glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
#         Cube()
#
#         pygame.display.flip()
#         pygame.time.wait(10)
#
#
# main()
import numpy as np

from circle import MidpointCircle
from line import MidpointLine
from digits import Digits


from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

import threading
from time import sleep
from pynput.keyboard import Key, Controller

rotate = 0
keyboard = Controller()

def rotating():
    global rotate
    while True:
        keyboard.press("z")
        sleep(0.01)z
        rotate += 1
        glutPostRedisplay()








class Start_OpenGL:
    """
    This class is designed to a circle using midpoint circle algorithm with 8-way symmetry
    Author- Priom Deb
    http://priomdeb.com, priom@priomdeb.com
    """
    def __init__(self, win_size_x=500, win_size_y=500, win_pos_x=0, win_pos_y=0, title="Priom OpenGL Class",
                 pixel_size=1):
        self.win_size_x = win_size_x
        self.win_size_y = win_size_y
        self.win_pos_x = win_pos_x
        self.win_pos_y = win_pos_y
        self.title = title
        self.pixel_size = pixel_size

        self.__midpoint_points = []
        self.__radius = 450
        self.__center_x = 0
        self.__center_y = 0

        self.circle_radius = 0
        self.move_x = 0
        self.move_y = 0
        self.score = 10
        self.rotate = 0

    def set_circle_values(self, radius, center_x=0, center_y=0):
        self.__radius = radius
        self.__center_x = center_x
        self.__center_y = center_y

    def initialize(self):
        glutInit()
        glutInitDisplayMode(GLUT_RGBA)
        glutInitWindowSize(self.win_size_x, self.win_size_y)
        glutInitWindowPosition(500, 0)
        glutCreateWindow(self.title)
        glClearColor(0, 0, 0, 0)
        glutDisplayFunc(self.show_screen)

        glutKeyboardFunc(self.buttons)
        thread_1 = threading.Thread(target=rotating)
        thread_1.start()

        glViewport(0, 0, self.win_size_x, self.win_size_y)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-self.win_size_x, self.win_size_x, -self.win_size_y, self.win_size_y, 0.0, 1.0)
        glMatrixMode(GL_MODELVIEW)
        glPointSize(self.pixel_size)
        glLoadIdentity()


    def buttons(self, key, x, y):
        move = 20
        if key == b"w":
            self.score += 1
            self.move_y += move
        if key == b"s":
            self.move_y -= move
        if key == b"a":
            self.move_x -= move
        if key == b"d":
            self.move_x += move

        if key == b"q":
            self.move_x -= move
            self.move_y += move
            self.rotate += 15
        if key == b"e":
            self.move_x += move
            self.move_y += move
            self.rotate += - 15
        if key == b"z":
            self.move_x -= move
            self.move_y -= move
        if key == b"c":
            self.move_x += move
            self.move_y -= move

        glutPostRedisplay()

    # Glut Display
    def show_screen(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glColor3f(1, 1, 0)

        # Drawing methods
        glColor3f(.5, .3, .7)
        glPointSize(5)

        glBegin(GL_LINES)
        glVertex2f(0, -1)
        glVertex2f(0, 1)
        glVertex2f(1, 0)
        glVertex2f(-1, 0)
        glEnd()

        glColor3f(0, .5, 0)
        glBegin(GL_POINTS)
        glVertex2f(.75, .80)
        glVertex2f(.1, 0)
        glEnd()

        glBegin(GL_QUADS)
        glVertex2f(200, 200)
        glVertex2f(-200, 200)
        glVertex2f(-200, -200)
        glVertex2f(200, -200)
        glColor3f(0, 255, 0)
        glEnd()

        a = math.cos(math.radians(rotate))
        b = math.sin(math.radians(rotate))

        r = np.array([[a, -b, 0],
                      [b, a, 0],
                      [0, 0, 1]])

        v1 = np.array([[200],
                       [200],
                       [1]])
        v2 = np.array([[-200],
                       [200],
                       [1]])
        v3 = np.array([[-200],
                       [-200],
                       [1]])
        v4 = np.array([[200],
                       [-200],
                       [1]])

        v11 = np.matmul(r, v1)
        v22 = np.matmul(r, v2)
        v33 = np.matmul(r, v3)
        v44 = np.matmul(r, v4)

        glBegin(GL_QUADS)
        glVertex2f(v11[0][0], v11[1][0])
        glVertex2f(v22[0][0], v22[1][0])
        glVertex2f(v33[0][0], v33[1][0])
        glVertex2f(v44[0][0], v44[1][0])
        glEnd()


        glutSwapBuffers()


    def start_main_loop(self):
        glutMainLoop()


gl = Start_OpenGL(win_size_x=800, win_size_y=800, pixel_size=1)

gl.initialize()
gl.start_main_loop()




