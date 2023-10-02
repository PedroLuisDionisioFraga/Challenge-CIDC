# Quality Report of Sites in 2023

This is a Python project that processes Excel files `SiteList.xlsx` and `Results.xlsx` to generate a quality report of sites in 2023.

## Prerequisites

- Python 3.x installed on your system.
- pandas library installed. You can install it with the command `pip install pandas`.

## How to Use

1. Place the Excel files SiteList.xlsx and Results.xlsx in the same directory as this script.

2. Run the Python script:

  ```bash
  python Solution/generate_report.py
  ```
## The report will be displayed in the terminal with all datas, not only 2023, including:
`
  Sites with active alerts.
  Sites with a quality score of 0.
  Sites with more than 80 Mbps.
  Sites with less than 10 Mbps.
`

## File Structure
`Solution/generate_report.py`: The Python script to process the Excel files and generate the report.
`Solution/Tests/generate_report.ipynb`: The notebook to tests.
`SiteList.xlsx`: Excel file containing general site data.
`Results.xlsx`: Excel file containing test results for locations.
### Excel files after filter.
`Solution/Reports/`

# Author
Pedro Luis Dionísio Fraga
