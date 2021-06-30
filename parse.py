import json
import pandas as pd

all = []
for i in range(1, 21):
    with open("page" + str(i) + ".txt") as file:
        content = file.read()
    data = json.loads(content)
    values = data["value"]
    for v in values:
        name = v["displayName"]
        mail = v["mail"]
        other = v["userPrincipalName"]
        all.append([name, mail, other])
df = pd.DataFrame(all, columns = ['Name', 'Mail', 'Other'])
df.to_csv("output.csv", encoding='utf8')
