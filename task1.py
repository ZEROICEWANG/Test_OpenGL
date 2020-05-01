from OpenGL.GL import *
from OpenGL.GLUT import *


def draw_point():
    # ---------------------------------------------------------------
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(10)
    glBegin(GL_POINTS)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(0.5, 0.5)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(0.5, -0.5)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(-0.5, 0.5)
    glColor3f(1.0, 0.0, 1.0)
    glVertex2f(-0.5, -0.5)
    glEnd()
    glFlush()


def draw_line():
    glColor3f(0.0, 1.0, 0.0)
    glLineWidth(2)
    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(0.5, 0.5)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(0.5, -0.5)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(-0.5, 0.5)
    glColor3f(1.0, 0.0, 1.0)
    glVertex2f(-0.5, -0.5)
    glEnd()
    glFlush()


def draw_lines():
    glLineWidth(2)
    glBegin(GL_LINE_STRIP)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(0.5, 0.5)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(0.5, -0.5)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(-0.5, 0.5)
    glColor3f(1.0, 0.0, 1.0)
    glVertex2f(-0.5, -0.5)
    glEnd()
    glFlush()


def draw_line_loop():
    glLineWidth(2)
    glBegin(GL_LINE_LOOP)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(0.5, 0.5)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(0.5, -0.5)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(-0.5, 0.5)
    glColor3f(1.0, 0.0, 1.0)
    glVertex2f(-0.5, -0.5)
    glEnd()
    glFlush()


def draw_triangles():
    glColor3f(0.0, 0.0, 1.0)
    glLineWidth(2)
    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(0.5, 0.5)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(0.5, -0.5)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(-0.5, 0.5)
    glColor3f(1.0, 0.0, 1.0)
    glVertex2f(-0.5, -0.5)
    glEnd()
    glFlush()


def draw_triangles_strip():
    glColor3f(0.0, 0.0, 1.0)
    glLineWidth(2)
    glBegin(GL_TRIANGLE_STRIP)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(0.5, 0.5)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(0.5, -0.5)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(-0.5, 0.5)
    glColor3f(1.0, 0.0, 1.0)
    glVertex2f(-0.5, -0.5)
    glEnd()
    glFlush()


def draw_triangles_fan():
    glColor3f(0.0, 0.0, 1.0)
    glLineWidth(2)
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(0.5, 0.5)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(0.5, -0.5)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(-0.5, 0.5)
    glColor3f(1.0, 0.0, 1.0)
    glVertex2f(-0.5, -0.5)
    glEnd()
    glFlush()


if __name__ == "__main__":
    print('使用四个点进行不同绘制：(0.5,0.5),(0.5,-0.5),(-0.5,0.5),(-0.5,-0.5),')
    glutInit()  # 1. 初始化glut库
    glutCreateWindow('point')  # 2. 创建glut窗口
    glutDisplayFunc(draw_point)  # 3. 注册回调函数draw()

    glutCreateWindow('line')  # 2. 创建glut窗口
    glutDisplayFunc(draw_line)  # 3. 注册回调函数draw()

    glutCreateWindow('lines')  # 2. 创建glut窗口
    glutDisplayFunc(draw_lines)  # 3. 注册回调函数draw()

    glutCreateWindow('line_loop')  # 2. 创建glut窗口
    glutDisplayFunc(draw_line_loop)  # 3. 注册回调函数draw()

    glutCreateWindow('triangles')  # 2. 创建glut窗口
    glutDisplayFunc(draw_triangles)  # 3. 注册回调函数draw()

    glutCreateWindow('triangles_strip')  # 2. 创建glut窗口
    glutDisplayFunc(draw_triangles_strip)  # 3. 注册回调函数draw()

    glutCreateWindow('triangles_fan')  # 2. 创建glut窗口
    glutDisplayFunc(draw_triangles_fan)  # 3. 注册回调函数draw()

    glutMainLoop()  # 4. 进入glut主循环
