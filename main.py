from circle import MidpointCircle
from line import MidpointLine


from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math


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

        glViewport(0, 0, self.win_size_x, self.win_size_y)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-self.win_size_x, self.win_size_x, -self.win_size_y, self.win_size_y, 0.0, 1.0)
        glMatrixMode(GL_MODELVIEW)
        glPointSize(self.pixel_size)
        glLoadIdentity()

    def mouse(self, x, y):
        print(x, y)
        # if x < self.win_size_x / 2:
        #     self.move_x = - x
        # if y < self.win_size_y / 2:
        #     self.move_y = - y
        #
        # if x > self.win_size_x / 2:
        #     self.move_x = x
        # if y > self.win_size_y / 2:
        #     self.move_y = y

        self.move_x = x - 450
        self.move_y = y - 450
        glutPostRedisplay()

    def buttons(self, key, x, y):
        move = 20
        if key == b"w":
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
        if key == b"e":
            self.move_x += move
            self.move_y += move
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
        circle = MidpointCircle()
        circle.midpoint_circle_algorithm(250, self.move_x, self.move_y)
        circle.filled_circle(50, self.move_x, self.move_y)

        line = MidpointLine()
        line.midpoint(0 + self.move_x, 0 + self.move_y, 0 + self.move_x, 250 + self.move_y)

        glutSwapBuffers()

    def start_main_loop(self):
        glutMainLoop()


gl = Start_OpenGL(win_size_x=900, win_size_y=900, pixel_size=1)

gl.initialize()
gl.start_main_loop()


