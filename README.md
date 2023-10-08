# connect_presto_and_excel_with_python

---


## Overview

This project is a simple Python script that reads an SQL query from a file, executes it against a Presto database, and saves the query results into an Excel spreadsheet. The main goal is to provide an easy way to export SQL query results to Excel.

## Features

- Connects to a Presto database and executes SQL queries.
- Reads SQL queries from an external file (`query.sql`).
- Converts query results into an Excel spreadsheet (`read_sql.xlsx`).
- Offers flexibility by allowing customization of Presto connection parameters.

## Prerequisites

Before running this script, ensure you have the following prerequisites installed:

- Python 3.x: You can download Python from [python.org](https://www.python.org/downloads/).
- Required Python libraries: Install them using `pip` by running `pip install pyhive pandas openpyxl`.

## Usage

1. Clone or download this project to your local machine.

2. Update the Presto connection parameters in the script:

   - `host`: Replace with your Presto host IP or hostname.
   - `port`: Replace with the Presto port.
   - `username`: Replace with your Presto username.

3. Create an SQL file (`query.sql`) containing the SQL query you want to execute.

4. Open a terminal or command prompt and navigate to the project directory.

5. Run the script:

   ```bash
   python your_script_name.py
   ```

   Replace `your_script_name.py` with the name of your Python script that contains the code.

6. The script will execute the SQL query, fetch the results, and save them in an Excel spreadsheet named `read_sql.xlsx`.

7. You can open the generated Excel file using the default application.

## Note

- This project is intended for educational and demonstration purposes. In a production environment, consider using more robust and scalable solutions for data extraction and reporting.

---

Feel free to customize this README to suit your project's specific details and requirements. This should give users a clear understanding of how to use your SQL to Excel converter script.
