import requests
from bs4 import BeautifulSoup
import time 

know_skills=input('Please provide your skillsets in comma separated way')
know_skills=know_skills.split(",")

def scrap_jobs():
    #Read the HTML content of the webpage

    html_text=requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=").text
#print(html_text)

#scrape the data to fetch the results- beautifulsoup
    soup = BeautifulSoup (html_text, 'lxml')

#print(soup.prettify())

#print(date_posted)


    jobs=soup.find_all('li', class_="clearfix job-bx wht-shd-bx")

    for job in jobs :
        date_posted=job.find("span", class_="sim-posted").text.strip()
        skills= job.find("span", class_="srp-skills").text.replace(" ","").strip().split(",")
        if 'few' in date_posted and set(know_skills) & set(skills):
            company_name= job.find("h3", class_="joblist-comp-name").text.replace(" ","").strip()
            jd=job.header.h2.a["href"]
    


#print(company_name)
#print(skills)
            print(f'''
Company Name : {company_name}
Skills needed : {skills}
Date Published: {date_posted}
jd: {jd}
''')
        
            print("-------------------------------")



if __name__=='__main__':
    while True:
        scrap_jobs()
        print("Waiting for 5 Seconds")
        time.sleep(5)



    



