# Chemical Equipment Parameter Visualizer

This project was developed as part of the FOSSEE Internship screening task.
It is a hybrid Web and Desktop application that allows users to upload and analyze
chemical equipment data from a CSV file using a shared backend.

The focus of the project is on data handling, analytics, and visualization rather
than advanced UI design.

--------------------------------------------------

## Project Overview

The application accepts a CSV file containing chemical equipment details such as:

- Equipment Name
- Equipment Type
- Flowrate
- Pressure
- Temperature

The backend processes the uploaded data, computes summary statistics, stores recent
uploads, and exposes REST APIs that are used by both the web and desktop applications.

--------------------------------------------------

## Tech Stack

Backend:
- Python
- Django
- Django REST Framework
- Pandas
- SQLite

Web Frontend:
- React.js
- Chart.js

Desktop Frontend:
- PyQt5
- Matplotlib

Other Tools:
- Git and GitHub for version control

--------------------------------------------------

## Features

- Upload CSV files containing equipment data
- Backend analytics using Pandas
- Summary statistics (average values and maximum temperature)
- Equipment type distribution analysis
- Interactive charts in the web interface
- Desktop visualization using PyQt and Matplotlib
- PDF report generation for the latest uploaded dataset
- Basic authentication for protected endpoints
- Storage of recent upload history

--------------------------------------------------

## Project Structure

backend/    - Django REST API
frontend/   - React web application
desktop/    - PyQt desktop application
data/       - Sample CSV file for testing

--------------------------------------------------

## Setup Instructions

Backend Setup:

cd backend
pip install -r requirements.txt
python manage.py runserver

The backend server will run at:
http://127.0.0.1:8000/

--------------------------------------------------

Web Frontend Setup:

cd frontend
npm install
npm run dev

The web application will run at:
http://localhost:5173/

--------------------------------------------------

Desktop Application Setup:

cd desktop
python app.py

Make sure the backend server is running before starting the desktop application.

--------------------------------------------------

## PDF Report

A PDF summary report for the latest uploaded dataset can be downloaded from:
http://127.0.0.1:8000/api/report/

--------------------------------------------------

## Sample Data

A sample CSV file is provided in the data/ folder:
sample_equipment_data.csv

This file can be used to test both the web and desktop applications.

--------------------------------------------------

## What This Project Demonstrates

- Designing a shared REST backend for multiple client applications
- CSV-based data processing using Pandas
- Hybrid application development (Web + Desktop)
- Basic data visualization and reporting
- Clean separation between backend and frontend components

--------------------------------------------------

## Notes

This project was developed with an emphasis on clarity, correctness, and practical
implementation rather than extensive UI customization or advanced optimizations.
