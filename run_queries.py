import sqlite3
from pathlib import Path

PROJECT_FOLDER = Path(__file__).resolve().parent.parent
DATABASE_FILE = PROJECT_FOLDER / "database" / "ev_market.db"

connection = sqlite3.connect(DATABASE_FILE)
cursor = connection.cursor()

try:
    print("\n" + "=" * 55)
    print("ELECTRIC VEHICLE MARKET - DATA CHECK")
    print("=" * 55)

    # Query 1: Count all records
    cursor.execute("SELECT COUNT(*) FROM ev_vehicles")
    total_records = cursor.fetchone()[0]
    print(f"\n1. Total records: {total_records:,}")

    # Query 2: Count distinct manufacturers
    cursor.execute("""
        SELECT COUNT(DISTINCT manufacturer)
        FROM ev_vehicles
        WHERE manufacturer IS NOT NULL
          AND TRIM(manufacturer) <> ''
    """)
    total_manufacturers = cursor.fetchone()[0]
    print(f"2. Distinct manufacturers: {total_manufacturers:,}")

    # Query 3: Count distinct vehicle IDs
    cursor.execute("""
        SELECT COUNT(DISTINCT vehicle_id)
        FROM ev_vehicles
        WHERE vehicle_id IS NOT NULL
          AND TRIM(vehicle_id) <> ''
    """)
    total_vehicles = cursor.fetchone()[0]
    print(f"3. Distinct vehicle IDs: {total_vehicles:,}")

    # Query 4: Show the five most frequent manufacturers
    cursor.execute("""
        SELECT manufacturer, COUNT(*) AS record_count
        FROM ev_vehicles
        WHERE manufacturer IS NOT NULL
          AND TRIM(manufacturer) <> ''
        GROUP BY manufacturer
        ORDER BY record_count DESC
        LIMIT 5
    """)

    print("\n4. Five manufacturers with the most records:")
    for manufacturer, record_count in cursor.fetchall():
        print(f"   {manufacturer}: {record_count:,} records")

    # Query 5: Check missing or blank values in important columns
    important_columns = [
        "manufacturer",
        "annual_sales_units",
        "range_km",
        "price_usd",
        "customer_rating",
    ]

    print("\n5. Missing or blank values:")
    for column in important_columns:
        query = f"""
            SELECT COUNT(*)
            FROM ev_vehicles
            WHERE "{column}" IS NULL
               OR TRIM("{column}") = ''
        """
        cursor.execute(query)
        missing_count = cursor.fetchone()[0]
        print(f"   {column}: {missing_count:,}")

    print("\n" + "=" * 55)
    print("DATA CHECK COMPLETED")
    print("=" * 55)

finally:
    connection.close()