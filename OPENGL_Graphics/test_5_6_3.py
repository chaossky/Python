from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.mesh import Mesh
from geometry.rectangleGeometry import RectangleGeometry
from geometry.boxGeometry import BoxGeometry
from extras.textTexture import TextTexture
from material.textureMaterial import TextureMaterial

# render a basic scene
class Test(Base):
    
    def initialize(self):
        print("Initializing program...")
        
        self.renderer=Renderer()
        self.scene=Scene()
        self.camera=Camera(aspectRatio=800/600)
        # 카메라의 포지션은 나오는 이미지에 따라서 조절해야 할 것이다.
        self.camera.setPosition([0,0,2.5])
        
        # geometry=RectangleGeometry()
        geometry=BoxGeometry(width=1,height=1,depth=1)
        message=TextTexture(text="Python Graphics",
                            systemFontName="Impact",
                            fontSize=32,
                            fontColor=[0,0,200],
                            imageWidth=256,
                            imageHeight=256,
                            alignHorizontal=0.5,
                            alignVertical=0.5,
                            imageBorderWidth=4,
                            imageBorderColor=[255,0,0])
        material=TextureMaterial(message)
        self.mesh=Mesh(geometry,material)
        self.scene.add(self.mesh)
        
    def update(self):
        self.mesh.rotateY(0.00514)
        self.mesh.rotateX(0.00337)
        self.mesh.rotateZ(0.006)

        self.renderer.render(self.scene,self.camera)
        
# instantiate this class and run the program
if __name__ == "__main__":
    Test(screenSize=[800,600]).run()