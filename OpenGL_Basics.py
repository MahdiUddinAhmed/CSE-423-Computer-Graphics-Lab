from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random


def draw_points(x, y):
    glPointSize(5)  # pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x, y)  # jekhane show korbe pixel
    glEnd()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    #glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0)  # konokichur color set (RGB)
    # call the draw methods here
    draw_points(450, 450)
    # --------------------------------------------------------
    # -----------------------TASK2----------------------------
    # --------------------------------------------------------
    glColor3f(0.9, 0.0, 0.0)
    drawline(100, 100, 100, 300)  # Side
    drawline(100, 100, 300, 100)  # floor
    drawline(300, 100, 300, 300)  # side
    drawline(100, 300, 300, 300)  # Top
    drawline(100, 300, 200, 400)
    drawline(300, 300, 200, 400)

    # window1
    glColor3f(0.0, 0.9, 0.0)
    drawline(120, 120, 120, 160)
    drawline(120, 120, 160, 120)
    drawline(160, 120, 160, 160)
    drawline(120, 160, 160, 160)

    # window2
    glColor3f(0.0, 0.9, 0.0)
    drawline(250, 120, 250, 160)
    drawline(250, 120, 290, 120)
    drawline(290, 120, 290, 160)
    drawline(250, 160, 290, 160)

    # door
    glColor3f(0.0, 0.0, 0.9)
    drawline(190, 100, 190, 190)
    drawline(220, 100, 220, 190)
    drawline(190, 190, 220, 190)
    draw_points(210,130)

    # --------------------------------------------------------
    # -----------------------TASK1----------------------------
    # --------------------------------------------------------
    

    glColor3f(1.0, 1.0, 0.5)
    x = [random.randint(10, 500) for i in range(50)]
    y = [random.randint(400, 500) for i in range(50)]
    for i in range(50):
        draw_points(x[i], y[i])
    glutSwapBuffers()


def drawline(x, y, a, b):
    glBegin(GL_LINES)
    glVertex2f(x, y)
    glVertex2f(a, b)
    glEnd()


def DrawLine(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    d = 2 * dy - dx
    incE = 2 * dy
    incNE = 2 * (dy - dx)
    y = y1
    x = x1
    while x <= x2:
        draw_points(x, y)
        if d > 0:
            d = d + incNE
            y = y + 1
        else:
            d = d + incE

        x = x + 1


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)  # window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice")  # window name
glutDisplayFunc(showScreen)

glutMainLoop()
