import zipfile
import datetime
import requests
import os 
import shutil

#+++++++++++++++++++++++++++++++++++++++++++Переменные++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
token = ''
chat_id = ''
a=0
#+++++++++++++++++++++++++++++++++++++++++++Функции+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def News ():
    content=[]
    now = datetime.date.today()
    Delta = datetime.timedelta(1)
    data = now - Delta
    
    r= requests.get(url=url)
    f=open(r'file_bdseo.zip',"wb")
    f.write(r.content) 
    f.close()
    z = zipfile.ZipFile("file_bdseo.zip", 'r')
    z.extractall()
    z.close()
    os.remove("file_bdseo.zip")
    file ='day\\ru-'+str(data)+'_23_55_00.tsv' 
   
    return content

def posting (kontent,token,chat_id):
    url =  
    requests.get(url=url)

 #+++++++++++++++++++++++++++++++++++++++++++Тело_ПО++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

