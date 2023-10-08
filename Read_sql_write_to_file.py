# Import necessary libraries
from pyhive import presto
import pandas as pd
import openpyxl
from config import presto_host, presto_port, presto_username



# Connect to the Presto database
cursor = presto.connect(host=presto_host, port=presto_port, username=presto_username).cursor()
df = pd.DataFrame()

# Read the SQL query from a file
with open('query.sql', 'r') as f:
    sql = f.read()

# Execute the SQL query
cursor.execute(sql)

# Fetch the results of the query
x = cursor.fetchall()

# Create a DataFrame from the query results
df = pd.DataFrame.from_records(x, columns=[i[0] for i in cursor.description])

# Create an Excel file and write the DataFrame to it
with pd.ExcelWriter('read_sql.xlsx') as writer:
    df.to_excel(writer, sheet_name='Sheet', index=False)

# Open the generated Excel file using the default application
import os
os.startfile('read_sql.xlsx')
