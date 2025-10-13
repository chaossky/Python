from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.texture import Texture
from core.mesh import Mesh
from geometry.rectangleGeometry import RectangleGeometry
from material.spriteMaterial import SpriteMaterial
from extras.movementRig import MovementRig
from extras.gridHelper import GridHelper
from math import floor

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
        self.rig.setPosition([0,0.5,3])
        self.scene.add(self.rig)
        
        geometry=RectangleGeometry()
        tileSet=Texture("images/rolling-ball.png")
        
        spriteMaterial=SpriteMaterial(tileSet,{
            "billboard":1,
            "tileCount":[4,4],
            "tileNumber":0
        })
        self.tilesPerSecond=8
        
        self.sprite=Mesh(geometry,spriteMaterial)
        self.scene.add(self.sprite)
        
        grid=GridHelper()
        grid.rotateX(-3.14/2)
        self.scene.add(grid)        
        
    def update(self):
        # self.mesh.rotateY(0.00514)
        # self.mesh.rotateX(0.0337)
        # self.mesh.rotateZ(0.006)
        self.renderer.render(self.scene,self.camera)
        tileNumber=floor(self.time*self.tilesPerSecond)
        self.sprite.material.uniforms["tileNumber"].data=tileNumber
        self.rig.update(self.input,self.deltaTime)
        
# instantiate this class and run the program
if __name__ == "__main__":
    Test(screenSize=[800,600]).run()