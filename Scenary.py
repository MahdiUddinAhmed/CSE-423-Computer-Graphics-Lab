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
    glColor3f(1.0, 1.0, 0.0)

    Ground = 0
    while Ground <= 500:
        glColor3f(0, 1.0, 0)
        draw_line(Ground, 0, Ground, 150)
        Ground = Ground + 1
    sky = 0
    while sky <= 500:
        glColor3f(0, 1.0, 1.0)
        draw_line(sky, 150, sky, 500)
        sky = sky + 1

    house = 100
    while house <= 200:
        glColor3f(1.0, 1.0, 0.0)
        draw_line(house, 100, house, 200)
        house = house + 1

    roof = 0
    while roof <= 50:
        glColor3f(1.0, 0.5, 0.0)
        draw_line(100 + roof, 200, 100 + roof, 200 + roof)
        roof = roof + 1
    roof = 0
    while roof <= 50:
        glColor3f(1.0, 0.5, 0.0)
        draw_line(150 + roof, 200, 150 + roof, 250 - roof)
        roof = roof + 1
    # door
    glColor3f(0.0, 0.0, 0.0)
    draw_line(140, 100, 160, 100)
    draw_line(140, 100, 140, 150)
    draw_line(140, 150, 160, 150)
    draw_line(160, 100, 160, 150)
    #window
    glColor3f(0, 1.0, 1.0)
    window1 = 0
    while window1 <= 10:
        draw_line(110+window1, 130, 110+window1, 150)
        window1 =  window1+ 1
    window2 = 0
    while window2 <= 10:
        draw_line(180+window2, 130, 180+window2, 150)
        window2 = window2+1
    # Shadow
    shadow = 0
    while shadow <= 100:
        glColor3f(21 / 255, 71 / 255, 52 / 255)
        draw_line(0 + shadow, 0, 100 + shadow, 100)
        shadow = shadow + 1
    r = 50
    x = 400
    y = 400
    # Drawing Sun
    glColor3f(1.0, 1.0, 0.0)
    draw_circle(x, y, r)

    # drawing clouds
    glColor3f(1.0, 1.0, 1.0)
    draw_circle(300, 300, 50)
    draw_circle(330, 300, 35)
    draw_circle(250, 300, 25)
    x = [(110, 420, 15), (170, 400, 25), (120, 350, 30), (85, 390, 25), (200, 410, 11), (130, 390, 40)]
    for i in x:
        draw_circle(i[0], i[1], i[2])

    # tree
    tree = 0
    while tree <= 15:
        glColor3f(.2549, .2078, .2078)
        draw_line(255 + tree, 110, 255 + tree, 210)
        tree = tree + 1
    glColor3f(21 / 255, 71 / 255, 52 / 255)
    x = [(320, 220, 15), (280, 200, 25), (290, 250, 30), (285, 230, 25), (300, 210, 11), (230, 220, 40)]
    for i in x:
        draw_circle(i[0], i[1], i[2])

    shadow2 = 0
    while shadow2 <= 15:
        draw_line(200 + shadow2, 0, 255 + shadow2, 110)
        shadow2 = shadow2 + 1

    glutSwapBuffers()


def write_pixel(x, y, zone):
    x, y = convert_to_zone_original(x, y, zone)
    draw_points(x, y)


# Question theke neoa
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


# I tried
def find_zone(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    if abs(dx) >= abs(dy):
        if dx >= 0 and dy > 0:
            zone = 0
        elif dx <= 0 < dy:
            zone = 3
        elif dx <= 0 and dy < 0:
            zone = 4
        else:
            zone = 7
    else:
        if dx >= 0 and dy > 0:
            zone = 1
        elif dx <= 0 < dy:
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


def draw_circle(x_ori, y_ori, r):
    x = 0
    y = r
    d = 1 - r
    write_pixel2(x, y, x_ori, + y_ori)
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

        write_pixel2(x, y, x_ori, y_ori)


def write_pixel2(x, y, x_ori, y_ori):
    draw_points(x_ori + x, y_ori + y)
    draw_line(x_ori, y_ori, x_ori + x, y_ori + y)
    draw_points(x_ori + y, y_ori + x)
    draw_line(x_ori, y_ori, x_ori + y, y_ori + x)
    draw_points(x_ori + y, y_ori - x)
    draw_line(x_ori, y_ori, x_ori + y, y_ori - x)
    draw_points(x_ori + x, y_ori - y)
    draw_line(x_ori, y_ori, x_ori + x, y_ori - y)
    draw_points(x_ori - x, y_ori - y)
    draw_line(x_ori, y_ori, x_ori - x, y_ori - y)
    draw_points(x_ori - y, y_ori - x)
    draw_line(x_ori, y_ori, x_ori - y, y_ori - x)
    draw_points(x_ori - y, y_ori + x)
    draw_line(x_ori, y_ori, x_ori - y, y_ori + x)
    draw_points(x_ori - x, y_ori + y)
    draw_line(x_ori, y_ori, x_ori - x, y_ori + y)


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500, 500)  # window size
    glutInitWindowPosition(0, 0)
    wind = glutCreateWindow(b"ID: 20301469 ")  # window name
    glutDisplayFunc(showScreen)
    glutMainLoop()
    glutDestroyWindow(wind)


if __name__ == "__main__":
    main()
