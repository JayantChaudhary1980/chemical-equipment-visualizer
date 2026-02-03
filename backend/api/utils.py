import pandas as pd

REQUIRED_COLUMNS = {
    "Equipment Name",
    "Type",
    "Flowrate",
    "Pressure",
    "Temperature"
}

def analyze_csv(file):
    df = pd.read_csv(file)

    # Validate required columns
    if not REQUIRED_COLUMNS.issubset(df.columns):
        missing = REQUIRED_COLUMNS - set(df.columns)
        raise ValueError(f"Missing columns: {', '.join(missing)}")

    # Remove empty rows
    df = df.dropna()

    # Convert numeric columns safely
    for col in ["Flowrate", "Pressure", "Temperature"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna()

    summary = {
        "total_equipment": int(len(df)),
        "average_flowrate": float(df["Flowrate"].mean()),
        "average_pressure": float(df["Pressure"].mean()),
        "max_temperature": float(df["Temperature"].max()),
        "equipment_type_distribution": df["Type"].value_counts().to_dict()
    }

    return summary
