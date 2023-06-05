import pandas as pd
df = pd.read_csv('./data_traffic/label_names.csv')
id = df['ClassId']
names = df['SignName']
for i in range(0, len(id)):
    ClassName = {id[i]:names[i]}
    print(ClassName)