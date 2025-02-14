import React from "react";
import FormatDesign from "./FormatDesign";

const ReceiveDesign = ({ designUrl }) => {
    return (
        <div>
            <h2>Generated Design</h2>
            {designUrl ? (
                <FormatDesign designUrl={designUrl} />
            ) : (
                <p>No design available yet.</p>
            )}
        </div>
    );
};

export default ReceiveDesign;
