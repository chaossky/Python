from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

# ===== 셰이더 코드 =====
vertex_shader_source = """
#version 330 core
layout (location = 0) in vec3 position;   // 입력: 정점 좌표
layout (location = 1) in vec3 color;      // 입력: 색상
out vec3 newColor;                        // 출력: 색상 전달
void main()
{
    gl_Position = vec4(position, 1.0);    // 클립 공간 좌표
    newColor = color;                     // 색상 전달
}
"""

fragment_shader_source = """
#version 330 core
in vec3 newColor;              // 정점 셰이더에서 받은 색상
out vec4 FragColor;            // 최종 출력 색상
void main()
{
    FragColor = vec4(newColor, 1.0);
}
"""

# ===== 셰이더 컴파일 =====
def compile_shader(source, shader_type):
    shader = glCreateShader(shader_type)
    glShaderSource(shader, source)
    glCompileShader(shader)

    # 에러 체크
    if glGetShaderiv(shader, GL_COMPILE_STATUS) != GL_TRUE:
        raise RuntimeError(glGetShaderInfoLog(shader))
    return shader

def create_shader_program():
    vertex_shader = compile_shader(vertex_shader_source, GL_VERTEX_SHADER)
    fragment_shader = compile_shader(fragment_shader_source, GL_FRAGMENT_SHADER)

    program = glCreateProgram()
    glAttachShader(program, vertex_shader)
    glAttachShader(program, fragment_shader)
    glLinkProgram(program)

    # 에러 체크
    if glGetProgramiv(program, GL_LINK_STATUS) != GL_TRUE:
        raise RuntimeError(glGetProgramInfoLog(program))

    # 셰이더 객체는 링크 후 삭제 가능
    glDeleteShader(vertex_shader)
    glDeleteShader(fragment_shader)

    return program

# ===== 초기화 =====
def init():
    global shaderProgram, VAO

    # 셰이더 프로그램 생성
    shaderProgram = create_shader_program()

    # 정점 데이터 (x, y, z, r, g, b)
    vertices = np.array([
        # 좌표(x,y,z)         # 색상(r,g,b)
        -0.5, -0.5, 0.0,      1.0, 0.0, 0.0,   # 왼쪽 아래 (빨강)
         0.5, -0.5, 0.0,      0.0, 1.0, 0.0,   # 오른쪽 아래 (초록)
         0.0,  0.5, 0.0,      0.0, 0.0, 1.0    # 위쪽 (파랑)
    ], dtype=np.float32)

    # VAO (Vertex Array Object)
    VAO = glGenVertexArrays(1)
    glBindVertexArray(VAO)

    # VBO (Vertex Buffer Object)
    VBO = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

    # 정점 좌표 속성 (location = 0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 6 * vertices.itemsize, ctypes.c_void_p(0))
    glEnableVertexAttribArray(0)

    # 색상 속성 (location = 1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 6 * vertices.itemsize, ctypes.c_void_p(12))
    glEnableVertexAttribArray(1)

    # 정리
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)

# ===== 디스플레이 =====
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glUseProgram(shaderProgram)
    glBindVertexArray(VAO)
    glDrawArrays(GL_TRIANGLES, 0, 3)  # 삼각형 3개 정점
    glBindVertexArray(0)

    glutSwapBuffers()

# ===== 메인 =====
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"PyOpenGL Modern Shader Example")

    init()

    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
