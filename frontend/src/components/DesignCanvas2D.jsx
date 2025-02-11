import React, { useRef, useState } from "react";
import { Stage, Layer, Line } from "react-konva";

const DesignCanvas2D = ({ drawingData }) => {
    const stageRef = useRef(null);
    const [scale, setScale] = useState(1);

    const handleWheel = (e) => {
        e.evt.preventDefault();
        const scaleBy = 1.1;
        const oldScale = stageRef.current.scaleX();
        const newScale = e.evt.deltaY > 0 ? oldScale / scaleBy : oldScale * scaleBy;
        setScale(newScale);
        stageRef.current.scale({ x: newScale, y: newScale });
    };

    return (
        <Stage width={800} height={600} draggable scaleX={scale} scaleY={scale} ref={stageRef} onWheel={handleWheel}>
            <Layer>
                {drawingData.map((line, index) => (
                    <Line key={index} points={line} stroke="black" strokeWidth={2} />
                ))}
            </Layer>
        </Stage>
    );
};

export default DesignCanvas2D;
