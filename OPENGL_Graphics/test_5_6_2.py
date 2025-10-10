from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.mesh import Mesh
from geometry.rectangleGeometry import RectangleGeometry
from shader.shader_load import ShaderLoad
from material.material import Material

# render a basic scene
class Test(Base):
    
    def initialize(self):
        print("Initializing program...")
        
        self.renderer=Renderer()
        self.scene=Scene()
        self.camera=Camera(aspectRatio=800/600)
        # 카메라의 포지션은 나오는 이미지에 따라서 조절해야 할 것이다.
        self.camera.setPosition([0,0,1])
        
        # 직접 vertexShader 와 fragmentShader 코드를 입력하는 대신
        # 외부 파일로 처리하고, 이를 로딩하는 방식으로 바꿨다.
        
        vertexShaderCode=ShaderLoad.load_shader_code("shader/vs_basic.glsl")
        fragmentShaderCode=ShaderLoad.load_shader_code("shader/fs_marble.glsl")
            
        material=Material(vertexShaderCode,fragmentShaderCode)
        material.locateUniforms()
        
        geometry=RectangleGeometry()
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