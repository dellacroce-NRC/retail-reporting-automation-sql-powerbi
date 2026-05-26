# Retail Reporting Automation with SQL and Power BI
### Building a Refreshable Commercial Dashboard from a MySQL Reporting Source

## Executive Summary

This project presents a retail reporting workflow designed to make commercial analysis more reliable, traceable and easier to refresh. A relational MySQL database is used as the reporting source, SQL queries validate the main business metrics, and Power BI turns those validated results into an interactive dashboard for sales, cost and branch performance analysis.

The workflow connects three common analyst responsibilities in one portfolio case: structuring business data, validating metrics before visualization, and delivering a dashboard that can be refreshed when new records are added to the database.

The result is a reporting setup where business users can review sales performance, product movement, regional behavior and branch-level profitability from a dashboard whose numbers can be traced back to SQL.

## Business Context

Retail teams often need recurring visibility into sales, costs, products and store performance. When reporting depends on static files or repeated manual updates, metric definitions can drift and dashboards become harder to trust.

This project simulates a more controlled reporting process: commercial data is stored in MySQL, analytical checks are performed in SQL, and Power BI is connected directly to the database as the visualization layer. The workflow supports a practical reporting question: how can a retail dashboard stay aligned with the underlying business data as new records are added?

## Business Questions Addressed

- Which branches generate the highest revenue?
- Which products concentrate the most sales volume?
- How do sales and costs compare across branches?
- Which locations show stronger commercial performance?
- Do Power BI visuals remain consistent with the SQL-validated metrics?
- Can the report reflect new database records after refreshing the model?

## Project Workflow

```text
Create MySQL retail database
        |
        v
Load sample sales, cost, product and branch data
        |
        v
Validate commercial metrics with SQL queries
        |
        v
Connect Power BI to MySQL
        |
        v
Build dashboard views for sales and performance analysis
        |
        v
Compare dashboard results against SQL outputs
        |
        v
Insert new records with Python
        |
        v
Refresh Power BI model and confirm report update
```

## What the Project Demonstrates

- A SQL-centered reporting workflow for recurring commercial analysis.
- Use of MySQL as a structured source for sales, cost, product and branch data.
- Metric validation in SQL before building dashboard visuals.
- Consistency checks between SQL outputs and Power BI results.
- A Power BI report connected to the database instead of a static spreadsheet export.
- A Python-based loading test to simulate new records entering the reporting source.
- Basic credential hygiene through environment variables for the local MySQL connection.

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

## Main Files

- `ventas_costos.sql`: creates the MySQL database, defines the retail tables and loads the initial sample data.
- `revisión_datos.sql`: contains SQL queries for inspecting tables and validating commercial metrics.
- `insertar_nuevos_datos.py`: inserts additional records into MySQL from CSV files to test report refresh behavior.
- `Retail_Intelligence_Dashboard.pbix`: Power BI report connected to the MySQL database.
- `requirements.txt`: Python dependencies needed to run the insertion script.
- `.env.example`: template for local MySQL connection variables.

## Metrics Validated in SQL

The SQL validation layer provides a source-level reference for the dashboard. The queries review:

- Total records by table.
- Product category distribution.
- Branch and regional coverage.
- Top-selling products by quantity sold.
- Total revenue by branch.
- Total costs by branch.
- Branch-level profit calculated from sales and costs.

This validation step is important because it keeps the dashboard grounded in explicit business logic. The Power BI report is not treated as a black box: its numbers can be checked against SQL outputs.

## Power BI Dashboard

The Power BI dashboard provides a business-facing view of the MySQL reporting source. It summarizes sales, costs, products and branch performance so the user can move from raw transactional records to a clearer commercial readout.

The dashboard was built with a simple principle: every visual should represent a metric that can be explained and validated from the database. This makes the report easier to defend in review, easier to maintain, and more useful for recurring business analysis.

<img width="726" height="439" alt="Retail Power BI dashboard screenshot" src="https://github.com/user-attachments/assets/6e417ce4-69c7-4b63-b2b9-d61e7a64e82a" />

## Refresh Test with Python

The Python script simulates the arrival of new data by inserting additional records into MySQL from CSV files. After the database is updated, the Power BI model can be refreshed to confirm that the report reflects the new state of the source.

This step demonstrates the practical value of connecting a dashboard to a database: the report can evolve with the underlying data while preserving a clear validation path through SQL.

To run the script locally, install the Python dependencies and create a local `.env` file based on `.env.example` with your own MySQL credentials. The real `.env` file should remain outside version control.

## Tools Used

- **MySQL:** relational database and reporting source.
- **SQL:** database creation, metric validation and commercial analysis queries.
- **Power BI:** dashboard development and reporting layer.
- **DAX:** KPI and measure logic inside the report.
- **Python:** insertion script used to test report refresh behavior.
- **pandas / MySQL Connector:** CSV reading and database insertion.
- **python-dotenv:** local environment variable management.

## Role

This project was adapted from a guided analytics course and developed into a portfolio case focused on SQL-based metric validation and refreshable business reporting. My role covered the full analytical workflow: creating the database, validating commercial metrics in SQL, building the Power BI report, checking consistency across tools, and using Python to test how the report responds when the database receives new records.

## Key Takeaway

The main takeaway is that reliable reporting depends on more than visual design. A dashboard becomes more useful when its metrics are validated at the source, its calculations are traceable, and its data model can be refreshed as new records enter the system.

This project shows a practical foundation for commercial reporting automation: SQL defines and validates the business logic, MySQL stores the reporting data, Power BI communicates the results, and Python supports a simple refresh test for new records.
