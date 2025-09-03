from OpenGL.GL import *
from OpenGL.GLUT import *
import random

PALETTE = {
    "tin": (0.659, 0.635, 0.616),
    "zukoscar": (0.651, 0.157, 0.133),
    "brown": (0.69, 0.533, 0.337),
    "skyblue": (0.725, 0.898, 0.91),
    "gloomblue": (0.259, 0.447, 0.522),
    "grassgreen": (0.306, 0.529, 0.255),
    "decay": (0.322, 0.298, 0.227)
}

def getColor(k):
    return PALETTE.get(k, (1, 1, 1))

def drawLand():
    glBegin(GL_QUADS)
    glColor3f(*getColor("decay"))
    glVertex2f(-200, -100)
    glVertex2f(200, -100)
    glVertex2f(200, -300)
    glVertex2f(-200, -300)
    glEnd()

def drawHouse():
    rx, ry = 0, 0
    rh, rw = 120, 280
    bh, bw = 1.1*rh, 0.75*rw
    bx, by = rx, ry - (rh/2 + bh/2)
    dh, dw = 0.65*bh, 0.35*bw
    dx, dy = bx, by - (bh - dh)/2
    
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

    # Door
    glColor3f(*getColor("zukoscar"))
    glVertex2f(dx + dw/2, dy + dh/2)
    glVertex2f(dx - dw/2, dy + dh/2)
    glVertex2f(dx - dw/2, dy - dh/2)
    glVertex2f(dx + dw/2, dy - dh/2)
    glEnd()




class Raindrop:
    x_inc = 0
    y_inc = 0.1
    length = 20
    drops = []

    def __init__(self):
        self.x, self.y =  random.randint(-200, 200), random.randint(-300, 300)
        Raindrop.drops.append(self)
    
    def update(self):
        self.x += self.x_inc
        self.y -= self.y_inc
        self.x = ((self.x + 200) % 400) - 200
        self.y = ((self.y + 300) % 600) - 300

    def draw(self):
        offset = self.x_inc * 50
        tx, ty = self.x - offset, self.y + self.length/2
        bx, by = self.x + offset, self.y - self.length/2
        glBegin(GL_LINES)
        glColor3f(*getColor("gloomblue"))
        glVertex2f(tx, ty)
        glVertex2f(bx, by)
        glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    drawLand()
    drawHouse()
    for drop in Raindrop.drops: drop.draw()
    glutSwapBuffers()

def animate():
    for drop in Raindrop.drops: drop.update()
    glutPostRedisplay()

def keybinds(key, x, y):
    if key == b"w":
        Raindrop.y_inc -= 0.01
        Raindrop.y_inc = max(0.05, Raindrop.y_inc)
    if key == b"s":
        Raindrop.y_inc += 0.01
        Raindrop.y_inc = min(0.5, Raindrop.y_inc)
    if key == b"a":
        Raindrop.x_inc -= 0.01
        Raindrop.x_inc = max(-0.05, Raindrop.x_inc)
    if key == b"d":
        Raindrop.x_inc += 0.01
        Raindrop.x_inc = min(0.05, Raindrop.x_inc)
    
def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
    glutInitWindowPosition(0, 0)
    glutInitWindowSize(400, 600)
    glutCreateWindow(b"A rainy world")
    glutDisplayFunc(display)
    glutIdleFunc(animate)
    glutKeyboardFunc(keybinds)
    glMatrixMode(GL_PROJECTION)
    glOrtho(-200, 200, -300, 300, -1, 1)
    glClearColor(*getColor("skyblue"), 1)
    for i in range(50): Raindrop()
    glutMainLoop()
if __name__ == '__main__': main()
