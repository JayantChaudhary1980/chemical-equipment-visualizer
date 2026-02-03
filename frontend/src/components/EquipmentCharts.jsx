import {
  Chart as ChartJS,
  ArcElement,
  Tooltip,
  Legend,
  CategoryScale,
  LinearScale,
  BarElement,
} from "chart.js";
import { Pie, Bar } from "react-chartjs-2";

ChartJS.register(
  ArcElement,
  Tooltip,
  Legend,
  CategoryScale,
  LinearScale,
  BarElement
);

function EquipmentCharts({ summary }) {
  const typeLabels = Object.keys(summary.equipment_type_distribution);
  const typeCounts = Object.values(summary.equipment_type_distribution);

  const pieData = {
    labels: typeLabels,
    datasets: [
      {
        label: "Equipment Count",
        data: typeCounts,
        backgroundColor: [
          "#4CAF50",
          "#2196F3",
          "#FFC107",
          "#9C27B0",
          "#FF5722",
          "#607D8B",
        ],
      },
    ],
  };

  const barData = {
    labels: ["Avg Flowrate", "Avg Pressure", "Max Temperature"],
    datasets: [
      {
        label: "Values",
        data: [
          summary.average_flowrate,
          summary.average_pressure,
          summary.max_temperature,
        ],
        backgroundColor: "#2196F3",
      },
    ],
  };

  return (
    <div style={{ marginTop: "40px" }}>
      <h3>Equipment Type Distribution</h3>
      <Pie data={pieData} />

      <h3 style={{ marginTop: "40px" }}>Key Parameters</h3>
      <Bar data={barData} />
    </div>
  );
}

export default EquipmentCharts;
