from arxivscraper import Scraper
import pandas as pd
from rake_nltk import Rake
import traceback
r = Rake()
#scraper = Scraper(category='physics:cond-mat', date_from='2017-05-27',date_until='2017-06-07')
scraper = Scraper(category='physics:hep-th', date_from='2016-01-27',date_until='2018-06-07')
output = scraper.scrape()
file_name = open("Data_sep.txt",'wb+')
cols = ('id', 'title', 'categories', 'abstract', 'doi', 'created', 'updated', 'authors','keywords','year','month')
file_name.write("id\ttitle\tcategories\tabstract\tdoi\tcreated\tupdated\tauthors\tkeywords\tyear\tmonth")
file_name.write("\n")
df = pd.DataFrame(columns=cols)
for paper in output:
    try:
        r.extract_keywords_from_text(paper['abstract'])
        keywords = r.get_ranked_phrases()
        paper['keywords'] = str(keywords)
        d= str(paper['created'])
        d = d.split("-")
        year = d[0]
        month = d[1]
        s=str(paper['id']).encode('ascii', 'ignore').replace(";","")+"\t"+str(paper['title']).encode('ascii', 'ignore').replace(";","")+"\t"+str(paper['categories']).encode('ascii', 'ignore').replace(";","")+"\t"+str(paper['abstract']).encode('ascii', 'ignore').replace(";","")+"\t"+str(paper['doi']).encode('ascii', 'ignore').replace(";","")+"\t"+str(paper['created'])+"\t"+str(paper['updated'])+"\t"+str(paper['authors'])+"\t"+str(paper['keywords'].encode('ascii', 'ignore').replace(";",""))+"\t"+str(year)+"\t"+str(month)
        file_name.write(s)
        file_name.write("\n")
    except:
        print traceback.print_exc()
        pass
"""
for index, row in df.iterrows():
    text = row['abstract']
    r.extract_keywords_from_text(text)
    keywords = r.get_ranked_phrases()
    df['keywords'] = str(keywords)
"""
#df.to_csv(file_name, sep=';')
#print (df.shape)
file_name.close()
