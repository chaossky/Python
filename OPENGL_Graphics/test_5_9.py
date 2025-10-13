from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.texture import Texture
from core.mesh import Mesh
from geometry.boxGeometry import BoxGeometry
from geometry.rectangleGeometry import RectangleGeometry
from material.textureMaterial import TextureMaterial
from extras.movementRig import MovementRig
from extras.gridHelper import GridHelper

# render a basic scene
class Test(Base):
    
    def initialize(self):
        print("Initializing program...")
        
        self.renderer=Renderer()
        self.scene=Scene()
        self.camera=Camera(aspectRatio=800/600)
        # 카메라의 포지션은 나오는 이미지에 따라서 조절해야 할 것이다.
        self.rig=MovementRig()
        self.rig.add(self.camera)
        self.rig.setPosition([0,0.5,3])
        self.scene.add(self.rig)        
        self.camera.setPosition([0,0,2.00])
        
        crateGeometry=BoxGeometry()
        crateMaterial=TextureMaterial(Texture("images/crate.jpg"))
        crate=Mesh(crateGeometry,crateMaterial)
        self.scene.add(crate)
        
        grid=GridHelper(gridColor=[1,1,1],centerColor=[1,1,0])
        grid.rotateX(-3.14/2)
        self.scene.add(grid)
        
        self.hudScene=Scene()
        self.hudCamera=Camera()
        self.hudCamera.setOrthographic(0,800,0,600,-1,1)
        labelGeo1=RectangleGeometry(width=600,height=80,position=[0,600],alignment=[0,1])
        labelMat1=TextureMaterial(Texture("images/crate-sim.png"))
        label1=Mesh(labelGeo1,labelMat1)
        self.hudScene.add(label1)
        labelGeo2=RectangleGeometry(width=400,height=80,position=[800,0],alignment=[1,0])
        labelMat2=TextureMaterial(Texture("images/version-1.png"))
        label2=Mesh(labelGeo2,labelMat2)
        self.hudScene.add(label2)
        
    def update(self):
        # self.mesh.rotateY(0.00514)
        # self.mesh.rotateX(0.0337)
        # self.mesh.rotateZ(0.006)
        self.renderer.render(self.scene,self.camera)
        self.rig.update(self.input,self.deltaTime)
        self.renderer.render(self.hudScene,self.hudCamera,clearColor=False)
        
# instantiate this class and run the program
if __name__ == "__main__":
    Test(screenSize=[800,600]).run()