# UK Business Portal Web Scraper

A Python-based web scraper that extracts professional information from the UK Business Portal. This tool collects contact details, websites, and email addresses for various service categories including personal trainers, cleaners, and electricians.

## 📋 Project Overview

This project automates the extraction of business information from [ukbusinessportal.co.uk](https://ukbusinessportal.co.uk) using Selenium and BeautifulSoup. The scraper navigates through category pages, extracts structured data, and exports results to CSV files for further analysis.

## ✨ Features

- **Multi-category Support**: Scrape different professional categories with a single configuration
- **Headless Browser Automation**: Uses Selenium with headless Chrome for JavaScript-rendered content
- **Automatic ChromeDriver Management**: Handles driver installation and path detection
- **Structured Data Extraction**: Captures name, website, email, and phone contact information
- **CSV Export**: Saves extracted data in organized CSV format
- **Error Handling**: Includes binary execution checks and fallback mechanisms for driver paths

## 🛠️ Requirements

- Python 3.7+
- Google Chrome or Chromium browser

## 📦 Installation

1. **Clone or download this project**
   ```bash
   git clone <repository-url>
   cd uk-business-portal-scraper
   ```

2. **Install required Python packages**
   ```bash
   pip install selenium pandas beautifulsoup4 requests webdriver-manager
   ```

## 🚀 Usage

### Option 1: Scrape Multiple Categories (Recommended)

Use `category.py` to scrape multiple service categories:

```bash
python category.py
```

By default, this scrapes:
- Cleaners
- Electricians

To add or modify categories, edit the `categories` dictionary in `category.py`:

```python
categories = {
    'cleaners': 'https://ukbusinessportal.co.uk/category/cleaning/',
    'electricians': 'https://ukbusinessportal.co.uk/category/electricians/',
    'plumbers': 'https://ukbusinessportal.co.uk/category/plumbers/'
}
```

### Option 2: Scrape Personal Trainers (Single Category)

Use `main.py` for a focused scrape of personal trainers:

```bash
python main.py
```

This creates `personal_trainers.csv` with trainer information.

## 📂 Project Structure

```
├── main.py                    # Single-category scraper (personal trainers)
├── category.py                # Multi-category scraper
├── personal_trainers.csv      # Sample output (personal trainers)
├── cleaners.csv               # Sample output (cleaners)
├── electricians.csv           # Sample output (electricians)
└── README.md                  # This file
```

## 📊 Output Format

Each CSV file contains the following columns:

| Column | Description |
|--------|-------------|
| `name` | Business or professional name |
| `website` | Business website URL |
| `email` | Contact email address |
| `contact` | Phone number |

**Example:**
```csv
name,website,email,contact
John's Cleaning Services,https://johnscleaning.co.uk,john@johnscleaning.co.uk,+44 1234 567890
```

## 🔧 Key Functions

### `chrome_driver()`
Initializes a headless Chrome WebDriver with:
- Automatic driver installation via webdriver-manager
- Binary execution validation
- Fallback path detection for driver executables
- Sandbox and headless mode options for robust execution

### `scrape_category(driver, url, category_name)`
Scrapes a single category page:
- Loads the URL via Selenium (handles JavaScript)
- Waits 12 seconds for dynamic content to load
- Parses HTML with BeautifulSoup
- Extracts contact information from structured divs
- Exports results to CSV

## ⏱️ Performance Notes

- **Page Load Wait Time**: 12 seconds per page (adjustable in code)
- **Headless Mode**: Significantly faster than UI rendering
- **Single-threaded**: Processes one category at a time; modify code for parallel processing if needed

## 🛡️ Ethical Considerations

- **Respect robots.txt**: Always check the website's robots.txt before scraping
- **Rate Limiting**: Current script waits 12 seconds per page to avoid server strain
- **Terms of Service**: Ensure scraping complies with the website's terms of service
- **Data Privacy**: Handle collected personal data responsibly and in compliance with GDPR

## 🐛 Troubleshooting

### Issue: "Not executable. Trying to locate the real binary."
The ChromeDriver path validation fails but the script attempts to find the executable. This is usually handled automatically by the fallback mechanism.

**Solution**: Ensure Chrome is installed on your system.

### Issue: Timeout or incomplete data
The 12-second wait time may not be sufficient for slow connections.

**Solution**: Increase `time.sleep(12)` to a higher value (e.g., 15 or 20 seconds).

### Issue: No data extracted
The HTML structure of the target website may have changed.

**Solution**: 
1. Inspect the website to verify the CSS classes (`pl-4`, `flex items-center gap-2`)
2. Update selectors in the code if needed

## 🚀 Future Improvements

- Add pagination support for categories with many listings
- Implement multi-threading for faster multi-category scraping
- Add retry logic for failed requests
- Create a database backend (SQLite/PostgreSQL) for data storage
- Add CLI arguments for flexible category selection
- Implement logging for better debugging and monitoring
- Add data validation and cleaning pipeline

## 📝 License

This project is provided as-is for educational and personal use.

## 💡 Contributing

Contributions are welcome! Feel free to:
- Report bugs or issues
- Suggest improvements
- Add new features or categories
- Improve documentation

---

**Created by**: Chima  
**Last Updated**: December 2025
