import pandas as pd
import os

file_path = 'C:/Users/do0ob/OneDrive/바탕 화면/english-hashtag-crawl/crawled2/

for file_name in file_list :
    print(file_name)
    
    file_path = 'C:/Users/do0ob/OneDrive/바탕 화면/english-hashtag-crawl/crawled2/' + file_name
    df = pd.read_csv (file_path)
    
    df2 = df.apply(pd.value_counts).fillna(0).astype(int)
    df2["RowSum"] = df2.sum(axis=1)
    
    df3 = pd.DataFrame()
    df3 = df2['RowSum']
    
    save_file_name = path + 'aligned-' + file_name
    print(save_file_name)
    df3.to_csv(save_file_name,
               sep=',',
               na_rep='NaN',
               header = True
              )
