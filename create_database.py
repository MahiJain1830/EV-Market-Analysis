import sqlite3
import csv
from pathlib import Path

# Locate the main project folder
PROJECT_FOLDER = Path(__file__).resolve().parent.parent

# Define the CSV and database file paths
CSV_FILE = PROJECT_FOLDER / "data" / "ev_market_data.csv"
DATABASE_FILE = PROJECT_FOLDER / "database" / "ev_market.db"

# Check whether the CSV file exists
if not CSV_FILE.exists():
    raise FileNotFoundError(
        f"Dataset not found at: {CSV_FILE}"
    )

# Connect to SQLite and create the database file
connection = sqlite3.connect(DATABASE_FILE)

try:
    with CSV_FILE.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        if not reader.fieldnames:
            raise ValueError("The CSV file has no column headers.")

        # Create a table using the CSV column names.
        # All columns are initially stored as TEXT to preserve
        # the original CSV values during import.
        columns = ", ".join(
            '"' + name.replace('"', '""') + '" TEXT'
            for name in reader.fieldnames
        )

        connection.execute("DROP TABLE IF EXISTS ev_vehicles")

        connection.execute(
            f"CREATE TABLE ev_vehicles ({columns})"
        )

        column_names = ", ".join(
            '"' + name.replace('"', '""') + '"'
            for name in reader.fieldnames
        )

        placeholders = ", ".join(
            "?" for _ in reader.fieldnames
        )

        insert_sql = (
            f"INSERT INTO ev_vehicles ({column_names}) "
            f"VALUES ({placeholders})"
        )

        # Import the CSV in batches to handle large datasets.
        batch = []
        total_rows = 0

        for row in reader:
            batch.append([
                row.get(name) for name in reader.fieldnames
            ])

            if len(batch) >= 2000:
                connection.executemany(insert_sql, batch)
                total_rows += len(batch)
                batch.clear()

        if batch:
            connection.executemany(insert_sql, batch)
            total_rows += len(batch)

        connection.commit()

        print("Database created successfully!")
        print(f"Database location: {DATABASE_FILE}")
        print(f"Rows imported: {total_rows}")
        print(f"Columns imported: {len(reader.fieldnames)}")
        print("Table name: ev_vehicles")

finally:
    connection.close()