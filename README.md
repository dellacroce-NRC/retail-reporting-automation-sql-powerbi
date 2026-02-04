# Retail Intelligence Pipeline  
### Operationalizing Profitability via End-to-End Data Engineering

## 🚀 Executive Summary

In high-volume retail, fragmented data is the enemy of profitability.  
I developed a **comprehensive data ecosystem** that transforms sales and cost records into a **Single Source of Truth (SSOT)**.

This project demonstrates a full-stack transition from manual spreadsheets to an **automated relational architecture**, moving the needle from *“just reporting sales”* to providing **real-time visibility into Net Profit, Unit Economics, and Geospatial Performance**.

## 📈 Projected Business Impact & Benchmarks

*Note: These metrics are projected based on industry standards for manual data reconciliation in retail environments.*

- **Operational Efficiency:**  
  Automated an ETL workflow that reduces manual reporting lead time by ~10 hours per week, eliminating the “manual reporting tax” on analytical teams.

- **Scalability & Integrity:**  
  Unlike Excel-based silos, this SQL-centered architecture ensures **100% data consistency** by centralizing business logic at the model level.

- **Strategic Profitability:**  
  Enabled the identification of high-volume but low-margin clusters, shifting analytical focus from top-line revenue to actual **net utility**.

## 🏗️ Data Architecture & Modeling (ERD)

I implemented a **Star Schema (Fact Constellation)** to ensure high query performance.  
The model centers on two primary **Fact Tables** (`ventas` and `costos`) sharing common dimensions.

**Analyst Note on Architecture:**  
The model utilizes **1:N relationships** with dimension tables for `Products`, `Branches`, and a dedicated `Calendar`.  
This structure enables seamless comparison between revenue and operational costs, ensuring that **utility metrics** are calculated along a unified temporal and categorical axis.

## ⚙️ Technical Implementation

### 1. Data Ingestion & Automation (Python)

- **Pipeline:** Built a robust ingestion script using `pandas` and `SQLAlchemy` for dynamic data loading.
- **Idempotency:** Implemented **Upsert logic** to ensure idempotent executions, preventing duplicate records while maintaining historical accuracy.
- **Performance:** Optimized ingestion through bulk loading techniques to minimize database latency.

### 2. Data Auditing & Source Optimization (SQL)

- **Relational QA:** Developed an auditing suite to validate record counts and relational consistency across tables prior to visualization.
- **Server-Side Filtering:** Restricted the dataset to the last 24 months at the source level, improving query performance and reducing Power BI memory footprint.

### 3. Intelligence Layer (Power BI / DAX)

- **Advanced Ranking Logic:** Engineered dynamic measures using `TOPN` and `SUMMARIZE` to identify top-performing Managers and Cities based on net profitability.
- **Time Intelligence:** Implemented `PREVIOUSMONTH` logic to track Month-over-Month (MoM) growth, visualized via variance charts to highlight seasonal trends.
- **Geospatial Analysis:** Integrated regional mapping to correlate sales density with geographic performance indicators.

## 📊 Key Outcomes & Behavioral Insights

- **Granular Performance Visibility:**  
  Identified divergent margin profiles across high-revenue cities (e.g., Santiago vs. Concepción), prompting a re-evaluation of regional cost structures.

- **Evidence-Based Pricing:**  
  Detected product categories with sub-optimal margins, providing the analytical foundation for pricing adjustments or supplier renegotiations.

- **Cultural Shift:**  
  By removing manual data-preparation friction, the project enables a transition from reactive reporting to proactive strategic analysis.

## 🧑‍💼 Role & Tooling

**Role:** Product & Behavioral Data Analyst  
**Tools:** Python (pandas, SQLAlchemy), SQL (MySQL), Power BI (DAX), Git

<img width="726" height="439" alt="image" src="https://github.com/user-attachments/assets/6e417ce4-69c7-4b63-b2b9-d61e7a64e82a" />

