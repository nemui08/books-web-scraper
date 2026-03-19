# Books Web Scraper

A Python project that scrapes book data from https://books.toscrape.com/

## Feature 

* Scrapes 1000 books from 50 pages
* Extracts title and price
* Cleans messy data using regex
* Exports data to Excel file

## Tech Stack

* Python
* requests
* BeautifulSoup
* pandas

## Project Structure

```
books-web-scraper
│
├── scraper.py
└── README.md
```

## How to Run

1. Install dependencies

```
pip install requests beautifulsoup4 pandas openpyxl
```

2. Run the script

```
python scraper.py
```

## Output

* books_1000.xlsx
