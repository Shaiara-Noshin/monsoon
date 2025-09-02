from OpenGL.GL import *
from OpenGL.GLUT import *

PALETTE = {
    "tin" : (0.659, 0.635, 0.616),
    "skyblue" : (0.725, 0.898, 0.91),
    "brown" : (0.69, 0.533, 0.337)
}

def getColor(k):
    return PALETTE.get(k, (1, 1, 1))

def drawHouse():
    rx, ry = 0, 0
    rh, rw = 140, 260
    bh, bw = 1.5*rh, 0.75*rw
    bx, by = rx, ry - (rh/2 + bh/2)
    
    # Roof
    glBegin(GL_TRIANGLES)
    glColor3f(*getColor("tin"))
    glVertex2f(rx, ry + rh/2)
    glVertex2f(rx - rw/2, ry - rh/2)
    glVertex2f(rx + rw/2, ry - rh/2)
    glEnd()

    # Body
    glBegin(GL_QUADS)
    glColor3f(*getColor("brown"))
    glVertex2f(bx + bw/2, by + bh/2)
    glVertex2f(bx - bw/2, by + bh/2)
    glVertex2f(bx - bw/2, by - bh/2)
    glVertex2f(bx + bw/2, by - bh/2)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    drawHouse()
    glutSwapBuffers()

def animate():
    glutPostRedisplay()
    
def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
    glutInitWindowPosition(0, 0)
    glutInitWindowSize(400, 600)
    glutCreateWindow(b"A rainy world")
    glutDisplayFunc(display)
    glutIdleFunc(animate)
    glMatrixMode(GL_PROJECTION)
    glOrtho(-200, 200, -400, 400, -1, 1)
    glClearColor(*getColor("skyblue"), 1)
    glutMainLoop()
if __name__ == '__main__': main()
