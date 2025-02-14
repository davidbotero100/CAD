import React, { useState } from "react";
import DesignCanvas2D from "./components/DesignCanvas2D.jsx";
import DesignCanvas3D from "./components/DesignCanvas3D.jsx";
import UserPrompt from "./components/UserPrompt.jsx"; // Correct import
import ReceiveDesign from "./components/ReceiveDesign.jsx";

function App() {
  const [mode, setMode] = useState("2D"); // Default mode
  const [designUrl, setDesignUrl] = useState(null); // Stores received design

  return (
    <div>
      <h1>CAD Design Viewer</h1>
      <button onClick={() => setMode("2D")}>2D View</button>
      <button onClick={() => setMode("3D")}>3D View</button>

      {/* User Input Section */}
      <UserPrompt onReceiveDesign={setDesignUrl} />

      {/* Design Display Section */}
      {mode === "2D" ? (
        <DesignCanvas2D drawingData={[[50, 50, 200, 200], [100, 300, 400, 500]]} />
      ) : (
        <DesignCanvas3D designUrl={designUrl} />
      )}

      {/* Receiving and Formatting the Design */}
      <ReceiveDesign designUrl={designUrl} />
    </div>
  );
}

export default App;
