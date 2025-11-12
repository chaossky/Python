// three.js 라이브러리를 불러옵니다.
import * as THREE from 'three';
// 마우스로 회전/줌 제어가 가능한 OrbitControls 모듈을 불러옵니다.
//import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

let renderer;
let scene;
let camera;
let cube;
// 3D 장면(Scene)을 생성합니다.

function init(){
scene = new THREE.Scene();
camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);

renderer = new THREE.WebGLRenderer();
renderer.setClearColor(0x000000,1.0);
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.shadowMap.enabled=true;

//plane
const planeGeometry=new THREE.PlaneGeometry(20,20);
const planeMaterial=new THREE.MeshLambertMaterial({color:0xcccccc});
const plane=new THREE.Mesh(planeGeometry,planeMaterial);
plane.receiveShadow=true;
plane.rotation.x=-0.5*Math.PI;
plane.position.set(0,-2,0);
scene.add(plane);

// // 큐브 지오메트리 생성 (가로 6, 세로 4, 깊이 6)
const cubeGeometry = new THREE.BoxGeometry(6, 4, 6);
const cubeMaterial = new THREE.MeshLambertMaterial({ color: "red" });
cube = new THREE.Mesh(cubeGeometry, cubeMaterial);
cube.castShadow=true;
scene.add(cube);
 
//spot light
const spotLight=new THREE.SpotLight(0xffffff,1);
spotLight.position.set(10,20,20);
spotLight.castShadow=true;
spotLight.shadow.mapSize.set(1024, 1024); // 그림자 해상도
spotLight.angle = Math.PI / 6; // 빛 확산 각도
spotLight.penumbra = 0.3; // 가장자리 부드러움
spotLight.decay = 2; // 거리 감쇠
spotLight.distance = 100; // 유효 거리
scene.add(spotLight);

//camera
camera.position.set(15,16,13);
camera.lookAt(scene.position);

//ambient light
const ambient = new THREE.AmbientLight(0xcccccc, 0.3);
scene.add(ambient);

document.body.appendChild(renderer.domElement);

render();
}

function render(){
    requestAnimationFrame(render);
    // cube.rotation.x += 0.01;
    // cube.rotation.y += 0.01;
    renderer.render(scene,camera);
}

function handleResize(){
    camera.aspect=window.innerWidth/window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth,window.innerHeight);
}
window.onload=init;
window.addEventListener('resize',handleResize,false);

