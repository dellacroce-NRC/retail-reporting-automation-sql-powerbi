Retail Intelligence Pipeline: Operationalizing Profitability via End-to-End Data Engineering
🚀 Executive Summary
This project develops a comprehensive data ecosystem to transform sales and cost records into actionable financial insights. The core objective was to mitigate the lack of real-time visibility into profitability margins per branch, enabling data-driven decision-making based on actual net profit rather than just sales volume.

🛠️ Technical Stack & Implementation
1. Data Ingestion & Automation (Python)
I implemented an automation pipeline for dynamic data loading from CSV files.

Data Integrity: Utilized Upsert logic (ON DUPLICATE KEY UPDATE) to ensure the database is idempotent, preventing duplicates and maintaining historical accuracy across recurring executions.

Performance: Optimized bulk loading into MySQL by leveraging executemany to reduce ingestion latency.

2. Database Modeling (SQL)
Designed a relational architecture that serves as the "Single Source of Truth" (SSOT) for the business:

Modeling: Normalized star-schema structure with dimension tables (sucursales, productos) and fact tables (ventas, costos).

Business Queries: Optimized queries to calculate net operational utility and branch-level performance.

3. Business Intelligence (Power BI & DAX)
The final dashboard provides a strategic view of critical KPIs through custom metrics engineering:

Time Intelligence: Month-over-Month growth measures (PREVIOUSMONTH) for seasonal trend analysis.

Performance Ranking: Dynamic logic (TOPN) to identify the branch managers contributing most to net utility.

Profitability Logic: Implementation of VAR logic to decouple revenue and cost calculations in real-time.

📈 Key Insights
Through this pipeline, management can detect branches with high sales volumes but low-profit margins (as seen in the city-by-city comparison), allowing for strategic adjustments in cost structure or pricing strategies.
