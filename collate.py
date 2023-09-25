import os
import csv
import json
import sqlite3
import pandas as pd

data = []
for i in os.listdir("/expense-data/"):
    with open("/expense-data/" + i, "r") as json_file:
        data += json.load(json_file)
df = pd.DataFrame(data)

csv_file_path = '/expense-data/collated-expenses.csv'
# db_file_path = '/expense-data/database.db'

if os.path.exists(csv_file_path):
    os.remove(csv_file_path)
# if os.path.exists(db_file_path):
#     os.remove(db_file_path)

df.to_csv(csv_file_path, index=False)

# conn = sqlite3.connect(db_file_path)
# cursor = conn.cursor()
# create_table_query = '''
# CREATE TABLE IF NOT EXISTS transactions (
#     date TEXT,
#     category TEXT,
#     amount REAL,
#     note TEXT
# )
# '''
# cursor.execute(create_table_query)
# conn.commit()

# with open(csv_file_path, 'r') as csvfile:
#     csvreader = csv.DictReader(csvfile)
#     for row in csvreader:
#         insert_query = '''
#         INSERT INTO transactions (date, category, amount, note)
#         VALUES (?, ?, ?, ?)
#         '''
#         values = (
#             row['date'],
#             row['category'],
#             float(row['amount']),
#             row['note']
#         )
#         cursor.execute(insert_query, values)
#     conn.commit()

# conn.close()
