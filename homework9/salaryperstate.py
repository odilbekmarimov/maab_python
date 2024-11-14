import sqlite3
import pandas as pd
from openpyxl import load_workbook

with sqlite3.connect('population.db') as con:
    df = pd.read_sql("SELECT * FROM population", con = con)

state_group = df.groupby('state')
population_count = state_group.size()
average_salary = state_group['salary'].mean()
median_salary = state_group['salary'].median()

total_population = len(df)
percentage_population = (population_count / total_population) * 100

analysis_df = pd.DataFrame({
    'State': population_count.index,
    'Percentage': percentage_population.values,
    'Average Salary': average_salary.values,
    'Median Salary': median_salary.values,
    'Number of population': population_count.values
})

file_path = "population salary analysis.xlsx"
try:
    workbook = load_workbook(file_path)
    if "State" not in workbook.sheetnames:
        writer = pd.ExcelWriter(file_path, engine="openpyxl", mode="a")
        analysis_df.to_excel(writer, sheet_name="State", index=False, startrow=1, header=False)
        writer.close()
    else:
        with pd.ExcelWriter(file_path, engine="openpyxl", mode="a", if_sheet_exists="overlay") as writer:
            analysis_df.to_excel(writer, sheet_name="State", index=False, startrow=1, header=False)
            
except FileNotFoundError:
    with pd.ExcelWriter(file_path, engine="openpyxl") as writer:
        analysis_df.to_excel(writer, sheet_name="State", index=False, startrow=1, header=False)

print("Data exported to {file_path}")
