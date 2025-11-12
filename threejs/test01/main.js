// thee.js 라이브러리를 불러옵니다.
import * as THREE from 'three';
// 추가 기능 중 마우스로 회전/줌으로 제어가 가능한 모듈을 불러옵니다. 
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

//3D 장면을 생성합니다.
const scene = new THREE.Scene();

//원근 카메라를 생성합니다.
// 시야각은 75도, 화면 비율, 가까운 클리핑과 먼 클리핑을 정합니다.
const camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );

// WebGL 랜더러를 생성합니다.(그림을 그려주는 역할)
const renderer = new THREE.WebGLRenderer();

// 랜더의 크기를 정합니다.
renderer.setSize( window.innerWidth, window.innerHeight );

//렌더러가 그린 캔버스를 HTML문서 body에 추가합니다.
document.body.appendChild( renderer.domElement );

// 가로, 세로, 깊이가 각각 1인 정육면체 BOX 지오메트리를 생성합니다.
const geometry = new THREE.BoxGeometry( 1, 1, 1 );

// 초록색을 기본 재질(material)로 생성합니다.
const material = new THREE.MeshBasicMaterial( { color: 0x00ff00 } );
// 지오메트리와 머티리얼을 합쳐서 3D Mesh 객체 생성
const cube = new THREE.Mesh( geometry, material );
//생성한 큐브를 장면에 추가합니다.
scene.add( cube );

// 카메라를 Z축 방향을 4만큼 이동
camera.position.z = 4;


//애니메이션 루프 함수를 정의 합니다.
function animate() {
    //현재 장면을 카메라 시점으로 렌더링합니다.
  renderer.render( scene, camera );

  //x 축과 y축 방향으로 회전합니다.
  cube.rotation.x += 0.01;
  cube.rotation.y += 0.01;
}

// 애니메이션 루프를 실행합니다. 
// 브라우저의 프레임 마다 animate 함수를 호출합니다.
renderer.setAnimationLoop( animate );