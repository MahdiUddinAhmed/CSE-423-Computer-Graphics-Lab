#20301469
#Mahdi Uddin Ahmed

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

points = 0


def draw_points(x, y):
    global points
    points = points + 1
    glPointSize(1)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(5 / 255, 250 / 255, 225 / 255)  # color set (RGB)
    r = 150
    x = 250
    y = 250
    # Drawing Circle
    draw_circle(x, y, r)
    '''
    draw_circle(x+(r/2), y, r/2)
    draw_circle(x,y+(r/2), r / 2)
    draw_circle(x-(r/2), y, r/2)
    draw_circle(x,y-(r/2), r / 2)
    draw_circle(x+(r/2.83), y+(r/2.83), r/2)
    draw_circle(x +(r /2.83), y - (r /2.83), r / 2)
    draw_circle(x - (r /2.83) , y + (r /2.83), r / 2)
    draw_circle(x - (r /2.83), y - (r /2.83), r / 2)
'''
    glutSwapBuffers()


def draw_circle(x_ori, y_ori, r):
    x = 0
    y = r
    d = 1 - r
    write_pixel(x, y, x_ori, + y_ori)
    while x < y:
        inc_E = 2 * x + 3
        inc_SE = 2 * x - 2 * y + 5
        if d < 0:
            d += inc_E
            x = x + 1

        else:
            d += inc_SE
            y = y - 1
            x = x + 1


        write_pixel(x, y, x_ori, y_ori)



def write_pixel(x, y, x_ori, y_ori):
    draw_points(x_ori + x, y_ori + y)
    draw_points(x_ori + y, y_ori + x)
    draw_points(x_ori + y, y_ori - x)
    draw_points(x_ori + x, y_ori - y)
    draw_points(x_ori - x, y_ori - y)
    draw_points(x_ori - y, y_ori - x)
    draw_points(x_ori - y, y_ori + x)
    draw_points(x_ori - x, y_ori + y)




def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(710, 290)
    wind = glutCreateWindow(b"Midpoint Circle Drawing")
    glutDisplayFunc(showScreen)
    glutMainLoop()


if __name__ == '__main__':
    main()
