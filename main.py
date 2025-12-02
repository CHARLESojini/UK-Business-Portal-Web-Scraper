import requests
import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import os

def chrome_driver():
    driver_path = ChromeDriverManager().install()
    print("Driver path:", driver_path)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    
    if not os.access(driver_path, os.X_OK):
        print("❌ Not executable. Trying to locate the real binary.")
        for root, dirs, files in os.walk(os.path.dirname(driver_path)):
            for file in files:
                if "chromedriver" in file and not file.endswith(".chromedriver"):
                    potential_path = os.path.join(root, file)
                    print("✅ Found likely candidate:", potential_path)
                    driver_path = potential_path
                    break

    return webdriver.Chrome(service=ChromeService(driver_path), options=options)


driver = chrome_driver()

# Initialize lists
trainer_names = []
trainer_websites = []
trainer_emails = []
trainer_contacts = []

# URL
url = "https://ukbusinessportal.co.uk/category/personal-trainer/"

res = requests.get(url)
print(res.status_code)

driver.get(url)
time.sleep(12)

source_code = driver.page_source
soup = BeautifulSoup(source_code, 'html.parser')

# Extract trainers
trainer_info = soup.find_all('div', class_="pl-4")

for info in trainer_info:
    # NAME
    name = info.find('h3').text.strip() if info.find('h3') else None
    trainer_names.append(name)
    
    # CONTACT LINKS (all have same class, different href)
    links = info.find_all('a', class_='flex items-center gap-2 text-sm sm:text-xs lg:text-sm mb-1')
    
    for link in links:
        href = link.get('href', '')
        
        # WEBSITE (starts with http)
        if href.startswith('http'):
            trainer_websites.append(href)
        
        # EMAIL (starts with mailto:)
        elif href.startswith('mailto:'):
            email = href.replace('mailto:', '').strip()
            trainer_emails.append(email)
        
        # PHONE (starts with tel:)
        elif href.startswith('tel:'):
            phone = href.replace('tel:', '').strip()
            trainer_contacts.append(phone)

# Create DataFrame
data = {
    'name': trainer_names,
    'website': trainer_websites,
    'email': trainer_emails,
    'contact': trainer_contacts
}

df = pd.DataFrame(data)
df.to_csv('personal_trainers.csv', index=False)

print(f"Total trainers scraped: {len(df)}")
print(df.head())

