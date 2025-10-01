import pygame

class Input(object):

    def __init__(self):
        # has the user tried to quit the program?
        self.quit = False
        # keyboard input
        # self.keyDown = {}
        # self.keyPressed = {}
        # self.keyUp = {}
        # # mouse input
        # self.mouseButtonDown = {}
        # self.mouseButtonPressed = {}
        # self.mouseButtonUp = {}
        # self.mousePosition = [0, 0]
        # self.mouseMovement = [0, 0]

    def update(self):
        # iterate over all user input events(such as keyboard or mouse)
        # that occured since the last time events were checked
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
                
        # quit event occurs by clicking button to close window
        
        # reset some of the input properties
        # as they are only True for a single frame
    #     self.keyDown = {}
    #     self.keyUp = {}
    #     self.mouseButtonDown = {}
    #     self.mouseButtonUp = {}
    #     self.mouseMovement = [0, 0]
    
    #      # keyboard input
    #         elif event.type == pygame.KEYDOWN:
    #             self.keyDown[event.key] = True
    #             self.keyPressed[event.key] = True
    #         elif event.type == pygame.KEYUP:
    #             self.keyUp[event.key] = True
    #             self.keyPressed[event.key] = False

    #         # mouse input
    #         elif event.type == pygame.MOUSEBUTTONDOWN:
    #             self.mouseButtonDown[event.button] = True
    #             self.mouseButtonPressed[event.button] = True
    #         elif event.type == pygame.MOUSEBUTTONUP:
    #             self.mouseButtonUp[event.button] = True
    #             self.mouseButtonPressed[event.button] = False
    #         elif event.type == pygame.MOUSEMOTION:
    #             self.mousePosition = list(event.pos)
    #             self.mouseMovement = list(event.rel)

    # # keyboard input functions
    # def isKeyDown(self, keyCode):
    #     return keyCode in self.keyDown

    # def isKeyPressed(self, keyCode):
    #     return keyCode in self.keyPressed

    # def isKeyUp(self, keyCode):
    #     return keyCode in self.keyUp

    # # mouse input functions
    # def isMouseButtonDown(self, buttonNumber):
    #     return buttonNumber in self.mouseButtonDown