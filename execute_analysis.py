import sqlite3
from pathlib import Path

PROJECT_FOLDER = Path(__file__).resolve().parent.parent
DATABASE_FILE = PROJECT_FOLDER / "database" / "ev_market.db"
SQL_FILE = PROJECT_FOLDER / "database" / "analysis_queries.sql"

connection = sqlite3.connect(DATABASE_FILE)

try:
    sql_text = SQL_FILE.read_text(encoding="utf-8")

    # Split the file into individual SQL statements.
    queries = [
        statement.strip()
        for statement in sql_text.split(";")
        if statement.strip()
    ]

    for number, query in enumerate(queries, start=1):
        print("\n" + "=" * 60)
        print(f"QUERY {number}")
        print("=" * 60)

        cursor = connection.execute(query)

        if cursor.description is None:
            print("Statement executed successfully.")
            continue

        columns = [item[0] for item in cursor.description]
        rows = cursor.fetchall()

        print(" | ".join(columns))
        print("-" * 60)

        for row in rows:
            print(" | ".join(
                str(value) if value is not None else "NULL"
                for value in row
            ))

        print(f"\nRows returned: {len(rows)}")

finally:
    connection.close()