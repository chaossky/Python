// three.js 라이브러리 전체를 THREE라는 이름으로 불러오기
import * as THREE from 'three';

// three.js의 추가 기능 중 OrbitControls 모듈 불러오기 (마우스로 회전/줌 제어 가능)
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

// 새로운 3D 장면(Scene) 생성
const scene = new THREE.Scene();

// 원근 카메라 생성 (시야각 75도, 화면 비율, 가까운 클리핑 0.1, 먼 클리핑 1000)
const camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );

// WebGL 렌더러 생성 (브라우저에서 3D 그래픽을 그려주는 역할)
const renderer = new THREE.WebGLRenderer();

// 렌더러 크기를 브라우저 창 크기에 맞게 설정
renderer.setSize( window.innerWidth, window.innerHeight );

// 렌더러가 그린 캔버스를 HTML 문서의 body에 추가
document.body.appendChild( renderer.domElement );

// 가로, 세로, 깊이가 각각 1인 정육면체(Box) 지오메트리 생성
const geometry = new THREE.BoxGeometry( 1, 1, 1 );

// 초록색(0x00ff00) 기본 재질(Material) 생성
const material = new THREE.MeshBasicMaterial( { color: 0x00ff00 } );

// 지오메트리와 재질을 합쳐서 실제 3D 객체(Mesh) 생성
const cube = new THREE.Mesh( geometry, material );

// 생성한 큐브를 장면(Scene)에 추가
scene.add( cube );

// 카메라를 z축 방향으로 4만큼 뒤로 이동 (객체를 바라볼 수 있도록 위치 조정)
camera.position.z = 4;

// 애니메이션 루프 함수 정의
function animate() {
  // 현재 장면(scene)을 카메라 시점(camera)으로 렌더링
  renderer.render( scene, camera );
  // 큐브를 x축 방향으로 조금씩 회전
  cube.rotation.x += 0.01;
  // 큐브를 y축 방향으로 조금씩 회전
  cube.rotation.y += 0.01;
}

// 애니메이션 루프 실행 (브라우저의 프레임마다 animate 함수 호출)
renderer.setAnimationLoop( animate );
