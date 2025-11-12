// three.js 라이브러리를 불러옵니다.
import * as THREE from 'three';
// 마우스로 회전/줌 제어가 가능한 OrbitControls 모듈을 불러옵니다.
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

// 3D 장면(Scene)을 생성합니다.
const scene = new THREE.Scene();

// 원근 카메라 생성 (시야각 75도, 화면 비율, near=0.1, far=1000)
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);

// WebGL 렌더러 생성
const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// 큐브 지오메트리 생성 (가로 6, 세로 4, 깊이 6)
const cubeGeometry = new THREE.BoxGeometry(6, 4, 6);

// 빨간색 Lambert 재질 생성 (빛의 영향을 받음)
const cubeMaterial = new THREE.MeshLambertMaterial({ color: "red" });

// 지오메트리와 재질을 합쳐서 Mesh 객체 생성
const cube = new THREE.Mesh(cubeGeometry, cubeMaterial);
scene.add(cube);

// 광원 추가 (DirectionalLight: 태양빛처럼 한 방향에서 오는 빛)
const light = new THREE.DirectionalLight(0xffffff, 1);
light.position.set(0.5, 1, 1).normalize();
scene.add(light);

// 카메라 위치를 z축 방향으로 4만큼 이동
camera.position.z = 10;

// 애니메이션 루프 정의
function animate() {
  renderer.render(scene, camera);

  // 큐브를 x축, y축 방향으로 회전
  cube.rotation.x += 0.02;
  cube.rotation.y += 0.02;
  cube.rotation.z -=0.01;
}

// 애니메이션 루프 실행
renderer.setAnimationLoop(animate);
