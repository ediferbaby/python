import requests
import re

for i in range(0,10):
    j = i*20
    url = 'https://yuedu.baidu.com/rank/hotsale?pn='+str(j)
    r = requests.get(url)
    
   
    print('第'+str(i+1)+'页')
    print(url)
    
  
    # print (r.status_code)
    r.encoding = r.apparent_encoding
    # print(r.encoding)

    pat = '<span class="title">(.*?)</span>'
    til = re.compile(pat,re.S).findall(r.text)
    print(til)
    print('----------------')