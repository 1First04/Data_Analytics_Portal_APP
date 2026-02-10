# Data_Analytics_Portal_APP

# Hunda Data Analytics Portal

A small, user-friendly Streamlit app for exploratory data analysis and visualization.

## Overview

This repository contains a lightweight Streamlit application that lets you upload CSV or Excel files and explore them interactively. The app provides quick descriptive statistics, top/bottom row views, data types, column lists, value counts with charts, and flexible group-by aggregation with multiple visualization options (line, bar, scatter, pie, sunburst).

Key features:

- Upload CSV or XLSX files
- View dataframe and descriptive statistics
- Inspect top / bottom rows and column data types
- Value counts with bar/line/pie charts
- Group-by aggregations and visualizations with configurable axes and color

## Files

- Myapp.py — the Streamlit application (entry point)

## Requirements

- Python 3.8+
- streamlit
- pandas
- plotly

Recommended install (Windows):

```powershell
python -m venv venv
venv\Scripts\activate
pip install --upgrade pip
pip install streamlit pandas plotly
```

Optionally create `requirements.txt`:

```powershell
pip freeze > requirements.txt
```

## Running the app

From the project directory run:

```powershell
streamlit run "Myapp.py"
```

This opens a browser window with the app UI. If a browser doesn't open automatically, the terminal will show a local URL (e.g., `http://localhost:8501`) you can visit.

## How to use

1. Click "Upload CSV / xls file" and select a `.csv` or `.xlsx` file.
2. Inspect the dataset using the tabs: Summary, Top and Bottom Rows, Data Types, Column Names.
3. Use "Value Counts" to select a column and view the most frequent values and corresponding charts.
4. Use "Groupby Operation" to choose grouping columns, aggregation column, and operation (sum, max, min, mean, median, count). Generate visualizations from the aggregated result.

<img width="1080" height="778" alt="image" src="https://github.com/user-attachments/assets/2357c64d-ee84-4e8c-bb99-f67fd7060c0d" />   <img width="1025" height="800" alt="image" src="https://github.com/user-attachments/assets/27ec5c77-ad3c-4aad-941d-2ede4a35c201" />  <img width="1096" height="751" alt="image" src="https://github.com/user-attachments/assets/d493a7d3-4a6b-460e-be3e-be80827459f8" /> <img width="1027" height="566" alt="image" src="https://github.com/user-attachments/assets/b55ec0b9-a287-428b-996b-207d43c933b0" />




## Notes and tips

- The app expects reasonably sized datasets for interactive use. Large files may slow the browser.
- Ensure numerical columns are properly typed for aggregation and plotting.
- If a visualization option fails, check the selected columns and operation types.

## Contributing

Contributions and improvements are welcome. For small fixes, open a pull request with a brief description of the change.

## Contact

For questions or help, open an issue in this repository or contact the project owner.
