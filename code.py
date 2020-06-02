# --------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Code starts here
df=pd.read_csv(path)
df['state']=df['state'].apply(lambda x:x.lower())
df['total']=df['Jan']+df['Feb']+df['Mar']
sum_row=df[['Jan','Feb','Mar','total']].sum()
df_final = df.append(sum_row,ignore_index=True)
# Code ends here


# --------------
import requests

# Code starts here
url='https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations'
response=requests.get(url)
df1=pd.read_html(response.content)[0]
df1.columns=df1.iloc[11]
df1=df1[12:]
df1['United States of America']=df1['United States of America'].apply(lambda x:x.strip())
print(df1)
# Code ends here


# --------------
df1['United States of America'] = df1['United States of America'].astype(str).apply(lambda x: x.lower())
df1['US'] = df1['US'].astype(str)
# Code starts here
mapping=df1.set_index('United States of America')['US'].to_dict()
df_final.insert(6,'abbr',df_final['state'].apply(lambda x:mapping[x] if x in mapping else ''))
#df_final['abbr']=df_final['state'].apply(lambda x:mapping[x] if x in mapping else '')
print(df_final)
# Code ends here


# --------------
# Code stars here
df_final.replace(df_final.iloc[6],df_final[df_final['state']=='tenessee'].replace('','TN'),inplace=True)
df_final.replace(df_final.iloc[6],df_final[df_final['state']=='mississipi'].replace('','MS'),inplace=True)
# Code ends here


# --------------
# Code starts here

# Calculate the total amount
df_sub=df_final[["abbr", "Jan", "Feb", "Mar", "total"]].groupby("abbr").sum()
print(df_sub.shape)
# Add the $ symbol
formatted_df = df_sub.applymap(lambda x: "${:,.0f}".format(x))

# Code ends here


# --------------
# Code starts here
sum_row=df[['Jan','Feb','Mar','total']].sum()
df_sub_sum=df_sub.append(sum_row,ignore_index=True)
print(df_sub_sum)
df_sub_sum=df_sub_sum.apply(lambda x:'$'+str(x))
print(df_sub_sum)
final_table=formatted_df.append(df_sub_sum,ignore_index=True)
# Code ends here


# --------------
# Code starts here
fig1, ax1 = plt.subplots()
ax1.pie(df_sub['total'], labels=df_sub.index,autopct='%1.1f%%',shadow=True, startangle=90)
ax1.axis('equal')
plt.show()
# Code ends here


