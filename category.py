import requests
import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import os


def chrome_driver():
    """Initialize Chrome driver"""
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


def scrape_category(driver, url, category_name):
    """Scrape and save category to separate CSV"""
    
    category_list = []
    
    res = requests.get(url)
    print(f"Status: {res.status_code}")
    
    driver.get(url)
    time.sleep(12)
    
    source_code = driver.page_source
    soup = BeautifulSoup(source_code, 'html.parser')
    
    trainer_info = soup.find_all('div', class_="pl-4")
    
    for info in trainer_info:
        trainer = {
            'name': None,
            'website': None,
            'email': None,
            'contact': None
        }
        
        name = info.find('h3').text.strip() if info.find('h3') else None
        trainer['name'] = name
        
        links = info.find_all('a', class_='flex items-center gap-2 text-sm sm:text-xs lg:text-sm mb-1')
        
        for link in links:
            href = link.get('href', '')
            
            if href.startswith('http'):
                trainer['website'] = href
            elif href.startswith('mailto:'):
                trainer['email'] = href.replace('mailto:', '').strip()
            elif href.startswith('tel:'):
                trainer['contact'] = href.replace('tel:', '').strip()
        
        trainers_list.append(trainer)
    
    df = pd.DataFrame(trainers_list)
    filename = f"{category_name}.csv"
    df.to_csv(filename, index=False)
    
    print(f"✓ Saved {len(df)} records to {filename}")
    return df


# Scrape multiple categories
driver = chrome_driver()

categories = {
    'cleaners': 'https://ukbusinessportal.co.uk/category/cleaning/',
    'electricians': 'https://ukbusinessportal.co.uk/category/electricians/'
}

for category_name, url in categories.items():
    print(f"\nScraping {category_name}...")
    scrape_category(driver, url, category_name)

driver.quit()