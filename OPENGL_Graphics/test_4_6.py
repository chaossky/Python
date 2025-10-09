from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from extras.axesHelper import AxesHelper
from extras.gridHelper import GridHelper
from math import pi
from extras.movementRig import MovementRig
from core.mesh import Mesh
from geometry.boxGeometry import BoxGeometry
from material.surfaceMaterial import SurfaceMaterial


# render a basic scene
class Test(Base):
    
    def initialize(self):
        print("Initializing program...")
        
        self.renderer=Renderer()
        self.scene=Scene()
        self.camera=Camera(aspectRatio=800/600)
        # 카메라의 포지션은 나오는 이미지에 따라서 조절해야 할 것이다.
        self.camera.setPosition([0.5,1,5])
        
        axes=AxesHelper(axisLength=2)
        self.scene.add(axes)
        
        grid=GridHelper(size=20,gridColor=[1,1,1]
                        ,centerColor=[1,1,0])
        grid.rotateX(-pi/2)
        self.scene.add(grid)
        
        self.rig=MovementRig()
        self.rig.add(self.camera)
        self.rig.setPosition([0.5,1,0.5])
        self.scene.add(self.rig)
        
        geometry=BoxGeometry()
        material=SurfaceMaterial({"useVertexColors":True})
        # # material=SurfaceMaterial({
        # #     "useVertexColors":True,
        # #     "wireframe":True,
        # #     "lineWidth":8
        # # })
        self.mesh=Mesh(geometry,material)
        self.scene.add(self.mesh)
        
    def update(self):
        # self.mesh.rotateY(0.00514)
        # self.mesh.rotateX(0.0337)
        # self.mesh.rotateZ(0.006)
        self.rig.update(self.input,self.deltaTime)
        self.renderer.render(self.scene,self.camera)
        
# instantiate this class and run the program
if __name__ == "__main__":
    Test(screenSize=[800,600]).run()