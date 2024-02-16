from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.common.by import By


lis = []
def web_scrabing(num_iter , job):
    jobs =[]
    ## declare driver_chrome
    driver = webdriver.Chrome()
    url = 'https://www.glassdoor.com/Job/jobs.htm?sc.keyword="' + job + '"&locT=C&locId=1147401&locKeyword=San%20Francisco,%20CA&jobType=all&fromAge=-1&minSalary=0&includeNoSalaryJobs=true&radius=100&cityId=-1&minRating=0.0&industryId=-1&sgocId=-1&seniorityType=all&companyId=-1&employerSizes=0&applicationType=0&remoteWorkType=0'
    driver.get(url)
    #load page
    time.sleep(5)
    #create Loop for load all Jobs from page
    for i in range(num_iter):
        #Test for the "Sign Up" prompt and get rid of it.
        try:
            driver.find_element(By.CLASS_NAME,'CloseButton').click()
        except:
            pass
        time.sleep(1) # for cancel the sign up page
        #Click to 'See More' button
        try:
            driver.find_element(By.CLASS_NAME , 'JobsList_buttonWrapper__haBp5').click()
        except:
            break

        time.sleep(3) #very important step -> beacuse waite the new jops
        try:
            driver.find_element(By.CLASS_NAME,'CloseButton').click()
        except:
            pass


        numbers = 0
    all_jobs = driver.find_elements(By.CLASS_NAME , 'JobsList_jobListItem__JBBUV ')
    for job in all_jobs:
        try:
            driver.find_element(By.CLASS_NAME,'CloseButton').click()
        except:
            pass
        time.sleep(1)
        # open each Job in the list
        job.click()
        time.sleep(1) # for wait the loading
        try:
            driver.find_element(By.CLASS_NAME,'CloseButton').click()
        except:
            pass
        try:
            driver.find_element(By.CLASS_NAME,'JobDetails_showMore__j5Z_h').click()
        except:
            continue
        time.sleep(1)
        ok_scrabing = False
        count = 0
        while  count < 2 and ok_scrabing == False:
            try:
                company_name = driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[3]/div[2]/div[2]/div[1]/header/div[1]/a/div[2]/span').text                         
                location = driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[3]/div[2]/div[2]/div[1]/header/div[1]/div[2]').text
                job_title = driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[3]/div[2]/div[2]/div[1]/header/div[1]/div[1]').text
                job_description = driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[3]/div[2]/div[2]/div[1]/section/div[1]/div[1]/div').text
                try:
                    Average_salary_estimate = driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[3]/div[2]/div[2]/div[1]/section/section[1]/div/div[2]/div[1]/div[1]').text
                except NoSuchElementException:
                    Average_salary_estimate = "-1" #You need to set a "not found value. It's important."
                try:
                    rating = driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[3]/div[2]/div[2]/div[1]/section/section[3]/div/div/div/div/div').text
                except NoSuchElementException:
                    rating = '-1' #You need to set a "not found value. It's important."
                try:
                    industry = driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[3]/div[2]/div[2]/div[1]/section/section[2]/div/div/div[4]').text
                except NoSuchElementException:
                    industry = '-1'
                try:
                    sector = driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[3]/div[2]/div[2]/div[1]/section/section[2]/div/div/div[5]/div').text
                except NoSuchElementException:
                    sector = '-1'
                #lis.append({"Job Title" : job_title,"Job Description" : job_description,"Company Name" : company_name,"Location" : location})
                # jobs.append({"Job Title" : job_title,"Salary Estimate" : Average_salary_estimate,"Rating" : rating,"Company Name" : company_name,
                # "Location" : location,
                # "Industry" : industry,
                # "Sector" : sector,"Job Description" : job_description})
                lis.append({"Job Title" : job_title,"Salary Estimate" : Average_salary_estimate,"Rating" : rating,"Company Name" : company_name,
                "Location" : location,
                "Industry" : industry,
                "Sector" : sector,"Job Description" : job_description})
                numbers = numbers +1
                print({"# --> ":numbers,"Job Title" : job_title,"Salary Estimate" : Average_salary_estimate,"Rating" : rating,"Company Name" : company_name,
                "Location" : location,
                "Industry" : industry,
                "Sector" : sector,"Job Description" : job_description})
                ok_scrabing = True
            except:
                time.sleep(1)
            count = count +1
if __name__ == '__main__':
    web_scrabing(100,'devops')