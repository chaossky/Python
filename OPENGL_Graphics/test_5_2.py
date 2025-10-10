from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.texture import Texture
from core.mesh import Mesh
from geometry.rectangleGeometry import RectangleGeometry
from geometry.sphereGeometry import SphereGeometry
from material.textureMaterial import TextureMaterial
from extras.movementRig import MovementRig

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
        self.scene.add(self.rig)
        self.rig.setPosition([0,1,4])
       
        skyGeometry=SphereGeometry(radius=50)
        skyMaterial=TextureMaterial(Texture("images/sky-earth.jpg"))
        sky=Mesh(skyGeometry,skyMaterial)
        self.scene.add(sky)
        
        grassGeometry=RectangleGeometry(width=100,height=100)
        grassMaterial=TextureMaterial(Texture("images/grass.jpg"),
                                      {"repeatUV":[50,50]})
        grass=Mesh(grassGeometry,grassMaterial)
        grass.rotateX(-3.14/2)
        self.scene.add(grass)
                
    def update(self):
        # self.mesh.rotateY(0.00514)
        # self.mesh.rotateX(0.0337)
        # self.mesh.rotateZ(0.006)
        self.renderer.render(self.scene,self.camera)
        self.rig.update(self.input,self.deltaTime)
        
# instantiate this class and run the program
if __name__ == "__main__":
    Test(screenSize=[800,600]).run()