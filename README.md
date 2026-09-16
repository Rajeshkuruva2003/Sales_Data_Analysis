# Sales Data Analysis & Reporting

## Objective
Analyze sales data to identify revenue trends, product performance, and regional sales patterns.

## Skills Demonstrated
- Python and Pandas
- Data cleaning and validation
- SQL and MySQL
- Data aggregation and analysis
- Excel-ready reporting
- Matplotlib visualization
- Data quality checks and problem solving.

## Workflow
1. Load the CSV dataset.
2. Check duplicates, missing values, and invalid records.
3. Clean and validate the data.
4. Recalculate sales values.
5. Analyze monthly, regional, category, and product performance.
6. Run SQL queries for business questions.
7. Create visual reports.
8. Open the cleaned CSV in Excel for Pivot Tables and charts.

## Run
```bash
pip install -r requirements.txt
python src/analysis.py
```

## Project Structure
- `data/sales_data.csv` - sample raw dataset
- `src/analysis.py` - Python analysis
- `sql/queries.sql` - MySQL queries
- `reports/clean_sales_data.csv` - cleaned dataset
- `reports/` - generated charts
