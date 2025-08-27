# pygame library for window management and event handling, 
# and the PyOpenGL library for 3D graphics rendering. 
# Its primary purpose is to display a rotating 3D cube 
# with distinct colored faces and white edges.

import pygame
#Used for creating the window, handling events 
# (like closing the window), and managing the display.
from pygame.locals import *

# Provide the necessary functions for OpenGL rendering, 
# such as drawing primitives, setting up the camera, 
# and transformations.
from OpenGL.GL import *
from OpenGL.GLU import *

# A tuple of 8 tuples, where each inner tuple represents the 
# (x, y, z) coordinates of a corner of the cube. 
# These are the building blocks of the cube.
# 큐브의 각각의 모서리 꼭지점
vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

# A tuple of 12 tuples, where each inner tuple contains two 
# indices from the vertices tuple. 
# These define the lines that form the wireframe 
# (skeleton) of the cube.
#큐뷰의 모서리
edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)
#큐브의 면
surfaces = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6)
)
#큐브의 색
colors = (
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 1, 0),
    (1, 0, 1),
    (0, 1, 1)
)


def Cube():
    glBegin(GL_QUADS)
    for i, surface in enumerate(surfaces):#열거형 자료는 어떻게 만들까?
        glColor3fv(colors[i])
        for vertex in surface:
            glVertex3fv(vertices[vertex])
    glEnd()

    glColor3fv((1, 1, 1))  # 흰색 선
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    
    # Set up the perspective projection 
    # (Field of View, Aspect Ratio, Near/Far Clipping Planes)
    # fovy=40, aspect=900/700, zNear=0.1, zFar=50.0
    gluPerspective(99, (display[0] / display[1]), 0.9, 70.0) 
    glTranslatef(0.0, 0.0, -5)

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        glRotatef(0.5, 0.1, 0.1, 0)  # 매 프레임 회전
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        clock.tick(45)

    pygame.quit()


if __name__ == "__main__":
    main()


    """
uses the pygame library for window management and event handling, and the PyOpenGL library for 3D graphics rendering. Its primary purpose is to display a rotating 3D cube with distinct colored faces and white edges.

Here's a breakdown of the code:

Imports:

pygame and pygame.locals: Used for creating the window, handling events (like closing the window), and managing the display.
OpenGL.GL and OpenGL.GLU: Provide the necessary functions for OpenGL rendering, such as drawing primitives, setting up the camera, and transformations.
Cube Definition Data:

vertices: 
A tuple of 8 tuples, where each inner tuple represents the (x, y, z) coordinates of a corner of the cube. These are the building blocks of the cube.

edges: 
A tuple of 12 tuples, where each inner tuple contains two indices from the vertices tuple. These define the lines that form the wireframe (skeleton) of the cube.

surfaces: 
A tuple of 6 tuples, where each inner tuple contains four indices from the vertices tuple. These define the six quadrilateral faces of the cube. The order of vertices in each surface is important for determining the face's normal direction (which affects lighting and culling).

colors: 
A tuple of 6 RGB color tuples. Each color corresponds to one of the surfaces, allowing each face of the cube to have a unique color.
Cube() Function:

This function is responsible for drawing the 3D cube using OpenGL commands.
Drawing Faces:
glBegin(GL_QUADS): Initiates the drawing of quadrilaterals.
It iterates through each surface in the surfaces tuple.

glColor3fv(colors[i]): Sets the current drawing color to the corresponding color from the colors tuple for the current face.
For each vertex index within the current surface, glVertex3fv(vertices[vertex]) is called. This tells OpenGL to draw a vertex at the specified 3D coordinates.
glEnd(): Ends the quadrilateral drawing mode.

Drawing Edges:
glColor3fv((1, 1, 1)): Sets the drawing color to white for the edges.

glBegin(GL_LINES): Initiates the drawing of lines.
It iterates through each edge in the edges tuple.
For each vertex index within the current edge, glVertex3fv(vertices[vertex]) is called, drawing a line segment between the two vertices of the edge.
glEnd(): Ends the line drawing mode.

main() Function:

Initialization:
pygame.init(): Initializes all the Pygame modules.
display = (800, 600): Defines the width and height of the display window.
pygame.display.set_mode(display, DOUBLEBUF | OPENGL): Creates the display surface. DOUBLEBUF enables double buffering for smooth animation, and OPENGL tells Pygame to create an OpenGL context.
OpenGL Setup:
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0): Sets up the perspective projection matrix.
45: Field of view angle in degrees.
(display[0] / display[1]): Aspect ratio of the window.
0.1: Near clipping plane (objects closer than this won't be rendered).
50.0: Far clipping plane (objects farther than this won't be rendered).
glTranslatef(0.0, 0.0, -5): Translates the camera (or the entire scene) 5 units back along the Z-axis. This moves the cube into view, as it's initially centered at the origin.
Main Loop:
clock = pygame.time.Clock(): Creates a Clock object to control the frame rate.
running = True: A flag to keep the main loop running.
The while running: loop continues until the user quits.
Event Handling: for event in pygame.event.get(): checks for user input. If event.type == QUIT, the running flag is set to False, exiting the loop.
Rotation: glRotatef(1, 3, 1, 1): Applies a rotation transformation. It rotates the scene by 1 degree around the vector (3, 1, 1) in each frame, creating the continuous rotation effect.
Clearing Buffers: glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT): Clears the color buffer (which holds the pixel data for the screen) and the depth buffer (which stores depth information for correct 3D rendering, ensuring closer objects obscure farther ones).
Drawing: Cube(): Calls the function to draw the cube.
Display Update: pygame.display.flip(): Swaps the front and back buffers, displaying the newly rendered frame on the screen.
Frame Rate Control: clock.tick(60): Limits the loop to a maximum of 60 frames per second.
Cleanup:
pygame.quit(): Uninitializes Pygame modules before the script exits.
if __name__ == "__main__": Block:

This is a standard Python construct that ensures the main() function is called only when the script is executed directly (not when imported as a module).
In summary, the script sets up a basic 3D environment, defines a cube's geometry and colors, and then enters a loop to continuously rotate and render this cube, providing a simple interactive 3D visualization.
    """