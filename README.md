# Electric Vehicle Market Analysis & Insights Dashboard

## Project Overview

The **Electric Vehicle (EV) Market Analysis & Insights Dashboard** is a data analytics project designed to explore the electric vehicle market through interactive visualizations and database-driven analysis.

The project uses Python, SQL, SQLite, and Tableau to organize EV market data and present insights into vehicle sales, manufacturers, categories, battery technologies, driving range, customer ratings, and manufacturing countries.

## Project Objectives

- Analyze electric vehicle sales across manufacturers.
- Compare sales across different vehicle categories.
- Examine average driving range by category.
- Explore the distribution of battery technologies.
- Compare average customer ratings across manufacturers.
- Explore vehicle distribution by manufacturing country.
- Present findings through an interactive Tableau dashboard.

## Technologies Used

- **Tableau Public** — Interactive dashboard and data visualization.
- **Python** — Data processing and application development.
- **SQL** — Database queries and data analysis.
- **SQLite** — Relational database storage.
- **Flask** — Python web application framework.
- **GitHub** — Source code management and project documentation.

## Dataset

The project uses an electric vehicle market dataset containing approximately 100,000 records and 37 columns.

Important fields include:

- Vehicle ID
- Manufacturer
- Vehicle category
- Model year
- Manufacturing country
- Market region
- Battery capacity
- Battery type
- Driving range
- Vehicle price
- Annual sales units
- Customer rating
- Annual CO₂ savings

The dataset is provided in CSV format, and a SQLite database is included for database-based analysis.

**Note:** Missing values exist in some dataset columns. Analysis should account for missing values where relevant.

## Tableau Dashboard

The dashboard is titled **Electric Vehicle Market Analysis & Insights**.

### Dashboard Visualizations

1. **EV Sales by Manufacturer** — Compares annual sales across manufacturers.
2. **Sales by Category** — Compares annual sales across vehicle categories.
3. **Average Range by Category** — Examines average driving range by category.
4. **Battery Distribution** — Shows the distribution of battery types among vehicles.
5. **Customer Ratings** — Compares average customer ratings across manufacturers.
6. **Country Distribution** — Shows the distribution of vehicles by manufacturing country.

The dashboard also includes a manufacturer filter for interactive exploration.

### Live Dashboard

[View the Interactive Tableau Dashboard](https://public.tableau.com/app/profile/mahi.manoj.jain/viz/EV_Market_Analysis_17931111351670/EVMarketOverview?publish=yes
)

## Project Structure

```text
EV-Market-Analysis/
│
├── README.md
├── app.py
├── requirements.txt
│
├── data/
│   └── ev_market_data.csv
│
├── database/
│   ├── README.md
│   ├── ev_market.db
│   ├── create_database.py
│   ├── execute_analysis.py
│   └── run_queries.py
│
└── tableau/
    └── EV_Market_Analysis.twbx
```

*The structure above illustrates the intended organization. Actual filenames and locations may differ.*

## Getting Started

### Prerequisites

Install the following software before running the project:

- Python 3
- Tableau Public, if you want to explore the workbook
- A code editor such as Visual Studio Code

### Setup Instructions

1. Clone or download this repository.
2. Open the project folder in Visual Studio Code.
3. Create and activate a Python virtual environment.
4. Install the required Python packages using `requirements.txt`.
5. Review the database scripts before executing them.
6. Open the Tableau workbook to explore the dashboard.

### Python Environment

After cloning the repository, you can create a virtual environment with:

```bash
python -m venv .venv
```

On Windows, activate it using:

```bash
.venv\Scripts\activate
```

Install dependencies using:

```bash
pip install -r requirements.txt
```

**Note:** The exact commands required to initialize the database and run the Flask application depend on the implementation of the Python scripts.

## Key Areas of Analysis

This project explores:

- Manufacturer-level sales comparisons
- Sales differences between vehicle categories
- Average driving range
- Battery technology distribution
- Customer ratings
- Manufacturing-country distribution

The dashboard can be used to explore these dimensions interactively. Numerical conclusions should be drawn from the actual dataset and verified analysis results.

## Future Improvements

- Add additional market trend visualizations.
- Improve data cleaning and missing-value handling.
- Add more SQL-based analytical queries.
- Enhance the Flask application's functionality.
- Add more interactive dashboard filters.
- Include documented findings and recommendations.

## Author

**Student Data Analytics Project**

Developed as an academic project to explore data analysis, database management, Python programming, and business intelligence using electric vehicle market data.
