# Compass Agent Crawler
This is a scrapy project to crawl agents from http://www.compass.com
This project is meant only for educational purposes only.
## 🔍 Extracted Data
The extracted data would look like the table below

**link**|**name**|**phone**|**email**|**location**
:-----:|:-----:|:-----:|:-----:|:-----:
http://compass.com/agents/san\_diego/jane-doe/|Jane Doe|M: 760.123.4567|jane.doe@compass.com|San Diego
http://compass.com/agents/san\_diego/john-doe/|John Doe|M: 858.123.4567|john.doe@compass.com|San Diego

## ⚙️ Requirements
- Python 3.7
- Scrapy

## 🚀 Usage
1. Run the crawler
```bash
scrapy crawl -o agents.csv -t csv
```
2. Wait. ^_~


## 😜 Project History 
This project was originally done for a bid in upwork. Unfortunately, I didn't win the bid. Nonetheless, I've still learned the basics of scrapy.