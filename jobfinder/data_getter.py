from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from jobfinder.models import JobListing
import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def selenium_init():
    # Get the directory of the current file
    current_dir = os.path.dirname(__file__)

    # Construct the path to chromedriver.exe
    chromedriver_path = os.path.join(current_dir, '..', 'chromedriver-win64', 'chromedriver.exe')

    # If needed, convert to an absolute path
    absolute_chromedriver_path = os.path.abspath(chromedriver_path)
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    # chrome_options.add_argument('--window-size=1920,1080')
    service = Service(absolute_chromedriver_path)  # Update with your ChromeDriver path
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def scrape_naukri_jobs(driver,url):
    driver.get(url)
    jobs = []
    # WebDriverWait(driver, 10).until(
    # EC.presence_of_element_located((By.ID, 'element_id')))
    time.sleep(5)
    # Wait for the job listings to load
    job_tuple_element = driver.find_elements(By.CLASS_NAME, 'sjw__tuple')
    # print(job_tuple_element)
    for job_listing in job_tuple_element:
        job_title_element = job_listing.find_element(By.CLASS_NAME, 'row1')
        job_title = job_title_element.text.strip() if job_title_element else 'N/A'

        company_name_element = job_listing.find_element(By.CLASS_NAME, 'row2')
        company_name = company_name_element.text.strip() if company_name_element else 'N/A'

        job_details_element = job_listing.find_element(By.CLASS_NAME, 'row4')
        job_details = job_details_element.text.strip() if job_details_element else 'N/A'

        link_element = job_listing.find_element(By.TAG_NAME, 'a')
        job_link = link_element.get_attribute('href') if link_element else 'N/A'

        job = {
            'Job Title': job_title,
            'Company Name': company_name,
            'Job Details': job_details,
            'Job Link': job_link
        }
        jobs.append(job)
    # print(jobs)
    df_jobs = pd.DataFrame(jobs)
    name_list=df_jobs.iloc[:,1]
    for i in range(0,len(name_list)-1):
        a=name_list[i].split("\n")
        name_list[i]=a[0]
    df_jobs["Company Name"]=name_list
    driver.quit()
    return df_jobs
    # return jobs

def get_naukri_jobs(driver,profile):
    if(profile=="Software Developer"):
        url = 'https://www.naukri.com/software-developer-jobs'
    elif (profile=="UI UX"):
        url = 'https://www.naukri.com/ui-ux-jobs'
    elif (profile == "Graphic Designer"):
        url = 'https://www.naukri.com/graphic-designer-jobs'
    elif (profile == "App Developer"):
        url = 'https://www.naukri.com/app-developer-jobs'
    elif (profile == "AI ML"):
        url = 'https://www.naukri.com/machine-learning-jobs'
    # url="https://www.naukri.com/software-developer-jobs"
    # print(driver)
    naukri_jobs = scrape_naukri_jobs(driver, url)
    # print(naukri_jobs)
    return naukri_jobs


def get_indeed_jobs(driver,profile):
    print(profile)
    if(profile=="Software Developer"):
            url = 'https://in.indeed.com/jobs?q=software+developer'
    elif (profile=="UI UX"):
        url = 'https://in.indeed.com/jobs?q=ui-ux-jobs'
    elif (profile == "Graphic Designer"):
        url = 'https://in.indeed.com/jobs?q=graphic-designer-jobs'
    elif (profile == "App Developer"):
        url = 'https://in.indeed.com/jobs?q=app-developer-jobs'
    elif (profile == "AI ML"):
        url = 'https://in.indeed.com/jobs?q=machine-learning-jobs'
    naukri_jobs = scrape_jobs(driver, url)
    print(naukri_jobs)

def scrape_indeed_jobs(driver,url):
    driver.get(url)
    jobs = []
    time.sleep(5)
    # Wait for the job listings to load
    job_tuple_element = driver.find_elements(By.CLASS_NAME, 'sjw__tuple')
    # print(job_tuple_element)
    for job_listing in job_tuple_element:
        job_title_element = job_listing.find_element(By.CLASS_NAME, 'row1')
        job_title = job_title_element.text.strip() if job_title_element else 'N/A'

        company_name_element = job_listing.find_element(By.CLASS_NAME, 'row2')
        company_name = company_name_element.text.strip() if company_name_element else 'N/A'

        job_details_element = job_listing.find_element(By.CLASS_NAME, 'row4')
        job_details = job_details_element.text.strip() if job_details_element else 'N/A'

        link_element = job_listing.find_element(By.TAG_NAME, 'a')
        job_link = link_element.get_attribute('href') if link_element else 'N/A'

        job = {
            'Job Title': job_title,
            'Company Name': company_name,
            'Job Details': job_details,
            'Job Link': job_link
        }
        print(job)
        jobs.append(job)
    # print(jobs)
    df_jobs = pd.DataFrame(jobs)
    name_list=df_jobs.iloc[:,1]
    for i in range(0,len(name_list)-1):
        a=name_list[i].split("\n")
        name_list[i]=a[0]
    df_jobs["Company Name"]=name_list
    driver.quit()
    return df_jobs
    # return jobs

def jobs(profile):
    JobListing.objects.filter(job_type=profile).delete()
    driver = selenium_init()
    naukri_jobs=get_naukri_jobs(driver,profile)
    # driver = selenium_init()
    # indeed_jobs=get_indeed_jobs(profile, driver)
    job_listings = [
        JobListing(
            job_title=row['Job Title'],
            job_type=profile,
            company_name=row['Company Name'],
            job_details=row['Job Details'],
            job_link=row['Job Link'],
            job_origin="Naukri",
        )
        for index, row in naukri_jobs.iterrows()
    ]

    JobListing.objects.bulk_create(job_listings)