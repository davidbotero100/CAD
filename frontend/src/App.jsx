import React, { useState } from "react";
import DesignCanvas2D from "./components/DesignCanvas2D.jsx";
import DesignCanvas3D from "./components/DesignCanvas3D.jsx";

function App() {
  const [mode, setMode] = useState("2D"); // Default mode

  return (
    <div>
      <h1>CAD Design Viewer</h1>
      <button onClick={() => setMode("2D")}>2D View</button>
      <button onClick={() => setMode("3D")}>3D View</button>

      {/* {mode === "2D" ? <DesignCanvas2D drawingData={[]} /> : <DesignCanvas3D />}*/}

      {/* Temporary data for GUI testing */}
      {mode === "2D" ? <DesignCanvas2D drawingData={[[50, 50, 200, 200], [100, 300, 400, 500]]} /> : <DesignCanvas3D />}

    </div>
  );
}

export default App;
