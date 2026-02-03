import sys
import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QPushButton, QLabel, QFileDialog
)
import matplotlib.pyplot as plt


API_UPLOAD_URL = "http://127.0.0.1:8000/api/upload/"


class DesktopApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chemical Equipment Visualizer")
        self.resize(400, 300)

        layout = QVBoxLayout()

        self.info_label = QLabel("Upload a CSV file to analyze equipment data.")
        layout.addWidget(self.info_label)

        upload_btn = QPushButton("Upload CSV")
        upload_btn.clicked.connect(self.upload_csv)
        layout.addWidget(upload_btn)

        self.summary_label = QLabel("")
        layout.addWidget(self.summary_label)

        self.setLayout(layout)

    def upload_csv(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select CSV File", "", "CSV Files (*.csv)"
        )

        if not file_path:
            return

        with open(file_path, "rb") as f:
            response = requests.post(API_UPLOAD_URL, files={"file": f})

        if response.status_code != 201:
            self.summary_label.setText("Upload failed.")
            return

        summary = response.json()["summary"]

        self.summary_label.setText(
            f"Total Equipment: {summary['total_equipment']}\n"
            f"Avg Flowrate: {summary['average_flowrate']:.2f}\n"
            f"Avg Pressure: {summary['average_pressure']:.2f}\n"
            f"Max Temperature: {summary['max_temperature']}"
        )

        self.show_chart(summary)

    def show_chart(self, summary):
        types = summary["equipment_type_distribution"]
        labels = list(types.keys())
        values = list(types.values())

        plt.figure(figsize=(6, 4))
        plt.bar(labels, values)
        plt.title("Equipment Type Distribution")
        plt.xlabel("Type")
        plt.ylabel("Count")
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DesktopApp()
    window.show()
    sys.exit(app.exec_())
