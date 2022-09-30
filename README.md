# GoogleTrendsScrapper

Idea:
Write a python script that will scrape weekly,daily and hourly google trends data for a specific keyword.

Time Consumption:
Coding the program took less than half hour. Running the program and execution could take time.

Approach:
Initial approach:
Scrapping results from google trends page by using web tool kits of python (Selenium,beutifulsoup).
Current approach:
Install and utilize pytrends library of python to trends data.

Reasons for current approach:

- The pytrends library provides extensive function that are customizable for example to get region specific , time specific data. 
- Fast and efficient execution

Script Execution:
python3 Google_trends_scrapper.py

Possible issues:
While running the script you might encounter 429 response code which just means you are exceeding the request limit set by google. This happens when we are requesting data for long periods

Work around:
- There are possible workarounds like using proxies, using multiple servers for request etc. The best solution that worked was to wait for a while or send request in lesser batches.
- We can also just get the hourly data and retrieve the weekly and daily data from it.


Other_notes:
- Here the default timezone is retained i.e UTC which can be converted to other timezones. Even country specifice data could work.
- Only time based numerical trends is retrieved in this script and other data in google trends page could also be retrieved.
-The weekly data is got through 2 steps: first getting the last 5 year data followed by the first two years. When we need data for more decades,change in technique would be required


