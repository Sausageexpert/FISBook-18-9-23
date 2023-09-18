import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

document.addEventListener('DOMContentLoaded', function(){

    const scene = new THREE.Scene()
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);
    camera.position.set(0,0,10);

    const renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, window.innerHeight);

    const scenebox = document.getElementById('scene-box');
    scenebox.appendChild(renderer.domElement);

    const geometry = new THREE.TorusGeometry(10, 3, 16, 100);
    const material = new THREE.MeshBasicMaterial({color: 0xFF6347, wireframe:true}); // only visible when you have a light source
    const torus = new THREE.Mesh(geometry, material);
    scene.add(torus);

    const ambientLight = new THREE.AmbientLight(0xffffff);
    scene.add(ambientLight);

    const controls = new OrbitControls(camera, renderer.domElement)
    const animate = () => {
        torus.rotation.x+=0.02;
        renderer.render(scene, camera);
        controls.update();
        requestAnimationFrame(animate);
        
    }

    animate();


});
