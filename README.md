# Retail Reporting Automation with SQL and Power BI
### From SQL Metric Validation to Refreshable Business Dashboards

## Executive Summary

This project demonstrates a practical retail reporting workflow built around a relational MySQL database connected to Power BI. The objective was to move from static reporting logic toward a refreshable dashboard model, where commercial metrics are validated in SQL and then reproduced in Power BI as a business-facing report.

The project follows a guided analytics sequence:

1. Create a relational retail database in MySQL using SQL scripts.
2. Validate sales, cost, product and branch metrics through SQL queries.
3. Build a Power BI dashboard connected to the MySQL database.
4. Reconcile Power BI visuals and measures against the SQL query results.
5. Insert new records into the database with a Python script to test whether the dashboard can reflect updated data after refreshing the model.

The focus is not advanced ETL or end-to-end data engineering. The value of the project is in showing how SQL can act as the source of truth for recurring business reporting, while Power BI becomes the visualization and decision-support layer.

## Business Context

Many commercial reports are rebuilt manually from spreadsheets or static exports, which makes it harder to keep metric definitions consistent over time. This project simulates a more reliable reporting setup: business data lives in a relational database, metric logic is first validated with SQL, and the dashboard is refreshed from the same source.

For a retail team, this type of workflow can support recurring questions such as:

- Which branches generate the highest sales?
- Which products sell the most units?
- How do sales and costs compare by branch?
- Which locations show stronger or weaker commercial performance?
- Does the report update correctly when new transactional records are added?

## What This Project Demonstrates

- Using MySQL as a structured source for retail reporting.
- Creating relational tables for branches, products, sales and costs.
- Validating business metrics directly with SQL before visualization.
- Building a Power BI dashboard connected to the database.
- Checking consistency between SQL query outputs and Power BI visuals.
- Using Python to insert additional records and test dashboard refresh behavior.

## Analytical Workflow

```text
MySQL database creation
        |
        v
SQL metric validation
        |
        v
Power BI connection to MySQL
        |
        v
Dashboard construction
        |
        v
Metric reconciliation between SQL and Power BI
        |
        v
Python-based insertion of new records
        |
        v
Power BI model refresh and report update
```

## Repository Structure

```text
.
+-- ventas_costos.sql
+-- revisión_datos.sql
+-- insertar_nuevos_datos.py
+-- Retail_Intelligence_Dashboard.pbix
+-- requirements.txt
+-- .env.example
+-- README.md
```

### Main Files

- `ventas_costos.sql`: creates the MySQL database, defines the core retail tables and loads the initial sample data.
- `revisión_datos.sql`: contains SQL queries used to inspect the database and validate business metrics such as record counts, product sales, branch revenue, branch costs and branch-level profit.
- `insertar_nuevos_datos.py`: inserts additional records into MySQL from CSV files to simulate new data being added to the reporting database.
- `Retail_Intelligence_Dashboard.pbix`: Power BI report connected to the MySQL database.
- `requirements.txt`: Python dependencies needed to run the insertion script.
- `.env.example`: example environment variables for the local MySQL connection.

## Metrics Validated in SQL

The SQL validation layer checks the structure and results behind the dashboard. Examples include:

- Total records by table.
- Product category distribution.
- Branch and regional coverage.
- Top-selling products by quantity sold.
- Total revenue by branch.
- Total costs by branch.
- Estimated profit by branch, calculated as sales minus costs.

These queries provide a traceable baseline for checking whether Power BI visuals are aligned with the database results.

## Power BI Dashboard

The Power BI report was built as the reporting layer on top of the MySQL database. Its purpose is to make the validated SQL metrics easier to explore through business visuals.

The dashboard supports commercial analysis across branches, products, regions, sales and costs. The important design principle is consistency: the dashboard should reflect the same business definitions validated in SQL, instead of becoming a separate layer with disconnected calculations.

<img width="726" height="439" alt="Retail Power BI dashboard screenshot" src="https://github.com/user-attachments/assets/6e417ce4-69c7-4b63-b2b9-d61e7a64e82a" />

## Python Loading Test

The Python script is used to simulate the insertion of new retail records into MySQL. This is a simple loading test, not a complex ETL pipeline.

Its role is to validate the reporting workflow:

1. New records are inserted into the database.
2. Power BI refreshes the model.
3. The dashboard reflects the updated database state.

This demonstrates the practical benefit of connecting a dashboard to a relational source instead of rebuilding reports manually from static files.

To run the script locally, install the Python dependencies and create a local `.env` file based on `.env.example` with your own MySQL credentials. The real `.env` file should not be committed to the repository.

## Tools Used

- **MySQL:** relational database used as the reporting source.
- **SQL:** database creation, metric validation and business analysis queries.
- **Power BI:** dashboard development and reporting layer.
- **DAX:** measures and KPI logic inside the Power BI model.
- **Python:** script-based insertion of additional records for refresh testing.
- **pandas / MySQL connector:** CSV reading and database insertion support.

## Role

This project was adapted from a guided data analytics course and structured as a portfolio case focused on reporting automation. My role was to build and validate the workflow across SQL, MySQL, Power BI and Python, with emphasis on metric consistency and dashboard refresh behavior.

The project is intentionally positioned as a practical analytics and reporting automation exercise, not as an advanced data engineering pipeline.

## Key Learning Outcome

The main learning outcome was understanding how recurring business reporting becomes more reliable when metrics are validated at the database level and then visualized from the same source.

By comparing SQL query outputs with Power BI visuals, the project reinforces a key analytics practice: dashboards should not only be visually clear; their numbers should be traceable, reproducible and connected to the source data.
