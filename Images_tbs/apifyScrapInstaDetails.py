import requests
import pandas as pd
import json

wb = pd.read_excel('./fear_with_username.xlsx')
wb = wb.iloc[c:, ]
#4594
print(len(wb.columns))

#wb.insert(1, 'en',"", allow_duplicates=True)
wb.insert(14, 'followersCount',"", allow_duplicates=True)
wb.insert(15, 'followsCount',"", allow_duplicates=True)
wb.insert(16, 'bio',"", allow_duplicates=True)
wb.insert(17, 'postsCount',"", allow_duplicates=True)


print(wb.columns)
i=0
try: 
  for index, row in wb.iterrows():
    i=i+1   
    user = wb.loc[index, "ownerUsername"]
    r = user#requests.get(row['url']).text
    #start = '(@'
    end = ') on Instagram:'
    
    indexS = user.index(end)

   
    user = user[0:indexS]
    wb.loc[index, "ownerUsername"] = user

    #print(indexS)
    #print(user)
      #wb.loc[index, "ownerUsername"] = user

      # print(wb.loc[index, "ownerUsername"])
      #url = 'https://www.instagram.com/' + user
    id1 = 'J2pkCAyPJau77kp8J'
    id2 = 'bigGq4McRjWtKAs6AHNiwN4iJ'
    s = requests.get('https://api.apify.com/v2/actor-tasks/'+ id1+'/input?token='+id2+'&ui=1').json()
      #print(s)
    s['search'] = user
    print(i)
    u = requests.put('https://api.apify.com/v2/actor-tasks/'+id1+'/input?token='+id2+'&ui=1', json=s)
    v = requests.post('https://api.apify.com/v2/actor-tasks/'+id1+'/run-sync?token='+id2+'&ui=1', json = s)
    print(v)
    t = requests.get('https://api.apify.com/v2/actor-tasks/'+id1+'/runs/last/dataset/items?token='+id2+'&ui=1').json()
      #print(t)
    if(t!=[]):
        #print(t)
        wb.loc[index, "followersCount"] = t[0]["followersCount"]
        wb.loc[index, "followsCount"] = t[0]["followsCount"]
        wb.loc[index, "postsCount"] = t[0]["postsCount"]
        wb.loc[index, "bio"] = t[0]["biography"]
   
    #print(t[0]["followersCount"])

      
    wb.to_excel('fearscrappeddataset'+str(c)+'.xlsx', sheet_name='sheet1', index=False)
     

      #start = '"edge_followed_by":{"count":'
      #end = '},"followed_by_viewer"'

      #print (r[r.find(start)+len(start):r.rfind(end)])
      #row['followersCount'] = (r[r.find(start)+len(start):r.rfind(end)])

except Exception as e : print(e)
 
    #pass#
    
