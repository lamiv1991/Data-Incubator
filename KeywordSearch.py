import pandas as pd
import traceback
from collections import Counter
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import operator
Input = raw_input("Enter a keyword ")
Input = Input.lower()
Inputs = Input.split(" ")
length = len(Inputs)
file = 'ArXivHEP-TH_year_month.xlsx'
xl = pd.ExcelFile(file)
df1 = xl.parse('Sheet1')
#print list(df1.columns.values)
Master_set = []
Authors = []
years = []
i=0
for index,row in df1.iterrows():
    words=row['keywords']
    Words = words.lower()
    words = (words.split(","))
    for word in words:
        word.replace('[','')
        word.replace(']','')
        word = word.split(" ")
        for keys in word:
            Master_set.append(keys)
        result = False
    for inputs in Inputs:
        if inputs in Words:
            result = True
            #print "True"
        else:
            result = False
            #print "False"
            break
    if result==True:
        r = row['authors']
        r = r.split(',')
        for XX in r:
            XX = XX.replace('[','')
            XX = XX.replace(']','')
            Authors.append(str(XX.encode('ascii', 'ignore')))
        XX=row['year']
        years.append(str(XX))   
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
counts_author = Counter(Authors)
counts_year = Counter(years)
#print counts_author,counts_year
i=0
X=[]
Y=[]
for w in sorted(counts_author, key=counts_author.get, reverse=True):
   X.append(w)
   Y.append(counts_author[w])
   i=i+1
   if(i>6):
       break
y_pos = np.arange(len(Y))
print Y
plt.subplot(2,1,1)
plt.bar(y_pos, Y, align='center', alpha=0.5)
plt.xticks(y_pos, X)
plt.ylabel('Usage')
Label = "Author vs Occurances for " + Input 
plt.title(Label)
i=0
X=[]
Y=[]
for w in sorted(counts_year, key=counts_year.get, reverse=True):
   X.append(w)
   Y.append(counts_year[w])
   i=i+1
   if(i>6):
       break
y_pos = np.arange(len(Y))
print Y
plt.subplot(2,1,2)
plt.bar(y_pos, Y, align='center', alpha=0.5)
plt.xticks(y_pos, X)
plt.ylabel('Usage')
Label = "Year vs Occurances for " + Input 
plt.title(Label)
plt.show()


