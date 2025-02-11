import React from "react";
import { Canvas } from "@react-three/fiber";
import { OrbitControls } from "@react-three/drei";

const DesignCanvas3D = () => {
    return (
        <div style={{ width: "800px", height: "600px", border: "1px solid black" }}>
            <Canvas camera={{ position: [5, 5, 5] }}>
                <ambientLight />
                <pointLight position={[10, 10, 10]} />
                <OrbitControls />
                <mesh>
                    <boxGeometry args={[2, 2, 2]} />
                    <meshStandardMaterial color="blue" />
                </mesh>
            </Canvas>
        </div>
    );
};

export default DesignCanvas3D;
