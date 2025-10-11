from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.texture import Texture
from core.mesh import Mesh
from core.matrix import Matrix
from extras.textTexture import TextTexture
from extras.movementRig import MovementRig
from geometry.rectangleGeometry import RectangleGeometry
from geometry.boxGeometry import BoxGeometry
from material.textureMaterial import TextureMaterial

# render a basic scene
class Test(Base):
    
    def initialize(self):
        print("Initializing program...")
        
        self.renderer=Renderer()
        self.scene=Scene()
        self.camera=Camera(aspectRatio=800/600)
        # 카메라의 포지션은 나오는 이미지에 따라서 조절해야 할 것이다.
        self.camera.setPosition([0,0,2.00])
        
        self.rig=MovementRig()
        self.rig.add(self.camera)
        self.rig.setPosition([0,1,5])
        self.scene.add(self.rig)
        
        labelTexture=TextTexture(text="This is a Crate. ",
                          systemFontName="Arial Bold",
                          fontSize=40,
                          fontColor=[0,0,200],
                          imageWidth=256,
                          imageHeight=128,
                          alignHorizontal=0.5,
                          alignVertical=0.5,    
                          imageBorderWidth=4,
                          imageBorderColor=[255,0,0])
        
        labelMaterial=TextureMaterial(labelTexture)
        labelGeometry=RectangleGeometry(width=1,height=0.5)
        labelGeometry.applyMatrix(Matrix.makeRotationY(3.14))
        
        self.label=Mesh(labelGeometry,labelMaterial)
        self.label.setPosition([0,1,0])
        self.scene.add(self.label)
        
        crateGeometry=BoxGeometry()
        crateTexture=Texture("images/crate.jpg")
        crateMaterial=TextureMaterial(crateTexture)
        crate=Mesh(crateGeometry,crateMaterial)
        self.scene.add(crate)
        
    def update(self):
        # self.mesh.rotateY(0.00514)
        # self.mesh.rotateX(0.0337)
        # self.mesh.rotateZ(0.006)
        self.renderer.render(self.scene,self.camera)
        self.rig.update(self.input,self.deltaTime)
        self.label.lookAt(self.rig.getWorldPosition())
        
# instantiate this class and run the program
if __name__ == "__main__":
    Test(screenSize=[800,600]).run()