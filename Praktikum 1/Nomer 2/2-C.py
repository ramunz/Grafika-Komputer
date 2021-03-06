# Nama  : Muhammad Ramadhan Muna
# NIM   : 20051397059
# Praktikum 1 Grafika Komputer

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys


def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-6, 6, -6, 6, -1, 1)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glColor3f(1, 1, 1)
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.00)
    glVertex2f(-3.00, 2.00)
    glVertex2f(0.0, 0.00)
    glVertex2f(-2.00, 1.00)
    glVertex2f(0.0, 0.00)
    glVertex2f(-2.00, 0.00)
    glVertex2f(0.0, 0.00)
    glVertex2f(-2.00, -1.00)
    glVertex2f(0.0, 0.00)
    glVertex2f(-2.00, -2.00)
    glVertex2f(0.0, 0.00)
    glVertex2f(0.0, 0.00)
    glVertex2f(-1.00, -3.00)
    glEnd()

    glutSwapBuffers()


glutInit(sys.argv)
glutInitWindowSize(500, 500)
glutCreateWindow("Praktikum 1 Grafika Komputer - No. 2C")
glutDisplayFunc(draw)
glutMainLoop()
