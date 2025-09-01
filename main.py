from OpenGL.GL import *
from OpenGL.GLUT import *

def display():
    glBegin(GL_TRIANGLES)
    glColor3f(0, 0, 1)
    glVertex2f(-30, 0)
    glVertex2f(30, 0)
    glVertex2f(0, 45)
    glEnd()
    glutSwapBuffers()

def animate():
    glutPostRedisplay()
    
def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowPosition(0, 0)
    glutInitWindowSize(400, 800)
    glutCreateWindow(b"A rainy world")
    glutDisplayFunc(display)
    glutIdleFunc(animate)
    glMatrixMode(GL_PROJECTION)
    glOrtho(-200, 200, -400, 400, -1, 1)
    glutMainLoop()
if __name__ == '__main__': main()