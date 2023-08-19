import os
import json
import pandas as pd

data = []
for i in os.listdir("/expense-data/"):
    with open("/expense-data/" + i, "r") as json_file:
        data += json.load(json_file)

df = pd.DataFrame(data)
if os.path.exists("/expense-data/collated-expenses.csv"):
    os.remove("/expense-data/collated-expenses.csv")
df.to_csv("/expense-data/collated-expenses.csv", index=False)
