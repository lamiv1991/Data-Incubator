import pandas as pd
import traceback
from collections import Counter

file = 'ArXivHEP-TH_year_month.xlsx'
xl = pd.ExcelFile(file)
df1 = xl.parse('Sheet1')
#print list(df1.columns.values)
Master_set = []
for index,row in df1.iterrows():
    words=row['keywords']
    words = (words.split(","))
    for word in words:
        word.replace('[','')
        word.replace(']','')
        word = word.split(" ")
        for keys in word:
            Master_set.append(keys)
file = open("MasterSet2.txt",'wb+')
file.write(str(Master_set))
file.write("\n")
counts = Counter(Master_set)
file.write(str(counts))
file.close()
file = open("counters.csv",'wb+')
for key,value in counts.iteritems():
    s=str(key)+"\t"+str(value)+"\n"
    file.write(s)
file.close()

