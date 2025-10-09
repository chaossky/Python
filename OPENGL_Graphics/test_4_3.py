from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.mesh import Mesh
# from geometry.boxGeometry import BoxGeometry
from material.surfaceMaterial import SurfaceMaterial
from geometry.geometry import Geometry
from math import sin
from numpy import arange
from material.pointMaterial import PointMaterial
from material.lineMaterial import LineMaterial

# render a basic scene
class Test(Base):
    
    def initialize(self):
        print("Initializing program...")
        
        self.renderer=Renderer()
        self.scene=Scene()
        self.camera=Camera(aspectRatio=800/600)
        # 카메라의 포지션은 나오는 이미지에 따라서 조절해야 할 것이다.
        self.camera.setPosition([0,0,5.00])
        
        geometry=Geometry()
        posData=[]
        for x in arange(-3.2,3.2,0.2):
            posData.append([x,sin(x),0.0])
        geometry.addAttribute("vec3","vertexPosition",posData)
        geometry.countVertices()
        
        pointMaterial=PointMaterial({
            "baseColor":[1,1,0],"pointSize":10
        })
        pointMesh=Mesh(geometry,pointMaterial)
        self.scene.add(pointMesh)
        
        lineMaterial=LineMaterial({
            "baseColor":[1,0,1],"lineWidth":4
        })
        lineMesh=Mesh(geometry,lineMaterial)
        
        self.scene.add(pointMesh)
        self.scene.add(lineMesh)
        
        material=SurfaceMaterial({"useVertexColors":True})
               
        self.mesh=Mesh(geometry,material)
        self.scene.add(self.mesh)
        
    def update(self):
        # self.mesh.rotateY(0.00514)
        # self.mesh.rotateX(0.0337)
        # self.mesh.rotateZ(0.006)
        self.renderer.render(self.scene,self.camera)
        
# instantiate this class and run the program
if __name__ == "__main__":
    Test(screenSize=[800,600]).run()