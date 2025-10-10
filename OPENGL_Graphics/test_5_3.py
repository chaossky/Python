from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.texture import Texture
from core.mesh import Mesh
from geometry.rectangleGeometry import RectangleGeometry
from material.surfaceMaterial import SurfaceMaterial
from geometry.sphereGeometry import SphereGeometry
from material.textureMaterial import TextureMaterial
from material.material import Material


# render a basic scene
class Test(Base):
    
    def initialize(self):
        print("Initializing program...")
        
        self.renderer=Renderer()
        self.scene=Scene()
        self.camera=Camera(aspectRatio=800/600)
        # 카메라의 포지션은 나오는 이미지에 따라서 조절해야 할 것이다.
        self.camera.setPosition([0,0,1.5])
        
        vertexShaderCode="""
        uniform mat4 projectionMatrix;
        uniform mat4 viewMatrix;
        uniform mat4 modelMatrix;
        in vec3 vertexPosition;
        in vec2 vertexUV;
        out vec2 UV;
        
        void main()
        {
            gl_Position=projectionMatrix*viewMatrix*modelMatrix*vec4(vertexPosition,1.0);
            UV=vertexUV;
        }
        """
        
        fragmentShaderCode="""
        uniform sampler2D texture;
        in vec2 UV;
        uniform float time;
        out vec4 fragColor;
        
        void main()
        {
            vec2 shiftUV=UV+vec2(0,0.45*sin(5.0*UV.x + time));
            fragColor=texture2D(texture,shiftUV);
        }
        """
        gridTex=Texture("images/grid.png")
        self.waveMaterial=Material(vertexShaderCode,fragmentShaderCode)
        self.waveMaterial.addUniform("sampler2D","texture",[gridTex.textureRef,1])
        self.waveMaterial.addUniform("float","time",0.0)
        self.waveMaterial.locateUniforms()   
        
        #geometry=SphereGeometry(radius=0.5)
        geometry=RectangleGeometry(width=2,height=1.5)
        self.mesh=Mesh(geometry,self.waveMaterial)
        self.scene.add(self.mesh)
        
    def update(self):
        # self.mesh.rotateY(0.00514)
        # self.mesh.rotateX(0.0337)
        # self.mesh.rotateZ(0.006)
        self.renderer.render(self.scene,self.camera)
        self.waveMaterial.uniforms["time"].data+=self.deltaTime
        
# instantiate this class and run the program
if __name__ == "__main__":
    Test(screenSize=[800,600]).run()