# Description
Code to crawl data from the website: "http://alonhadat.com.vn/" and output a CSV file.
It uses the Scrapy framework for web scraping. Here's a brief description of the files and folders in the project:

* scrapy.cfg: This file is the configuration file for Scrapy. It specifies the project settings and deployment options.

* data_price folder: This folder serves as the Scrapy project folder.

* items.py: This file defines the data structure (item) for storing the scraped information. It contains various fields such as area, address, description, price, etc.

* middlewares.py: This file includes middleware components that can modify Scrapy's behavior during the crawling process. It contains a downloader middleware for handling proxy servers.

* pipelines.py: This file defines the data processing pipelines for scraped items. Currently, it only passes the items through without any modification.

* settings.py: This file contains the project settings for Scrapy. It includes configurations like the user-agent, download delay, and the middlewares to be used.

* spiders folder: This folder contains the spiders, which define how to extract data from websites.

* alonhadat.py: This spider is responsible for crawling the data from the "alonhadat.com.vn" website. It starts by sending requests to multiple pages and then extracts the links to individual property listings. It further parses each property page to extract relevant information using CSS selectors. The extracted data is stored in the defined item structure and yielded as results.

We will be provided with two CSV files containing housing data:
- 'can_ban.csv': This file contains data about houses available for sale.
- 'cho_thue.csv': This file contains data about houses available for rent.

For the "can_ban.csv" and "cho_thue.csv" files, the headers (columns) will be as follows:

- area
- address
- description
- floor_number
- bedroom_number
- is_dinning_room
- is_kitchen
- is_terrace
- is_car_pack
- is_owner
- start_date
- end_date
- type
- direction
- street_in_front_of_house
- width
- height
- law
- price

  
# Command to run project in terminal:
```bash
scrapy crawl alonhadat -t csv -o cho_thue.csv -a category=chothue --set FEED_EXPORT_ENCODING=utf-8
scrapy crawl alonhadat -t csv -o can_ban.csv -a category=canban --set FEED_EXPORT_ENCODING=utf-8
```

