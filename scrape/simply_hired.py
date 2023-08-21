from bs4 import BeautifulSoup
from selenium import webdriver
from config import config
import time

def simplyHired(searchString, noOfPages):
    driver = webdriver.Chrome(config.chromeDriverPath)
    URL = "https://www.simplyhired.com/search?q=" + searchString
    driver.get(URL)
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    jobListUl=soup.find(id='job-list')
    jobHeaderList = jobListUl.find_all('h3')
    jobURLList=[]
    for jobHeader in jobHeaderList:
        jobURLList.append("https://www.simplyhired.com"+jobHeader.find('a').get('href'))
    
    jobURLList = jobURLList[:noOfPages]
    skills=[]
    for jobURL in jobURLList:
        driver.get(jobURL)
        time.sleep(2)
        soupJob = BeautifulSoup(driver.page_source, 'html.parser')
        skillDiv=soupJob.find(string="Qualifications").parent.parent
        skillLiList=skillDiv.find_all('li')
        for skillLi in skillLiList:
            skills.append(skillLi.text)
    driver.close()
    return skills