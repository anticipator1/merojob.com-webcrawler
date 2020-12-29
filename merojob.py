import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

from time import sleep
from random import randint
import unicodedata

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }


#url='https://merojob.com/search/?q=web+developer&page=1'
#page=requests.get(url,headers=headers)


#data storage
jobTitle=[]
jobCompany=[]
applyDate=[]
jobAddress=[]
keySkill=[]


#pages = np.arange(1, 4, 1)

def process_job(pages,categoryName):

    #pages = np.arange(1, 4, 1)
    for page in pages: 
            page=requests.get('https://merojob.com/category/'+categoryName+'/?page='+str(page),headers=headers)
            soup=BeautifulSoup(page.content,'html.parser')
            mainDiv=soup.find_all('div',class_='card mt-3 hover-shadow')

            sleep(randint(10,100))

            for div in mainDiv:
                title=div.h1.text.strip()
                jobTitle.append(title)

                companyName=div.h3.text.strip()
                jobCompany.append(companyName)

                address1=div.find('span',{'itemprop':'addressLocality'})
                address=address1.text
                jobAddress.append(address)
    
                date=div.select('p > span')[1].text.strip()
                clean_text=unicodedata.normalize("NFKD",date)

                #skill=div.find_all(class_='badge badge-pill badge-white text-muted').text
                #line=div.find_all('span',class_='badge badge-pill badge-white text-muted')
                #skills =div.find('span',{'itemprop':'skills'})
                #name="  "
                #for skill in skills.children:
                    #print(skill.string)
                        #if skill.name=='span':
                         #   name+=skill.text
                          
                          #  name1=name+"  "
                           # print(name1)
                        #name1="".join(name)
                        #print(name1)
                        #name1=name+"        "

                    
                #keySkill.append(name)
                    #skill2=skill.text
                    #s=skill1.join(skill2)
                
                #print(name1)
                
                #keySkill.append(s)    
                    
                #for div1 in skill:
                    #key=div1.text
                #eySkill.append(div1)
               # keySkill.append(skill)                    

                 # date=div.span.text.strip()
                applyDate.append(clean_text)
       
   # print(jobTitle)
    
    
    
    #print(jobCompany)
    #print(applyDate)
    print(jobAddress)
    
    #print(keySkill)

    merojob=pd.DataFrame({
    'Job Title':jobTitle,
    'Job Company':jobCompany,
    'Apply Date':applyDate,
    'Apply Address':jobAddress
    }) 

    merojob.to_csv('merojob.csv')
            


def choose_jobtype():
    print('Choose the job type you want:')
    print('1)  it-telecommunication')
    print('2)  ngo-ingo-social-work')
    print('3)  marketing-advertising-customer-service')
    print('4)  general-mgmt-administration-operations')
    print('5)  healthcare-pharma-biotech-medical-rd')
    print('6}  banking-insurance-financial-services')
    print('7)  sales-public-relations')
    print('8)  teaching-education')
    print('9)  accounting-finance')
    print('10) journalism-editor-media')
    print('11) construction-engineering-architects')
    print('12) hospitality')
    print('13) creative-graphics-designing')
    print('14) human-resource-org-development')
    print('15) secretarial-front-office-data-entr')
    print('16) architecture-interior-designing')
   

def mainCode():
    choose_jobtype()
    x=input()

    if x=='1':
        pages = np.arange(1,11,1)
        categoryName='it-telecommunication'
        process_job(pages,categoryName)

    elif x=='2':
        pages=np.arange(1,6,1)
        categoryName='ngo-ingo-social-work'
        process_job(pages,categoryName)

    elif x=='3':
        pages=np.arange(1,8,1)
       
        categoryName='marketing-advertising-customer-service'
        process_job(pages,categoryName)
    
    elif x=='4':
        pages=np.arange(1,10,1)
        categoryName='general-mgmt-administration-operations'
        process_job(pages,categoryName)
    
    elif x=='5':
        pages=np.arange(1,7,1)
        categoryName='healthcare-pharma-biotech-medical-rd'
        process_job(pages,categoryName)

    elif x=='6':
        pages=np.arange(1,5,1)
        categoryName='banking-insurance-financial-services'
        process_job(pages,categoryName)

    elif x=='7':
        pages=np.arange(1,5,1)
        categoryName='sales-public-relations'
        process_job(pages,categoryName)

    elif x=='8':
        pages=np.arange(1,5,1)
        categoryName='teaching-education'
        process_job(pages,categoryName)
    
    elif x=='9':
        pages=np.arange(1,6,1)
        categoryName='accounting-finance'
        process_job(pages,categoryName)

    elif x=='10':
        pages=np.arange(1,2,1)
        categoryName='journalism-editor-media'
        process_job(pages,categoryName)
    
    elif x=='11':
        pages=np.arange(1,6,1)
        categoryName='construction-engineering-architects'
        process_job(pages,categoryName)

    elif x=='12':
        pages=np.arange(1,3,1)
        categoryName='hospitality'
        process_job(pages,categoryName)
    elif x=='13':
        pages=np.arange(1,3,1)
        categoryName='creative-graphics-designing'
        process_job(pages,categoryName)
    
    elif x=='14':
        pages=np.arange(1,3,1)
        categoryName='human-resource-org-development'
        process_job(pages,categoryName)

    elif x=='15':
        pages=np.arange(1,4,1)
        categoryName='secretarial-front-office-data-entr'
        process_job(pages,categoryName)

    elif x=='16':
        pages=np.arange(1,2,1)
        categoryName='architecture-interior-designing'
        process_job(pages,categoryName)

    else:
        print('please select from the above options')

    

mainCode()


"""
for page in pages: 
    page=requests.get('https://merojob.com/industry/e-commerce-e-business/?page='+str(page),headers=headers)
    soup=BeautifulSoup(page.content,'html.parser')


    mainDiv=soup.find_all('div',class_='card mt-3 hover-shadow')

    sleep(randint(2,10))

    for div in mainDiv:
        title=div.h1.text.strip()
        jobTitle.append(title)

        companyName=div.h3.text.strip()
        jobCompany.append(companyName)
    
        date=div.select('p > span')[1].text.strip()
        clean_text=unicodedata.normalize("NFKD",date)
 
   # date=div.span.text.strip()
        applyDate.append(clean_text)
       
     

print(jobTitle)
print(jobCompany)
print(applyDate)
#print(applyDate)
"""
    