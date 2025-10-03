from OpenGL.GL import *
import numpy

class Attribute(object):

    def __init__(self, dataType, data):
        
        # type of data: "int" | "float" | "vec2" | "vec3" | "vec4"
        self.dataType = dataType
        
        # array of data
        self.data=data
        
        # reference of available buffer in GPU
        self.bufferRef = glGenBuffers(1)
        
        # upload data immediately
        self.uploadData()
        
    # upload data to GPU
    def uploadData(self):
        
        # convert data to numpy array format
        # convert numbers to 32 bit floats
        data=numpy.array(self.data).astype(numpy.float32)
        
        # select buffer used by the following functions
        glBindBuffer(GL_ARRAY_BUFFER, self.bufferRef)
        
        # upload data
        glBufferData(GL_ARRAY_BUFFER, data.ravel(), GL_STATIC_DRAW)
        
    # associate variable in program with this buffer
    def associateVariable(self, programRef, variableName):
        
        # get reference for a variable in program
        variableRef = glGetAttribLocation(programRef, variableName)
        
        # if the variable does not exist, then exit
        if variableRef == -1:
            return
        
        # select buffer used for upload
        glBindBuffer(GL_ARRAY_BUFFER, self.bufferRef)
        
        # types of data
        if self.dataType == "int":
            glVertexAttribPointer(variableRef, 1, GL_INT, GL_FALSE, 0, None)
        elif self.dataType == "float":
            glVertexAttribPointer(variableRef, 1, GL_FLOAT, GL_FALSE, 0, None)
        elif self.dataType == "vec2":
            glVertexAttribPointer(variableRef, 2, GL_FLOAT, GL_FALSE, 0, None)
        elif self.dataType == "vec3":
            glVertexAttribPointer(variableRef, 3, GL_FLOAT, GL_FALSE, 0, None)
        elif self.dataType == "vec4":
            glVertexAttribPointer(variableRef, 4, GL_FLOAT, GL_FALSE, 0, None)
        else:
            raise Exception("Attribute " + variableName + " has unknown type " + self.dataType)
        
        # indicate that data will be streamed to this variable
        glEnableVertexAttribArray(variableRef)