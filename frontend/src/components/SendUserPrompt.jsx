import React, { useState } from "react";

const SendUserPrompt = ({ prompt, onReceiveDesign }) => {
    const sendPromptToBackend = async () => {
        try {
            const response = await fetch("http://127.0.0.1:8000/submit-prompt/", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ prompt }),
            });

            const data = await response.json();
            console.log("Server Response:", data);

            // Fetch the design file after processing
            const fileResponse = await fetch("http://127.0.0.1:8000/get-design/");
            if (fileResponse.ok) {
                onReceiveDesign(fileResponse.url);
            }
        } catch (error) {
            console.error("Error sending prompt:", error);
        }
    };

    return <button onClick={sendPromptToBackend}>Submit Prompt</button>;
};

export default SendUserPrompt;
