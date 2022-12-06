from circle import MidpointCircle
from line import MidpointLine
from digits import Digits
from cube import CUBE


from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


line = MidpointLine()
circle = MidpointCircle()


class UI_Text:
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

    def initialize(self):
        glutInit()
        glutInitDisplayMode(GLUT_RGBA)
        glutInitWindowSize(self.win_size_x, self.win_size_y)
        glutInitWindowPosition(self.win_size_x // 2 - self.win_size_x, 0)
        glutCreateWindow(self.title)
        glClearColor(0, 0, 0, 0),
        glutDisplayFunc(self.show_screen)

        glViewport(0, 0, self.win_size_x, self.win_size_y)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-self.win_size_x, self.win_size_x, -self.win_size_y, self.win_size_y, 0.0, 1.0)
        glMatrixMode(GL_MODELVIEW)
        glPointSize(self.pixel_size)
        glLoadIdentity()

    # Glut Display
    def show_screen(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glColor3f(1, 1, 0)

        # Drawing methods
        self.text()

        glutSwapBuffers()

    def start_main_loop(self):
        glutMainLoop()

    def game_over_text(self, x=0, y=0):
        for i in range(10, 50, 4):
            self.g(adjust=0, x=i + x, y=i + y)
            self.a(adjust=150, x=i + x, y=i + y)
            self.m(adjust=300, x=i + x, y=i + y)
            self.e(adjust=450, x=i + x, y=i + y)
            self.o(adjust=750, x=i + x, y=i + y)
            self.v(adjust=900, x=i + x, y=i + y)
            self.e(adjust=1050, x=i + x, y=i + y)
            self.r(adjust=1200, x=i + x, y=i + y)

    def health_text(self, x=0, y=0):
        for i in range(10, 40, 4):
            self.h(adjust=0, x=i + x, y=i + y)
            self.e(adjust=150, x=i + x, y=i + y)
            self.a(adjust=300, x=i + x, y=i + y)
            self.l(adjust=450, x=i + x, y=i + y)
            self.t(adjust=600, x=i + x, y=i + y)
            self.h(adjust=750, x=i + x, y=i + y)

    def text(self, adjust=0, x=0, y=0):
        for i in range(0, 10, 2):
            circle.midpoint_circle_algorithm(700 - i, 0, 0)

        for i in range(0, 100, 10):
            circle.midpoint_circle_algorithm(700 - i, 0, 0)

        left_x1, left_y1 = -700, -900
        offset = -50

        line.midpoint(left_x1 + offset, left_y1, left_x1 + offset, 900)
        line.midpoint(-left_x1 - offset, left_y1, -left_x1 - offset, 900)

        for i in range(10):
            line.midpoint(left_x1 + offset + i, left_y1, left_x1 + offset + i + i * 10, 900)
            line.midpoint(-left_x1 - offset - i, left_y1, -left_x1 - offset - i - i * 10, 900)

        score_and_health_text = Digits()
        digit_position = 900
        SCORE = 10
        HEALTH = 50

        for i in range(10, 50, 4):
            score_and_health_text.draw_digit(f"{SCORE}", offset_x=i, offset_y=i, digit_position_x=digit_position)

        for i in range(10, 50, 2):
            score_and_health_text.draw_digit(f"{HEALTH}", digit_position_x=-1920 + i, offset_x=i, offset_y=i)

        # line.midpoint(x + 0 + adjust, y + 0, x + 0 + adjust, y + 70)  # Left Bottom
        # line.midpoint(x + 0 + adjust, y + 80, x + 0 + adjust, y + 150)  # Left Top
        # line.midpoint(x + 10 + adjust, y + 150, x + 70 + adjust, y + 150)  # Top
        # line.midpoint(x + 80 + adjust, y + 80, x + 80 + adjust, y + 150)  # Right Top
        # line.midpoint(x + 80 + adjust, y + 0, x + 80 + adjust, y + 70)  # Right Bottom
        # line.midpoint(x + 10 + adjust, y + 0, x + 70 + adjust, y + 0)  # Bottom
        # line.midpoint(x + 10 + adjust, y + 70, x + 70 + adjust, y + 70)  # Middle
        #
        # line.midpoint(x + 10 + adjust, y + 10, x + 70 + adjust, y + 60)  # Bottom Right Corner
        # line.midpoint(x + 70 + adjust, y + 10, x + 10 + adjust, y + 60)  # Bottom Left Corner
        # line.midpoint(x + 10 + adjust, y + 10 + 80, x + 70 + adjust, y + 60 + 80)  # Top Right Corner
        # line.midpoint(x + 70 + adjust, y + 10 + 80, x + 10 + adjust, y + 60 + 80)  # Top Left Corner

    def a(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 0, x + 0 + adjust, y + 70)  # Left Bottom
        line.midpoint(x + 0 + adjust, y + 80, x + 0 + adjust, y + 150)  # Left Top
        line.midpoint(x + 10 + adjust, y + 150, x + 70 + adjust, y + 150)  # Top
        line.midpoint(x + 80 + adjust, y + 80, x + 80 + adjust, y + 150)  # Right Top
        line.midpoint(x + 80 + adjust, y + 0, x + 80 + adjust, y + 70)  # Right Bottom
        line.midpoint(x + 10 + adjust, y + 70, x + 70 + adjust, y + 70)  # Middle

    def g(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 0, x + 0 + adjust, y + 70)  # Left Bottom
        line.midpoint(x + 0 + adjust, y + 80, x + 0 + adjust, y + 150)  # Left Top
        line.midpoint(x + 10 + adjust, y + 150, x + 70 + adjust, y + 150)  # Top
        line.midpoint(x + 80 + adjust, y + 0, x + 80 + adjust, y + 70)  # Right Bottom
        line.midpoint(x + 10 + adjust, y + 0, x + 70 + adjust, y + 0)  # Bottom
        line.midpoint(x + 10 + adjust, y + 70, x + 70 + adjust, y + 70)  # Middle

    def m(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 0, x + 0 + adjust, y + 70)  # Left Bottom
        line.midpoint(x + 0 + adjust, y + 80, x + 0 + adjust, y + 150)  # Left Top
        line.midpoint(x + 80 + adjust, y + 80, x + 80 + adjust, y + 150)  # Right Top
        line.midpoint(x + 80 + adjust, y + 0, x + 80 + adjust, y + 70)  # Right Bottom

        line.midpoint(x + 45 + adjust, y + 10 + 80, x + 70 + adjust, y + 60 + 80)
        line.midpoint(x + 40 + adjust, y + 10 + 80, x + 10 + adjust, y + 60 + 80)

    def e(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 0, x + 0 + adjust, y + 70)  # Left Bottom
        line.midpoint(x + 0 + adjust, y + 80, x + 0 + adjust, y + 150)  # Left Top
        line.midpoint(x + 10 + adjust, y + 150, x + 70 + adjust, y + 150)  # Top
        line.midpoint(x + 10 + adjust, y + 0, x + 70 + adjust, y + 0)  # Bottom
        line.midpoint(x + 10 + adjust, y + 70, x + 70 + adjust, y + 70)  # Middle

    def o(self,  x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 0, x + 0 + adjust, y + 70)  # Left Bottom
        line.midpoint(x + 0 + adjust, y + 80, x + 0 + adjust, y + 150)  # Left Top
        line.midpoint(x + 10 + adjust, y + 150, x + 70 + adjust, y + 150)  # Top
        line.midpoint(x + 80 + adjust, y + 80, x + 80 + adjust, y + 150)  # Right Top
        line.midpoint(x + 80 + adjust, y + 0, x + 80 + adjust, y + 70)  # Right Bottom
        line.midpoint(x + 10 + adjust, y + 0, x + 70 + adjust, y + 0)  # Bottom

    def v(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 80, x + 0 + adjust, y + 150)  # Left Top
        line.midpoint(x + 80 + adjust, y + 80, x + 80 + adjust, y + 150)  # Right Top

        line.midpoint(x + 45 + adjust, y + 0, x + 80 + adjust, y + 60)  # Bottom Right Corner
        line.midpoint(x + 35 + adjust, y + 0, x + 0 + adjust, y + 60)  # Bottom Left Corner

    def r(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 0, x + 0 + adjust, y + 70)  # Left Bottom
        line.midpoint(x + 0 + adjust, y + 80, x + 0 + adjust, y + 150)  # Left Top
        line.midpoint(x + 10 + adjust, y + 150, x + 70 + adjust, y + 150)  # Top
        line.midpoint(x + 80 + adjust, y + 80, x + 80 + adjust, y + 150)  # Right Top
        line.midpoint(x + 10 + adjust, y + 70, x + 70 + adjust, y + 70)  # Middle

        line.midpoint(x + 80 + adjust, y + 0, x + 10 + adjust, y + 60)  # Bottom Left Corner

    def h(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 0, x + 0 + adjust, y + 70)  # Left Bottom
        line.midpoint(x + 0 + adjust, y + 80, x + 0 + adjust, y + 150)  # Left Top
        line.midpoint(x + 80 + adjust, y + 80, x + 80 + adjust, y + 150)  # Right Top
        line.midpoint(x + 80 + adjust, y + 0, x + 80 + adjust, y + 70)  # Right Bottom
        line.midpoint(x + 10 + adjust, y + 70, x + 70 + adjust, y + 70)  # Middle

    def l(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 0, x + 0 + adjust, y + 70)  # Left Bottom
        line.midpoint(x + 0 + adjust, y + 80, x + 0 + adjust, y + 150)  # Left Top
        line.midpoint(x + 10 + adjust, y + 0, x + 70 + adjust, y + 0)  # Bottom

    def t(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 150, x + 80 + adjust, y + 150)  # Top
        line.midpoint(x + 35 + adjust, y + 0, x + 35 + adjust, y + 70)  # Left Bottom
        line.midpoint(x + 35 + adjust, y + 80, x + 35 + adjust, y + 150)  # Left Top


# gl = UI_Text(win_size_x=1920, win_size_y=900, pixel_size=1)
#
# gl.initialize()
# gl.start_main_loop()
