from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from jobfinder.models import JobListing
import pandas as pd
import time


def selenium_init():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    service = Service(
        r"C:\Users\yashg\Desktop\Projects\test_folder\chromedriver-win64\chromedriver.exe")  # Update with your ChromeDriver path
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def scrape_jobs(driver,url):
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

        job = {
            'Job Title': job_title,
            'Company Name': company_name,
            'Job Details': job_details
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

def jobs(profile):
    driver = selenium_init()
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
    jobs = scrape_jobs(driver, url)
    print(jobs)
    JobListing.objects.filter(job_type=profile).delete()
    job_listings = [
        JobListing(
            job_title=row['Job Title'],
            job_type=profile,
            company_name=row['Company Name'],
            job_details=row['Job Details']
        )
        for index, row in jobs.iterrows()
    ]

    JobListing.objects.bulk_create(job_listings)