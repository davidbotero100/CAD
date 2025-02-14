import React, { useState } from "react";
import SendUserPrompt from "./SendUserPrompt";
import ReceiveDesign from "./ReceiveDesign";

const UserPrompt = () => {
    const [userInput, setUserInput] = useState("");
    const [designUrl, setDesignUrl] = useState(null);

    return (
        <div>
            <textarea
                value={userInput}
                onChange={(e) => setUserInput(e.target.value)}
                placeholder="Enter your design prompt..."
                rows="4"
                cols="50"
            />
            <SendUserPrompt prompt={userInput.trim()} onReceiveDesign={setDesignUrl} />
            <ReceiveDesign designUrl={designUrl} />
        </div>
    );
};

export default UserPrompt;
