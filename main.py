from circle import MidpointCircle
from line import MidpointLine
from digits import Digits
from cube import CUBE


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
scale_radius = 0
SCORE = 0

line = MidpointLine()
circle = MidpointCircle()
colors = 0, 0, 0

PLAYER_CURRENT_X_POSITION = 0
PLAYER_CURRENT_Y_POSITION = - 600
PLAYER_RADIUS = 40

OBJECT1_CURRENT_X_POSITION = randint(-600, 600)  # - 600 => 600
OBJECT1_CURRENT_Y_POSITION = 900
OBJECT1_SPEED = 10

OBJECT2_CURRENT_X_POSITION = randint(-600, 600)
OBJECT2_CURRENT_Y_POSITION = 900
OBJECT2_SPEED = 12

OBJECT3_CURRENT_X_POSITION = randint(-600, 600)
OBJECT3_CURRENT_Y_POSITION = 900
OBJECT3_SPEED = 20

OBJECT4_CURRENT_X_POSITION = randint(-600, 600)
OBJECT4_CURRENT_Y_POSITION = 900
OBJECT4_SPEED = 14

OBJECT5_CURRENT_X_POSITION = randint(-600, 600)
OBJECT5_CURRENT_Y_POSITION = 900
OBJECT5_SPEED = 22

OBJECT6_CURRENT_X_POSITION = randint(-600, 600)
OBJECT6_CURRENT_Y_POSITION = 900
OBJECT6_SPEED = 10

OBJECT7_CURRENT_X_POSITION = randint(-600, 600)
OBJECT7_CURRENT_Y_POSITION = 900
OBJECT7_SPEED = 8

OBJECT8_CURRENT_X_POSITION = randint(-600, 600)
OBJECT8_CURRENT_Y_POSITION = 900
OBJECT8_SPEED = 14

OBJECT9_CURRENT_X_POSITION = randint(-600, 600)
OBJECT9_CURRENT_Y_POSITION = 900
OBJECT9_SPEED = 20

OBJECT10_CURRENT_X_POSITION = randint(-600, 600)
OBJECT10_CURRENT_Y_POSITION = 900
OBJECT10_SPEED = 12


OBSTACLE_RADIUS = 40

SPEED_MULTIPLIER = 2


def stars_draw(value=10):
    # Stars animation
    glBegin(GL_POINTS)
    for i in range(value):
        stars_x, stars_y = randint(-1920, -700), randint(-900, 900)
        glVertex2f(stars_x, stars_y),
    for i in range(value):
        stars_x, stars_y = randint(700, 1920), randint(-900, 900)
        glVertex2f(stars_x, stars_y)
    glEnd()

    # Air animation
    for i in range(value - 4,):
        line_x, line_y = randint(-1920, -700), randint(-900, 900)
        line1_y = randint(-900, 900)
        line.midpoint(line_x, line_y, line_x, line1_y)
    for i in range(value - 4,):
        line_x, line_y = randint(700, 1920), randint(-900, 900)
        line1_y = randint(-900, 900)
        line.midpoint(line_x, line_y, line_x, line1_y)


def animate():
    global y, scale_radius, colors, \
        OBJECT1_CURRENT_Y_POSITION, \
        OBJECT1_CURRENT_X_POSITION, \
        OBJECT2_CURRENT_Y_POSITION, \
        OBJECT2_CURRENT_X_POSITION, \
        OBJECT3_CURRENT_Y_POSITION, \
        OBJECT3_CURRENT_X_POSITION, \
        OBJECT4_CURRENT_Y_POSITION, \
        OBJECT4_CURRENT_X_POSITION, \
        OBJECT5_CURRENT_Y_POSITION, \
        OBJECT5_CURRENT_X_POSITION, \
        OBJECT1_SPEED, \
        OBJECT2_SPEED, \
        OBJECT3_SPEED, \
        OBJECT4_SPEED, \
        OBJECT5_SPEED, \
        OBJECT6_CURRENT_Y_POSITION, \
        OBJECT6_CURRENT_X_POSITION, \
        OBJECT7_CURRENT_Y_POSITION, \
        OBJECT7_CURRENT_X_POSITION, \
        OBJECT8_CURRENT_Y_POSITION, \
        OBJECT8_CURRENT_X_POSITION, \
        OBJECT9_CURRENT_Y_POSITION, \
        OBJECT9_CURRENT_X_POSITION, \
        OBJECT10_CURRENT_Y_POSITION, \
        OBJECT10_CURRENT_X_POSITION, \
        OBJECT6_SPEED, \
        OBJECT7_SPEED, \
        OBJECT8_SPEED, \
        OBJECT9_SPEED, \
        OBJECT10_SPEED, \
        OBSTACLE_RADIUS, \
        PLAYER_CURRENT_Y_POSITION, \
        PLAYER_CURRENT_X_POSITION, \
        SPEED_MULTIPLIER

    red = True
    green = False
    blue = False

    while True:
        SPEED_MULTIPLIER += 0.001
        scale_radius += 1
        auto_key_press.press(",")
        sleep(0.1)
        y -= 20
        if y <= -900:
            y = 900
            scale_radius = 0

        if red:
            red = False
            green = True
            blue = True
            colors = 1, 0, 0
        elif blue:
            red = False
            green = True
            blue = False
            colors = 0, 0, 1
        elif green:
            red = True
            green = False
            blue = True
            colors = 0, 1, 0,

        OBJECT1_CURRENT_Y_POSITION += - OBJECT1_SPEED * SPEED_MULTIPLIER
        if OBJECT1_CURRENT_Y_POSITION < - 900:
            OBJECT1_CURRENT_Y_POSITION = 900
            OBJECT1_CURRENT_X_POSITION = randint(-600, 600)

        OBJECT2_CURRENT_Y_POSITION += - OBJECT2_SPEED * SPEED_MULTIPLIER
        if OBJECT2_CURRENT_Y_POSITION < - 900:
            OBJECT2_CURRENT_Y_POSITION = 900
            OBJECT2_CURRENT_X_POSITION = randint(-600, 600)

        OBJECT3_CURRENT_Y_POSITION += - OBJECT3_SPEED * SPEED_MULTIPLIER
        if OBJECT3_CURRENT_Y_POSITION < - 900:
            OBJECT3_CURRENT_Y_POSITION = 900
            OBJECT3_CURRENT_X_POSITION = randint(-600, 600)

        OBJECT4_CURRENT_Y_POSITION += - OBJECT4_SPEED * SPEED_MULTIPLIER
        if OBJECT4_CURRENT_Y_POSITION < - 900:
            OBJECT4_CURRENT_Y_POSITION = 900
            OBJECT4_CURRENT_X_POSITION = randint(-600, 600)

        OBJECT5_CURRENT_Y_POSITION += - OBJECT5_SPEED * SPEED_MULTIPLIER
        if OBJECT5_CURRENT_Y_POSITION < - 900:
            OBJECT5_CURRENT_Y_POSITION = 900
            OBJECT5_CURRENT_X_POSITION = randint(-600, 600)

        OBJECT6_CURRENT_Y_POSITION += - OBJECT6_SPEED * SPEED_MULTIPLIER
        if OBJECT6_CURRENT_Y_POSITION < - 900:
            OBJECT6_CURRENT_Y_POSITION = 900
            OBJECT6_CURRENT_X_POSITION = randint(-600, 600)

        OBJECT7_CURRENT_Y_POSITION += - OBJECT7_SPEED * SPEED_MULTIPLIER
        if OBJECT7_CURRENT_Y_POSITION < - 900:
            OBJECT7_CURRENT_Y_POSITION = 900
            OBJECT7_CURRENT_X_POSITION = randint(-600, 600)

        OBJECT8_CURRENT_Y_POSITION += - OBJECT8_SPEED * SPEED_MULTIPLIER
        if OBJECT8_CURRENT_Y_POSITION < - 900:
            OBJECT8_CURRENT_Y_POSITION = 900
            OBJECT8_CURRENT_X_POSITION = randint(-600, 600)

        OBJECT9_CURRENT_Y_POSITION += - OBJECT9_SPEED * SPEED_MULTIPLIER
        if OBJECT9_CURRENT_Y_POSITION < - 900:
            OBJECT9_CURRENT_Y_POSITION = 900
            OBJECT9_CURRENT_X_POSITION = randint(-600, 600)

        OBJECT10_CURRENT_Y_POSITION += - OBJECT5_SPEED * SPEED_MULTIPLIER
        if OBJECT10_CURRENT_Y_POSITION < - 900:
            OBJECT10_CURRENT_Y_POSITION = 900
            OBJECT10_CURRENT_X_POSITION = randint(-600, 600)

        glutPostRedisplay()

def score_increment():
    global SCORE
    while True:
        sleep(1)
        glutPostRedisplay()
        SCORE += 1


def RESTART():
    global y, scale_radius, colors, \
        OBJECT1_CURRENT_Y_POSITION, \
        OBJECT1_CURRENT_X_POSITION, \
        OBJECT2_CURRENT_Y_POSITION, \
        OBJECT2_CURRENT_X_POSITION, \
        OBJECT3_CURRENT_Y_POSITION, \
        OBJECT3_CURRENT_X_POSITION, \
        OBJECT4_CURRENT_Y_POSITION, \
        OBJECT4_CURRENT_X_POSITION, \
        OBJECT5_CURRENT_Y_POSITION, \
        OBJECT5_CURRENT_X_POSITION, \
        OBJECT1_SPEED, OBJECT2_SPEED, \
        OBJECT3_SPEED, OBJECT4_SPEED, \
        OBJECT5_SPEED, SPEED_MULTIPLIER, \
        PLAYER_CURRENT_X_POSITION, \
        PLAYER_CURRENT_Y_POSITION, \
        PLAYER_RADIUS, \
        SCORE, \
        OBSTACLE_RADIUS, \
        OBJECT6_CURRENT_Y_POSITION, \
        OBJECT6_CURRENT_X_POSITION, \
        OBJECT7_CURRENT_Y_POSITION, \
        OBJECT7_CURRENT_X_POSITION, \
        OBJECT8_CURRENT_Y_POSITION, \
        OBJECT8_CURRENT_X_POSITION, \
        OBJECT9_CURRENT_Y_POSITION, \
        OBJECT9_CURRENT_X_POSITION, \
        OBJECT10_CURRENT_Y_POSITION, \
        OBJECT10_CURRENT_X_POSITION, \
        OBJECT6_SPEED, \
        OBJECT7_SPEED, \
        OBJECT8_SPEED, \
        OBJECT9_SPEED, \
        OBJECT10_SPEED

    PLAYER_CURRENT_X_POSITION = 0
    PLAYER_CURRENT_Y_POSITION = - 600
    PLAYER_RADIUS = 40

    SCORE = 0
    OBSTACLE_RADIUS = 40

    OBJECT1_CURRENT_X_POSITION = randint(-600, 600)  # - 600 => 600
    OBJECT1_CURRENT_Y_POSITION = 900
    OBJECT1_SPEED = 10

    OBJECT2_CURRENT_X_POSITION = randint(-600, 600)
    OBJECT2_CURRENT_Y_POSITION = 900
    OBJECT2_SPEED = 12

    OBJECT3_CURRENT_X_POSITION = randint(-600, 600)
    OBJECT3_CURRENT_Y_POSITION = 900
    OBJECT3_SPEED = 20

    OBJECT4_CURRENT_X_POSITION = randint(-600, 600)
    OBJECT4_CURRENT_Y_POSITION = 900
    OBJECT4_SPEED = 14

    OBJECT5_CURRENT_X_POSITION = randint(-600, 600)
    OBJECT5_CURRENT_Y_POSITION = 900
    OBJECT5_SPEED = 22

    OBJECT6_CURRENT_X_POSITION = randint(-600, 600)
    OBJECT6_CURRENT_Y_POSITION = 900
    OBJECT6_SPEED = 10

    OBJECT7_CURRENT_X_POSITION = randint(-600, 600)
    OBJECT7_CURRENT_Y_POSITION = 900
    OBJECT7_SPEED = 8

    OBJECT8_CURRENT_X_POSITION = randint(-600, 600)
    OBJECT8_CURRENT_Y_POSITION = 900
    OBJECT8_SPEED = 14

    OBJECT9_CURRENT_X_POSITION = randint(-600, 600)
    OBJECT9_CURRENT_Y_POSITION = 900
    OBJECT9_SPEED = 20

    OBJECT10_CURRENT_X_POSITION = randint(-600, 600)
    OBJECT10_CURRENT_Y_POSITION = 900
    OBJECT10_SPEED = 12

    SPEED_MULTIPLIER = 2




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

        self.player2_radius = 20
        self.player_move_x = 0
        self.player_move_y = 0

    def set_circle_values(self, radius, center_x=0, center_y=0):
        self.__radius = radius
        self.__center_x = center_x
        self.__center_y = center_y

    def initialize(self):
        glutInit()
        glutInitDisplayMode(GLUT_RGBA)
        glutInitWindowSize(self.win_size_x, self.win_size_y)
        glutInitWindowPosition(self.win_size_x // 2 - self.win_size_x, 0)
        glutCreateWindow(self.title)
        # glClearColor(0.3, 0.3, 0.3, 0)
        glClearColor(0, 0, 0, 0),
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
        print(x, y)

        self.player1_move_x = x - 450
        self.player1_move_y = y - 450
        glutPostRedisplay()

    def buttons(self, key, x, y):
        global PLAYER_CURRENT_Y_POSITION, PLAYER_CURRENT_X_POSITION, PLAYER_RADIUS
        move = 50

        if key == b"w":
            PLAYER_CURRENT_Y_POSITION += move
        if key == b"a" and PLAYER_CURRENT_X_POSITION > - 600:
            PLAYER_CURRENT_X_POSITION -= move
        if key == b"s":
            PLAYER_CURRENT_Y_POSITION -= move
        if key == b"d" and PLAYER_CURRENT_X_POSITION < 600:
            PLAYER_CURRENT_X_POSITION += move

        if self.player1_radius > 0:
            if key == b"m":
                PLAYER_RADIUS += move
            if key == b"n":
                PLAYER_RADIUS -= move
        else:
            self.player1_radius += 10

        if PLAYER_CURRENT_Y_POSITION < - self.win_size_y:
            PLAYER_CURRENT_Y_POSITION = self.win_size_y

        if PLAYER_CURRENT_X_POSITION < - self.win_size_x:
            PLAYER_CURRENT_X_POSITION = self.win_size_x

        if PLAYER_CURRENT_Y_POSITION > self.win_size_y:
            PLAYER_CURRENT_Y_POSITION = - self.win_size_y

        if PLAYER_CURRENT_X_POSITION > self.win_size_x:
            PLAYER_CURRENT_X_POSITION = - self.win_size_x

        # PLAYER_CURRENT_X_POSITION = self.player_move_x
        # PLAYER_CURRENT_Y_POSITION = self.player_move_y

        # print(f"Player x: {PLAYER_CURRENT_X_POSITION}, Player y: {PLAYER_CURRENT_Y_POSITION} Radius: {OBSTACLE_RADIUS}"),

        # Collision detection
        # if (PLAYER_CURRENT_Y_POSITION - PLAYER_RADIUS <= OBJECT1_CURRENT_Y_POSITION + OBSTACLE_RADIUS and PLAYER_CURRENT_Y_POSITION + PLAYER_RADIUS >=OBJECT1_CURRENT_Y_POSITION - OBSTACLE_RADIUS) and ((PLAYER_CURRENT_X_POSITION + PLAYER_RADIUS >= OBJECT1_CURRENT_X_POSITION - OBSTACLE_RADIUS and PLAYER_CURRENT_X_POSITION - PLAYER_RADIUS <= OBJECT1_CURRENT_X_POSITION + OBSTACLE_RADIUS)):
        #     print("Collision with Object 1")
        #     RESTART(),
        if PLAYER_CURRENT_Y_POSITION - PLAYER_RADIUS <= OBJECT1_CURRENT_Y_POSITION <= PLAYER_CURRENT_Y_POSITION + PLAYER_RADIUS and PLAYER_CURRENT_X_POSITION - PLAYER_RADIUS <= OBJECT1_CURRENT_X_POSITION <= PLAYER_CURRENT_X_POSITION + PLAYER_RADIUS:
            print("Collision with Object 1")
            RESTART()
        if PLAYER_CURRENT_Y_POSITION - PLAYER_RADIUS <= OBJECT2_CURRENT_Y_POSITION <= PLAYER_CURRENT_Y_POSITION + PLAYER_RADIUS and PLAYER_CURRENT_X_POSITION - PLAYER_RADIUS <= OBJECT2_CURRENT_X_POSITION <= PLAYER_CURRENT_X_POSITION + PLAYER_RADIUS:
            print("Collision with Object 2")
            RESTART()
        if PLAYER_CURRENT_Y_POSITION - PLAYER_RADIUS <= OBJECT3_CURRENT_Y_POSITION <= PLAYER_CURRENT_Y_POSITION + PLAYER_RADIUS and PLAYER_CURRENT_X_POSITION - PLAYER_RADIUS <= OBJECT3_CURRENT_X_POSITION <= PLAYER_CURRENT_X_POSITION + PLAYER_RADIUS:
            print("Collision with Object 3")
            RESTART()
        if PLAYER_CURRENT_Y_POSITION - PLAYER_RADIUS <= OBJECT4_CURRENT_Y_POSITION <= PLAYER_CURRENT_Y_POSITION + PLAYER_RADIUS and PLAYER_CURRENT_X_POSITION - PLAYER_RADIUS <= OBJECT4_CURRENT_X_POSITION <= PLAYER_CURRENT_X_POSITION + PLAYER_RADIUS:
            print("Collision with Object 4")
            RESTART()
        if PLAYER_CURRENT_Y_POSITION - PLAYER_RADIUS <= OBJECT5_CURRENT_Y_POSITION <= PLAYER_CURRENT_Y_POSITION + PLAYER_RADIUS and PLAYER_CURRENT_X_POSITION - PLAYER_RADIUS <= OBJECT5_CURRENT_X_POSITION <= PLAYER_CURRENT_X_POSITION + PLAYER_RADIUS:
            print("Collision with Object 5")
            RESTART()
        if PLAYER_CURRENT_Y_POSITION - PLAYER_RADIUS <= OBJECT6_CURRENT_Y_POSITION <= PLAYER_CURRENT_Y_POSITION + PLAYER_RADIUS and PLAYER_CURRENT_X_POSITION - PLAYER_RADIUS <= OBJECT6_CURRENT_X_POSITION <= PLAYER_CURRENT_X_POSITION + PLAYER_RADIUS:
            print("Collision with Object 6")
            RESTART()
        if PLAYER_CURRENT_Y_POSITION - PLAYER_RADIUS <= OBJECT7_CURRENT_Y_POSITION <= PLAYER_CURRENT_Y_POSITION + PLAYER_RADIUS and PLAYER_CURRENT_X_POSITION - PLAYER_RADIUS <= OBJECT7_CURRENT_X_POSITION <= PLAYER_CURRENT_X_POSITION + PLAYER_RADIUS:
            print("Collision with Object 7")
            RESTART()
        if PLAYER_CURRENT_Y_POSITION - PLAYER_RADIUS <= OBJECT8_CURRENT_Y_POSITION <= PLAYER_CURRENT_Y_POSITION + PLAYER_RADIUS and PLAYER_CURRENT_X_POSITION - PLAYER_RADIUS <= OBJECT8_CURRENT_X_POSITION <= PLAYER_CURRENT_X_POSITION + PLAYER_RADIUS:
            print("Collision with Object 8")
            RESTART()
        if PLAYER_CURRENT_Y_POSITION - PLAYER_RADIUS <= OBJECT9_CURRENT_Y_POSITION <= PLAYER_CURRENT_Y_POSITION + PLAYER_RADIUS and PLAYER_CURRENT_X_POSITION - PLAYER_RADIUS <= OBJECT9_CURRENT_X_POSITION <= PLAYER_CURRENT_X_POSITION + PLAYER_RADIUS:
            print("Collision with Object 9")
            RESTART()
        if PLAYER_CURRENT_Y_POSITION - PLAYER_RADIUS <= OBJECT10_CURRENT_Y_POSITION <= PLAYER_CURRENT_Y_POSITION + PLAYER_RADIUS and PLAYER_CURRENT_X_POSITION - PLAYER_RADIUS <= OBJECT10_CURRENT_X_POSITION <= PLAYER_CURRENT_X_POSITION + PLAYER_RADIUS:
            print("Collision with Object 10")
            RESTART(),



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
        CUBE(y=OBJECT1_CURRENT_Y_POSITION)

        # Stars
        glColor3f(1, 1, 1)
        stars_draw(value=10)

        # Obstacles
        glColor3f(1, 0, 0)
        self.obstacle(OBJECT1_CURRENT_X_POSITION, OBJECT1_CURRENT_Y_POSITION)
        self.obstacle(OBJECT2_CURRENT_X_POSITION, OBJECT2_CURRENT_Y_POSITION)
        self.obstacle(OBJECT3_CURRENT_X_POSITION, OBJECT3_CURRENT_Y_POSITION)
        self.obstacle(OBJECT4_CURRENT_X_POSITION, OBJECT4_CURRENT_Y_POSITION)
        self.obstacle(OBJECT5_CURRENT_X_POSITION, OBJECT5_CURRENT_Y_POSITION)
        self.obstacle(OBJECT6_CURRENT_X_POSITION, OBJECT6_CURRENT_Y_POSITION)
        self.obstacle(OBJECT7_CURRENT_X_POSITION, OBJECT7_CURRENT_Y_POSITION)
        self.obstacle(OBJECT8_CURRENT_X_POSITION, OBJECT8_CURRENT_Y_POSITION)
        self.obstacle(OBJECT9_CURRENT_X_POSITION, OBJECT9_CURRENT_Y_POSITION)
        self.obstacle(OBJECT10_CURRENT_X_POSITION, OBJECT10_CURRENT_Y_POSITION)

        # Player
        glColor3f(255, 255, 100)
        # circle.filled_circle(self.player2_radius, self.player2_move_x, self.player2_move_y)
        circle.midpoint_circle_algorithm(PLAYER_RADIUS, PLAYER_CURRENT_X_POSITION, PLAYER_CURRENT_Y_POSITION)
        circle.filled_circle(PLAYER_RADIUS // 2 - 4, PLAYER_CURRENT_X_POSITION, PLAYER_CURRENT_Y_POSITION + 10)

        offset = 350

        # line.midpoint(-500 - offset, y, -200 - offset, y)  # Top
        # line.midpoint(-500 - offset, y - 100, -200 - offset, y - 100)  # Bottom
        # line.midpoint(-500 - offset, y, -500 - offset, y - 100)  # Left
        # line.midpoint(-200 - offset, y - 100, -200 - offset, y)  # Right

        # Score
        score_draw = Digits()
        digit_position = 900
        glColor3f(colors[0], colors[1], colors[2])
        score_draw.draw_digit(f"{SCORE}", digit_position_x=digit_position)
        score_draw.draw_digit(f"{SCORE}", offset_x=20, offset_y=20, digit_position_x=digit_position)


        glutSwapBuffers()

    def start_main_loop(self):
        glutMainLoop()

    def road(self):
        left_x1, left_y1 = -700, -900
        offset = -50

        line.midpoint(left_x1 + offset, left_y1, left_x1 + offset, 900)
        line.midpoint(-left_x1 - offset, left_y1, -left_x1 - offset, 900),

        for i in range(10):
            line.midpoint(left_x1 + offset + i, left_y1, left_x1 + offset + i + i*10, 900)
            line.midpoint(-left_x1 - offset - i, left_y1, -left_x1 - offset - i - i*10, 900)

    def trees(self, offset_x=0, offset_y=0):
        circle.midpoint_circle_algorithm(scale_radius + 10, -700 + offset_x, y + offset_y)
        circle.midpoint_circle_algorithm(scale_radius + 10, -700 + 20 + offset_x, y + offset_y)
        circle.midpoint_circle_algorithm(scale_radius + 10, -700 + 10 + offset_x, y + 10 + offset_y)

        # line.midpoint(-700, -700 + y, 680, y - 800)

    def obstacle(self, obstacle_x_position, obstacle_y_position):
        circle.midpoint_circle_algorithm(OBSTACLE_RADIUS, obstacle_x_position, obstacle_y_position)
        circle.filled_circle(OBSTACLE_RADIUS // 2 - 4, obstacle_x_position, obstacle_y_position - 10)


gl = Start_OpenGL(win_size_x=1920, win_size_y=900, pixel_size=1)

gl.initialize()
gl.start_main_loop()


