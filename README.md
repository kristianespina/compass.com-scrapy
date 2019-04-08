# Compass Agent Crawler
This is a scrapy project to crawl agents from http://www.compass.com
This project is meant only for educational purposes only.
## 🔍 Extracted Data
The extracted data would look like the table below
|link                                                            |name                          |phone          |email                           |location     |
|----------------------------------------------------------------|------------------------------|---------------|--------------------------------|-------------|
|http://compass.com//agents/chicago/jane-doe/                |Jane Doe                  |M: 217.123.456|jane.doe@compass.com        |Chicago      |
|http://compass.com//agents/chicago/john-doe/             |John Doe              |M: 312.123.456|john.doe@compass.com     |Chicago      |

## ⚙️ Requirements
- Python 3.x
- Scrapy

## 🚀 Usage
1. Run the crawler
```bash
scrapy crawl -o agents.csv -t csv
```
2. Wait. ^_~


## 😜 Project History 
This project was originally done for a bid in upwork. Unfortunately, I didn't win the bid. Nonetheless, I've still learned the basics of scrapy.