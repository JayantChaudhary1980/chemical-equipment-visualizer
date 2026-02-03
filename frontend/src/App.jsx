import { useState } from "react";
import FileUpload from "./components/FileUpload";

function App() {
  const [summary, setSummary] = useState(null);

  return (
    <div style={{ padding: "20px", fontFamily: "Arial, sans-serif" }}>
      <h2>Chemical Equipment Parameter Visualizer</h2>
      <p>
        Upload a CSV file containing chemical equipment parameters to view
        summary analytics.
      </p>

      <FileUpload onUploadSuccess={setSummary} />

      {summary && (
        <div style={{ marginTop: "30px" }}>
          <h3>Summary</h3>
          <p>Total Equipment: {summary.total_equipment}</p>
          <p>Average Flowrate: {summary.average_flowrate.toFixed(2)}</p>
          <p>Average Pressure: {summary.average_pressure.toFixed(2)}</p>
          <p>Max Temperature: {summary.max_temperature}</p>
        </div>
      )}
    </div>
  );
}

export default App;
