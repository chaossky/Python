import glfw
from OpenGL.GL import *
import numpy as np
import ctypes
# The line import ctypes brings in Python’s C Foreign Function Interface (FFI)
# module, which allows Python code to interact with C-compatible data types 
# and memory structures. In OpenGL programming—especially 
# with PyOpenGL—this is super useful 
# because OpenGL expects pointers and raw memory buffers, 
# just like C does.
from pyrr import Matrix44
# imports the Matrix44 class from the Pyrr library, 
# which is a Pythonic wrapper around the powerful glm 
# (OpenGL Mathematics) library. 
# It’s designed to make working with 3D math—like transformations 
# and projections—much easier and more intuitive in Python.
from OpenGL.GL.shaders import compileProgram, compileShader


# Vertex Shader
VERTEX_SHADER = """
#version 330 core
layout(location = 0) in vec3 position;
layout(location = 1) in vec3 color;
out vec3 vertexColor;
uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;
void main() {
    vertexColor = color;
    gl_Position = projection * view * model * vec4(position, 1.0);
}
"""

# Fragment Shader
FRAGMENT_SHADER = """
#version 330 core
in vec3 vertexColor;
out vec4 FragColor;
void main() {
    FragColor = vec4(vertexColor, 1.0);
}
"""

# Vertex data: position (x, y, z) + color (r, g, b)
vertices = np.array([
    # Front face           (red)
    -0.5, -0.5,  0.5,  1.0, 0.0, 0.0,
     0.5, -0.5,  0.5,  1.0, 0.0, 0.0,
     0.5,  0.5,  0.5,  1.0, 0.0, 0.0,
    -0.5,  0.5,  0.5,  1.0, 0.0, 0.0,

    # Back face            (green)
    -0.5, -0.5, -0.5,  0.0, 1.0, 0.0,
     0.5, -0.5, -0.5,  0.0, 1.0, 0.0,
     0.5,  0.5, -0.5,  0.0, 1.0, 0.0,
    -0.5,  0.5, -0.5,  0.0, 1.0, 0.0,

    # Left face            (blue)
    -0.5, -0.5, -0.5,  0.0, 0.0, 1.0,
    -0.5, -0.5,  0.5,  0.0, 0.0, 1.0,
    -0.5,  0.5,  0.5,  0.0, 0.0, 1.0,
    -0.5,  0.5, -0.5,  0.0, 0.0, 1.0,

    # Right face          (yellow)
     0.5, -0.5, -0.5,  1.0, 1.0, 0.0,
     0.5, -0.5,  0.5,  1.0, 1.0, 0.0,
     0.5,  0.5,  0.5,  1.0, 1.0, 0.0,
     0.5,  0.5, -0.5,  1.0, 1.0, 0.0,

    # Top face             (cyan)
    -0.5,  0.5,  0.5,  0.0, 1.0, 1.0,
     0.5,  0.5,  0.5,  0.0, 1.0, 1.0,
     0.5,  0.5, -0.5,  0.0, 1.0, 1.0,
    -0.5,  0.5, -0.5,  0.0, 1.0, 1.0,

    # Bottom face        (magenta)
    -0.5, -0.5,  0.5,  1.0, 0.0, 1.0,
     0.5, -0.5,  0.5,  1.0, 0.0, 1.0,
     0.5, -0.5, -0.5,  1.0, 0.0, 1.0,
    -0.5, -0.5, -0.5,  1.0, 0.0, 1.0,
], dtype=np.float32)

# Indices (each face has 2 triangles)
indices = np.array([
    0, 1, 2, 2, 3, 0,       # Front
    4, 5, 6, 6, 7, 4,       # Back
    8, 9,10,10,11, 8,       # Left
   12,13,14,14,15,12,       # Right
   16,17,18,18,19,16,       # Top
   20,21,22,22,23,20        # Bottom
], dtype=np.uint32)

# 회전 각도 변수
rotation_angle_y = 0.0
rotation_angle_x = 0.0
rotation_angle_z = 0.0

# 키 입력 콜백 함수
def key_callback(window, key, scancode, action, mods):
    global rotation_angle_y
    global rotation_angle_x
    global rotation_angle_z
    
    if action == glfw.PRESS or action == glfw.REPEAT:
        if key == glfw.KEY_LEFT:
            rotation_angle_y -= 0.05
        elif key == glfw.KEY_RIGHT:
            rotation_angle_y += 0.05
        elif key == glfw.KEY_UP:
            rotation_angle_x += 0.05
        elif key == glfw.KEY_DOWN:
            rotation_angle_x -= 0.05
        elif key == glfw.KEY_A:
            rotation_angle_z += 0.05    
        elif key == glfw.KEY_Z:
            rotation_angle_z -= 0.05

# 셰이더 프로그램 생성 함수

def create_shader_program():
    return compileProgram(
        compileShader(VERTEX_SHADER, GL_VERTEX_SHADER),
        compileShader(FRAGMENT_SHADER, GL_FRAGMENT_SHADER)
    )

def main():
    if not glfw.init():
        return

    window = glfw.create_window(800, 600, "Colorful Cube", None, None)
    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)  # 키 콜백 등록
    glClearColor(0.1, 0.1, 0.1, 1.0)

    shader = create_shader_program()
    glUseProgram(shader)

    VAO = glGenVertexArrays(1)
    glBindVertexArray(VAO)

    VBO = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

    EBO = glGenBuffers(1)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)

    # Position attribute
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 6 * 4, ctypes.c_void_p(0))
    glEnableVertexAttribArray(0)

    # Color attribute
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 6 * 4, ctypes.c_void_p(3 * 4))
    glEnableVertexAttribArray(1)

    glEnable(GL_DEPTH_TEST)

    model_loc = glGetUniformLocation(shader, "model")
    view_loc = glGetUniformLocation(shader, "view")
    proj_loc = glGetUniformLocation(shader, "projection")

    projection = Matrix44.perspective_projection(45.0, 800/600, 0.1, 100.0)
    glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection.astype('float32'))

    while not glfw.window_should_close(window):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        view = Matrix44.look_at(
            eye=[0.0, 0.0, 3.0],
            target=[0.0, 0.0, 0.0],
            up=[0.0, 1.0, 0.0]
        )
        glUniformMatrix4fv(view_loc, 1, GL_FALSE, view.astype('float32'))

        # angle = glfw.get_time()
        
        # rotation_x = Matrix44.from_x_rotation(angle)
        # rotation_y = Matrix44.from_y_rotation(angle)
        # rotation_z = Matrix44.from_z_rotation(angle)
        # rotation = rotation_x * rotation_y * rotation_z
        
        rotation_y = Matrix44.from_y_rotation(rotation_angle_y)
        rotation_x = Matrix44.from_x_rotation(rotation_angle_x)
        rotation_z = Matrix44.from_z_rotation(rotation_angle_z)
        rotation = rotation_y * rotation_x * rotation_z
        
        glUniformMatrix4fv(model_loc, 1, GL_FALSE, rotation.astype('float32'))

        glBindVertexArray(VAO)
        glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, None)

        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    main()
