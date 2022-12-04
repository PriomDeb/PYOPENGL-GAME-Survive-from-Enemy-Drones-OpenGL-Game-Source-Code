import OpenGL.GL.shaders

from circle import MidpointCircle
from line import MidpointLine
from digits import Digits


from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math
from random import randint
from threading import Thread
from time import sleep
from pynput.keyboard import Key, Controller

y = 900
auto_key_press = Controller()
stars = True
scale_radius = 0
score = 10

line = MidpointLine()
circle = MidpointCircle()


def animate():
    global y, scale_radius
    while True:
        scale_radius += 1
        auto_key_press.press(",")
        sleep(0.1)
        y -= 20
        if y <= -900:
            y = 900
            scale_radius = 0
        glutPostRedisplay()

def score_increment():
    global score
    while True:
        sleep(1)
        glutPostRedisplay()
        score += 1





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

        self.player1_radius = 40
        self.player1_move_x = 0
        self.player1_move_y = 0
        self.score = 10

        self.player2_radius = 40
        self.player2_move_x = 0
        self.player2_move_y = 0

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
        glClearColor(0.3, 0.3, 0.3, 0)
        glutDisplayFunc(self.show_screen)

        glutKeyboardFunc(self.buttons)
        glutMotionFunc(self.mouse)

        animation_thread = Thread(target=animate)
        animation_thread.start()

        score_thread = Thread(target=score_increment)
        score_thread.start()

        glViewport(0, 0, self.win_size_x, self.win_size_y)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-self.win_size_x, self.win_size_x, -self.win_size_y, self.win_size_y, 0.0, 1.0)
        glMatrixMode(GL_MODELVIEW)
        glPointSize(self.pixel_size)
        glLoadIdentity()

    def mouse(self, x, y):
        # print(x, y)

        self.player1_move_x = x - 450
        self.player1_move_y = y - 450
        glutPostRedisplay()

    def buttons(self, key, x, y):
        move = 50
        if key == b"w":
            self.score += 1
            self.player1_move_y += move
        if key == b"s":
            self.player1_move_y -= move
        if key == b"a":
            self.player1_move_x -= move
        if key == b"d":
            self.player1_move_x += move

        if self.player1_radius > 0:
            if key == b"m":
                self.player1_radius += move
            if key == b"n":
                self.player1_radius -= move
        else:
            self.player1_radius += 10

        if self.player1_move_y < - self.win_size_y:
            self.player1_move_y = self.win_size_y
        if self.player1_move_x < - self.win_size_x:
            self.player1_move_x = self.win_size_x
        if self.player1_move_y > self.win_size_y:
            self.player1_move_y = - self.win_size_y
        if self.player1_move_x > self.win_size_x:
            self.player1_move_x = - self.win_size_x

        if self.player2_move_y < - self.win_size_y:
            self.player2_move_y = self.win_size_y
        if self.player2_move_x < - self.win_size_x:
            self.player2_move_x = self.win_size_x
        if self.player2_move_y > self.win_size_y:
            self.player2_move_y = - self.win_size_y
        if self.player2_move_x > self.win_size_x:
            self.player2_move_x = - self.win_size_x

        if key == b"6":
            self.player2_move_x += move
        if key == b"8":
            self.player2_move_y += move
        if key == b"4":
            self.player2_move_x -= move
        if key == b"2":
            self.player2_move_y -= move

        if self.player1_radius + self.player1_move_x == self.player2_radius + self.player2_move_x \
                and self.player1_radius + self.player1_move_y == self.player2_radius + self.player2_move_y:
            pass
            # print("Collision")

        if key == b"t":
            global stars
            stars = True

        glutPostRedisplay()

    def another_circle(self, radius):
        circle1 = MidpointCircle()
        circle1.midpoint_circle_algorithm(500)

    # Glut Display
    def show_screen(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glColor3f(1, 1, 0)

        # Drawing methods
        self.road()
        self.trees()
        self.trees(1350, 0)

        # circle.midpoint_circle_algorithm(scale_radius, self.player1_move_x - 40, y)
        # circle.midpoint_circle_algorithm(scale_radius, self.player1_move_x - 600, y)

        glColor3f(255, 255, 100)
        circle.filled_circle(self.player2_radius, self.player2_move_x, self.player2_move_y)

        offset = 350

        line.midpoint(-500 - offset, y, -200 - offset, y)  # Top
        line.midpoint(-500 - offset, y - 100, -200 - offset, y - 100)  # Bottom
        line.midpoint(-500 - offset, y, -500 - offset, y - 100)  # Left
        line.midpoint(-200 - offset, y - 100, -200 - offset, y)  # Right

        score_draw = Digits()
        score_draw.draw_digit(f"{score}")



        glutSwapBuffers()

    def start_main_loop(self):
        glutMainLoop()

    def road(self):
        left_x1, left_y1 = -700, -900
        offset = 100

        line.midpoint(left_x1 + offset, left_y1, left_x1 + 100 + offset, 900)
        line.midpoint(-left_x1 - offset, left_y1, -left_x1 - 100 - offset, 900)

        for i in range(10):
            line.midpoint(left_x1 + offset + i, left_y1, left_x1 + 100 + offset + i, 900)
            line.midpoint(-left_x1 - offset - i, left_y1, -left_x1 - 100 - offset - i, 900)

    def trees(self, offset_x=0, offset_y=0):
        circle.midpoint_circle_algorithm(scale_radius + 10, -700 + offset_x, y + offset_y)
        circle.midpoint_circle_algorithm(scale_radius + 10, -700 + 20 + offset_x, y + offset_y)
        circle.midpoint_circle_algorithm(scale_radius + 10, -700 + 10 + offset_x, y + 10 + offset_y)

        # line.midpoint(-700, -700 + y, 680, y - 800)


gl = Start_OpenGL(win_size_x=900, win_size_y=900, pixel_size=1)

gl.initialize()
gl.start_main_loop()


