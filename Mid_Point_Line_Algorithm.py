#Ja bujhi tai Lekhsi just conditions implement kora try korsi
#Output paben na


#Lab1 theke neoa
from OpenGL.GL import *
from OpenGL.GLUT import *

def draw_points(x, y):
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
    glColor3f(1.0, 1.0, 0.0)  # konokichur color set (RGB)
    # Drawing the ID Digits
    draw_line(50, 250, 100, 250)
    draw_line(50, 250, 50, 250)
    draw_line(50, 250, 50, 150)
    draw_line(50, 150, 100, 150)
    draw_line(100, 150, 100, 200)
    draw_line(100, 200, 50, 200)
    draw_line(50, 200, 100, 200)



    draw_line(50+80, 250, 100+80, 250)
    draw_line(50 + 80, 250, 50 + 80, 200)
    draw_line(50 + 80, 250, 100 + 80, 250)
    draw_line(100 + 80, 250, 100 + 80, 200)
    draw_line(100 + 80, 200, 100 + 80, 150)
    draw_line(100 + 80, 150, 50 + 80, 150)
    draw_line(50 + 80, 250, 50 + 80, 200)
    draw_line(50 + 80, 200, 100 + 80, 200)
    draw_line(100 + 80, 150, 50 + 80, 150)
    draw_line(50 + 80, 150, 100 + 80, 150)




    glutSwapBuffers()
#kaj korena keno jani
def write_pixel(x, y, zone):
    x, y = convert_to_zone_original(x, y, zone)
    print(x, y)
    draw_points(x, y)

#Question theke neoa
def draw_line(x1, y1, x2, y2):
    zone = find_zone(x1, y1, x2, y2)
    x1, y1 = convert_zone_to_zero(x1, y1, zone)
    x2, y2 = convert_zone_to_zero(x2, y2, zone)
    dx = x2 - x1
    dy = y2 - y1
    d = 2 * dy - dx
    incE = 2 * dy
    incNE = 2 * (dy - dx)
    y = y1
    x = x1
    while x <= x2:
        write_pixel(x, y, zone)
        if d > 0:
            d = d + incNE
            y = y + 1
        else:
            d = d + incE
        x = x + 1

#I tried
def find_zone(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    if abs(dx) >= abs(dy):
        if dx >= 0 and dy > 0:
            zone = 0
        elif dx <= 0 and dy > 0:
            zone = 3
        elif dx <= 0 and dy < 0:
            zone = 4
        else:
            zone = 7
    else:
        if dx >= 0 and dy > 0:
            zone = 1
        elif dx <= 0 and dy > 0:
            zone = 2
        elif dx <= 0 and dy < 0:
            zone = 5
        else:
            zone = 6

    return zone

def convert_zone_to_zero(x, y, zone):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return y, -x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return -y, x
    else:
        return x, -y


def convert_to_zone_original(x, y, zone):
    if zone == 2:
        return -y, x
    elif zone == 6:
        return y, -x
    else:
        return convert_zone_to_zero(x, y, zone)


#exkhon ki korbo janina
#def draw_point():


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500, 500)  # window size
    glutInitWindowPosition(0, 0)
    wind = glutCreateWindow(b"ID: 20301469 Draw:69")  # window name
    glutDisplayFunc(showScreen)
    glutMainLoop()
    glutDestroyWindow(wind)


if __name__ == "__main__":
    main()

