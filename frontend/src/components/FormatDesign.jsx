import React, { useState, useEffect } from "react";
import DesignCanvas2D from "./DesignCanvas2D";
import DesignCanvas3D from "./DesignCanvas3D";

const FormatDesign = ({ designUrl }) => {
    const [designType, setDesignType] = useState(null);
    const [formattedData, setFormattedData] = useState(null);

    useEffect(() => {
        // Simulate checking the file type (2D or 3D)
        if (designUrl.endsWith(".dwg")) {
            setDesignType("3D");
        } else if (designUrl.endsWith(".json")) {
            setDesignType("2D");
        }

        // Fetch and format the design data
        const fetchDesignData = async () => {
            try {
                const response = await fetch(designUrl);
                if (!response.ok) throw new Error("Failed to fetch design");
                const data = await response.json();
                setFormattedData(data);
            } catch (error) {
                console.error("Error processing design:", error);
            }
        };

        fetchDesignData();
    }, [designUrl]);

    return (
        <div>
            {designType === "2D" && formattedData ? (
                <DesignCanvas2D drawingData={formattedData.lines} />
            ) : designType === "3D" ? (
                <DesignCanvas3D designFile={designUrl} />
            ) : (
                <p>Loading design...</p>
            )}
        </div>
    );
};

export default FormatDesign;
